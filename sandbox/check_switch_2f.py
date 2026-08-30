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

# 1. Warp DOWN to 2F West from 3F West (5, 10)
print("Stepping DOWN into stairs to warp to 2F West...")
warp_res = step_strict("Down", 5, 10)
print(f"Warp result: {warp_res}. Position: {mgba.get_coordinates()}")

if warp_res == "WARPED" or mgba.get_coordinates() == {'x': 5, 'y': 11}:
    print("Arrived on 2F West! Walking to (2, 12)...")
    path_to_switch = [
        (4, 11), (3, 11), (3, 12), (2, 12)
    ]
    res = walk_path_safe(path_to_switch)
    print(f"Walk result: {res}. Position: {mgba.get_coordinates()}")
    
    if mgba.get_coordinates() == {'x': 2, 'y': 12}:
        print("Facing UP...")
        mgba.press_buttons(["Up"])
        time.sleep(1.0)
        
        # Take a screenshot to inspect if there is a Mewtwo statue at (2, 11)
        screenshot_path = mgba.take_screenshot()
        print(f"Screenshot taken at {screenshot_path}")
else:
    print("Failed to warp DOWN to 2F.")

