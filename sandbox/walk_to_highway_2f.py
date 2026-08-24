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

# From (3, 13) to (6, 3) on 2F West of Pokemon Mansion in State B
steps = [
    ("Right", {"x": 4, "y": 13}),
    ("Right", {"x": 5, "y": 13}),
    ("Up", {"x": 5, "y": 12}),
    ("Up", {"x": 5, "y": 11}),
    ("Up", {"x": 5, "y": 10}),
    ("Right", {"x": 6, "y": 10}),
    ("Up", {"x": 6, "y": 9}),
    ("Up", {"x": 6, "y": 8}),
    ("Up", {"x": 6, "y": 7}),
    ("Up", {"x": 6, "y": 6}),
    ("Up", {"x": 6, "y": 5}),
    ("Up", {"x": 6, "y": 4}),
    ("Up", {"x": 6, "y": 3}),
]

success = True
for direction, coords in steps:
    if not walk_step(direction, coords):
        success = False
        break

if success:
    print("Reached (6, 3) on 2F West successfully!")
else:
    print("Failed to reach (6, 3).")
