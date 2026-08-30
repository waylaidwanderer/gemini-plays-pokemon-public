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

# Walk from current (5, 10) on 3F West to balcony drop at (19, 18) in State A via Row 11, Column 12, Row 3 and Column 25
path = [
    # 1. DOWN to Row 11
    (5, 11),
    # 2. Right along Row 11 to Column 12 (gate at 12,11 is open in State A)
    (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11), (12, 11),
    # 3. UP Column 12 to Row 3 (bypasses Row 8 rubble and Column 5 Row 9 permanent wall)
    (12, 10), (12, 9), (12, 8), (12, 7), (12, 6), (12, 5), (12, 4), (12, 3),
    # 4. Right along Row 3 to Column 25
    (13, 3), (14, 3), (15, 3), (16, 3), (17, 3), (18, 3), (19, 3), (20, 3), (21, 3), (22, 3), (23, 3), (24, 3), (25, 3),
    # 5. DOWN Column 25 to Row 16 (gate at 25,13 is open in State A)
    (25, 4), (25, 5), (25, 6), (25, 7), (25, 8), (25, 9), (25, 10), (25, 11), (25, 12), (25, 13), (25, 14), (25, 15), (25, 16),
    # 6. Left along Row 16 to Column 21
    (24, 16), (23, 16), (22, 16), (21, 16),
    # 7. DOWN Column 21 to Row 18 (balcony gates at 21,17 are open in State A)
    (21, 17), (21, 18),
    # 8. Left to balcony drop warp at (19, 18)
    (20, 18), (19, 18)
]

print("Executing master State A walk to balcony drop...")
res = walk_path_safe(path)
print(f"Path result: {res}. End position: {mgba.get_coordinates()}")

