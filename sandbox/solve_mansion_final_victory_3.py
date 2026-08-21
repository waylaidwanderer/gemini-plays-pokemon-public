import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

def handle_battle(expected_pos):
    print("  Suspected Battle/Dialogue! Clearing text...")
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.05)
    print("  Attempting to RUN...")
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.5)
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.05)
    
    # Check if we drifted
    c = get_pos()
    if c['x'] != expected_pos['x'] or c['y'] != expected_pos['y']:
        print(f"  Drift detected! Current position {c}, expected {expected_pos}. Walking back...")
        walk_back(expected_pos)

def walk_back(target):
    print(f"  Walking back to {target}...")
    for _ in range(5):
        c = get_pos()
        if c['x'] == target['x'] and c['y'] == target['y']:
            print("  Successfully walked back.")
            return True
        dx = target['x'] - c['x']
        dy = target['y'] - c['y']
        btn = None
        if abs(dx) >= abs(dy):
            btn = "Right" if dx > 0 else "Left"
        else:
            btn = "Down" if dy > 0 else "Up"
        mgba.press_buttons([btn])
        time.sleep(0.4)
    return False

def step_dir(d):
    before = get_pos()
    print(f"  Stepping {d} from {before}...")
    for attempt in range(3):
        mgba.press_buttons([d])
        for _ in range(5):
            time.sleep(0.1)
            after = get_pos()
            if after['x'] != before['x'] or after['y'] != before['y']:
                return True, after
        print(f"  Attempt {attempt + 1} to step {d} failed. Retrying...")
    handle_battle(before)
    after = get_pos()
    return after['x'] != before['x'] or after['y'] != before['y'], after

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
                btn = "Right" if dx > 0 else "Left"
            else:
                btn = "Down" if dy > 0 else "Up"
            success, new_pos = step_dir(btn)
            if not success:
                other_btn = "Down" if btn in ["Left", "Right"] else "Right"
                print(f"  Blocked! Trying alternative direction {other_btn}...")
                success, new_pos = step_dir(other_btn)
                if not success:
                    print(f"  Completely blocked at {c}!")
                    return False
        if not reached:
            c = get_pos()
            if c['x'] != tx or c['y'] != ty:
                print(f"Failed to reach target ({tx}, {ty})")
                return False
    return True

# Clear any lingering menus
mgba.press_buttons(["B"])
time.sleep(0.3)

# 1. Walk from (8, 12) to switch (2, 11) on 3F and toggle to State A
path_to_switch = [
    (8, 11),
    (7, 11),
    (6, 11),
    (5, 11),
    (4, 11),
    (3, 11),
    (3, 12),
    (2, 12)
]

print("--- PHASE 1: WALKING TO 3F SWITCH ---")
if walk_path(path_to_switch):
    print("Reached (2, 12) on 3F. Turning UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    print("Toggling switch to State A...")
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    mgba.press_buttons(["B", "sleep 100", "B", "sleep 100", "B"])
    time.sleep(0.5)
    mgba.take_screenshot()
    
    # 2. Walk to East Stairs via column 19 on 3F (State A)
    path_to_east_stairs = [
        (3, 12),
        (3, 11),
        (12, 11),
        (12, 10),
        (12, 9),
        (12, 8),
        (12, 7),
        (12, 6),
        (13, 6),
        (14, 6),
        (15, 6),
        (16, 6),
        (17, 6),
        (18, 6),
        (19, 6),
        (19, 7),
        (19, 8),
        (19, 9),
        (19, 10),
        (19, 11),
        (18, 11),
        (17, 11),
        (16, 11),
        (15, 11) # East Stairs
    ]
    print("--- PHASE 2: WALKING TO 3F EAST STAIRS (STATE A) ---")
    if walk_path(path_to_east_stairs):
        print("Reached East Stairs on 3F! Warping to 2F...")
        time.sleep(2.0)
        pos_2f = get_pos()
        print("Arrived on 2F (East side). Position:", pos_2f)
        mgba.take_screenshot()
        
        # 3. Walk to (14, 11) on 2F and toggle switch to State B
        path_to_switch_b = [
            (15, 11),
            (14, 11)
        ]
        print("--- PHASE 3: WALKING TO SWITCH ON 2F ---")
        if walk_path(path_to_switch_b):
            print("Reached (14, 11) on 2F. Turning Left...")
            mgba.press_buttons(["Left"])
            time.sleep(0.4)
            print("Toggling switch to State B...")
            mgba.press_buttons(["A"])
            time.sleep(0.5)
            mgba.press_buttons(["B", "sleep 100", "B", "sleep 100", "B"])
            time.sleep(0.5)
            mgba.take_screenshot()
            
            # 4. Walk back to East Stairs and warp to 3F (State B)
            path_back_to_stairs = [
                (15, 11)
            ]
            print("--- PHASE 4: WARPING TO 3F (STATE B) ---")
            if walk_path(path_back_to_stairs):
                print("Warping to 3F...")
                time.sleep(2.0)
                pos_3f_b = get_pos()
                print("Arrived on 3F. Position:", pos_3f_b)
                mgba.take_screenshot()
                
                # 5. Walk to Balcony landing (20, 15) on 3F (State B)
                path_to_balcony = [
                    (17, 11),
                    (18, 11),
                    (19, 11),
                    (20, 11),
                    (21, 11),
                    (21, 12),
                    (21, 13),
                    (21, 14),
                    (21, 15),
                    (20, 15)
                ]
                print("--- PHASE 5: WALKING TO BALCONY ON 3F (STATE B) ---")
                if walk_path(path_to_balcony):
                    print("Reached Balcony landing (20, 15) on 3F!")
                    mgba.take_screenshot()
                    
                    # 6. Step to drop edge and drop Left
                    path_to_edge = [
                        (20, 16),
                        (20, 17),
                        (20, 18)
                    ]
                    print("--- PHASE 6: STEPPING TO DROP EDGE AND DROPPING ---")
                    if walk_path(path_to_edge):
                        print("At drop edge (20, 18). Dropping Left to B1F!")
                        mgba.take_screenshot()
                        mgba.press_buttons(["Left"])
                        time.sleep(3.0)
                        print("Landed on B1F! Position:", get_pos())
                        mgba.take_screenshot()
                    else:
                        print("Failed to reach drop edge.")
                else:
                    print("Failed to walk to Balcony.")
            else:
                print("Failed to return to East Stairs.")
        else:
            print("Failed to reach 2F Switch B.")
    else:
        print("Failed to reach East Stairs on 3F.")
else:
    print("Failed to reach 3F Switch.")
