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

# Starting at (7, 14) on 3F West (State B)
# 1. Walk back to (6, 11)
steps = [
    ("Left", {"x": 6, "y": 14}),
    ("Left", {"x": 5, "y": 14}),
    ("Up", {"x": 5, "y": 13}),
    ("Up", {"x": 5, "y": 12}),
    ("Up", {"x": 5, "y": 11}),
    ("Right", {"x": 6, "y": 11}),
]

success = True
for d, c in steps:
    if not walk_step(d, c):
        success = False
        break

if success:
    print("Reached (6, 11)! Walking UP Column 6 to Row 6...")
    steps_up_col6 = [
        ("Up", {"x": 6, "y": 10}),
        ("Up", {"x": 6, "y": 9}),
        ("Up", {"x": 6, "y": 8}),
        ("Up", {"x": 6, "y": 7}),
        ("Up", {"x": 6, "y": 6}),
    ]
    for d, c in steps_up_col6:
        if not walk_step(d, c):
            print(f"Failed to walk up past {mgba.get_coordinates()} on Column 6!")
            success = False
            break
            
    if success:
        print("Successfully reached Row 6 on Column 6! Walking to 3F East...")
        # Walk Right to Column 11/12
        curr = mgba.get_coordinates()
        while curr['x'] < 11:
            if not walk_step("Right", {"x": curr['x'] + 1, "y": 6}):
                success = False
                break
            curr = mgba.get_coordinates()
            
        if success:
            print("Successfully reached 3F East on Row 6! Position:", mgba.get_coordinates())
else:
    print("Failed to reach (6, 11).")

