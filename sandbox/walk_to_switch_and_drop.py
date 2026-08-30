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
    print("Toggling Mewtwo Switch at (12, 10) from (12, 11)...")
    # We are already facing UP
    
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

# Path from current (12, 11) after toggle to balcony drop at (19, 18)
path = [
    # 1. Walk down and around to Column 10
    (12, 12), (11, 12), (10, 12),
    # 2. Walk up Column 10 to Row 9
    (10, 11), (10, 10), (10, 9),
    # 3. Walk right to Column 12
    (11, 9), (12, 9),
    # 4. Walk up Column 12 to Row 3 (bypasses rubble at 10,8-11,8)
    (12, 8), (12, 7), (12, 6), (12, 5), (12, 4), (12, 3),
    # 5. Walk right along Row 3 to Column 25
    (13, 3), (14, 3), (15, 3), (16, 3), (17, 3), (18, 3), (19, 3), (20, 3), (21, 3), (22, 3), (23, 3), (24, 3), (25, 3),
    # 6. Walk down Column 25 to Row 16 (gate at 25,13 open in State A)
    (25, 4), (25, 5), (25, 6), (25, 7), (25, 8), (25, 9), (25, 10), (25, 11), (25, 12), (25, 13), (25, 14), (25, 15), (25, 16),
    # 7. Walk left along Row 16 to Column 21
    (24, 16), (23, 16), (22, 16), (21, 16),
    # 8. Walk down Column 21 to Row 18 (gate at 21,17 open in State A)
    (21, 17), (21, 18),
    # 9. Walk left to balcony drop at (19, 18)
    (20, 18), (19, 18)
]

print("Starting toggle...")
toggle_switch()

print("Executing walk to balcony drop...")
res = walk_path_safe(path)
print(f"Path result: {res}. End position: {mgba.get_coordinates()}")

