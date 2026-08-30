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

# 1. Flee from the wild Ponyta battle
# flee_battle()

# 2. Walk to the 2F West stairs at (5, 11) from (4, 11)
print("Walking to stairs at (5, 11)...")
walk_path_safe([(5, 11)])

# 3. Warp UP to 3F West from 2F West (5, 11)
print("Stepping UP into stairs to warp to 3F West...")
warp_res = step_strict("Up", 5, 10)
print(f"Warp result: {warp_res}. Position: {mgba.get_coordinates()}")

if warp_res == "WARPED" or mgba.get_coordinates() == {'x': 5, 'y': 11}:
    print("Arrived on 3F West! Testing if Column 5 Row 9 is open...")
    # Test stepping Up to (5, 9) on 3F West
    step_res = step_strict("Up", 5, 9)
    if step_res == "SUCCESS":
        print("Column 5 Row 9 is OPEN! Walking straight to balcony...")
        path_straight = [
            (5, 8), (5, 7), (5, 6), (5, 5), (5, 4), (5, 3),
            (6, 3), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (12, 3), (13, 3), (14, 3), (15, 3), (16, 3), (17, 3), (18, 3), (19, 3), (20, 3), (21, 3), (22, 3), (23, 3), (24, 3), (25, 3),
            (25, 4), (25, 5), (25, 6), (25, 7), (25, 8), (25, 9), (25, 10), (25, 11), (25, 12), (25, 13), (25, 14), (25, 15), (25, 16),
            (24, 16), (23, 16), (22, 16), (21, 16),
            (21, 17), (21, 18),
            (20, 18), (19, 18)
        ]
        res = walk_path_safe(path_straight)
        print(f"Path straight result: {res}. Position: {mgba.get_coordinates()}")
    else:
        print("Column 5 Row 9 is BLOCKED! Detouring via Column 12...")
        # Step back to (5, 11) if we are at (5, 10)
        if mgba.get_coordinates() == {'x': 5, 'y': 10}:
            step_strict("Down", 5, 11)
            
        path_detour = [
            # Walk Right along Row 11 to Column 12 (gate at 12,11 is open in State A)
            (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11), (12, 11),
            # UP Column 12 to Row 3 (bypasses Row 8 rubble and Column 5 Row 9 permanent wall)
            (12, 10), (12, 9), (12, 8), (12, 7), (12, 6), (12, 5), (12, 4), (12, 3),
            # Right along Row 3 to Column 25
            (13, 3), (14, 3), (15, 3), (16, 3), (17, 3), (18, 3), (19, 3), (20, 3), (21, 3), (22, 3), (23, 3), (24, 3), (25, 3),
            # DOWN Column 25 to Row 16 (gate at 25,13 is open in State A)
            (25, 4), (25, 5), (25, 6), (25, 7), (25, 8), (25, 9), (25, 10), (25, 11), (25, 12), (25, 13), (25, 14), (25, 15), (25, 16),
            # Left along Row 16 to Column 21
            (24, 16), (23, 16), (22, 16), (21, 16),
            # DOWN Column 21 to Row 18 (balcony gates at 21,17 are open in State A)
            (21, 17), (21, 18),
            # Left to balcony drop warp at (19, 18)
            (20, 18), (19, 18)
        ]
        res = walk_path_safe(path_detour)
        print(f"Path detour result: {res}. Position: {mgba.get_coordinates()}")
else:
    print("Failed to warp UP to 3F.")

