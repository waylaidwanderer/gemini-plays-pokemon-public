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

def toggle_switch():
    print("Toggling Mewtwo Switch at (2, 11) from (2, 12)...")
    mgba.press_buttons(["Up"])
    time.sleep(1.0)
    
    print("Pressing A (1/4)...")
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    
    print("Pressing A (2/4)...")
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    
    print("Pressing A (3/4)...")
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    
    print("Pressing A (4/4)...")
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    print("Switch toggle complete.")

# 1. Path from current (5, 11) to (2, 12)
path_to_switch = [
    (4, 11), (3, 11), (3, 12), (2, 12)
]

print("Walking to switch...")
res = walk_path_safe(path_to_switch)
print(f"Walk result: {res}. Position: {mgba.get_coordinates()}")

if mgba.get_coordinates() == {'x': 2, 'y': 12}:
    toggle_switch()
    
    # 2. Path back to stairs at (5, 11)
    path_to_stairs = [
        (3, 12), (3, 11), (4, 11), (5, 11)
    ]
    print("Walking back to 2F West stairs...")
    res_back = walk_path_safe(path_to_stairs)
    print(f"Walk back result: {res_back}. Position: {mgba.get_coordinates()}")

