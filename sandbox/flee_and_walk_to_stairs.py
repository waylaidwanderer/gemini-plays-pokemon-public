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

def flee_battle():
    print("Clearing encounter text...")
    mgba.press_buttons(["A"])
    time.sleep(2.0)

    print("Clearing player summon text...")
    mgba.press_buttons(["A"])
    time.sleep(2.5)

    print("Navigating menu to RUN...")
    mgba.press_buttons(["Right", "sleep 200", "Down", "sleep 200", "A"])
    time.sleep(2.0)

    print("Clearing escape text...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    print("Fled battle.")

# 1. Flee from the Koffing battle
flee_battle()

# 2. Walk remaining path to the northeast stairs area
path = [
    # UP Column 5 to Row 1
    (5, 7), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1),
    # Right along Row 1 to Column 22
    (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 1), (13, 1), (14, 1), (15, 1), (16, 1), (17, 1), (18, 1), (19, 1), (20, 1), (21, 1), (22, 1),
    # DOWN to (22, 2)
    (22, 2)
]

print("Walking to northeast area at (22, 2)...")
res = walk_path_safe(path)
print(f"Walk result: {res}. Position: {mgba.get_coordinates()}")

if mgba.get_coordinates() == {'x': 22, 'y': 2}:
    # Test warp: step UP to (22, 1)
    print("Testing UP from (22, 2)...")
    res_warp = step_strict("Up", 22, 1)
    print(f"Warp result: {res_warp}. Position: {mgba.get_coordinates()}")

