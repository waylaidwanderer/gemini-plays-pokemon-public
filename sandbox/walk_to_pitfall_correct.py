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

# Starting at (2, 12) on 3F West in State B
steps = [
    # Navigate 3F West
    ("Down", {"x": 2, "y": 13}),
    ("Right", {"x": 3, "y": 13}),
    ("Right", {"x": 4, "y": 13}),
    ("Right", {"x": 5, "y": 13}),
    ("Right", {"x": 6, "y": 13}),
    ("Up", {"x": 6, "y": 12}),
    ("Up", {"x": 6, "y": 11}),
    ("Up", {"x": 6, "y": 10}),
    ("Up", {"x": 6, "y": 9}),  # OPEN Row 9 Shutter Gate
    ("Up", {"x": 6, "y": 8}),
    ("Up", {"x": 6, "y": 7}),
    ("Up", {"x": 6, "y": 6}),
    ("Right", {"x": 7, "y": 6}),
    ("Right", {"x": 8, "y": 6}),
    ("Right", {"x": 9, "y": 6}),
    ("Right", {"x": 10, "y": 6}),
    ("Right", {"x": 11, "y": 6}),
    ("Right", {"x": 12, "y": 6}), # Crosses to 3F East
    # Navigate 3F East
    ("Right", {"x": 13, "y": 6}),
    ("Right", {"x": 14, "y": 6}),
    ("Right", {"x": 15, "y": 6}),
    ("Right", {"x": 16, "y": 6}),
    ("Right", {"x": 17, "y": 6}),
    ("Right", {"x": 18, "y": 6}),
    ("Right", {"x": 19, "y": 6}),
    ("Up", {"x": 19, "y": 5}),
    ("Up", {"x": 19, "y": 4}),
    ("Up", {"x": 19, "y": 3}),
    ("Right", {"x": 20, "y": 3}),
    ("Right", {"x": 21, "y": 3}),
    ("Right", {"x": 22, "y": 3}),
    ("Right", {"x": 23, "y": 3}),
    ("Right", {"x": 24, "y": 3}),
    ("Right", {"x": 25, "y": 3}),
    ("Right", {"x": 26, "y": 3}),
]

success = True
for direction, coords in steps:
    if not walk_step(direction, coords):
        success = False
        break

if success:
    print("Reached (26, 3) successfully! Stepping DOWN to trigger pitfall...")
    mgba.press_buttons(["Down"])
    time.sleep(1.0) # Wait for drop animation
    pos = mgba.get_coordinates()
    print(f"Dropped! New coordinates: {pos}")
    img_path = mgba.take_screenshot()
    print(f"Screenshot saved to {img_path}")
else:
    print("Navigation failed.")
