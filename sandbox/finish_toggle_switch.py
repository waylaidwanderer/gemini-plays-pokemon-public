import mgba
import time

# Starting at (16, 10) on 2F East in State A
steps = [
    ("Up", {"x": 16, "y": 9}),
    ("Up", {"x": 16, "y": 8}),  # Open in State A!
    ("Up", {"x": 16, "y": 7}),
    ("Up", {"x": 16, "y": 6}),
    ("Left", {"x": 15, "y": 6}),
    ("Left", {"x": 14, "y": 6}),
    ("Left", {"x": 13, "y": 6}),
    ("Left", {"x": 12, "y": 6}),
    ("Down", {"x": 12, "y": 7}),
    ("Down", {"x": 12, "y": 8}),
    ("Down", {"x": 12, "y": 9}),
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
    print("Successfully reached (12, 9) on 2F East! Interacting with switch...")
    # Stand at (12, 9) facing UP towards switch at (12, 8)
    mgba.press_buttons(["Up"])
    time.sleep(0.3)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])   # Select YES
    time.sleep(1.0)
    mgba.press_buttons(["B"])   # Dismiss dialog
    time.sleep(0.5)
    print("Switch toggled to State B! Current coordinates:", mgba.get_coordinates())
else:
    print("Failed to reach switch on 2F East.")
