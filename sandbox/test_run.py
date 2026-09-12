import mgba
import time
from PIL import Image

def dismiss_and_run():
    # Advance battle start text
    mgba.press_buttons(["A", "sleep 250", "B", "sleep 250", "B", "sleep 250"])
    # Move to RUN (bottom-right: Down, Right, A)
    mgba.press_buttons(["Down", "Right", "A", "sleep 350", "B", "sleep 250", "B", "sleep 250"])

def get_pos():
    return mgba.get_coordinates()

print("Initial pos:", get_pos())
dismiss_and_run()
print("Pos after run attempt 1:", get_pos())
