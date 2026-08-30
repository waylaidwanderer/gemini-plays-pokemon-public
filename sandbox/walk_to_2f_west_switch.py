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

# 1. Dismiss "Got away safely!" textbox
print("Dismissing battle screen...")
mgba.press_buttons(["A"])
time.sleep(1.0)

pos = mgba.get_coordinates()
print(f"Position in overworld: {pos}")

# Walk from current (26, 3) to the northeast stairs warp (22, 1) on 3F East
path_3f = [
    (25, 3), (24, 3), (23, 3), (22, 3),
    (22, 2),
    (22, 1) # Staircase warp
]

print("Walking to the 3F East stairs...")
res = walk_path(path_3f)
print(f"3F path result: {res}. Position: {mgba.get_coordinates()}")

# On 2F East (landing at 22, 1 on 2F East):
# Walk to 2F West (2, 12) via Row 11
if mgba.get_coordinates() == {'x': 22, 'y': 1}:
    to_2f_west_path = [
        (22, 2), (22, 3), (22, 4), (22, 5), (22, 6), (22, 7), (22, 8), (22, 9), (22, 10), (22, 11),
        (21, 11), (20, 11), (19, 11), (18, 11), (17, 11), (16, 11), (15, 11), (14, 11), (13, 11), (12, 11), (11, 11), (10, 11), (9, 11), (8, 11), (7, 11), (6, 11), (5, 11), (4, 11), (3, 11), (2, 11),
        (2, 12)
    ]
    print("Walking on 2F East to 2F West switch...")
    res_2f = walk_path(to_2f_west_path)
    print(f"2F walk result: {res_2f}. Position: {mgba.get_coordinates()}")
    
    if mgba.get_coordinates() == {'x': 2, 'y': 12}:
        # Face UP
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        
        # Toggle Mewtwo switch to State B with 4 A-presses
        print("Toggling Mewtwo switch to State B...")
        mgba.press_buttons(["A"])
        time.sleep(2.5)
        mgba.press_buttons(["A"])
        time.sleep(2.5)
        mgba.press_buttons(["A"])
        time.sleep(2.5)
        mgba.press_buttons(["A"])
        time.sleep(2.5)
