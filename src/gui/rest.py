import tkinter as tk
import tkinter.font as tkfont
import config as cfg
from src.utils import Markers


class RestScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.rest_font = tkfont.Font(family=cfg.TEXT_FAMILY, size=cfg.TITLE_FONT, weight="bold")
        self.hint_font = tkfont.Font(family=cfg.TEXT_FAMILY, size=cfg.TEXT_FONT)

        self.content_frame = tk.Frame(self)
        self.content_frame.grid(row=0, column=0)

        self.rest_label = tk.Label(
            self.content_frame, text="Resting...",
            font=self.rest_font, justify=tk.CENTER, anchor=tk.CENTER,
        )
        self.rest_label.grid(row=0, column=0, pady=(0, 20))

        self.hint_label = tk.Label(
            self.content_frame, text="Press SPACE to continue",
            font=self.hint_font, justify=tk.CENTER, anchor=tk.CENTER,
        )
        self.hint_label.grid(row=1, column=0)

    def on_show(self):
        self.controller.send_marker(Markers.START_RESTING)
        self.bind_all("<space>", self.resume)

    def on_hide(self):
        self.unbind_all("<space>")

    def resume(self, event=None):
        self.controller.send_marker(Markers.END_RESTING)
        previous = self.controller.previous_frame
        if previous:
            self.controller.show_frame(previous)
