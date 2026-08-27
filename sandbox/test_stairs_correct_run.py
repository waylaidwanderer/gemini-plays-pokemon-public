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

# We are at (7, 10). Let's go DOWN to (7, 11)
print("Moving Down to (7, 11)...")
mgba.press_buttons(["Down"])
time.sleep(0.5)
pos = check_pos()

# Walk Left to (2, 11)
if pos == {"x": 7, "y": 11}:
    print("Walking Left to (2, 11)...")
    for x in range(6, 1, -1):
        mgba.press_buttons(["Left"])
        time.sleep(0.45)
    pos = check_pos()

# Now run the exact sequence from test_stairs_correct.py
if pos == {"x": 2, "y": 11}:
    print("Running test_stairs_correct sequence...")
    mgba.press_buttons([
        "Right", "sleep 450",
        "Right", "sleep 450",
        "Right", "sleep 450",
        "Up"
    ])
    time.sleep(2.5)
    pos = check_pos()

mgba.take_screenshot()
