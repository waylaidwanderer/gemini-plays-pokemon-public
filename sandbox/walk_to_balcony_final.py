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

# Start at current (12, 12) in State A
path = [
    # 1. Walk Left to Column 11
    (11, 12),
    # 2. Walk UP Column 11 to Row 9
    (11, 11), (11, 10), (11, 9),
    # 3. Walk Right to Column 12
    (12, 9),
    # 4. Walk UP Column 12 to Row 3
    (12, 8), (12, 7), (12, 6), (12, 5), (12, 4), (12, 3),
    # 5. Walk Right along Row 3 to Column 25 (bypasses green windows on Row 2)
    (13, 3), (14, 3), (15, 3), (16, 3), (17, 3), (18, 3), (19, 3), (20, 3), (21, 3), (22, 3), (23, 3), (24, 3), (25, 3),
    # 6. Walk UP Column 25 to Row 2
    (25, 2),
    # 7. Walk Right along Row 2 to Column 27 (bypasses pitfall at 26, 3)
    (26, 2), (27, 2),
    # 8. Walk DOWN Column 27 to Row 16
    (27, 3), (27, 4), (27, 5), (27, 6), (27, 7), (27, 8), (27, 9), (27, 10), (27, 11), (27, 12), (27, 13), (27, 14), (27, 15), (27, 16),
    # 9. Walk Left along Row 16 to Column 20 (bypasses Column 18 Row 16 wall!)
    (26, 16), (25, 16), (24, 16), (23, 16), (22, 16), (21, 16), (20, 16),
    # 10. Walk DOWN Column 20 through open gate to Row 18
    (20, 17), (20, 18),
    # 11. Walk Left to Column 19 (balcony grass drop warp!)
    (19, 18)
]

print("Executing walk to balcony drop in State A...")
res = walk_path_safe(path)
print(f"Path result: {res}. End position: {mgba.get_coordinates()}")
