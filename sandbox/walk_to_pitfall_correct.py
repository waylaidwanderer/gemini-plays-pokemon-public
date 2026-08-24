import mgba
import time
import os

# Clean up obsolete workspace files
obsolete_files = [
    "walk_to_statue_2f.py",
    "test_col9_up.py",
    "go_to_2f_east_switch.py",
    "mansion_2f_traverse.py"
]
for f in obsolete_files:
    if os.path.exists(f):
        try:
            os.remove(f)
            print(f"Deleted obsolete file: {f}")
        except Exception as e:
            print(f"Error deleting {f}: {e}")

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

# Starting at (1, 10) on 3F West in State A
steps_to_switch = [
    ("Down", {"x": 1, "y": 11}),
    ("Down", {"x": 1, "y": 12}),
    ("Down", {"x": 1, "y": 13}),
    ("Right", {"x": 2, "y": 13}),
    ("Up", {"x": 2, "y": 12}),
]

success = True
for direction, coords in steps_to_switch:
    if not walk_step(direction, coords):
        success = False
        break

if success:
    print("Reached (2, 12) successfully! Toggling the switch to State B...")
    # Stand at (2, 12) facing UP towards statue at (2, 11) and toggle
    mgba.press_buttons(["Up"])
    time.sleep(0.3)
    mgba.press_buttons(["A"])   # Opens "A secret switch! Press it?"
    time.sleep(1.0)             # Wait for text scroll
    mgba.press_buttons(["A"])   # Selects YES and toggles
    time.sleep(1.0)             # Wait for toggle transition
    mgba.press_buttons(["B"])   # Safely dismisses the text box
    time.sleep(0.5)
    print("Switch toggled!")

    # 2. Walk the State B bypass route to Row 6 on 3F West
    steps_bypass_to_row6 = [
        ("Down", {"x": 2, "y": 13}),
        ("Left", {"x": 1, "y": 13}),
        ("Up", {"x": 1, "y": 12}),
        ("Up", {"x": 1, "y": 11}),
        ("Up", {"x": 1, "y": 10}),
        ("Up", {"x": 1, "y": 9}),  # Now OPEN in State B!
        ("Up", {"x": 1, "y": 8}),
        ("Up", {"x": 1, "y": 7}),
        ("Up", {"x": 1, "y": 6}),
        # Row 6 horizontal walk to (19, 6)
        ("Right", {"x": 2, "y": 6}),
        ("Right", {"x": 3, "y": 6}),
        ("Right", {"x": 4, "y": 6}),
        ("Right", {"x": 5, "y": 6}),
        ("Right", {"x": 6, "y": 6}),
        ("Right", {"x": 7, "y": 6}),
        ("Right", {"x": 8, "y": 6}),
        ("Right", {"x": 9, "y": 6}),
        ("Right", {"x": 10, "y": 6}),
        ("Right", {"x": 11, "y": 6}),
        ("Right", {"x": 12, "y": 6}), # Crosses to 3F East
        ("Right", {"x": 13, "y": 6}),
        ("Right", {"x": 14, "y": 6}),
        ("Right", {"x": 15, "y": 6}),
        ("Right", {"x": 16, "y": 6}),
        ("Right", {"x": 17, "y": 6}),
        ("Right", {"x": 18, "y": 6}),
        ("Right", {"x": 19, "y": 6}),
        # Up Column 19 to Row 3
        ("Up", {"x": 19, "y": 5}),
        ("Up", {"x": 19, "y": 4}),
        ("Up", {"x": 19, "y": 3}),
        # Right along Row 3 to (26, 3)
        ("Right", {"x": 20, "y": 3}),
        ("Right", {"x": 21, "y": 3}),
        ("Right", {"x": 22, "y": 3}),
        ("Right", {"x": 23, "y": 3}),
        ("Right", {"x": 24, "y": 3}),
        ("Right", {"x": 25, "y": 3}),
        ("Right", {"x": 26, "y": 3}),
    ]

    for direction, coords in steps_bypass_to_row6:
        if not walk_step(direction, coords):
            success = False
            break

    if success:
        print("Reached (26, 3) successfully! Stepping DOWN to trigger pitfall...")
        mgba.press_buttons(["Down"])
        time.sleep(1.0) # Wait for drop animation
        pos = mgba.get_coordinates()
        print(f"Dropped! New coordinates: {pos}")
        img_path = mgba.take_screenshot()
        print(f"Screenshot saved to {img_path}")
    else:
        print("Bypass or horizontal walk failed.")
else:
    print("Failed to reach the switch.")
