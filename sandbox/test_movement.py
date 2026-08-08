import mgba
import time

def test_dir(direction):
    print(f"Testing {direction}...")
    mgba.press_buttons([direction])
    time.sleep(0.1)
    pos = mgba.get_coordinates()
    print(f"Position after {direction}: {pos}")
    return pos

# First, get current starting position
start_pos = mgba.get_coordinates()
print(f"Start position: {start_pos}")

# Try moving Up
pos_up = test_dir("Up")

# If we moved Up, move back Down
if pos_up != start_pos:
    print("Moved Up successfully, returning to start...")
    mgba.press_buttons(["Down"])
    time.sleep(0.1)

# Try moving Right
pos_right = test_dir("Right")
if pos_right != start_pos:
    print("Moved Right successfully, returning to start...")
    mgba.press_buttons(["Left"])
    time.sleep(0.1)

# Try moving Left
pos_left = test_dir("Left")
if pos_left != start_pos:
    print("Moved Left successfully, returning to start...")
    mgba.press_buttons(["Right"])
    time.sleep(0.1)

# Try moving Down again
pos_down = test_dir("Down")
