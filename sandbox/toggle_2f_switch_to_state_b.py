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

# 1. Walk from current (15, 7) on 3F to (15, 11) to warp down to 2F
path_to_stairs = [
    (15, 8),
    (15, 9),
    (15, 10),
    (15, 11)
]

print("--- STEP 1: WALKING TO 3F EAST STAIRS ---")
if walk_path(path_to_stairs):
    print("Reached stairs at (15, 11). Warping to 2F...")
    time.sleep(2.0) # Wait for warp
    pos_2f = get_pos()
    print("Arrived on 2F. Position:", pos_2f)
    mgba.take_screenshot()
    
    # 2. Walk to (12, 11) on 2F to toggle the switch
    path_to_switch = [
        (15, 11),
        (14, 11),
        (13, 11),
        (12, 11)
    ]
    print("--- STEP 2: WALKING TO SWITCH ON 2F ---")
    if walk_path(path_to_switch):
        print("Reached (12, 11) on 2F. Turning Right...")
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        print("Toggling 2F switch to State B...")
        mgba.press_buttons(["A"])
        time.sleep(0.5)
        mgba.press_buttons(["B", "sleep 100", "B", "sleep 100", "B"])
        time.sleep(0.5)
        mgba.take_screenshot()
        
        # 3. Walk back to (15, 11) on 2F to warp back to 3F
        path_back_to_stairs = [
            (13, 11),
            (14, 11),
            (15, 11)
        ]
        print("--- STEP 3: RETURNING TO EAST STAIRS ON 2F ---")
        if walk_path(path_back_to_stairs):
            print("Reached stairs on 2F! Warping back to 3F...")
            time.sleep(2.0) # Wait for warp
            pos_3f = get_pos()
            print("Arrived on 3F. Position:", pos_3f)
            mgba.take_screenshot()
        else:
            print("Failed to return to 2F stairs.")
    else:
        print("Failed to walk to 2F switch.")
else:
    print("Failed to reach 3F stairs.")

