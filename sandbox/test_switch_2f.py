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

# Starting at (12, 9) on 2F West
# Walk to (12, 11)
success = walk_step("Down", {"x": 12, "y": 10})
if success:
    success = walk_step("Down", {"x": 12, "y": 11})

if success:
    print("Reached (12, 11)! Turning to face RIGHT...")
    mgba.press_buttons(["Right"])
    time.sleep(0.3)
    print("Pressing A to check for a switch...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    screenshot_file = mgba.take_screenshot()
    print(f"Screenshot taken at {screenshot_file}")
    print("Current position:", mgba.get_coordinates())
else:
    print("Failed to reach (12, 11).")

