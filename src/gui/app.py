import tkinter as tk
import serial
from pylsl import local_clock
import pandas as pd
from pylsl import StreamInfo, StreamOutlet

import config as cfg
from src.gui.instructions import InstructionsScreen
from src.gui.start import MainPage
from src.gui.rest import RestScreen
from src.gui.experiment import ExperimentScreen
from src.gui.end import EndScreen
from src.utils import MarkerConfig, Markers


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(cfg.APP_TITLE)


        if not cfg.FULL_SCREEN:
            self.geometry(f"{cfg.SCREEN_WIDTH}x{cfg.SCREEN_HEIGHT}")
            self.resizable(width=False, height=False)

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.current_frame = None
        self.previous_frame = None
        self.last_marker_time = 0

        self.maker_details = []
        self.images_details = []
        self.time_details = []

        self.frames = {}
        for F in (MainPage, InstructionsScreen, RestScreen, ExperimentScreen, EndScreen,):
            page_name = F.__name__
            frame =F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.info = StreamInfo(
            name='ContineousSpeechMarkerStream', type='Markers',
            channel_count=1, nominal_srate=0, channel_format='string',
            source_id='emuidw22',
        )
        self.outlet = StreamOutlet(self.info)
        if cfg.TRIGGER_PORT:
            self.serial_port = serial.Serial(
                cfg.TRIGGER_PORT, baudrate=128000, timeout=0.1
            )
        else:
            self.serial_port = None

        self.bind_all("q", lambda event: self.quit())

        self.run_app()

    def show_frame(self, page_name):
        current = self.frames.get(self.current_frame)
        if current and hasattr(current, "on_hide"):
            current.on_hide()
        self.previous_frame = self.current_frame
        self.current_frame = page_name
        frame = self.frames[page_name]
        frame.tkraise()
        if hasattr(frame, "on_show"):
            frame.on_show()

    def run_app(self):
        #self.send_marker(Markers.START_EXPERIMENT)
        self.show_frame("MainPage")

    def send_marker(self, marker, image_name=None):
        marker_cfg = MarkerConfig()
        current_time = local_clock()
        time_since_last_ms = (current_time - self.last_marker_time) * 1000
        if time_since_last_ms < cfg.MIN_MARKER_INTERVAL:
            delay_ms = int(cfg.MIN_MARKER_INTERVAL - time_since_last_ms)
            self.after(delay_ms, lambda: self.send_marker(marker, image_name))
            return
        self.last_marker_time = current_time
        self.time_details.append(current_time)
        self.maker_details.append(marker)
        serial_cmd, lsl_base_marker = marker_cfg.get_command(marker)
        if image_name:
            lsl_base_marker = f"{lsl_base_marker}:{image_name}"
            self.images_details.append(image_name)
        else:
            self.images_details.append(' ')
        if self.serial_port:
            self.serial_port.write(serial_cmd)
        else:
            print(f"[{current_time:.3f}]  serial={serial_cmd.strip()} | lsl={lsl_base_marker}")
        self.outlet.push_sample([lsl_base_marker])

    def quit(self):
        data = {
            'Time': self.time_details,
            'Marker': self.maker_details,
            'Images': self.images_details,
        }
        df = pd.DataFrame(data)
        print(df)
        self.send_marker(Markers.END_EXPERIMENT)
        df.to_csv('info.csv', index=False)


        if hasattr(self, 'ser') and self.ser.is_open:
            self.ser.flush()
            self.ser.close()

        self.destroy()




