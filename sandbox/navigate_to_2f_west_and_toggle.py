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

# 1. Walk from current (23, 1) to (2, 12) on 2F West via Row 6
path_to_switch = [
    (23, 2),
    (23, 3),
    (22, 3), (21, 3),
    (21, 4),
    (20, 4), (19, 4),
    (19, 5), (19, 6),
    # Walk left along Row 6
    (18, 6), (17, 6), (16, 6), (15, 6), (14, 6), (13, 6), (12, 6), (11, 6), (10, 6), (9, 6), (8, 6), (7, 6), (6, 6), (5, 6), (4, 6), (3, 6),
    # Walk down Column 3 to Row 12
    (3, 7), (3, 8), (3, 9), (3, 10), (3, 11), (3, 12),
    # Walk left to (2, 12)
    (2, 12)
]

print("Walking to the 2F West switch...")
res = walk_path(path_to_switch)
print(f"Path to switch result: {res}. Position: {mgba.get_coordinates()}")

if mgba.get_coordinates() == {'x': 2, 'y': 12}:
    # Face UP to look at the switch at (2, 11)
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # Toggle switch with exactly 4 A-presses and 2.5-second delays
    print("Toggling the switch to State A...")
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    
    # Walk back to 2F East stairs at (22, 1) via Row 11
    print("Walking back to 2F East stairs...")
    path_back_to_stairs = [
        (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11), (12, 11), (13, 11), (14, 11), (15, 11), (16, 11), (17, 11), (18, 11), (19, 11), (20, 11), (21, 11), (22, 11),
        (21, 11),
        (21, 10), (21, 9), (21, 8), (21, 7), (21, 6), (21, 5), (21, 4),
        (21, 3), (22, 3),
        (22, 2),
        (22, 1)
    ]
    res_back = walk_path(path_back_to_stairs)
    print(f"Path back result: {res_back}. Position: {mgba.get_coordinates()}")
