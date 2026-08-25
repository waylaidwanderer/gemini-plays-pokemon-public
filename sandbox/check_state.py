import mgba
import time

def run_from_battle():
    print("In battle! Attempting to escape...")
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)
    mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A"])
    time.sleep(1.5)
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)
    return mgba.get_coordinates()

def walk_step(direction, expected_coords, retries=15):
    for i in range(retries):
        mgba.press_buttons([direction])
        time.sleep(0.3)
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            print(f"Moved {direction}, current position: {pos}")
            return True
        if pos == {"x": 0, "y": 0}:
            run_from_battle()
            pos = mgba.get_coordinates()
            if pos == expected_coords:
                return True
        print(f"Blocked! Retrying {direction} to {expected_coords} (attempt {i+1}/{retries}), current: {pos}")
        time.sleep(0.2)
    return False

# Starting at (15, 7) on 2F East
# 1. Walk LEFT along Row 7 to Column 12
steps_left = [
    ("Left", {"x": 14, "y": 7}),
    ("Left", {"x": 13, "y": 7}),
    ("Left", {"x": 12, "y": 7}),
]
success = True
for d, c in steps_left:
    if not walk_step(d, c):
        success = False
        break

if success:
    # 2. Test if we can walk DOWN to (12, 8)
    print("Testing if (12, 8) is open...")
    if walk_step("Down", {"x": 12, "y": 8}):
        print("Mansion is in STATE B! Gate at (12, 8) is OPEN.")
    else:
        print("Mansion is in STATE A! Gate at (12, 8) is CLOSED.")
