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

# Walk from current (21, 4) to stairs entrance at (22, 5) via Column 26
path = [
    # 1. UP to Row 3
    (21, 3),
    # 2. Right to Column 26 (pitfall closed/walkable in State B)
    (22, 3), (23, 3), (24, 3), (25, 3), (26, 3),
    # 3. DOWN Column 26 to Row 5
    (26, 4), (26, 5),
    # 4. Left to Column 23
    (25, 5), (24, 5), (23, 5),
    # 5. Left into staircase at (22, 5) -> triggers warp!
    (22, 5)
]

print("Walking to stairs entrance at (22, 5)...")
res = walk_path_safe(path)
print(f"Walk result: {res}. Position: {mgba.get_coordinates()}")

