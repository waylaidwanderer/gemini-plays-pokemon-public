import mgba
import time

def step_safe(direction, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"Moving {direction} to ({target_x}, {target_y}). Current: {pos_before}")
    mgba.press_buttons([direction])
    time.sleep(0.5)
    pos_after = mgba.get_coordinates()
    
    if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 5 or abs(pos_after['y'] - pos_before['y']) > 5):
        print(f"Warped! From {pos_before} to {pos_after}")
        return "WARPED"
        
    if pos_after['x'] == target_x and pos_after['y'] == target_y:
        return "SUCCESS"
        
    if pos_before == pos_after:
        print(f"Blocked at {pos_before} trying to reach ({target_x}, {target_y})")
        return "BLOCKED"
            
    return "SUCCESS"

def walk_path(coords):
    for target_x, target_y in coords:
        pos = mgba.get_coordinates()
        dx = target_x - pos['x']
        dy = target_y - pos['y']
        
        direction = ""
        if dx > 0: direction = "Right"
        elif dx < 0: direction = "Left"
        elif dy > 0: direction = "Down"
        elif dy < 0: direction = "Up"
        
        if direction == "":
            continue
            
        attempts = 0
        while attempts < 3:
            res = step_safe(direction, target_x, target_y)
            if res == "SUCCESS":
                break
            elif res == "WARPED":
                return "WARPED"
            attempts += 1
            time.sleep(0.2)
        if attempts == 3:
            return "BLOCKED"
    return "SUCCESS"

# We are at (23, 11) on 3F East in State A.
# 1. Walk to 3F East stairs at (22, 1) via Column 26/27 bypass and go down to 2F East
stairs_path_3f = [
    # Walk RIGHT to Column 26
    (24, 11), (25, 11), (26, 11),
    # Walk UP Column 26 to Row 7 (safe from Row 6 pitfall)
    (26, 10), (26, 9), (26, 8), (26, 7),
    # Walk RIGHT to Column 27
    (27, 7),
    # Walk UP Column 27 to Row 3 (bypassing Row 10/11 rubble on Column 27)
    (27, 6), (27, 5), (27, 4), (27, 3),
    # Walk LEFT along Row 3 to Column 22 (safe from Column 26 Row 3 pitfall)
    (26, 3), (25, 3), (24, 3), (23, 3), (22, 3),
    # Walk UP Column 22 to (22, 1) (staircase warp)
    (22, 2),
    (22, 1)
]

print("Walking to 3F East stairs...")
res = walk_path(stairs_path_3f)
print(f"Stairs result: {res}. Position: {mgba.get_coordinates()}")

# 2. On 2F East (landing at (22, 1) on 2F East):
# Walk down Column 22 to Row 11, then Left across Row 11 to 2F West (2, 12)
if mgba.get_coordinates() == {'x': 22, 'y': 1}:
    to_2f_west_path = [
        (22, 2), (22, 3), (22, 4), (22, 5), (22, 6), (22, 7), (22, 8), (22, 9), (22, 10), (22, 11),
        (21, 11), (20, 11), (19, 11), (18, 11), (17, 11), (16, 11), (15, 11), (14, 11), (13, 11), (12, 11), (11, 11), (10, 11), (9, 11), (8, 11), (7, 11), (6, 11), (5, 11), (4, 11), (3, 11), (2, 11),
        (2, 12)
    ]
    print("Walking on 2F East to 2F West switch...")
    res_2f = walk_path(to_2f_west_path)
    print(f"2F walk result: {res_2f}. Position: {mgba.get_coordinates()}")
