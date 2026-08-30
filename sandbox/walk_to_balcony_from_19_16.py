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

# Start at current (19, 16)
path = [
    (20, 16),
    (20, 17),
    (20, 18),
    (19, 18)
]

print("Executing final balcony drop via Column 20...")
res = walk_path_robust(path)
print(f"Path result: {res}. End position: {mgba.get_coordinates()}")
