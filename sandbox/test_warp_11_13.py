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

# We are at (11, 11). Walk to (11, 13)
if pos == {"x": 11, "y": 11}:
    print("Walking down to (11, 12)...")
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    pos = get_state()

if pos == {"x": 11, "y": 12}:
    print("Stepping DOWN onto stairs at (11, 13)...")
    mgba.press_buttons(["Down"])
    time.sleep(2.0)
    pos = get_state()
