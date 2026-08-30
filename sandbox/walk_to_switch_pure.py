import mgba
import time

def step_strict(direction, target_x, target_y):
    # Allow 2 attempts per step to handle turning-in-place/lag
    for attempt in range(2):
        pos_before = mgba.get_coordinates()
        mgba.press_buttons([direction])
        time.sleep(0.4)
        pos_after = mgba.get_coordinates()
        
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
            print(f"BLOCKED! Position did not change while trying to go to {(target_x, target_y)}. Stopping script for manual handling.")
            return "BLOCKED_STATE"
        elif res == "WARPED":
            return "WARPED"
        time.sleep(0.1)
    return "SUCCESS"

# Start at current (23, 16) in State B
path = [
    # 1. Right to Column 24
    (24, 16),
    # 2. UP Column 24 to Row 10
    (24, 15), (24, 14), (24, 13), (24, 12), (24, 11), (24, 10),
    # 3. Right to Column 26
    (25, 10), (26, 10),
    # 4. UP Column 26 to Row 3
    (26, 9), (26, 8), (26, 7), (26, 6), (26, 5), (26, 4), (26, 3),
    # 5. Left along Row 3 to Column 12
    (25, 3), (24, 3), (23, 3), (22, 3), (21, 3), (20, 3), (19, 3), (18, 3), (17, 3), (16, 3), (15, 3), (14, 3), (13, 3), (12, 3),
    # 6. DOWN Column 12 to Row 10
    (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (12, 9), (12, 10),
    # 7. Detour around switch: Left to Column 11, DOWN to Row 12, Right to Column 12
    (11, 10),
    (11, 11), (11, 12),
    (12, 12)
]

print("Walking to switch cleanly from (23, 16)...")
res = walk_path_safe(path)
print(f"Path result: {res}. End position: {mgba.get_coordinates()}")
