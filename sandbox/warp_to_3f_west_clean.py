import mgba
import time

# 1. Dismiss the battle screen
mgba.press_buttons(["B"])
time.sleep(1.5) # Wait for fade back to overworld

# 2. Walk to stairs and warp UP
# Current position: (6, 9)
steps = [
    ("Down", {"x": 6, "y": 10}),
    ("Right", {"x": 7, "y": 10}),
]

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

success = True
for direction, coords in steps:
    if not walk_step(direction, coords):
        success = False
        break

if success:
    print("Reached (7, 10)! Waiting for warp...")
    time.sleep(1.5)
    pos = mgba.get_coordinates()
    print(f"Coordinates after warp: {pos}")
else:
    print("Failed to reach stairs.")
