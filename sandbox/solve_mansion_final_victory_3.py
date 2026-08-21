import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

def walk_back(target):
    print(f"  Walking back to {target}...")
    # Simple direct movement back to target without calling handle_battle
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

def handle_battle(expected_pos):
    print("  Battle/Dialogue/Menu suspected! Clearing text...")
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.05)
    print("  Attempting to RUN...")
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.5)
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.05)
    
    # Check if we drifted (meaning we were NOT in a battle, and overworld movement occurred)
    c = get_pos()
    if c['x'] != expected_pos['x'] or c['y'] != expected_pos['y']:
        print(f"  Drift detected! Current position {c}, expected {expected_pos}. Walking back...")
        walk_back(expected_pos)

def step_dir(d):
    before = get_pos()
    print(f"  Stepping {d} from {before}...")
    mgba.press_buttons([d])
    time.sleep(0.4)
    after = get_pos()
    if before['x'] == after['x'] and before['y'] == after['y']:
        # We did not move. This could be a battle or a wall collision.
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

# Clear menus
mgba.press_buttons(["B"])
time.sleep(0.3)

# Phase 1: Walk to northwest switch (1, 11) via row 13
path_to_switch = [
    (4, 13),
    (3, 13),
    (2, 13),
    (1, 13),
    (1, 12),
    (1, 11)
]

print("--- PHASE 1: WALKING TO WEST SWITCH ON 2F ---")
if walk_path(path_to_switch):
    print("Reached (1, 11) on 2F. Turning Right to face switch at (2, 11)...")
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    print("Interacting with switch to set State B...")
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    # Clear dialogue "A secret switch! Pressed it!"
    mgba.press_buttons(["B", "sleep 100", "B", "sleep 100", "B"])
    time.sleep(0.5)
    mgba.take_screenshot()
    
    # Phase 2: Walk to East Stairs (15, 11) via column 6 and row 8 (State B is active)
    path_to_east_stairs = [
        (1, 12),
        (1, 13),
        (2, 13),
        (3, 13),
        (4, 13),
        (5, 13),
        (6, 13),
        (6, 12),
        (6, 11),
        (6, 10),
        (6, 9),
        (6, 8),
        (7, 8),
        (8, 8),
        (9, 8),
        (10, 8), # open in State B
        (11, 8),
        (12, 8),
        (13, 8),
        (14, 8),
        (15, 8),
        (15, 9),
        (15, 10),
        (15, 11) # East Stairs
    ]
    print("--- PHASE 2: WALKING TO EAST STAIRS ON 2F (STATE B) ---")
    if walk_path(path_to_east_stairs):
        print("Reached East Stairs on 2F! Warping to 3F...")
        time.sleep(2.0) # Wait for warp
        pos_3f = get_pos()
        print("Arrived on 3F (East side). Position:", pos_3f)
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
            
            # Phase 4: Step Down through open balcony shutter and drop Left
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
        print("Failed to reach East Stairs on 2F.")
else:
    print("Failed to reach West Switch on 2F.")

