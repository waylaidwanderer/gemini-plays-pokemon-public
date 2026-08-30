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

# Start at current (25, 3)
path = [
    # 1. Walk UP to Row 2
    (25, 2),
    # 2. Walk RIGHT to Column 27 (safe from Column 26 pitfalls!)
    (26, 2), (27, 2),
    # 3. Walk DOWN Column 27 to Row 9
    (27, 3), (27, 4), (27, 5), (27, 6), (27, 7), (27, 8), (27, 9),
    # 4. Walk LEFT to Column 26 on Row 9 (safe!)
    (26, 9),
    # 5. Walk DOWN Column 26 to Row 12 (safe!)
    (26, 10), (26, 11), (26, 12),
    # 6. Walk LEFT to Column 25
    (25, 12),
    # 7. Walk DOWN Column 25 to Row 17 (shutter gate at 25, 13 is open in State A!)
    (25, 13), (25, 14), (25, 15), (25, 16), (25, 17),
    # 8. Walk LEFT along Row 17 to Column 19 (balcony gates open in State A!)
    (24, 17), (23, 17), (22, 17), (21, 17), (20, 17), (19, 17),
    # 9. Walk DOWN Column 19 to Row 18 (balcony drop warp!)
    (19, 18)
]

print("Executing walk to balcony drop in State A...")
res = walk_path_strict(path)
print(f"Path result: {res}. End position: {mgba.get_coordinates()}")
