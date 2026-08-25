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

# Starting at (16, 11) on 2F East (State B)
# Walk around to (12, 11) and toggle to State A
steps = [
    ("Right", {"x": 17, "y": 11}),
    ("Right", {"x": 18, "y": 11}),
    ("Up", {"x": 18, "y": 10}),
    ("Up", {"x": 18, "y": 9}),
    ("Up", {"x": 18, "y": 8}),
    ("Up", {"x": 18, "y": 7}),
    ("Up", {"x": 18, "y": 6}),
    ("Left", {"x": 17, "y": 6}),
    ("Left", {"x": 16, "y": 6}),
    ("Left", {"x": 15, "y": 6}),
    ("Left", {"x": 14, "y": 6}),
    ("Left", {"x": 13, "y": 6}),
    ("Left", {"x": 12, "y": 6}),
    ("Down", {"x": 12, "y": 7}),
    ("Down", {"x": 12, "y": 8}),
    ("Down", {"x": 12, "y": 9}),
    ("Down", {"x": 12, "y": 10}),
    ("Down", {"x": 12, "y": 11}),
]

success = True
for d, c in steps:
    if not walk_step(d, c):
        success = False
        break

if success:
    print("Reached (12, 11)! Facing RIGHT towards the switch...")
    mgba.press_buttons(["Right"])
    time.sleep(0.3)
    mgba.press_buttons(["A"]) # Secret switch!
    time.sleep(0.8)
    mgba.press_buttons(["A"]) # Select YES (State A)
    time.sleep(0.8)
    mgba.press_buttons(["A"]) # Dismiss "Pressed it!"
    time.sleep(0.8)
    print("Mansion should be in STATE A now! Current position:", mgba.get_coordinates())
else:
    print("Failed to reach (12, 11).")
