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

# Phase 1: Walk from current (22, 7) back to the 3F Switch at (2, 12) (State A)
# Tile-by-tile path to prevent drift
path_back_to_switch = [
    (21, 7),
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
    (6, 11),
    (5, 11),
    (4, 11),
    (3, 11),
    (3, 12),
    (2, 12)
]

print("--- PHASE 1: WALKING BACK TO WEST SWITCH (STATE A) ---")
if walk_path(path_back_to_switch):
    print("Reached (2, 12). Turning UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    print("Toggling switch to State B...")
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    mgba.press_buttons(["B", "sleep 100", "B", "sleep 100", "B"])
    time.sleep(0.5)
    mgba.take_screenshot()
    
    # Phase 2: Walk the verified Master Route to Balcony Landing (20, 15) on 3F (State B)
    # Tile-by-tile path to prevent any horizontal/vertical drift
    master_route = [
        (3, 12),
        (4, 12),
        (5, 12),
        (6, 12),
        (7, 12), # Stay on row 12!
        (7, 13),
        (8, 13),
        (9, 13),
        (9, 12),
        (9, 11),
        (9, 10),
        (10, 10),
        (11, 10),
        (11, 9),
        (11, 8),
        (11, 7),
        (11, 6),
        (11, 5),
        (12, 5),
        (13, 5),
        (14, 5),
        (15, 5),
        (16, 5),
        (17, 5),
        (18, 5),
        (19, 5),
        (20, 5),
        (21, 5),
        (21, 4),
        (21, 3),
        (22, 3),
        (23, 3),
        (24, 3),
        (25, 3),
        (26, 3),
        (26, 4),
        (26, 5),
        (25, 5),
        (24, 5),
        (24, 6),
        (24, 7),
        (25, 7),
        (26, 7),
        (26, 8),
        (26, 9),
        (26, 10),
        (26, 11),
        (26, 12),
        (25, 12),
        (25, 13),
        (25, 14),
        (24, 14),
        (23, 14),
        (22, 14),
        (21, 14),
        (21, 15),
        (20, 15)
    ]
    
    print("--- PHASE 2: WALKING MASTER ROUTE TO BALCONY (STATE B) ---")
    if walk_path(master_route):
        print("Reached Balcony landing (20, 15) on 3F!")
        mgba.take_screenshot()
        
        # Phase 3: Step Down and drop Left
        path_to_edge = [
            (20, 16),
            (20, 17),
            (20, 18)
        ]
        print("--- PHASE 3: STEPPING TO DROP EDGE AND DROPPING ---")
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
        print("Failed to walk Master Route.")
else:
    print("Failed to return to West Switch.")

