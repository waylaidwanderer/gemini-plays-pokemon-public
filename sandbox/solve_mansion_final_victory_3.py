import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

def handle_battle():
    print("  Battle/Dialogue/Menu detected! Handling...")
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.05)
    print("  Attempting to RUN...")
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.5)
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.05)

def step_dir(d):
    before = get_pos()
    print(f"  Stepping {d} from {before}...")
    mgba.press_buttons([d])
    time.sleep(0.4)
    after = get_pos()
    if before == after:
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

# Clear menus
mgba.press_buttons(["B"])
time.sleep(0.3)

# Phase 1: Walk from current (21, 7) on 3F (State A) to the West Stairs at (7, 10)
path_to_west_stairs = [
    (20, 7),
    (19, 7),
    (18, 7),
    (17, 7),
    (16, 7),
    (15, 7),
    (14, 7),
    (13, 7),
    (12, 7),
    (12, 8),
    (12, 9),
    (12, 10),
    (12, 11),
    (11, 11),
    (10, 11),
    (9, 11),
    (8, 11),
    (7, 11),
    (7, 10)
]

print("--- PHASE 1: WALKING TO 3F WEST STAIRS (STATE A) ---")
if walk_path(path_to_west_stairs):
    print("Reached West Stairs at (7, 10) on 3F! Warping to 2F...")
    time.sleep(2.0) # Wait for warp
    pos_2f = get_pos()
    print("Arrived on 2F. Position:", pos_2f)
    mgba.take_screenshot()
    
    # Phase 2: On 2F (State A), walk from landing (7, 11) to the switch at (12, 11)
    path_to_2f_switch = [
        (8, 11),
        (9, 11),
        (10, 11),
        (11, 11),
        (12, 11)
    ]
    print("--- PHASE 2: WALKING TO SWITCH ON 2F ---")
    if walk_path(path_to_2f_switch):
        print("Reached (12, 11) on 2F. Turning Right...")
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        print("Toggling 2F switch to State B...")
        mgba.press_buttons(["A"])
        time.sleep(0.5)
        mgba.press_buttons(["B", "sleep 100", "B", "sleep 100", "B"])
        time.sleep(0.5)
        mgba.take_screenshot()
        
        # Phase 3: Walk back to the East Stairs on 2F (State B)
        path_back_to_stairs = [
            (13, 11),
            (14, 11),
            (15, 11)
        ]
        print("--- PHASE 3: WALKING TO EAST STAIRS ON 2F ---")
        if walk_path(path_back_to_stairs):
            print("Reached stairs on 2F! Warping back to 3F...")
            time.sleep(2.0) # Wait for warp
            pos_3f = get_pos()
            print("Arrived on 3F. Position:", pos_3f)
            mgba.take_screenshot()
            
            # Phase 4: On 3F (State B), walk to the Balcony landing (20, 15)
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
            print("--- PHASE 4: WALKING TO BALCONY ON 3F (STATE B) ---")
            if walk_path(path_to_balcony):
                print("Reached Balcony landing (20, 15) on 3F!")
                mgba.take_screenshot()
                
                # Phase 5: Step Down through open shutter gate and drop Left
                path_to_edge = [
                    (20, 16),
                    (20, 17),
                    (20, 18)
                ]
                print("--- PHASE 5: STEPPING TO DROP EDGE AND DROPPING ---")
                if walk_path(path_to_edge):
                    print("At drop edge (20, 18). Dropping Left to B1F!")
                    mgba.take_screenshot()
                    mgba.press_buttons(["Left"])
                    time.sleep(3.0) # wait for falling warp
                    print("Landed on B1F! Position:", get_pos())
                    mgba.take_screenshot()
                else:
                    print("Failed to reach drop edge.")
            else:
                print("Failed to walk to Balcony.")
        else:
            print("Failed to return to 2F stairs.")
    else:
        print("Failed to walk to 2F switch.")
else:
    print("Failed to reach West Stairs on 3F.")

