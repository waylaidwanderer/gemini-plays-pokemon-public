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

# We are on 3F at (11, 10) in State A.
# Path to the balcony drop at (19, 18).
balcony_path = [
    # 1. Walk RIGHT to Column 12
    (12, 10),
    # 2. Walk UP Column 12 to Row 6 (bypassing the Column 10 rubble on Row 8)
    (12, 9), (12, 8), (12, 7), (12, 6),
    # 3. Walk LEFT to Column 10 on Row 6
    (11, 6), (10, 6),
    # 4. Walk UP Column 10 to Row 3
    (10, 5), (10, 4), (10, 3),
    # 5. Walk RIGHT along Row 3 to Column 25
    (11, 3), (12, 3), (13, 3), (14, 3), (15, 3), (16, 3), (17, 3), (18, 3), (19, 3), (20, 3), (21, 3), (22, 3), (23, 3), (24, 3), (25, 3),
    # 6. Walk DOWN Column 25 to Row 17
    (25, 4), (25, 5), (25, 6), (25, 7), (25, 8), (25, 9), (25, 10), (25, 11), (25, 12), (25, 13), (25, 14), (25, 15), (25, 16), (25, 17),
    # 7. Walk LEFT along Row 17 to Column 19 (through open State A gates)
    (24, 17), (23, 17), (22, 17), (21, 17), (20, 17), (19, 17),
    # 8. Walk DOWN Column 19 to (19, 18) (Trigger balcony fall warp!)
    (19, 18)
]

# 1. Dismiss "Got away safely!" textbox
print("Dismissing battle screen...")
mgba.press_buttons(["A"])
time.sleep(1.0)

print("Walking to the balcony at (19, 18) from (11, 10) via Column 12 & Row 3 bypass...")
res = walk_path(balcony_path)
print(f"Path result: {res}. Position: {mgba.get_coordinates()}")
