import mgba
import time

def step_strict(direction, target_x, target_y):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    
    if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 5 or abs(pos_after['y'] - pos_before['y']) > 5):
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

# Start at current (23, 5)
path = [
    # 1. Walk Right along Row 5 to Column 27
    (24, 5), (25, 5), (26, 5), (27, 5),
    # 2. Walk UP Column 27 to Row 2
    (27, 4), (27, 3), (27, 2),
    # 3. Walk LEFT along Row 2 to (22, 2)
    (26, 2), (25, 2), (24, 2), (23, 2), (22, 2)
]

print("Walking to (22, 2)...")
res = walk_path_strict(path)
print(f"Path result: {res}. Position: {mgba.get_coordinates()}")

if mgba.get_coordinates() == {'x': 22, 'y': 2}:
    # Test step Left to (21, 2)
    print("Testing step Left to (21, 2)...")
    test_res = step_strict("Left", 21, 2)
    print(f"Test result: {test_res}. Position: {mgba.get_coordinates()}")
    if test_res == "BLOCKED":
        print("RESULT: Mansion is in STATE B (Gate at (21,2) is closed).")
    elif test_res == "SUCCESS":
        print("RESULT: Mansion is in STATE A (Gate at (21,2) is open).")
