import mgba
import time

def step_strict(direction, target_x, target_y):
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
            print(f"BLOCKED! Position did not change while trying to go to {(target_x, target_y)}. Stopping script.")
            return "BLOCKED_STATE"
        elif res == "WARPED":
            return "WARPED"
        time.sleep(0.1)
    return "SUCCESS"

# We are currently at (5, 10). Step Down to (5, 11) to start.
print("Stepping Down to (5, 11)...")
step_strict("Down", 5, 11)

path_to_stairs = [
    # Walk Right along Row 11 to Column 9
    (6, 11), (7, 11), (8, 11), (9, 11),
    # Walk UP Column 9 to Row 6
    (9, 10), (9, 9), (9, 8), (9, 7), (9, 6),
    # Walk Right along Row 6 to Column 22
    (10, 6), (11, 6), (12, 6), (13, 6), (14, 6), (15, 6), (16, 6), (17, 6), (18, 6), (19, 6), (20, 6), (21, 6), (22, 6),
    # Walk UP Column 22 to Row 1 (stairs)
    (22, 5), (22, 4), (22, 3), (22, 2), (22, 1)
]

print("Walking to 2F East stairs at (22, 1)...")
res = walk_path_safe(path_to_stairs)
print(f"Result: {res}. Position: {mgba.get_coordinates()}")

