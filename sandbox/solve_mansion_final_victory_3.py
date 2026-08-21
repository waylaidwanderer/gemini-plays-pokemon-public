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
    # Clear dialogue text boxes or battle transitions
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.05)
    # Attempt to run: Down, Right, A
    print("  Attempting to RUN...")
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.5)
    # Clear potential "Escaped safely!" text
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
        # We might be in a battle or blocked
        handle_battle()
        after = get_pos()
    return after != before, after

def walk_path(path):
    print("Starting path traversal:", path)
    for target in path:
        tx, ty = target
        print(f"Targeting: ({tx}, {ty})")
        reached = False
        for attempt in range(25):
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
                # Try the alternative direction to slide around simple obstacle
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

# Phase 1: Walk back to (2, 12) from current (6, 13) and set switch to State A
path_to_switch = [
    (2, 13),
    (2, 12)
]

print("--- PHASE 1: RETURNING TO WEST SWITCH AND TOGGLING TO STATE A ---")
if walk_path(path_to_switch):
    print("Reached (2, 12). Turning UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    print("Toggling 3F switch to State A...")
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    # Clear text
    mgba.press_buttons(["B", "sleep 100", "B", "sleep 100", "B"])
    time.sleep(0.5)
    mgba.take_screenshot()
    
    # Phase 2: Walk along Row 11 on 3F (State A) to the East Stairs at (15, 11)
    path_to_east_stairs = [
        (3, 12),
        (3, 11),
        (14, 11),
        (15, 11)
    ]
    print("--- PHASE 2: WALKING TO EAST STAIRS ON 3F (STATE A) ---")
    if walk_path(path_to_east_stairs):
        print("Reached East Stairs on 3F! Stepping on stairs to warp to 2F...")
        time.sleep(2.0) # wait for warp transition
        print("Arrived on 2F. Position:", get_pos())
        mgba.take_screenshot()
        
        # Phase 3: On 2F (State A), walk from landing (likely 16, 11 or similar) to (12, 11)
        path_to_2f_switch = [
            (12, 11)
        ]
        print("--- PHASE 3: WALKING TO 2F SWITCH (13, 11) ---")
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
            
            # Phase 4: Walk back to the East Stairs on 2F (State B)
            path_back_to_stairs = [
                (15, 11)
            ]
            print("--- PHASE 4: WALKING BACK TO EAST STAIRS ON 2F ---")
            if walk_path(path_back_to_stairs):
                print("Reached East Stairs on 2F! Stepping to warp to 3F...")
                time.sleep(2.0)
                print("Arrived on 3F (East side, State B). Position:", get_pos())
                mgba.take_screenshot()
                
                # Phase 5: On 3F (State B), walk from landing (16, 11) to the Balcony
                path_to_balcony = [
                    (21, 11),
                    (21, 15),
                    (20, 15)
                ]
                print("--- PHASE 5: WALKING TO BALCONY ON 3F (STATE B) ---")
                if walk_path(path_to_balcony):
                    print("Reached Balcony landing (20, 15) on 3F!")
                    mgba.take_screenshot()
                    
                    # Phase 6: Step Down through open shutter gate and drop Left
                    path_to_edge = [
                        (20, 17),
                        (20, 18)
                    ]
                    print("--- PHASE 6: STEPPING TO DROP EDGE AND DROPPING ---")
                    if walk_path(path_to_edge):
                        print("At drop edge (20, 18). Dropping Left to B1F!")
                        mgba.take_screenshot()
                        mgba.press_buttons(["Left"])
                        time.sleep(3.0) # wait for falling warp
                        print("Landed on B1F! Position:", get_pos())
                        mgba.take_screenshot()
                    else:
                        print("Failed to reach drop edge.")
                        mgba.take_screenshot()
                else:
                    print("Failed to walk to Balcony.")
                    mgba.take_screenshot()
            else:
                print("Failed to return to East Stairs on 2F.")
                mgba.take_screenshot()
        else:
            print("Failed to reach 2F Switch.")
            mgba.take_screenshot()
    else:
        print("Failed to reach East Stairs on 3F.")
        mgba.take_screenshot()
else:
    print("Failed to reach West Switch to toggle to State A.")
    mgba.take_screenshot()

