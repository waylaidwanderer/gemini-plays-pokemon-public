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

# 1. Walk from current (3, 11) to 2F West stairs at (5, 11)
path_to_stairs = [
    (4, 11), (5, 11)
]

print("Walking to 2F West stairs at (5, 11)...")
walk_path_safe(path_to_stairs)

if mgba.get_coordinates() == {'x': 5, 'y': 11}:
    print("Warping UP to 3F West...")
    warp_res = step_strict("Up", 5, 10)
    print(f"Warp result: {warp_res}. Position: {mgba.get_coordinates()}")
    
    if warp_res == "WARPED" or mgba.get_coordinates() == {'x': 5, 'y': 11}:
        print("Arrived on 3F West! Walking to northeast area on Row 1...")
        path_to_row1 = [
            # Walk Right along Row 11 to Column 10
            (6, 11), (7, 11), (8, 11), (9, 11), (10, 11),
            # UP Column 10 to Row 9
            (10, 10), (10, 9),
            # Right to Column 12
            (11, 9), (12, 9),
            # UP Column 12 to Row 1
            (12, 8), (12, 7), (12, 6), (12, 5), (12, 4), (12, 3), (12, 2), (12, 1),
            # Right along Row 1 to Column 21
            (13, 1), (14, 1), (15, 1), (16, 1), (17, 1), (18, 1), (19, 1), (20, 1), (21, 1)
        ]
        res = walk_path_safe(path_to_row1)
        print(f"Walk to Row 1 result: {res}. Position: {mgba.get_coordinates()}")
        
        if mgba.get_coordinates() == {'x': 21, 'y': 1}:
            # Systematically test columns 21, 22, 23, 24, 25 to find the warp!
            for col in range(22, 26):
                print(f"Testing Column {col} on Row 1...")
                res_step = step_strict("Right", col, 1)
                if res_step == "WARPED":
                    print(f"WARPED DOWN at Column {col} Row 1!!!")
                    break
                elif res_step == "SUCCESS":
                    print(f"Column {col} is open. Trying UP/DOWN/LEFT/RIGHT to find warp...")
                    # Stand at (col, 1) and try UP
                    test_up = step_strict("Up", col, 0)
                    if test_up == "WARPED":
                        print(f"WARPED DOWN at Column {col} Row 1 (via UP)!!!")
                        break
                    # Stand at (col, 1) and try DOWN
                    test_down = step_strict("Down", col, 2)
                    if test_down == "WARPED":
                        print(f"WARPED DOWN at Column {col} Row 1 (via DOWN)!!!")
                        break
                    # Step back to Row 1 to continue
                    if mgba.get_coordinates() == {'x': col, 'y': 2}:
                        step_strict("Up", col, 1)
                else:
                    print(f"Column {col} is BLOCKED.")
                    break
else:
    print("Could not reach stairs.")

