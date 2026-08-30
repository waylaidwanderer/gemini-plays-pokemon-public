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

# Walk to (2, 6) on 3F West
path = [
    # 1. Left to Column 23
    (25, 12), (24, 12), (23, 12),
    # 2. UP Column 23 to Row 3
    (23, 11), (23, 10), (23, 9), (23, 8), (23, 7), (23, 6), (23, 5), (23, 4), (23, 3),
    # 3. LEFT along Row 3 to Column 2 on 3F West (completely open corridor!)
    (22, 3), (21, 3), (20, 3), (19, 3), (18, 3), (17, 3), (16, 3), (15, 3), (14, 3), (13, 3), (12, 3), (11, 3), (10, 3), (9, 3), (8, 3), (7, 3), (6, 3), (5, 3), (4, 3), (3, 3), (2, 3),
    # 4. DOWN to (2, 6)
    (2, 4), (2, 5), (2, 6)
]

print("Walking to (2, 6) on 3F West...")
res = walk_path_strict(path)
print(f"Path result: {res}. Position: {mgba.get_coordinates()}")

if mgba.get_coordinates() == {'x': 2, 'y': 6}:
    # Test step Right to (3, 6)
    print("Testing step Right to (3, 6)...")
    test_res = step_strict("Right", 3, 6)
    print(f"Test result: {test_res}. Position: {mgba.get_coordinates()}")
    if test_res == "BLOCKED":
        print("Mansion is in STATE A (Gate at (3,6) is closed).")
    elif test_res == "SUCCESS":
        print("Mansion is in STATE B (Gate at (3,6) is open).")
