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

# 1. Escape from wild Muk battle
print("Escaping from wild Muk battle at (20, 16)...")
mgba.press_buttons(["A"])
time.sleep(3.5) # Wait for slide-in animation and menu to fully load!

# Select RUN and press A (Down moves to ITEM, Right moves to RUN)
mgba.press_buttons(["Down", "sleep 250", "Right", "sleep 250", "A"])
time.sleep(2.0) # Wait for escape text to appear

# Dismiss escape text
mgba.press_buttons(["A"])
time.sleep(1.0)

print("Coordinates after escape:", mgba.get_coordinates())

# 2. Walk remaining path to (2, 6) from (20, 16)
path_to_switch = [
    # 1. Walk UP Column 20 to Row 1 (bypasses Row 13 in State B!)
    (20, 15), (20, 14), (20, 13), (20, 12), (20, 11), (20, 10), (20, 9), (20, 8), (20, 7), (20, 6), (20, 5), (20, 4), (20, 3), (20, 2), (20, 1),
    # 2. Walk LEFT along Row 1 to Column 6 (bypasses Column 5 Row 1 wall)
    (19, 1), (18, 1), (17, 1), (16, 1), (15, 1), (14, 1), (13, 1), (12, 1), (11, 1), (10, 1), (9, 1), (8, 1), (7, 1), (6, 1),
    # 3. Walk DOWN Column 6 to Row 3
    (6, 2), (6, 3),
    # 4. Walk LEFT Row 3 to Column 2 on 3F West
    (5, 3), (4, 3), (3, 3), (2, 3),
    # 5. Walk DOWN Column 2 to (2, 6) (directly below the switch!)
    (2, 4), (2, 5), (2, 6)
]

print("Walking to (2, 6) on 3F West...")
res = walk_path_strict(path_to_switch)
print(f"Path result: {res}. Position: {mgba.get_coordinates()}")

if mgba.get_coordinates() == {'x': 2, 'y': 6}:
    # Face UP towards (2, 5)
    print("Facing UP towards the switch at (2, 5)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # Toggle switch with 4 A-presses and 2.5-second delays
    print("Toggling Mewtwo switch to State A...")
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    print("Mewtwo switch toggled to State A successfully from the front!")
    
    # Walk directly to the balcony drop from 3F West in State A!
    path_to_balcony = [
        # 1. Walk Right to (3, 6)
        (3, 6),
        # 2. Walk UP Column 3 to Row 2
        (3, 5), (3, 4), (3, 3), (3, 2),
        # 3. Walk RIGHT along Row 2 to Column 10 (completely open in State A!)
        (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2), (10, 2),
        # 4. Walk DOWN Column 10 to Row 16 (completely open in State A!)
        (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10), (10, 11), (10, 12), (10, 13), (10, 14), (10, 15), (10, 16),
        # 5. Walk RIGHT Row 16 directly to balcony drop at (19, 18)!
        (11, 16), (12, 16), (13, 16), (14, 16), (15, 16), (16, 16), (17, 16), (18, 16), (19, 16),
        # 6. Walk DOWN Column 19 to Row 18 (balcony drop warp!)
        (19, 17), (19, 18)
    ]
    print("Walking to the balcony drop in State A directly from 3F West...")
    res_balcony = walk_path_strict(path_to_balcony)
    print(f"Balcony result: {res_balcony}. Final position: {mgba.get_coordinates()}")
