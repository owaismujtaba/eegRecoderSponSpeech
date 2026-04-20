import tkinter as tk
import tkinter.font as tkfont
import config as cfg
from src.utils import Markers

class EndScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.title_font = tkfont.Font(family=cfg.TEXT_FAMILY, size=cfg.TITLE_FONT, weight="bold")
        self.hint_font = tkfont.Font(family=cfg.TEXT_FAMILY, size=cfg.TEXT_FONT)

        self.content_frame = tk.Frame(self)
        self.content_frame.grid(row=0, column=0)

        self.title_label = tk.Label(
            self.content_frame, text=cfg.END_SCREEN,
            font=self.title_font, justify=tk.CENTER, anchor=tk.CENTER,
        )
        self.title_label.grid(row=0, column=0, pady=(0, 20))

        self.thanks_label = tk.Label(
            self.content_frame, text=cfg.THANK_YOU,
            font=self.hint_font, justify=tk.CENTER, anchor=tk.CENTER,
        )
        self.thanks_label.grid(row=1, column=0, pady=(0, 40))

        self.hint_label = tk.Label(
            self.content_frame, text=cfg.QUIT_MESSAGE,
            font=self.hint_font, justify=tk.CENTER, anchor=tk.CENTER,
        )
        self.hint_label.grid(row=2, column=0)

    def on_show(self):
        self.controller.send_marker(Markers.END_EXPERIMENT)
