import mgba
import time

def walk_step(direction, expected_coords):
    mgba.press_buttons([direction])
    time.sleep(0.45)
    pos = mgba.get_coordinates()
    if pos == expected_coords:
        print(f"Moved {direction} to {pos}")
        return True
    else:
        print(f"BLOCKED moving {direction} to {expected_coords}. Current: {pos}")
        return False

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

pos = mgba.get_coordinates()
print("Starting position:", pos)

# We are at (9, 10). Walk DOWN to (9, 11)
if pos == {"x": 9, "y": 10}:
    walk_step("Down", {"x": 9, "y": 11})
    pos = mgba.get_coordinates()

# Try to walk RIGHT to (10, 11)
if pos == {"x": 9, "y": 11}:
    walk_step("Right", {"x": 10, "y": 11})
    pos = mgba.get_coordinates()

mgba.take_screenshot()
