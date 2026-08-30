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

# Walk path from current (20, 3) on 3F East/Central to the pitfall at (18, 16) in State B!
path = [
    (20, 2),
    # Row 2 horizontal to Column 25
    (21, 2), (22, 2), (23, 2), (24, 2), (25, 2),
    # Column 25 vertical to Row 16 (gate at (25, 13) is OPEN in State B!)
    (25, 3), (25, 4), (25, 5), (25, 6), (25, 7), (25, 8), (25, 9), (25, 10), (25, 11), (25, 12), (25, 13), (25, 14), (25, 15), (25, 16),
    # Row 16 horizontal to the pitfall at (18, 16)
    (24, 16), (23, 16), (22, 16), (21, 16), (20, 16), (19, 16), (18, 16)
]

print("Executing walk path to pitfall...")
res = walk_path(path)
print("Path result:", res)
mgba.take_screenshot()
