import mgba
import time

def walk_step(direction, expected_coords, retries=15):
    for i in range(retries):
        mgba.press_buttons([direction])
        time.sleep(0.3)
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            print(f"Moved {direction}, current position: {pos}")
            return True
        print(f"Blocked! Retrying {direction} to {expected_coords} (attempt {i+1}/{retries}), current: {pos}")
        time.sleep(0.2)
    return False

# Starting at (4, 10) on 3F West (State B)
# Walk Down to Row 13, Left on Row 13 to Column 1, and UP Column 1
steps = [
    ("Down", {"x": 4, "y": 11}),
    ("Down", {"x": 4, "y": 12}),
    ("Down", {"x": 4, "y": 13}),
    ("Left", {"x": 3, "y": 13}),
    ("Left", {"x": 2, "y": 13}),
    ("Left", {"x": 1, "y": 13}),
    ("Up", {"x": 1, "y": 12}),
    ("Up", {"x": 1, "y": 11}),
    ("Up", {"x": 1, "y": 10}),
    ("Up", {"x": 1, "y": 9}),   # Open gate in State B!
    ("Up", {"x": 1, "y": 8}),
    ("Up", {"x": 1, "y": 7}),
    ("Up", {"x": 1, "y": 6}),
    ("Right", {"x": 2, "y": 6}),
    ("Right", {"x": 3, "y": 6}),
    ("Right", {"x": 4, "y": 6}),
    ("Right", {"x": 5, "y": 6}),
    ("Right", {"x": 6, "y": 6}),
    ("Right", {"x": 7, "y": 6}),
    ("Right", {"x": 8, "y": 6}),
    ("Right", {"x": 9, "y": 6}),
    ("Right", {"x": 10, "y": 6}),
    ("Right", {"x": 11, "y": 6}), # Crosses to 3F East!
]

success = True
for direction, coords in steps:
    if not walk_step(direction, coords):
        success = False
        break

if success:
    print("Successfully reached (11, 6) on 3F West!")
else:
    print("Failed to reach (11, 6).")
