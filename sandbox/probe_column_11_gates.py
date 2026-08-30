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

# 1. Dismiss text box if open
print("Dismissing battle screen...")
mgba.press_buttons(["A"])
time.sleep(1.0)

# Walk from (28, 12) to (10, 14) via Row 3 bypass
loop_path = [
    (27, 12), (26, 12),
    (26, 11), (26, 10), (26, 9), (26, 8), (26, 7),
    (27, 7),
    (27, 6), (27, 5), (27, 4), (27, 3),
    (26, 3), (25, 3), (24, 3), (23, 3), (22, 3), (21, 3), (20, 3), (19, 3), (18, 3), (17, 3), (16, 3), (15, 3), (14, 3), (13, 3), (12, 3), (11, 3), (10, 3),
    (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10), (10, 11), (10, 12), (10, 13), (10, 14)
]

print("Walking to (10, 14) via Row 3 bypass...")
res = walk_path(loop_path)
print(f"Bypass walk result: {res}. Position: {mgba.get_coordinates()}")

# Probing gates on Column 11
if mgba.get_coordinates() == {'x': 10, 'y': 14}:
    for y in [14, 15, 16, 17]:
        pos = mgba.get_coordinates()
        if pos['y'] != y:
            step_safe("Down", pos['x'], y)
        print(f"Probing Column 11 Row {y} from {mgba.get_coordinates()}...")
        res_probe = step_safe("Right", 11, y)
        if res_probe == "SUCCESS":
            print(f"FOUND OPEN GATE AT (11, {y})!")
            break
        else:
            print(f"Gate at (11, {y}) is CLOSED.")
