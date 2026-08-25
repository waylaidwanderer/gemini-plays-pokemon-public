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

# Starting at (9, 7) inside 1F West
# Walk to stairs at (5, 3)
steps = [
    ("Left", {"x": 8, "y": 7}),
    ("Left", {"x": 7, "y": 7}),
    ("Left", {"x": 6, "y": 7}),
    ("Left", {"x": 5, "y": 7}),
    ("Up", {"x": 5, "y": 6}),
    ("Up", {"x": 5, "y": 5}),
    ("Up", {"x": 5, "y": 4}),
]

success = True
for direction, coords in steps:
    if not walk_step(direction, coords):
        success = False
        break

if success:
    print("Reached (5, 4) on 1F West! Stepping UP onto stairs at (5, 3) to warp...")
    mgba.press_buttons(["Up"])
    time.sleep(1.5) # Wait for warp animation
    pos = mgba.get_coordinates()
    print(f"Warped! Current position: {pos}")
else:
    print("Failed to reach stairs.")
