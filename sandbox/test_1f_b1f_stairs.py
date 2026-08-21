import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

def handle_battle():
    print("  Battle/Dialogue detected! Handling...")
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.05)
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.2)
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.05)

def step_dir(d):
    before = get_pos()
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
                print(f"  Blocked! Trying alternative {other_btn}...")
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

# 1. Walk to West stairs on 3F and go down to 2F
path_3f = [
    (7, 10)
]
print("Walking to West stairs on 3F...")
if walk_path(path_3f):
    print("Warped down to 2F!")
    time.sleep(2.0)
    
    # 2. Go down West stairs on 2F to 1F
    print("Going down stairs from 2F to 1F...")
    # on 2F West stairs are at (7, 10), stepping on it warps to 1F (lands at (7, 11) or similar)
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    print("Arrived on 1F. Position:", get_pos())
    mgba.take_screenshot()
    
    # 3. Try to walk to B1F stairs on 1F (State B)
    # The B1F stairs are in the bottom-right corner, e.g. (21, 23)
    # Let's target (21, 23) directly and see if we can reach it!
    path_1f = [
        (21, 23)
    ]
    print("Attempting to walk to B1F stairs on 1F...")
    if walk_path(path_1f):
        print("Successfully reached B1F stairs on 1F! Warping to B1F...")
        time.sleep(2.0)
        print("Arrived on B1F! Position:", get_pos())
        mgba.take_screenshot()
        
        # 4. Walk to Secret Key room at (1, 4) on B1F
        path_b1f = [
            (1, 4)
        ]
        print("Walking to Secret Key on B1F...")
        if walk_path(path_b1f):
            print("Reached Secret Key! Picking it up...")
            mgba.press_buttons(["A"])
            time.sleep(1.0)
            print("Secret Key retrieved successfully! Current position:", get_pos())
            mgba.take_screenshot()
        else:
            print("Failed to reach Secret Key on B1F.")
            mgba.take_screenshot()
    else:
        print("Failed to reach B1F stairs on 1F.")
        mgba.take_screenshot()
else:
    print("Failed to reach West stairs on 3F.")
