import tkinter as tk
import tkinter.font as tkfont
from pathlib import Path
import random

from PIL import Image, ImageTk

import config as cfg
from src.utils import Markers


class ExperimentScreen(tk.Frame):
    IMAGE_DIR =  cfg.IMAGE_DIR

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.fixation_font = tkfont.Font(family=cfg.TEXT_FAMILY, size=80, weight="bold")

        self.fixation_label = tk.Label(self, text="+", font=self.fixation_font)
        self.fixation_label.grid(row=0, column=0)

        self.image_label = tk.Label(self)
        self.image_label.grid(row=0, column=0)

        self.images = sorted(self.IMAGE_DIR.glob("*.jpg"))
        self.current_index = 0
        self._photo = None
        self._fixation_timer = None

    def on_show(self):
        if self.controller.previous_frame == "InstructionsScreen":
            self.current_index = 0
            random.seed(cfg.IMAGE_SEED)
            random.shuffle(self.images)
        self.bind_all("<Return>", self.next_image)
        self.bind_all("<Escape>", self.go_rest)
        self.show_fixation()

    def on_hide(self):
        self.unbind_all("<Return>")
        self.unbind_all("<Escape>")
        if self._fixation_timer is not None:
            self.after_cancel(self._fixation_timer)
            self._fixation_timer = None

    def show_fixation(self):
        self.controller.send_marker(Markers.START_FIXATION)
        self.image_label.grid_remove()
        self.fixation_label.grid()
        self._fixation_timer = self.after(
            int(cfg.FIXATION_TIME), self.show_image
        )

    def show_image(self):
        self._fixation_timer = None
        self.controller.send_marker(Markers.END_FIXATION)

        if self.current_index >= len(self.images):
            self.controller.show_frame("EndScreen")
            return

        path = self.images[self.current_index]


        img = Image.open(path)

        w = cfg.SCREEN_WIDTH
        h = cfg.SCREEN_HEIGHT
        img.thumbnail((w, h), Image.LANCZOS)

        self._photo = ImageTk.PhotoImage(img)
        self.controller.send_marker(Markers.START_DISPLAY_IMAGE, image_name=path.name)
        self.image_label.config(image=self._photo)

        self.fixation_label.grid_remove()
        self.image_label.grid()

    def next_image(self, event=None):
        self.controller.send_marker(Markers.END_DISPLAY_IMAGE)
        self.current_index += 1
        self.show_fixation()

    def go_rest(self, event=None):
        self.controller.show_frame("RestScreen")
