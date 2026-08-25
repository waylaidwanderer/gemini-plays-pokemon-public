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

# Starting at (5, 12) on 3F West (State B)
# 1. Walk to (6, 11)
steps_to_col6 = [
    ("Up", {"x": 5, "y": 11}),
    ("Right", {"x": 6, "y": 11}),
]

success = True
for d, c in steps_to_col6:
    if not walk_step(d, c):
        success = False
        break

if success:
    # 2. Walk UP Column 6 to Row 6
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
            print(f"Failed to walk UP past {mgba.get_coordinates()} on Column 6!")
            success = False
            break

if success:
    # 3. Walk RIGHT along Row 6 to Column 20 (crossing horizontally to 3F East!)
    print("Reached (6, 6)! Walking RIGHT along Row 6 to Column 20...")
    curr = mgba.get_coordinates()
    while curr['x'] < 20:
        if not walk_step("Right", {"x": curr['x'] + 1, "y": 6}):
            success = False
            break
            curr = mgba.get_coordinates()

if success:
    # 4. Walk UP Column 20 to Row 3
    print("Reached (20, 6)! Walking UP Column 20 to Row 3...")
    steps_up_col20 = [
        ("Up", {"x": 20, "y": 5}),
        ("Up", {"x": 20, "y": 4}),
        ("Up", {"x": 20, "y": 3}),
    ]
    for d, c in steps_up_col20:
        if not walk_step(d, c):
            success = False
            break

if success:
    # 5. Walk RIGHT along Row 3 to Column 26
    print("Reached (20, 3)! Walking RIGHT along Row 3 to Column 26...")
    curr = mgba.get_coordinates()
    while curr['x'] < 26:
        if not walk_step("Right", {"x": curr['x'] + 1, "y": 3}):
            success = False
            break
            curr = mgba.get_coordinates()

if success:
    # 6. Step DOWN onto Column 26 Row 4 to drop to 1F East
    print("Reached (26, 3) on 3F East! Stepping DOWN to trigger pitfall...")
    mgba.press_buttons(["Down"])
    time.sleep(2.0) # Wait for drop animation
    pos = mgba.get_coordinates()
    print(f"Landed on 1F East inside fenced room! Position: {pos}")
else:
    print("Failed to complete walk_col6_and_drop.")

