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

# Starting at (10, 5) on B1F East in State A
# Walk DOWN Column 10 to Row 11, then LEFT to (8, 11)
steps = [
    ("Down", {"x": 10, "y": 6}),
    ("Down", {"x": 10, "y": 7}),
    ("Down", {"x": 10, "y": 8}),
    ("Down", {"x": 10, "y": 9}),
    ("Down", {"x": 10, "y": 10}),
    ("Down", {"x": 10, "y": 11}),  # Open gate in State A!
    ("Left", {"x": 9, "y": 11}),
    ("Left", {"x": 8, "y": 11}),
]

success = True
for direction, coords in steps:
    if not walk_step(direction, coords):
        success = False
        break

if success:
    print("Successfully reached (8, 11) on B1F West! Facing UP and toggling switch at (8, 10) to State B...")
    mgba.press_buttons(["Up"])
    time.sleep(0.3)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])   # Select YES to toggle to State B
    time.sleep(1.0)
    mgba.press_buttons(["B"])   # Dismiss dialog
    time.sleep(0.5)
    print("Switch toggled! Current coordinates:", mgba.get_coordinates())
else:
    print("Failed to reach B1F West switch.")
