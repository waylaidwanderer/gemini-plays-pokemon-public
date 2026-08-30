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

# We are at (21, 6) in State A
# Walk path to stairs at (22, 1) via Column 21, Row 11, Column 26, Row 2.
path_to_stairs = [
    # 1. Walk DOWN Column 21 to Row 11
    (21, 7), (21, 8), (21, 9), (21, 10), (21, 11),
    # 2. Walk RIGHT along Row 11 to Column 26
    (22, 11), (23, 11), (24, 11), (25, 11), (26, 11),
    # 3. Walk UP Column 26 to Row 2
    (26, 10), (26, 9), (26, 8), (26, 7), (26, 6), (26, 5), (26, 4), (26, 3), (26, 2),
    # 4. Walk LEFT along Row 2 to Column 22
    (25, 2), (24, 2), (23, 2), (22, 2),
    # 5. Walk UP Column 22 to the staircase warp at (22, 1)
    (22, 1)
]

print("Walking to stairs via Column 26 bypass...")
res = walk_path(path_to_stairs)
print(f"Path result: {res}. Position: {mgba.get_coordinates()}")
