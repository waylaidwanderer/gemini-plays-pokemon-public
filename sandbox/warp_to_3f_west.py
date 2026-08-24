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

# From (6, 8) to (7, 10) on 2F West, then warp UP
steps = [
    ("Down", {"x": 6, "y": 9}),
    ("Down", {"x": 6, "y": 10}),
    ("Right", {"x": 7, "y": 10}),
]

success = True
for direction, coords in steps:
    if not walk_step(direction, coords):
        success = False
        break

if success:
    print("Reached stairs at (7, 10)! Warping UP...")
    mgba.press_buttons(["Up"])
    time.sleep(1.0)
    pos = mgba.get_coordinates()
    print(f"Current position after warp: {pos}")
else:
    print("Failed to reach stairs.")
