import mgba
import time

def step_strict(direction, target_x, target_y):
    for attempt in range(2):
        pos_before = mgba.get_coordinates()
        mgba.press_buttons([direction])
        time.sleep(0.4)
        pos_after = mgba.get_coordinates()
        
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

# Start at current (20, 16)
# Walk to (22, 2) via:
# - Right to (24, 16) -> Up Column 24 to Row 10 -> Right to (26, 10) -> Up Column 26 to Row 2 -> Left to (22, 2)
path = [
    (21, 16), (22, 16), (23, 16), (24, 16),
    (24, 15), (24, 14), (24, 13), (24, 12), (24, 11), (24, 10),
    (25, 10), (26, 10),
    (26, 9), (26, 8), (26, 7), (26, 6), (26, 5), (26, 4), (26, 3), (26, 2),
    (25, 2), (24, 2), (23, 2), (22, 2)
]

print("Walking to (22, 2)...")
res = walk_path_safe(path)
print(f"Path result: {res}. Position: {mgba.get_coordinates()}")

if mgba.get_coordinates() == {'x': 22, 'y': 2}:
    # Test step Left to (21, 2)
    print("Testing step Left to (21, 2)...")
    test_res = step_strict("Left", 21, 2)
    print(f"Test result: {test_res}. Position: {mgba.get_coordinates()}")
    if test_res == "BLOCKED":
         print("VERDICT: Mansion is in STATE B (Gate at (21,2) is closed).")
    elif test_res == "SUCCESS":
         print("VERDICT: Mansion is in STATE A (Gate at (21,2) is open).")
