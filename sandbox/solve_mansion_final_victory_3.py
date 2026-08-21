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

# Phase 1: Walk from current (8, 11) on 3F to West Stairs at (7, 10) to warp down to 2F
path_to_stairs = [
    (7, 11),
    (7, 10)
]

print("--- PHASE 1: RETURNING TO 2F VIA WEST STAIRS ---")
if walk_path(path_to_stairs):
    print("Reached stairs at (7, 10). Warping to 2F...")
    time.sleep(2.0) # Wait for warp
    pos_2f = get_pos()
    print("Arrived on 2F. Position:", pos_2f)
    mgba.take_screenshot()
    
    # Phase 2: On 2F (State A), walk from (7, 11) to west switch at (2, 12)
    path_to_switch = [
        (6, 11),
        (5, 11),
        (4, 11),
        (3, 11),
        (3, 12),
        (2, 12)
    ]
    print("--- PHASE 2: WALKING TO WEST SWITCH ON 2F (STATE A) ---")
    if walk_path(path_to_switch):
        print("Reached (2, 12) on 2F. Turning UP...")
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        print("Toggling 2F switch to State B...")
        mgba.press_buttons(["A"])
        time.sleep(0.5)
        mgba.press_buttons(["B", "sleep 100", "B", "sleep 100", "B"])
        time.sleep(0.5)
        mgba.take_screenshot()
        
        # Phase 3: Walk to East Stairs (15, 11) via column 6 and row 8
        path_to_east_stairs = [
            (3, 12),
            (4, 12),
            (5, 12),
            (6, 12),
            (6, 11),
            (6, 10),
            (6, 9),
            (6, 8),
            (7, 8),
            (8, 8),
            (9, 8),
            (10, 8),
            (11, 8),
            (12, 8),
            (13, 8),
            (14, 8),
            (15, 8),
            (15, 9),
            (15, 10),
            (15, 11)
        ]
        print("--- PHASE 3: WALKING TO EAST STAIRS ON 2F (STATE B) ---")
        if walk_path(path_to_east_stairs):
            print("Reached East Stairs on 2F! Warping to 3F...")
            time.sleep(2.0) # Wait for warp
            pos_3f = get_pos()
            print("Arrived on 3F. Position:", pos_3f)
            mgba.take_screenshot()
            
            # Phase 4: Walk to Balcony landing (20, 15) on 3F (State B)
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
                
                # Phase 5: Step Down and drop Left
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
            print("Failed to reach East Stairs on 2F.")
    else:
        print("Failed to reach West Switch on 2F.")
else:
    print("Failed to reach West Stairs on 3F.")

