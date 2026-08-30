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
                return "BLOCKED"
            attempts += 1
            time.sleep(0.2)
        if attempts == 2:
            return "BLOCKED"
    return "SUCCESS"

# Start at current (22, 2)
path = [
    # 1. Walk RIGHT along Row 2 to Column 27
    (23, 2), (24, 2), (25, 2), (26, 2), (27, 2),
    # 2. Walk DOWN Column 27 to Row 9
    (27, 3), (27, 4), (27, 5), (27, 6), (27, 7), (27, 8), (27, 9),
    # 3. Walk LEFT to Column 26
    (26, 9),
    # 4. Walk DOWN Column 26 to Row 12
    (26, 10), (26, 11), (26, 12),
    # 5. Walk LEFT to Column 25
    (25, 12),
    # 6. Walk DOWN Column 25 (testing if open in State B!)
    (25, 13), (25, 14), (25, 15), (25, 16), (25, 17),
    # 7. Walk LEFT to Column 19 (testing if balcony gates are open!)
    (24, 17), (23, 17), (22, 17), (21, 17), (20, 17), (19, 17),
    # 8. Drop to B1F West
    (19, 18)
]

print("Executing State B balcony check walk...")
res = walk_path_strict(path)
print(f"Path result: {res}. End position: {mgba.get_coordinates()}")
