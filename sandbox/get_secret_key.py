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

pos = mgba.get_coordinates()
print(f"Starting get_secret_key path from {pos}")

# 1. Walk from 2F East (22, 3) back to 2F West stairs at (5, 10)
# We must bypass the Column 22 debris via Row 3 and Column 19
to_stairs_path = [
    (21, 3), (20, 3), (19, 3),
    (19, 4), (19, 5), (19, 6),
    (18, 6), (17, 6), (16, 6), (15, 6), (14, 6), (13, 6), (12, 6),
    (12, 7), (12, 8), (12, 9), (12, 10), (12, 11),
    (11, 11), (10, 11), (9, 11), (8, 11), (7, 11), (6, 11), (5, 11),
    (5, 10)
]

res = walk_path(to_stairs_path)
print(f"To 2F West stairs result: {res}. Pos: {mgba.get_coordinates()}")

# 2. On 3F West: Walk to Column 25 and down to balcony
# We will land on 3F West (which should be around (5, 10))
# Let's check our position after the warp
pos = mgba.get_coordinates()
if pos['y'] == 10 and pos['x'] == 5:
    # We are on 3F West! Walk to Column 25 Row 3, and down Column 25 to balcony!
    to_balcony_path = [
        (5, 9), (5, 8), (5, 7), (5, 6), (5, 5), (5, 4), (5, 3),
        (6, 3), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (12, 3), (13, 3), (14, 3), (15, 3), (16, 3), (17, 3), (18, 3), (19, 3), (20, 3), (21, 3), (22, 3), (23, 3), (24, 3), (25, 3),
        (25, 4), (25, 5), (25, 6), (25, 7), (25, 8), (25, 9), (25, 10), (25, 11), (25, 12), (25, 13), (25, 14), (25, 15), (25, 16), (25, 17),
        (24, 17), (23, 17), (22, 17), (21, 17), (20, 17), (19, 17),
        (19, 18) # Trigger the fall to B1F West!
    ]
    res_balc = walk_path(to_balcony_path)
    print(f"Balcony drop result: {res_balc}. Pos: {mgba.get_coordinates()}")
