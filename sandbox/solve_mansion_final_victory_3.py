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
    
    # Try up to 3 times to step in direction d to prevent dropped inputs from triggering handle_battle
    for attempt in range(3):
        mgba.press_buttons([d])
        # Wait up to 0.5 seconds for position to change (polling)
        for _ in range(5):
            time.sleep(0.1)
            after = get_pos()
            if after['x'] != before['x'] or after['y'] != before['y']:
                return True, after
        print(f"  Attempt {attempt + 1} to step {d} failed. Retrying...")
        
    # If we still haven't moved after 3 attempts, handle potential battle/dialogue
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

# Phase 1: Walk from current (13, 12) on 2F (State B) to West Stairs at (7, 10) and warp to 3F
path_to_west_stairs = [
    (12, 12),
    (11, 12),
    (11, 13),
    (11, 14),
    (10, 14),
    (9, 14),
    (8, 14),
    (7, 14),
    (7, 13),
    (7, 12),
    (7, 11),
    (7, 10) # West Stairs
]

print("--- PHASE 1: WALKING TO WEST STAIRS ON 2F (STATE B) ---")
if walk_path(path_to_west_stairs):
    print("Reached West Stairs at (7, 10). Warping to 3F...")
    time.sleep(2.0) # Wait for warp
    pos_3f = get_pos()
    print("Arrived on 3F. Position:", pos_3f)
    mgba.take_screenshot()
    
    # Phase 2: Walk to switch at (2, 11) on 3F and toggle to State A
    path_to_switch = [
        (6, 11),
        (5, 11),
        (4, 11),
        (3, 11),
        (3, 12),
        (2, 12)
    ]
    print("--- PHASE 2: WALKING TO 3F SWITCH ---")
    if walk_path(path_to_switch):
        print("Reached switch location (2, 12) on 3F. Turning UP...")
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        print("Toggling switch to State A...")
        mgba.press_buttons(["A"])
        time.sleep(0.5)
        mgba.press_buttons(["B", "sleep 100", "B", "sleep 100", "B"])
        time.sleep(0.5)
        mgba.take_screenshot()
        
        # Phase 3: Walk to East Stairs via column 19 on 3F (State A)
        path_to_east_stairs = [
            (3, 12),
            (3, 11),
            (12, 11), # gate at 10,11 is OPEN in State A!
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
            (19, 8), # open gate in State A!
            (19, 9),
            (19, 10),
            (19, 11),
            (18, 11),
            (17, 11),
            (16, 11),
            (15, 11) # East Stairs
        ]
        print("--- PHASE 3: WALKING TO 3F EAST STAIRS (STATE A) ---")
        if walk_path(path_to_east_stairs):
            print("Reached East Stairs on 3F! Warping to 2F...")
            time.sleep(2.0) # Wait for warp
            pos_2f = get_pos()
            print("Arrived on 2F (East side). Position:", pos_2f)
            mgba.take_screenshot()
            
            # Phase 4: Walk to (12, 11) on 2F and toggle switch to State B
            path_to_switch_b = [
                (14, 11),
                (13, 11),
                (12, 11)
            ]
            print("--- PHASE 4: WALKING TO SWITCH B ON 2F ---")
            if walk_path(path_to_switch_b):
                print("Reached (12, 11) on 2F. Turning Right...")
                mgba.press_buttons(["Right"])
                time.sleep(0.4)
                print("Toggling switch to State B...")
                mgba.press_buttons(["A"])
                time.sleep(0.5)
                mgba.press_buttons(["B", "sleep 100", "B", "sleep 100", "B"])
                time.sleep(0.5)
                mgba.take_screenshot()
                
                # Phase 5: Walk back to stairs (15, 11) and warp to 3F (State B)
                path_back_to_stairs = [
                    (13, 11),
                    (14, 11),
                    (15, 11)
                ]
                print("--- PHASE 5: WARPING TO 3F (STATE B) ---")
                if walk_path(path_back_to_stairs):
                    print("Warping to 3F...")
                    time.sleep(2.0)
                    pos_3f_b = get_pos()
                    print("Arrived on 3F. Position:", pos_3f_b)
                    mgba.take_screenshot()
                    
                    # Phase 6: Walk to Balcony landing (20, 15) on 3F (State B)
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
                    print("--- PHASE 6: WALKING TO BALCONY ON 3F (STATE B) ---")
                    if walk_path(path_to_balcony):
                        print("Reached Balcony landing (20, 15) on 3F!")
                        mgba.take_screenshot()
                        
                        # Phase 7: Step Down and drop Left
                        path_to_edge = [
                            (20, 16),
                            (20, 17),
                            (20, 18)
                        ]
                        print("--- PHASE 7: STEPPING TO DROP EDGE AND DROPPING ---")
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
            print("Failed to reach East Stairs on 3F.")
    else:
        print("Failed to reach 3F Switch.")
else:
    print("Failed to reach West Stairs.")

