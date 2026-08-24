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

# From (7, 11) on 2F West: walk to (5, 11), then step UP onto (5, 10) to warp
steps = [
    ("Left", {"x": 6, "y": 11}),
    ("Left", {"x": 5, "y": 11}),
]

success = True
for direction, coords in steps:
    if not walk_step(direction, coords):
        success = False
        break

if success:
    print("Reached (5, 11) on 2F West! Stepping UP to warp...")
    mgba.press_buttons(["Up"])
    time.sleep(1.5) # Wait for warp animation
    pos = mgba.get_coordinates()
    print(f"Current position after warp: {pos}")
else:
    print("Failed to reach (5, 11).")
