import mgba
import time

def step_strict(direction, target_x, target_y):
    # Allow 2 attempts per step to handle turning-in-place/lag
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
            print(f"BLOCKED! Position did not change while trying to go to {(target_x, target_y)}. Stopping script for manual handling.")
            return "BLOCKED_STATE"
        elif res == "WARPED":
            return "WARPED"
        time.sleep(0.1)
    return "SUCCESS"

# Start at current (27, 9) in State A
path = [
    # 1. Left to Column 26
    (26, 9),
    # 2. DOWN to Row 10
    (26, 10),
    # 3. Left to Column 25
    (25, 10),
    # 4. DOWN Column 25 to Row 16 (bypasses Column 27 rubble and Column 26 shutter gate!)
    (25, 11), (25, 12), (25, 13), (25, 14), (25, 15), (25, 16),
    # 5. Left along Row 16 to Column 20 (bypasses Column 18 Row 16 wall!)
    (24, 16), (23, 16), (22, 16), (21, 16), (20, 16),
    # 6. DOWN Column 20 through open gate to Row 18
    (20, 17), (20, 18),
    # 7. Left to Column 19 (balcony grass drop warp!)
    (19, 18)
]

print("Executing correct detour walk to balcony drop from current position (27, 9) in State A...")
res = walk_path_safe(path)
print(f"Path result: {res}. End position: {mgba.get_coordinates()}")
