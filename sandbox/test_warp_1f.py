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
print("Starting position on 2F West:", pos)

# We are at (1, 11). Walk DOWN Column 1 to Row 13: (1, 13)
if pos == {"x": 1, "y": 11}:
    print("Walking DOWN to Row 13...")
    walk_step("Down", {"x": 1, "y": 12})
    walk_step("Down", {"x": 1, "y": 13})
    pos = mgba.get_coordinates()

# Walk RIGHT along Row 13 to Column 5: (5, 13)
if pos == {"x": 1, "y": 13}:
    print("Walking RIGHT along Row 13 to Column 5...")
    for x in range(2, 6):
        if not walk_step("Right", {"x": x, "y": 13}):
            break
    pos = mgba.get_coordinates()

# Walk UP Column 5 to Row 11: (5, 11)
if pos == {"x": 5, "y": 13}:
    print("Walking UP to (5, 11)...")
    walk_step("Up", {"x": 5, "y": 12})
    walk_step("Up", {"x": 5, "y": 11})
    pos = mgba.get_coordinates()

# Step UP onto stairs at (5, 10) to warp down to 1F West!
if pos == {"x": 5, "y": 11}:
    print("Stepping UP onto stairs at (5, 10) to warp down to 1F West...")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)
    pos = mgba.get_coordinates()
    print("Position after warping down to 1F West:", pos)

mgba.take_screenshot()
