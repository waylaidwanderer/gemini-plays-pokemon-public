import mgba
import time

def get_state():
    pos = mgba.get_coordinates()
    print("Current position:", pos)
    return pos

# Clear any text/menus
mgba.press_buttons(["B"])
time.sleep(0.3)

pos = get_state()

# We are at (7, 10). Let's walk DOWN to (7, 11)
if pos == {"x": 7, "y": 10}:
    print("Walking Down to (7, 11)...")
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    pos = get_state()

# Walk to (8, 10) via (8, 11)
if pos == {"x": 7, "y": 11}:
    print("Walking to (8, 10)...")
    mgba.press_buttons(["Right", "sleep 450", "Up"])
    time.sleep(1.0)
    pos = get_state()

# Now try to step LEFT onto the stairs at (7, 10)
if pos == {"x": 8, "y": 10}:
    print("Stepping LEFT onto stairs...")
    mgba.press_buttons(["Left"])
    time.sleep(2.0)
    pos = get_state()
