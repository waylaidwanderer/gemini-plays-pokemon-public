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

# Start at current (4, 3)
path_to_switch_front = [
    # 1. Down to (4, 4)
    (4, 4),
    # 2. Left to (3, 4)
    (3, 4),
    # 3. Down to (3, 5)
    (3, 5),
    # 4. Down to (3, 6)
    (3, 6),
    # 5. Left to (2, 6)
    (2, 6)
]

print("Walking to (2, 6) on 3F West...")
res = walk_path_strict(path_to_switch_front)
print(f"Path result: {res}. Position: {mgba.get_coordinates()}")

if mgba.get_coordinates() == {'x': 2, 'y': 6}:
    # Face UP towards (2, 5)
    print("Facing UP towards the switch at (2, 5)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # Toggle switch with 4 A-presses and 2.5-second delays
    print("Toggling Mewtwo switch to State A...")
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    print("Mewtwo switch toggled to State A successfully from the front!")
    
    # Walk to the balcony drop in State A!
    path_to_balcony = [
        # 1. UP Column 2 to Row 2
        (2, 5), (2, 4), (2, 3), (2, 2),
        # 2. Walk RIGHT along Row 2 to Column 25 (completely open in State A!)
        (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2), (10, 2), (11, 2), (12, 2), (13, 2), (14, 2), (15, 2), (16, 2), (17, 2), (18, 2), (19, 2), (20, 2), (21, 2), (22, 2), (23, 2), (24, 2), (25, 2),
        # 3. Walk DOWN Column 25 to Row 17 (shutter gate at 25, 13 is open in State A!)
        (25, 3), (25, 4), (25, 5), (25, 6), (25, 7), (25, 8), (25, 9), (25, 10), (25, 11), (25, 12), (25, 13), (25, 14), (25, 15), (25, 16), (25, 17),
        # 4. Walk LEFT along Row 17 to Column 19 (balcony gates open in State A!)
        (24, 17), (23, 17), (22, 17), (21, 17), (20, 17), (19, 17),
        # 5. Walk DOWN Column 19 to Row 18 (balcony drop warp!)
        (19, 18)
    ]
    print("Walking to the balcony drop in State A...")
    res_balcony = walk_path_strict(path_to_balcony)
    print(f"Balcony result: {res_balcony}. Final position: {mgba.get_coordinates()}")
