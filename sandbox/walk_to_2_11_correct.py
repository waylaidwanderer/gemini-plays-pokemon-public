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

# We are at (9, 12). Let's walk UP to (9, 11)
if pos == {"x": 9, "y": 12}:
    print("Walking UP to (9, 11)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    pos = get_state()

# Walk LEFT along Row 11 to (2, 11)
if pos == {"x": 9, "y": 11}:
    print("Walking LEFT to (2, 11)...")
    steps = []
    for x in range(8, 1, -1):
        steps.append(("Left", {"x": x, "y": 11}))
    
    for d, c in steps:
        mgba.press_buttons([d])
        time.sleep(0.4)
    pos = get_state()

# Face UP to inspect (2, 10)
if pos == {"x": 2, "y": 11}:
    print("Facing UP to inspect (2, 10)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    # Take screenshot
    scr = mgba.take_screenshot()
    print("Screenshot at (2, 11) facing UP:", scr)
    
    # Try interacting
    print("Pressing A...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Walk to (2, 12) and face UP to inspect (2, 11)
    mgba.press_buttons(["Down"])
    time.sleep(0.45)
    pos = get_state()
    
    if pos == {"x": 2, "y": 12}:
        print("Facing UP to inspect (2, 11)...")
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        
        scr = mgba.take_screenshot()
        print("Screenshot at (2, 12) facing UP:", scr)
        
        print("Pressing A...")
        mgba.press_buttons(["A"])
        time.sleep(1.0)
