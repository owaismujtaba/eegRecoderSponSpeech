import tkinter as tk
import tkinter.font as tkfont

import config as cfg

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.title_font = tkfont.Font(family=cfg.TEXT_FAMILY, size=cfg.TITLE_FONT, weight="bold")

        self.message = tk.Label(
            self, text=cfg.DISPLAY_MESSAGE,
            font=self.title_font, justify=tk.CENTER,
        )

        self.message.grid(row=0, column=0, sticky="nsew")

    def on_show(self):
        self.bind_all("<space>", lambda event: self.controller.show_frame("InstructionsScreen"))

    def on_hide(self):
        self.unbind_all("<space>")