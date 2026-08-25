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

# Starting at (1, 12) on 3F West
# 1. Walk to (5, 13)
steps = [
    ("Down", {"x": 1, "y": 13}),
    ("Right", {"x": 2, "y": 13}),
    ("Right", {"x": 3, "y": 13}),
    ("Right", {"x": 4, "y": 13}),
    ("Right", {"x": 5, "y": 13}),
]

success = True
for d, c in steps:
    if not walk_step(d, c):
        success = False
        break

if success:
    print("Reached (5, 13)! Probing nearby paths to Column 11...")
    # Let's try to walk:
    # Down to (5, 14), Down to (5, 15)
    if walk_step("Down", {"x": 5, "y": 14}):
        if walk_step("Down", {"x": 5, "y": 15}):
            # Let's check if we can walk Right on Row 15
            if walk_step("Right", {"x": 6, "y": 15}):
                print("Row 15 Column 6 is open!")
                # Probe further right
                curr = mgba.get_coordinates()
                while curr['x'] < 11:
                    if not walk_step("Right", {"x": curr['x'] + 1, "y": 15}):
                        print(f"Blocked at x={curr['x']+1} on Row 15!")
                        break
                    curr = mgba.get_coordinates()
                print("Final probed position from Row 15:", mgba.get_coordinates())
            else:
                print("Row 15 Column 6 is blocked.")
        else:
            print("Row 14 Column 5 is open, but Row 15 is blocked.")
    else:
        print("Row 14 Column 5 is blocked.")
else:
    print("Failed to reach (5, 13).")

