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

# We are at (9, 11). Walk UP to (9, 9)
if pos == {"x": 9, "y": 11}:
    walk_step("Up", {"x": 9, "y": 10})
    walk_step("Up", {"x": 9, "y": 9})
    pos = mgba.get_coordinates()

# Walk LEFT to Column 5 Row 9: (5, 9)
if pos == {"x": 9, "y": 9}:
    print("Walking LEFT along Row 9 to Column 5...")
    for x in range(8, 4, -1):
        if not walk_step("Left", {"x": x, "y": 9}):
            break
    pos = mgba.get_coordinates()

# Walk UP Column 5 to Row 6: (5, 6)
if pos == {"x": 5, "y": 9}:
    print("Walking UP Column 5 to Row 6...")
    for y in range(8, 5, -1):
        if not walk_step("Up", {"x": 5, "y": y}):
            break
    pos = mgba.get_coordinates()

# Walk RIGHT along Row 6 directly to 1F East at (22, 6)
if pos == {"x": 5, "y": 6}:
    print("Crossing horizontally on Row 6 to 1F East...")
    for x in range(6, 23):
        if not walk_step("Right", {"x": x, "y": 6}):
            break

pos = mgba.get_coordinates()
print("Final position:", pos)
mgba.take_screenshot()
