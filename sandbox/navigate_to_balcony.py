import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

def handle_battle():
    print("  Battle/Dialogue detected! Handling...")
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.05)
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.2)
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.05)

def step_dir(d):
    before = get_pos()
    mgba.press_buttons([d])
    time.sleep(0.4)
    after = get_pos()
    if before == after:
        # Check if we are in a battle
        handle_battle()
        after = get_pos()
    return after != before, after

def walk_path(path):
    print("Starting path traversal:", path)
    for target in path:
        tx, ty = target
        print(f"Targeting: ({tx}, {ty})")
        
        reached = False
        for attempt in range(15):
            c = get_pos()
            if c['x'] == tx and c['y'] == ty:
                reached = True
                print(f"Reached: ({tx}, {ty})")
                break
                
            dx = tx - c['x']
            dy = ty - c['y']
            
            btn = None
            if abs(dx) >= abs(dy):
                if dx > 0: btn = "Right"
                else: btn = "Left"
            else:
                if dy > 0: btn = "Down"
                else: btn = "Up"
                
            success, new_pos = step_dir(btn)
            if not success:
                # If direct approach failed, try the other axis
                other_btn = None
                if btn in ["Up", "Down"]:
                    other_btn = "Right" if dx > 0 else "Left"
                else:
                    other_btn = "Down" if dy > 0 else "Up"
                print(f"  Blocked moving {btn}. Trying alternative {other_btn}...")
                success, new_pos = step_dir(other_btn)
                if not success:
                    print(f"  Completely blocked at {c}!")
                    return False
                    
        if not reached:
            # Check final pos
            c = get_pos()
            if c['x'] != tx or c['y'] != ty:
                print(f"Failed to reach target ({tx}, {ty})")
                return False
    return True

# Clear menus
mgba.press_buttons(["B"])
time.sleep(0.3)

# First leg: to the northeast corner
leg1 = [
    (19, 5),
    (21, 5),
    (21, 3),
    (26, 3),
    (26, 5)
]

if walk_path(leg1):
    print("Reached (26, 5) successfully!")
    mgba.take_screenshot()
    
    # Check if we can go Left to (24, 5)
    print("Checking if we can walk Left to (25, 5)...")
    success, pos = step_dir("Left")
    if success and pos['x'] == 25:
        print("At (25, 5). Trying Left to (24, 5)...")
        success2, pos2 = step_dir("Left")
        if success2 and pos2['x'] == 24:
            print("Successfully reached (24, 5)! Following path A (Master Route).")
            path_a = [
                (24, 7),
                (26, 7),
                (26, 12),
                (25, 12),
                (25, 14),
                (21, 14),
                (21, 15),
                (20, 15)
            ]
            if walk_path(path_a):
                print("Reached balcony landing!")
            else:
                print("Failed path A.")
        else:
            print("Blocked at (25, 5). Retreating to (26, 5)...")
            step_dir("Right")
            success = False
            
    if not success:
        print("Path A blocked. Trying Path B (Direct column 26)...")
        path_b = [
            (26, 12),
            (25, 12),
            (25, 14),
            (21, 14),
            (21, 15),
            (20, 15)
        ]
        if walk_path(path_b):
            print("Reached balcony landing via Path B!")
        else:
            print("Failed Path B.")
            
    # Verify we are at (20, 15)
    final_pos = get_pos()
    if final_pos['x'] == 20 and final_pos['y'] == 15:
        print("Successfully at balcony landing (20, 15)!")
        mgba.take_screenshot()
        print("Attempting to drop to B1F...")
        mgba.press_buttons(["Down", "sleep 400", "Down", "sleep 400", "Down", "sleep 400", "Left"])
        time.sleep(3.0)
        print("Dropped! B1F Position:", get_pos())
        mgba.take_screenshot()
    else:
        print("Did not reach balcony landing.")
else:
    print("Failed to reach (26, 5).")
    mgba.take_screenshot()
