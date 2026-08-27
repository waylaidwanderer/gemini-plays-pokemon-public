import mgba
import time
from PIL import Image

def get_state():
    pos = mgba.get_coordinates()
    print("Current position:", pos)
    return pos

# Clear any text/menus
mgba.press_buttons(["B"])
time.sleep(0.3)

# Start path from (5, 10) on 2F West
# Path: Right -> Down -> Right -> Up (to warp)
get_state()

print("Walking to (6, 10)...")
mgba.press_buttons(["Right"])
time.sleep(0.4)
get_state()

print("Walking to (6, 11)...")
mgba.press_buttons(["Down"])
time.sleep(0.4)
get_state()

print("Walking to (7, 11)...")
mgba.press_buttons(["Right"])
time.sleep(0.4)
get_state()

print("Stepping UP onto stairs at (7, 10)...")
mgba.press_buttons(["Up"])
time.sleep(1.0)
pos = get_state()

# Take screenshot to see where we landed
scr = mgba.take_screenshot()
print("Screenshot saved:", scr)
