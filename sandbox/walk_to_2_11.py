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

pos = get_state()

# We are at (11, 12). Let's walk to (2, 12)
if pos == {"x": 11, "y": 12}:
    print("Walking left to (2, 12)...")
    steps = []
    for x in range(10, 1, -1):
        steps.append(("Left", {"x": x, "y": 12}))
    
    for d, c in steps:
        mgba.press_buttons([d])
        time.sleep(0.4)
    pos = get_state()

# Face UP to inspect (2, 11)
if pos == {"x": 2, "y": 12}:
    print("Facing UP to inspect (2, 11)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    # Take screenshot
    scr = mgba.take_screenshot()
    print("Screenshot at (2, 12) facing UP:", scr)
    
    # Try interacting
    print("Pressing A...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
