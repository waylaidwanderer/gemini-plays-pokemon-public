import mgba
import time

def check_pos():
    pos = mgba.get_coordinates()
    print("Current position:", pos)
    return pos

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

pos = check_pos()

# We are at (5, 10) on 1F West.
# Let's walk RIGHT to (7, 10) (staircase icon at 7, 10)
print("Moving Right to (6, 10)...")
mgba.press_buttons(["Right"])
time.sleep(0.5)
pos = check_pos()

if pos == {"x": 6, "y": 10}:
    print("Moving Right to (7, 10)...")
    mgba.press_buttons(["Right"])
    time.sleep(1.5)
    pos = check_pos()

mgba.take_screenshot()
