from src.gui.app import App
import config as cfg

app = App()
if cfg.FULL_SCREEN:
    app.attributes("-fullscreen", True)
app.mainloop()