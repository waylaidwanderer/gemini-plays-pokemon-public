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

# Starting at (10, 11) on 2F West
# Walk LEFT to Column 2 on Row 11
success = True
curr = mgba.get_coordinates()
while curr['x'] > 2:
    if not walk_step("Left", {"x": curr['x'] - 1, "y": 11}):
        success = False
        break
    curr = mgba.get_coordinates()

if success:
    print("Reached (2, 11)! Walking DOWN to (2, 12) to stand below the statue...")
    if walk_step("Down", {"x": 2, "y": 12}):
        mgba.press_buttons(["Up"]) # Face UP towards the statue
        time.sleep(0.3)
        print("Pressing A to check for a switch...")
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        screenshot_file = mgba.take_screenshot()
        print(f"Screenshot taken at {screenshot_file}")
        print("Current position:", mgba.get_coordinates())
    else:
        print("Failed to reach (2, 12).")
else:
    print("Failed to reach Column 2.")

