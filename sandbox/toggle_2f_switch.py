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

# From (5, 10) to (2, 12) on 2F West
steps = [
    ("Down", {"x": 5, "y": 11}),
    ("Down", {"x": 5, "y": 12}),
    ("Down", {"x": 5, "y": 13}),
    ("Left", {"x": 4, "y": 13}),
    ("Left", {"x": 3, "y": 13}), # The gap in the rubble!
    ("Left", {"x": 2, "y": 13}),
    ("Up", {"x": 2, "y": 12}),
]

success = True
for direction, coords in steps:
    if not walk_step(direction, coords):
        success = False
        break

if success:
    print("Reached (2, 12) on 2F West successfully! Facing UP and interacting with switch...")
    mgba.press_buttons(["Up"])
    time.sleep(0.3)
    mgba.press_buttons(["A"])   # Opens switch menu
    time.sleep(1.0)
    mgba.press_buttons(["A"])   # Selects YES to toggle
    time.sleep(1.0)
    mgba.press_buttons(["B"])   # Dismisses textbox
    time.sleep(0.5)
    print("Switch toggled!")
    print("Current position:", mgba.get_coordinates())
else:
    print("Failed to reach switch.")
