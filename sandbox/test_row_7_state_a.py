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

# 1. Walk from current (6, 13) on 3F to the west switch at (2, 12) and toggle to State A
path_to_switch = [
    (5, 13),
    (4, 13),
    (3, 13),
    (2, 13),
    (2, 12)
]

print("--- PHASE 1: RETURNING TO WEST SWITCH AND SETTING STATE A ---")
if walk_path(path_to_switch):
    print("Reached (2, 12). Turning UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    print("Toggling 3F switch to State A...")
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    mgba.press_buttons(["B", "sleep 100", "B", "sleep 100", "B"])
    time.sleep(0.5)
    mgba.take_screenshot()
    
    # 2. Walk to the east stairs via Column 19 on row 8
    path_to_stairs = [
        (3, 12),
        (3, 11),
        (12, 11),
        (12, 10),
        (12, 9),
        (12, 8),
        (12, 7),
        (13, 7),
        (14, 7),
        (15, 7),
        (16, 7),
        (17, 7),
        (18, 7),
        (19, 7),
        (19, 8), # Test column 19!
        (19, 9),
        (19, 10),
        (19, 11),
        (18, 11),
        (17, 11),
        (16, 11),
        (15, 11)
    ]
    print("--- PHASE 2: WALKING TO 3F EAST STAIRS VIA COLUMN 19 ---")
    if walk_path(path_to_stairs):
        print("Reached East Stairs on 3F! Warping to 2F...")
        time.sleep(2.0)
        print("Arrived on 2F. Position:", get_pos())
        mgba.take_screenshot()
    else:
        print("Failed to reach East Stairs via column 19.")
        mgba.take_screenshot()
else:
    print("Failed to reach West Switch.")

