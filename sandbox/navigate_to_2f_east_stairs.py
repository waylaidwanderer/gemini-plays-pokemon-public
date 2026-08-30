import mgba
import time

def escape_battle_proactive():
    print("PROACTIVE ESCAPE SEQUENCE...")
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    mgba.press_buttons(["Down", "sleep 250", "Right", "sleep 250", "A", "sleep 1200", "B"])
    time.sleep(1.5)
    mgba.press_buttons(["A"])
    time.sleep(0.5)

def step_safe(direction, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"Moving {direction} to ({target_x}, {target_y}). Current: {pos_before}")
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    
    if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 5 or abs(pos_after['y'] - pos_before['y']) > 5):
        print(f"Warped! From {pos_before} to {pos_after}")
        return "WARPED"
        
    if pos_after['x'] == target_x and pos_after['y'] == target_y:
        return "SUCCESS"
        
    if pos_before == pos_after:
        escape_battle_proactive()
        mgba.press_buttons([direction])
        time.sleep(0.4)
        pos_after = mgba.get_coordinates()
        if pos_after['x'] == target_x and pos_after['y'] == target_y:
            return "SUCCESS"
        return "BLOCKED"
            
    return "SUCCESS"

def walk_path(coords):
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
        while attempts < 3:
            res = step_safe(direction, target_x, target_y)
            if res == "SUCCESS":
                break
            elif res == "WARPED":
                return "WARPED"
            attempts += 1
            time.sleep(0.2)
        if attempts == 3:
            return "BLOCKED"
    return "SUCCESS"

# Path from (7, 11) on 2F West to northeast stairs at (22, 1)
stairs_path = [
    # 1. UP to Row 10
    (7, 10),
    # 2. LEFT to Column 4
    (6, 10), (5, 10), (4, 10),
    # 3. UP Column 4 to Row 6
    (4, 9), (4, 8), (4, 7), (4, 6),
    # 4. RIGHT along Row 6 to Column 19
    (5, 6), (6, 6), (7, 6), (8, 6), (9, 6), (10, 6), (11, 6), (12, 6), (13, 6), (14, 6), (15, 6), (16, 6), (17, 6), (18, 6), (19, 6),
    # 5. UP Column 19 to Row 4
    (19, 5), (19, 4),
    # 6. RIGHT to Column 21
    (20, 4), (21, 4),
    # 7. UP Column 21 to Row 3
    (21, 3),
    # 8. RIGHT to Column 22
    (22, 3),
    # 9. UP Column 22 to stairs warp at (22, 1)
    (22, 2),
    (22, 1)
]

print("Walking to the northeast stairs on 2F East...")
res = walk_path(stairs_path)
print(f"Path result: {res}. Position: {mgba.get_coordinates()}")
