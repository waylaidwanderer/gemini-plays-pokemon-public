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
    print("Facing UP towards Mewtwo Switch at (12, 11)...")
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

# 1. Path from current (22, 2) to below switch at (12, 12)
path1 = [
    (22, 3), (21, 3), (20, 3), (19, 3), (18, 3), (17, 3), (16, 3), (15, 3), (14, 3), (13, 3), (12, 3),
    (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (12, 9), (12, 10),
    (11, 10),
    (11, 11), (11, 12),
    (12, 12)
]

# 2. Path from (12, 12) to balcony drop at (19, 18)
path2 = [
    (11, 12), (10, 12),
    (10, 13), (10, 14), (10, 15), (10, 16),
    (11, 16), (12, 16), (13, 16), (14, 16), (15, 16), (16, 16), (17, 16), (18, 16), (19, 16), (20, 16), (21, 16),
    (21, 17), (21, 18),
    (20, 18), (19, 18)
]

print("Executing Step 1: Walk to switch at (12, 11)...")
res1 = walk_path_safe(path1)
print(f"Path 1 result: {res1}. Position: {mgba.get_coordinates()}")

if res1 == "SUCCESS" and mgba.get_coordinates() == {'x': 12, 'y': 12}:
    print("Executing Step 2: Toggle Mewtwo Switch...")
    toggle_switch()
    
    print("Executing Step 3: Walk to balcony drop...")
    res2 = walk_path_safe(path2)
    print(f"Path 2 result: {res2}. End position: {mgba.get_coordinates()}")
else:
    print("Failed to reach the switch or was interrupted.")

