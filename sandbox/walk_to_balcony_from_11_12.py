import mgba
import time

def run_from_battle():
    print("Detected possible battle! Attempting to escape...")
    for _ in range(3):
        mgba.press_buttons(["B"])
        time.sleep(0.3)
    
    # Down, Right, A to select RUN
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
    time.sleep(2.0)
    
    mgba.press_buttons(["A"])
    time.sleep(1.0)

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

def walk_path_robust(path):
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
            time.sleep(0.5)
            pos_after = mgba.get_coordinates()
            if pos_after['x'] == target_x and pos_after['y'] == target_y:
                idx += 1
                continue
            run_from_battle()
            pos_current = mgba.get_coordinates()
            print(f"Current position after run attempt: {pos_current}")
            if pos_current == pos:
                print("Retrying step...")
            else:
                print("Position changed after escape, re-aligning path...")
        elif res == "WARPED":
            return "WARPED"
        time.sleep(0.1)
    return "SUCCESS"

# Start at current (11, 12) in State A
path = [
    (11, 11), (11, 10), (11, 9),
    (12, 9),
    (12, 8), (12, 7), (12, 6), (12, 5), (12, 4), (12, 3), (12, 2),
    (13, 2), (14, 2), (15, 2), (16, 2), (17, 2), (18, 2), (19, 2), (20, 2), (21, 2), (22, 2), (23, 2), (24, 2), (25, 2), (26, 2), (27, 2),
    (27, 3), (27, 4), (27, 5), (27, 6), (27, 7), (27, 8), (27, 9), (27, 10), (27, 11), (27, 12), (27, 13), (27, 14), (27, 15), (27, 16), (27, 17),
    (26, 17), (25, 17), (24, 17), (23, 17), (22, 17), (21, 17), (20, 17), (19, 17),
    (19, 18)
]

print("Executing walk to balcony drop...")
res = walk_path_robust(path)
print(f"Path result: {res}. End position: {mgba.get_coordinates()}")
