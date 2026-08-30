import mgba
import time

def handle_battle_if_present():
    print("Detected battle. Fleeing...")
    mgba.press_buttons(["B"])
    time.sleep(0.8)
    mgba.press_buttons(["Down", "sleep 300", "Right", "sleep 300", "A"])
    time.sleep(2.0)
    mgba.press_buttons(["B"])
    time.sleep(1.0)

def step_safe(direction, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"Moving {direction} to ({target_x}, {target_y}). Current: {pos_before}")
    mgba.press_buttons([direction])
    time.sleep(0.6)
    pos_after = mgba.get_coordinates()
    
    # Check for warp
    if abs(pos_after['x'] - pos_before['x']) > 5 or abs(pos_after['y'] - pos_before['y']) > 5:
        print(f"WARPED! From {pos_before} to {pos_after}")
        return "WARPED"
        
    if pos_after['x'] == target_x and pos_after['y'] == target_y:
        return "SUCCESS"
        
    # Check if blocked
    if pos_before == pos_after:
        handle_battle_if_present()
        mgba.press_buttons([direction])
        time.sleep(0.6)
        pos_after = mgba.get_coordinates()
        if abs(pos_after['x'] - pos_before['x']) > 5 or abs(pos_after['y'] - pos_before['y']) > 5:
            print(f"WARPED on retry! From {pos_before} to {pos_after}")
            return "WARPED"
        if pos_after['x'] == target_x and pos_after['y'] == target_y:
            return "SUCCESS"
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
            
        res = step_safe(direction, target_x, target_y)
        if res == "WARPED":
            return "WARPED"
        elif res == "BLOCKED":
            print(f"Failed to reach ({target_x}, {target_y}). Aborting.")
            return "BLOCKED"
    return "SUCCESS"

# 1. Walk from current (17, 9) to (2, 6)
path_to_switch = [
    (17, 8), (17, 7), (17, 6), (17, 5), (17, 4), (17, 3),
    (16, 3), (15, 3), (14, 3), (13, 3), (12, 3), (11, 3), (10, 3), (9, 3), (8, 3), (7, 3), (6, 3), (5, 3), (4, 3), (3, 3), (2, 3),
    (2, 4), (2, 5), (2, 6)
]

print("Executing path to switch...")
res = walk_path(path_to_switch)
if res == "SUCCESS":
    print("Arrived at (2, 6). Facing UP to interact with switch at (2, 5)...")
    # Face UP
    mgba.press_buttons(["Up"])
    time.sleep(0.6)
    
    # 4 A-press sequence to toggle switch to State B
    print("Interacting with Mewtwo switch...")
    mgba.press_buttons(["A"])
    time.sleep(2.0)
    mgba.press_buttons(["A"])
    time.sleep(2.0)
    mgba.press_buttons(["A"])
    time.sleep(2.0)
    mgba.press_buttons(["A"])
    time.sleep(2.0)
    
    print("Switch toggled. Walking back to 3F East Row 16...")
    path_back = [
        (2, 5), (2, 4), (2, 3),
        (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (12, 3), (13, 3), (14, 3), (15, 3), (16, 3), (17, 3), (18, 3), (19, 3), (20, 3), (21, 3), (22, 3), (23, 3), (24, 3), (25, 3),
        (25, 4), (25, 5), (25, 6), (25, 7), (25, 8), (25, 9), (25, 10), (25, 11), (25, 12), (25, 13), (25, 14), (25, 15), (25, 16),
        (24, 16), (23, 16), (22, 16), (21, 16), (20, 16), (19, 16), (18, 16)
    ]
    res_back = walk_path(path_back)
    print("Path back result:", res_back)
    mgba.take_screenshot()
else:
    print("Failed to reach switch path.")
