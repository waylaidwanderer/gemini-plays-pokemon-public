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

# Start at (8, 13)
steps = [
    ("Up", {"x": 8, "y": 12}),
    ("Up", {"x": 8, "y": 11}),
    ("Right", {"x": 9, "y": 11}),
    ("Up", {"x": 9, "y": 10}),
    ("Up", {"x": 9, "y": 9}),
]

success = True
for direction, coords in steps:
    if not walk_step(direction, coords):
        success = False
        break

if success:
    print("Reached (9, 9) successfully! Trying to walk UP further...")
    # Attempt to go UP as much as possible, printing positions
    for _ in range(7):
        mgba.press_buttons(["Up"])
        time.sleep(0.3)
        pos = mgba.get_coordinates()
        print(f"Tried Up, current position: {pos}")
    img_path = mgba.take_screenshot()
    print(f"Screenshot saved to {img_path}")
else:
    print("Failed to navigate to (9, 9)")
