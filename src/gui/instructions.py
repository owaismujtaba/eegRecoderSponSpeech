import tkinter as tk
import tkinter.font as tkfont
import config as cfg


class InstructionsScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Configure the root to center its content
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Create a container for all widgets to center them as a block
        self.content_frame = tk.Frame(self)
        self.content_frame.grid(row=0, column=0)

        self.title_font = tkfont.Font(family=cfg.TEXT_FAMILY, size=cfg.TITLE_FONT, weight="bold")
        self.overview_font = tkfont.Font(family=cfg.TEXT_FAMILY, size=cfg.OVERVIEW_FONT, weight="bold")
        self.text_font = tkfont.Font(family=cfg.TEXT_FAMILY, size=cfg.TEXT_FONT)

        self.create_display()

    def on_show(self):
        self.bind_all("<space>", self.start_experiment)
        self.bind_all("<Escape>", self.rest)

    def on_hide(self):
        self.unbind_all("<space>")
        self.unbind_all("<Escape>")

    def start_experiment(self, event=None):
        self.controller.show_frame("ExperimentScreen")

    def rest(self, event=None):
        self.controller.show_frame("MainPage")

    def get_instruction_text(self):
        instruction_text = ""
        for key, instruction in cfg.INSTRUCTIONS.items():
            instruction_text += f"{key}. {instruction}\n"
        return instruction_text

    def create_display(self):
        self.title_label = tk.Label(
            self.content_frame, text="Experiment Instructions",
            font=self.title_font, justify=tk.CENTER, anchor=tk.CENTER
        )
        self.title_label.grid(row=0, column=0, pady=(0, 30))

        self.overview_label = tk.Label(
            self.content_frame, text=cfg.OVERVIEW,
            font=self.overview_font, justify=tk.CENTER,anchor=tk.CENTER
        )
        self.overview_label.grid(row=1, column=0, pady=20)

        instruction_text = self.get_instruction_text()
        self.instruction_label = tk.Label(
            self.content_frame, text=instruction_text,
            font=self.text_font, justify='left',
        )
        self.instruction_label.grid(row=2, column=0, pady=20)



