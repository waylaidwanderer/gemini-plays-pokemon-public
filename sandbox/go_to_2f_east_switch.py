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
        # If we didn't reach the target, the NPC might be blocking us. Wait and retry.
        print(f"Blocked! Retrying {direction} to {expected_coords} (attempt {i+1}/{retries}), current: {pos}")
        time.sleep(0.2)
    return False

# We are currently at (5, 11)
steps = [
    # Walk from (5, 11) to (10, 13)
    ("Right", {"x": 6, "y": 11}),
    ("Right", {"x": 7, "y": 11}),
    ("Right", {"x": 8, "y": 11}),
    ("Down", {"x": 8, "y": 12}),
    ("Down", {"x": 8, "y": 13}),
    ("Right", {"x": 9, "y": 13}),
    ("Right", {"x": 10, "y": 13}),
    # Walk up Column 10 to Row 3
    ("Up", {"x": 10, "y": 12}),
    ("Up", {"x": 10, "y": 11}),
    ("Up", {"x": 10, "y": 10}),
    ("Up", {"x": 10, "y": 9}),
    ("Up", {"x": 10, "y": 8}),
    ("Up", {"x": 10, "y": 7}),
    ("Up", {"x": 10, "y": 6}),
    ("Up", {"x": 10, "y": 5}),
    ("Up", {"x": 10, "y": 4}),
    ("Up", {"x": 10, "y": 3}),
    # Walk to Column 12
    ("Right", {"x": 11, "y": 3}),
    ("Right", {"x": 12, "y": 3}),
    # Walk down Column 12 to Row 9
    ("Down", {"x": 12, "y": 4}),
    ("Down", {"x": 12, "y": 5}),
    ("Down", {"x": 12, "y": 6}),
    ("Down", {"x": 12, "y": 7}),
    ("Down", {"x": 12, "y": 8}),
    ("Down", {"x": 12, "y": 9}),
]

success = True
for direction, coords in steps:
    if not walk_step(direction, coords):
        success = False
        break

if success:
    print("Reached (12, 9) successfully! Turning UP and interacting...")
    mgba.press_buttons(["Up"])
    time.sleep(0.3)
    mgba.press_buttons(["A"])
    time.sleep(0.3)
    img_path = mgba.take_screenshot()
    print(f"Screenshot saved to {img_path}")
else:
    print("Navigation failed.")
