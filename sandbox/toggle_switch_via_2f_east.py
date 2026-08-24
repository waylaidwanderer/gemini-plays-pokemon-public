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

# Starting at (2, 13) on 2F West in State A
steps = [
    ("Right", {"x": 3, "y": 13}),
    ("Right", {"x": 4, "y": 13}),
    ("Right", {"x": 5, "y": 13}),
    ("Up", {"x": 5, "y": 12}),
    ("Up", {"x": 5, "y": 11}),
    ("Up", {"x": 5, "y": 10}),
    ("Right", {"x": 6, "y": 10}),
    ("Right", {"x": 7, "y": 10}),
    ("Right", {"x": 8, "y": 10}),
    ("Right", {"x": 9, "y": 10}),
    ("Right", {"x": 10, "y": 10}),
    ("Up", {"x": 10, "y": 9}),
    ("Up", {"x": 10, "y": 8}),  # Open in State A!
    ("Up", {"x": 10, "y": 7}),
    ("Up", {"x": 10, "y": 6}),
    ("Up", {"x": 10, "y": 5}),
    ("Up", {"x": 10, "y": 4}),
    ("Up", {"x": 10, "y": 3}),
    # Cross Row 3 to 2F East
    ("Right", {"x": 11, "y": 3}),
    ("Right", {"x": 12, "y": 3}),
    ("Right", {"x": 13, "y": 3}),
    ("Right", {"x": 14, "y": 3}),
    ("Right", {"x": 15, "y": 3}),
    ("Right", {"x": 16, "y": 3}),
    ("Right", {"x": 17, "y": 3}),
    ("Right", {"x": 18, "y": 3}),
    # Walk DOWN Column 18 to Row 10
    ("Down", {"x": 18, "y": 4}),
    ("Down", {"x": 18, "y": 5}),
    ("Down", {"x": 18, "y": 6}),
    ("Down", {"x": 18, "y": 7}),
    ("Down", {"x": 18, "y": 8}),
    ("Down", {"x": 18, "y": 9}),
    ("Down", {"x": 18, "y": 10}),
    # Walk LEFT along Row 10 to Column 12
    ("Left", {"x": 17, "y": 10}),
    ("Left", {"x": 16, "y": 10}),
    ("Left", {"x": 15, "y": 10}),
    ("Left", {"x": 14, "y": 10}),
    ("Left", {"x": 13, "y": 10}),
    ("Left", {"x": 12, "y": 10}),
    # Stand at (12, 9) facing switch at (12, 8)
    ("Up", {"x": 12, "y": 9}),
]

success = True
for direction, coords in steps:
    if not walk_step(direction, coords):
        success = False
        break

if success:
    print("Successfully reached (12, 9) on 2F East! Interacting with switch...")
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
