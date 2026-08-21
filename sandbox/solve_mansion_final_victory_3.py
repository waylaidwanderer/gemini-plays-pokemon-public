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
        for attempt in range(20):
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

# Phase 1: Walk to the 3F West-side Switch at (2, 11) via Row 11 (State A is active)
# Current position is (13, 12)
path_to_switch = [
    (12, 12),
    (12, 11),
    (3, 11),
    (3, 12),
    (2, 12)
]

print("--- PHASE 1: WALKING TO SWITCH (2, 11) ---")
if walk_path(path_to_switch):
    print("Reached switch location (2, 12)!")
    mgba.take_screenshot()
    
    # Face UP to statue at (2, 11)
    print("Turning UP to face statue...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    # Toggle switch to State B
    print("Interacting with statue switch to set State B...")
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    # Clear text
    mgba.press_buttons(["B", "sleep 100", "B", "sleep 100", "B"])
    time.sleep(0.5)
    mgba.take_screenshot()
    
    # Phase 2: Walk the Master Route to Balcony Drop (State B is active)
    # Starting from (2, 12) on 3F
    master_route = [
        (7, 12),
        (7, 13),
        (9, 13),
        (9, 10),
        (11, 10),
        (11, 5),
        (20, 5),
        (21, 3),
        (26, 3),
        (26, 5),
        (24, 5),
        (24, 7),
        (26, 7),
        (26, 12),
        (25, 12),
        (25, 14),
        (22, 14),
        (21, 14),
        (21, 15),
        (20, 15)
    ]
    
    print("--- PHASE 2: WALKING MASTER ROUTE TO BALCONY ---")
    if walk_path(master_route):
        print("Reached balcony landing (20, 15)!")
        mgba.take_screenshot()
        
        # Step Down to (20, 18) through open shutter gate
        print("Stepping Down to (20, 18)...")
        walk_to_edge = [
            (20, 17),
            (20, 18)
        ]
        if walk_path(walk_to_edge):
            print("At drop edge (20, 18). Dropping Left to B1F!")
            mgba.take_screenshot()
            mgba.press_buttons(["Left"])
            time.sleep(3.0) # wait for fall transition
            print("Dropped! New Position:", get_pos())
            mgba.take_screenshot()
        else:
            print("Failed to reach drop edge.")
            mgba.take_screenshot()
    else:
        print("Failed to navigate Master Route to Balcony.")
        mgba.take_screenshot()
else:
    print("Failed to reach West-side Switch.")
    mgba.take_screenshot()

