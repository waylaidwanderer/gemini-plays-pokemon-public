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
print("Starting position on 1F West:", pos)

# We are at (5, 10). Walk DOWN to (5, 11)
if pos == {"x": 5, "y": 10}:
    walk_step("Down", {"x": 5, "y": 11})
    pos = mgba.get_coordinates()

# Walk RIGHT to Column 13 on Row 11: (13, 11)
if pos == {"x": 5, "y": 11}:
    print("Walking RIGHT along Row 11 to Column 13...")
    for x in range(6, 14):
        if not walk_step("Right", {"x": x, "y": 11}):
            break
    pos = mgba.get_coordinates()

# Walk UP Column 13 to Row 5: (13, 5)
if pos == {"x": 13, "y": 11}:
    print("Walking UP Column 13 to Row 5...")
    for y in range(10, 4, -1):
        if not walk_step("Up", {"x": 13, "y": y}):
            break
    pos = mgba.get_coordinates()

# Walk RIGHT along Row 5 to Column 22 on 1F East: (22, 5)
if pos == {"x": 13, "y": 5}:
    print("Crossing horizontally on Row 5 to 1F East at (22, 5)...")
    for x in range(14, 23):
        if not walk_step("Right", {"x": x, "y": 5}):
            break

pos = mgba.get_coordinates()
print("Final position after walking to 1F East:", pos)
mgba.take_screenshot()
