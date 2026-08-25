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

# Start at (15, 7) on 2F East
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
    # 2. Walk DOWN Column 12 to Row 11
    steps_down = [
        ("Down", {"x": 12, "y": 8}),
        ("Down", {"x": 12, "y": 9}),
        ("Down", {"x": 12, "y": 10}),
        ("Down", {"x": 12, "y": 11}),
    ]
    for d, c in steps_down:
        if not walk_step(d, c):
            success = False
            break

if success:
    print("Reached (12, 11)! Facing RIGHT towards the switch...")
    mgba.press_buttons(["Right"])
    time.sleep(0.3)
    print("Current position:", mgba.get_coordinates())
else:
    print("Failed to reach (12, 11).")
