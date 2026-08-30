import mgba
import time

def step_strict(direction, target_x, target_y):
    # Allow 2 attempts per step to handle turning-in-place/lag
    for attempt in range(2):
        pos_before = mgba.get_coordinates()
        mgba.press_buttons([direction])
        time.sleep(0.4)
        pos_after = mgba.get_coordinates()
        
        # Check if coordinates changed significantly, indicating a warp
        if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 5 or abs(pos_after['y'] - pos_before['y']) > 5):
            print(f"WARPED! From {pos_before} to {pos_after}")
            return "WARPED"
        if pos_after['x'] == target_x and pos_after['y'] == target_y:
            return "SUCCESS"
        time.sleep(0.1)
    return "BLOCKED"

def walk_path_safe(path):
    idx = 0
    while idx < len(path):
        target_x, target_y = path[idx]
        pos = mgba.get_coordinates()
        dx = target_x - pos['x']
        dy = target_y - pos['y']
        
        direction = ""
        if dx > 0: direction = "Right"
        elif dx < 0: direction = "Left"
        elif dy > 0: direction = "Down"
        elif dy < 0: direction = "Up"
        
        if direction == "":
            idx += 1
            continue
            
        res = step_strict(direction, target_x, target_y)
        if res == "SUCCESS":
            idx += 1
        elif res == "BLOCKED":
            print(f"BLOCKED! Position did not change while trying to go to {(target_x, target_y)}. Stopping script.")
            return "BLOCKED_STATE"
        elif res == "WARPED":
            return "WARPED"
        time.sleep(0.1)
    return "SUCCESS"

# Walk from current (10, 7) to 3F West stairs at (5, 10) in State B via Column 12 and Row 11
path = [
    # 1. UP Column 10 to Row 1
    (10, 6), (10, 5), (10, 4), (10, 3), (10, 2), (10, 1),
    # 2. Right along Row 1 to Column 12
    (11, 1), (12, 1),
    # 3. DOWN Column 12 to Row 11 (bypasses Row 8 rubble)
    (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (12, 9), (12, 10), (12, 11),
    # 4. Walk Left along Row 11 to Column 5 (bypasses closed gate at 8,10)
    (11, 11), (10, 11), (9, 11), (8, 11), (7, 11), (6, 11), (5, 11),
    # 5. Walk UP Column 5 into stairs at (5, 10) -> triggers warp DOWN to 2F West!
    (5, 10)
]

print("Walking from (10, 7) to 3F West stairs at (5, 10) via Column 12...")
res = walk_path_safe(path)
print(f"Path result: {res}. End position: {mgba.get_coordinates()}")

