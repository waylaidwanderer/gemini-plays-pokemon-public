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
    if before['x'] == after['x'] and before['y'] == after['y']:
        handle_battle()
        after = get_pos()
    return after['x'] != before['x'] or after['y'] != before['y'], after

def walk_path(path):
    print("Starting path traversal:", path)
    for target in path:
        tx, ty = target
        print(f"Targeting: ({tx}, {ty})")
        reached = False
        for attempt in range(10):
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

# Phase 1: Walk from current (6, 14) on 2F (State B) back to (1, 11)
path_to_switch_landing = [
    (5, 14),
    (4, 14),
    (3, 14),
    (2, 14),
    (1, 14),
    (1, 13),
    (1, 12),
    (1, 11)
]

print("--- PHASE 1: WALKING TO SWITCH LANDING (1, 11) ---")
if walk_path(path_to_switch_landing):
    print("Reached (1, 11)!")
    mgba.take_screenshot()
    
    # Phase 2: Walk UP Column 1 to Row 8, and Right along Row 8 to East Stairs
    path_to_east_stairs = [
        (1, 10),
        (1, 9),
        (1, 8),
        (2, 8),
        (3, 8),
        (4, 8),
        (5, 8),
        (6, 8),
        (7, 8),
        (8, 8),
        (9, 8),
        (10, 8), # open gate in State B
        (11, 8),
        (12, 8),
        (13, 8),
        (14, 8),
        (15, 8),
        (15, 9),
        (15, 10),
        (15, 11) # East Stairs
    ]
    
    print("--- PHASE 2: WALKING TO EAST STAIRS VIA COLUMN 1 & ROW 8 ---")
    if walk_path(path_to_east_stairs):
        print("Reached East Stairs on 2F! Warping to 3F...")
        time.sleep(2.0) # Wait for warp
        pos_3f = get_pos()
        print("Arrived on 3F. Position:", pos_3f)
        mgba.take_screenshot()
        
        # Phase 3: Walk to Balcony landing (20, 15) on 3F (State B)
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
        print("--- PHASE 3: WALKING TO BALCONY ON 3F (STATE B) ---")
        if walk_path(path_to_balcony):
            print("Reached Balcony landing (20, 15) on 3F!")
            mgba.take_screenshot()
            
            # Phase 4: Step Down and drop Left
            path_to_edge = [
                (20, 16),
                (20, 17),
                (20, 18)
            ]
            print("--- PHASE 4: STEPPING TO DROP EDGE AND DROPPING ---")
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
        print("Failed to reach East Stairs via Column 1 & Row 8.")
else:
    print("Failed to reach (1, 11).")

