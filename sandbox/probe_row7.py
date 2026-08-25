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

# Starting at (18, 7) on 2F (State B)
# Walk LEFT along Row 7 to Column 12
success = True
curr = mgba.get_coordinates()
while curr['x'] > 12:
    if not walk_step("Left", {"x": curr['x'] - 1, "y": 7}):
        success = False
        break
    curr = mgba.get_coordinates()

if success:
    print("Successfully reached Column 12 on Row 7! Position:", mgba.get_coordinates())
    # Let's check if the Mewtwo switch at (12, 8) is reachable by walking UP/DOWN
    # Stand at (12, 9) facing UP towards (12, 8)
    if walk_step("Down", {"x": 12, "y": 8}):
        print("Walked to (12, 8)!")
        if walk_step("Down", {"x": 12, "y": 9}):
            print("Walked to (12, 9)! Trying to stand at (12, 9) and toggle switch at (12, 8)...")
            mgba.press_buttons(["Up"])
            time.sleep(0.3)
            # Try to toggle the switch
            mgba.press_buttons(["A"])
            time.sleep(1.0)
            # Dismiss NO/YES menu if any
            mgba.press_buttons(["Up", "A"])
            time.sleep(1.0)
            print("Completed switch toggle attempt at (12, 8).")
    else:
        print("Failed to reach (12, 9).")
else:
    print("Failed to reach Column 12 on Row 7.")

