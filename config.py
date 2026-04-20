from pathlib import Path

APP_TITLE = 'Spontaneous Speech Experiment'
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FULL_SCREEN = True

# Main Screen
DISPLAY_MESSAGE = 'Welcome to the Spontaneous Speech Experiment\nPress SPACE to continue'

# Instructions Screen
OVERVIEW = 'You will be shown a series of pictures.\n   Your goal is to describe each picture in as much detail as you can'
INSTRUCTIONS = {1: "A small cross (+) will appear in the center of the screen for 1.5 seconds. \n   Please keep your eyes fixed on this cross.",
                2: "A picture will then appear on the screen.",
                3: "Once you see the picture, please describe it in detail.\n   You may take as much time as you need to provide your description.",
                4: "Once you have finished speaking, please press the ENTER key \n   on your keyboard.",
                5: "After pressing Enter, the screen will return to the fixation cross for\n   1.5 seconds before the next picture appears.",
                6: "Press ESC for resting and Q for quit"}

TEXT_FAMILY = 'Courier'
TITLE_FONT = 40
OVERVIEW_FONT = 26
TEXT_FONT = 26

# SYSTEM VARIABLES
IMAGE_DIR = Path("images")
IMAGE_SEED = 42     # fixed seed ensures the same image order every run
TRIGGER_PORT = '/tmp/ttyV0' #'/dev/ttyS4'  #'/dev/ttyACM0'
FIXATION_TIME = 1500 #ms
MIN_MARKER_INTERVAL = 5

# End Screen

END_SCREEN = "End of Experiment"
THANK_YOU = "Thank you for your participation."
QUIT_MESSAGE = "Press Q to quit"