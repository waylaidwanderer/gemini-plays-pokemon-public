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

# We are at (8, 11). Walk to (11, 13)
# Path: Right -> Right -> Right -> Down -> Down
if pos == {"x": 8, "y": 11}:
    print("Walking to (11, 13)...")
    mgba.press_buttons(["Right", "sleep 450", "Right", "sleep 450", "Right", "sleep 450", "Down", "sleep 450", "Down"])
    time.sleep(2.0)
    pos = get_state()

# If we didn't warp, try to step LEFT or UP or DOWN on the stairs at (11, 13)
if pos == {"x": 11, "y": 13}:
    print("Currently at (11, 13). Trying to see if it warps...")
    # Try to walk UP or Right
    mgba.press_buttons(["Right"])
    time.sleep(1.0)
    pos = get_state()
