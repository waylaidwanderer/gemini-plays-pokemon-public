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
    
    # Wait up to 0.7 seconds for position to change (polling)
    after = before
    for _ in range(7):
        time.sleep(0.1)
        after = get_pos()
        if after['x'] != before['x'] or after['y'] != before['y']:
            break
            
    if before['x'] == after['x'] and before['y'] == after['y']:
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

# Phase 1: Walk to East Stairs (15, 11) via Row 7 and Column 12 (State A is active)
# We are currently at (5, 8)
path_to_east_stairs = [
    (5, 7),
    (6, 7),
    (7, 7),
    (8, 7),
    (9, 7),
    (10, 7),
    (11, 7),
    (12, 7),
    (12, 8),
    (12, 9),
    (12, 10),
    (12, 11),
    (13, 11),
    (14, 11),
    (15, 11)
]

print("--- PHASE 1: WALKING TO EAST STAIRS ON 2F (STATE A) ---")
if walk_path(path_to_east_stairs):
    print("Reached (15, 11). Walking Left to toggle to State B first...")
    path_to_switch_b = [
        (14, 11),
        (13, 11),
        (12, 11)
    ]
    if walk_path(path_to_switch_b):
        print("Reached (12, 11) on 2F. Turning Right to face switch at (13, 11)...")
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        print("Toggling switch to State B...")
        mgba.press_buttons(["A"])
        time.sleep(0.5)
        mgba.press_buttons(["B", "sleep 100", "B", "sleep 100", "B"])
        time.sleep(0.5)
        mgba.take_screenshot()
        
        # Phase 2: Walk to stairs (15, 11) and warp to 3F (State B)
        path_back_to_stairs = [
            (13, 11),
            (14, 11),
            (15, 11)
        ]
        print("--- PHASE 2: WARPING TO 3F (STATE B) ---")
        if walk_path(path_back_to_stairs):
            print("Warping to 3F...")
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
            print("Failed to return to East Stairs.")
    else:
        print("Failed to reach 2F Switch B.")
else:
    print("Failed to reach East Stairs on 2F.")

