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

def toggle_switch():
    print("Toggling Mewtwo Switch at (2, 5) from (2, 6)...")
    mgba.press_buttons(["Up"])
    time.sleep(1.0)
    
    print("Pressing A (1/4)...")
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    
    print("Pressing A (2/4)...")
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    
    print("Pressing A (3/4)...")
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    
    print("Pressing A (4/4)...")
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    print("Switch toggle complete.")

# 1. Path from (25, 3) to (2, 6) in State B
path1 = [
    # Walk Left along Row 3 from (25, 3) to (4, 3)
    (24, 3), (23, 3), (22, 3), (21, 3), (20, 3), (19, 3), (18, 3), (17, 3), (16, 3), (15, 3), (14, 3), (13, 3), (12, 3), (11, 3), (10, 3), (9, 3), (8, 3), (7, 3), (6, 3), (5, 3), (4, 3),
    # Walk DOWN Column 4 to Row 6 (bypasses trainer at 3,3)
    (4, 4), (4, 5), (4, 6),
    # Walk Left along Row 6 to (2, 6) (gate at 3,6 is open in State B)
    (3, 6), (2, 6)
]

# 2. Path from (2, 6) to balcony drop (19, 18) in State A
path2 = [
    # Walk Left to Column 1, UP to Row 3
    (1, 6), (1, 5), (1, 4), (1, 3),
    # Walk Right to Column 2, DOWN to Row 4, Right to Column 4, UP to Row 3 (bypasses trainer at 3,3)
    (2, 3), (2, 4), (3, 4), (4, 4), (4, 3),
    # Walk Right along Row 3 to Column 25
    (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (12, 3), (13, 3), (14, 3), (15, 3), (16, 3), (17, 3), (18, 3), (19, 3), (20, 3), (21, 3), (22, 3), (23, 3), (24, 3), (25, 3),
    # Walk DOWN Column 25 to Row 16
    (25, 4), (25, 5), (25, 6), (25, 7), (25, 8), (25, 9), (25, 10), (25, 11), (25, 12), (25, 13), (25, 14), (25, 15), (25, 16),
    # Walk Left along Row 16 to Column 21
    (24, 16), (23, 16), (22, 16), (21, 16),
    # Walk DOWN Column 21 to Row 18
    (21, 17), (21, 18),
    # Walk Left to (19, 18) (balcony drop!)
    (20, 18), (19, 18)
]

print("Executing Step 1: Walk to switch at (2, 5)...")
res1 = walk_path_safe(path1)
print(f"Path 1 result: {res1}. Position: {mgba.get_coordinates()}")

if res1 == "SUCCESS" and mgba.get_coordinates() == {'x': 2, 'y': 6}:
    print("Executing Step 2: Toggle Mewtwo Switch...")
    toggle_switch()
    
    print("Executing Step 3: Verifying State A...")
    test_res = step_strict("Right", 3, 6)
    if test_res == "BLOCKED":
        print("VERIFICATION SUCCESSFUL: Gate at (3, 6) is CLOSED. Mansion is in STATE A.")
        print("Executing Step 4: Walk to balcony drop...")
        res2 = walk_path_safe(path2)
        print(f"Path 2 result: {res2}. End position: {mgba.get_coordinates()}")
    else:
        print("VERIFICATION FAILED: Gate at (3, 6) is OPEN. Mansion is still in STATE B!")
else:
    print("Failed to reach the switch.")

