import mgba
import time
from PIL import Image

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def toggle_switch_once():
    print("Toggling Mewtwo Switch at (8, 9) from current (8, 10) facing UP...")
    mgba.press_buttons(["A", "sleep 1200", "A", "sleep 1200", "A", "sleep 1200", "A", "sleep 1200"])
    time.sleep(6.0)
    print("Toggle complete! Position after toggle:", get_pos())

# We are at (8, 10) facing UP.
toggle_switch_once()

# Take a screenshot to verify if dialogue is closed and we are in overworld
scr = mgba.take_screenshot()
print("Screenshot after toggle taken:", scr)
