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

# Start at current (24, 17)
path = [
    # 1. UP to Row 16
    (24, 16),
    # 2. LEFT along Row 16 to Column 19 (bypasses Row 17 counters and shutter gates!)
    (23, 16), (22, 16), (21, 16), (20, 16), (19, 16),
    # 3. DOWN Column 19 to Row 18 (balcony drop warp!)
    (19, 17), (19, 18)
]

print("Executing final walk to balcony drop via Row 16...")
res = walk_path_strict(path)
print(f"Path result: {res}. End position: {mgba.get_coordinates()}")
