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

# Starting at (6, 11) on 2F West (State B)
# 1. Walk UP Column 6 to Row 3
steps_up_col6 = [
    ("Up", {"x": 6, "y": 10}),
    ("Up", {"x": 6, "y": 9}),
    ("Up", {"x": 6, "y": 8}),
    ("Up", {"x": 6, "y": 7}),
    ("Up", {"x": 6, "y": 6}),
    ("Up", {"x": 6, "y": 5}),
    ("Up", {"x": 6, "y": 4}),
    ("Up", {"x": 6, "y": 3}),
]

success = True
for d, c in steps_up_col6:
    if not walk_step(d, c):
        success = False
        break

if success:
    # 2. Walk RIGHT along Row 3 to Column 18
    print("Reached (6, 3)! Walking RIGHT along Row 3 to Column 18...")
    curr = mgba.get_coordinates()
    while curr['x'] < 18:
        if not walk_step("Right", {"x": curr['x'] + 1, "y": 3}):
            success = False
            break
        curr = mgba.get_coordinates()

if success:
    # 3. Walk DOWN Column 18 to Row 10
    print("Reached (18, 3)! Walking DOWN Column 18 to Row 10...")
    curr = mgba.get_coordinates()
    while curr['y'] < 10:
        if not walk_step("Down", {"x": 18, "y": curr['y'] + 1}):
            success = False
            break
        curr = mgba.get_coordinates()

if success:
    # 4. Walk LEFT along Row 10 to Column 15
    print("Reached (18, 10)! Walking LEFT along Row 10 to Column 15...")
    curr = mgba.get_coordinates()
    while curr['x'] > 15:
        if not walk_step("Left", {"x": curr['x'] - 1, "y": 10}):
            success = False
            break
        curr = mgba.get_coordinates()

if success:
    # 5. Step DOWN/LEFT onto the stairs at (15, 11) to warp UP to 3F East
    print("Reached (15, 10)! Standing next to stairs. Walking DOWN onto stairs at (15, 11)...")
    mgba.press_buttons(["Down"])
    time.sleep(1.5)
    pos = mgba.get_coordinates()
    print(f"Warped UP to 3F East! Landing position: {pos}")
else:
    print("Bypass route failed or got blocked.")

