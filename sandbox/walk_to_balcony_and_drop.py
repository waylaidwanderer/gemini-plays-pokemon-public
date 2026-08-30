import mgba
import time

def step_strict(direction, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"Moving {direction} to ({target_x}, {target_y}). Current: {pos_before}")
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    
    if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 5 or abs(pos_after['y'] - pos_before['y']) > 5):
        print(f"Warped! From {pos_before} to {pos_after}")
        return "WARPED"
        
    if pos_after['x'] == target_x and pos_after['y'] == target_y:
        return "SUCCESS"
        
    if pos_before == pos_after:
        print(f"FAILED to move {direction} to ({target_x}, {target_y}). Position unchanged at {pos_before}")
        return "BLOCKED"
            
    return "SUCCESS"

def walk_path_strict(coords):
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
        while attempts < 2:
            res = step_strict(direction, target_x, target_y)
            if res == "SUCCESS":
                break
            elif res == "WARPED":
                return "WARPED"
            elif res == "BLOCKED":
                # We hit a battle or a wall. Stop immediately to handle it!
                return "BLOCKED"
            attempts += 1
            time.sleep(0.2)
        if attempts == 2:
            return "BLOCKED"
    return "SUCCESS"

# Start at current (25, 7)
path = [
    # 1. Walk Right to Column 26
    (26, 7),
    # 2. Walk Down Column 26 to Row 17
    (26, 8), (26, 9), (26, 10), (26, 11), (26, 12), (26, 13), (26, 14), (26, 15), (26, 16), (26, 17),
    # 3. Walk Left to Column 19 on Row 17 (balcony gates open in State A!)
    (25, 17), (24, 17), (23, 17), (22, 17), (21, 17), (20, 17), (19, 17),
    # 4. Walk Down Column 19 to Row 18 (balcony drop warp!)
    (19, 18)
]

print("Executing strict walk to balcony drop (no automated escapes)...")
res = walk_path_strict(path)
print(f"Path result: {res}. End position: {mgba.get_coordinates()}")
