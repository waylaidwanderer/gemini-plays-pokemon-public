import mgba
import time

def step_strict(direction, target_x, target_y):
    for attempt in range(2):
        pos_before = mgba.get_coordinates()
        mgba.press_buttons([direction])
        time.sleep(0.4)
        pos_after = mgba.get_coordinates()
        
        if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 5 or abs(pos_after['y'] - pos_before['y']) > 5):
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
            return "BLOCKED"
        elif res == "WARPED":
            return "WARPED"
        time.sleep(0.1)
    return "SUCCESS"

def toggle_switch():
    print("Toggling Mewtwo Switch...")
    mgba.press_buttons(["Up"])
    time.sleep(1.0)
    for _ in range(4):
        mgba.press_buttons(["A"])
        time.sleep(2.5)

# 1. Walk from (10, 3) in State B to (2, 6)
path_to_switch = [
    (10, 2), (9, 2), (8, 2), (7, 2), (6, 2), (5, 2), (4, 2), (3, 2), (2, 2),
    (2, 3), (2, 4), (1, 4), (1, 5), (1, 6), (2, 6)
]

print("Walking to switch...")
res = walk_path_safe(path_to_switch)
print(f"Path to switch result: {res}. Position: {mgba.get_coordinates()}")

if mgba.get_coordinates() == {'x': 2, 'y': 6}:
    toggle_switch()
    
    # Verify State A
    print("Verifying State A...")
    test_res = step_strict("Right", 3, 6)
    if test_res == "BLOCKED":
        print("VERIFIED STATE A. Testing crossings on Row 12/13...")
        
        # Walk back to Row 12 West via Column 1, Row 3, Column 12, Row 9
        path_to_row12 = [
            (1, 6), (1, 5), (1, 4), (1, 3),
            (2, 3), (2, 4), (3, 4), (4, 4), (4, 3),
            (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (12, 3),
            (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (12, 9), (12, 10), (12, 11), (12, 12)
        ]
        res_row12 = walk_path_safe(path_to_row12)
        print(f"Path to Row 12 result: {res_row12}. Position: {mgba.get_coordinates()}")
        
        if mgba.get_coordinates() == {'x': 12, 'y': 12}:
            # Systematically test columns from 12 to 21 to see if we can step down across Row 13
            # We are at (12, 12). Row 13 is below us.
            # Let's test walking from (12, 12) to (col, 12), then attempting Down to (col, 13).
            for col in range(12, 22):
                print(f"Testing Column {col} Row 13...")
                # Walk from current position to (col, 12)
                curr_pos = mgba.get_coordinates()
                steps_needed = col - curr_pos['x']
                if steps_needed > 0:
                    for _ in range(steps_needed):
                        step_strict("Right", curr_pos['x'] + 1, 12)
                        curr_pos = mgba.get_coordinates()
                elif steps_needed < 0:
                    for _ in range(-steps_needed):
                        step_strict("Left", curr_pos['x'] - 1, 12)
                        curr_pos = mgba.get_coordinates()
                
                # Check if we successfully reached (col, 12)
                if mgba.get_coordinates() == {'x': col, 'y': 12}:
                    # Try to step Down to Row 13
                    test_down = step_strict("Down", col, 13)
                    if test_down == "SUCCESS":
                        print(f"SUCCESS! Column {col} is open vertically across Row 13 in State A!")
                        # Step back up to Row 12 to continue testing
                        step_strict("Up", col, 12)
                    elif test_down == "WARPED":
                        print(f"SUCCESS! Column {col} Row 13 triggers a WARP!")
                    else:
                        print(f"Column {col} Row 13 is BLOCKED.")
                else:
                    print(f"Failed to align to Column {col}.")
    else:
        print("Verification failed, still in State B.")
else:
    print("Could not reach switch.")

