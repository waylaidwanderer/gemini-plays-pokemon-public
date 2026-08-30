import mgba
import time

def step_strict(direction, target_x, target_y):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    
    if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 5 or abs(pos_after['y'] - pos_before['y']) > 5):
        print(f"WARPED! From {pos_before} to {pos_after}")
        return "WARPED"
    if pos_after['x'] == target_x and pos_after['y'] == target_y:
        return "SUCCESS"
    if pos_before == pos_after:
        return "BLOCKED"
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
            print(f"BLOCKED! Position did not change while trying to go to {(target_x, target_y)}. This is likely a wild battle. Stopping script.")
            return "BATTLE"
        elif res == "WARPED":
            return "WARPED"
        time.sleep(0.1)
    return "SUCCESS"

# Start at current (27, 9) in State A
path = [
    (26, 9),
    (26, 10),
    (25, 10),
    (25, 11), (25, 12), (25, 13), (25, 14), (25, 15), (25, 16),
    (24, 16), (23, 16), (22, 16), (21, 16), (20, 16), (19, 16),
    (19, 17), (19, 18)
]

print("Executing safe walk to balcony drop...")
res = walk_path_safe(path)
print(f"Path result: {res}. End position: {mgba.get_coordinates()}")
