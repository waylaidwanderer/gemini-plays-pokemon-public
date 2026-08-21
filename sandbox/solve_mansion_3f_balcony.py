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

# 1. Walk to the West stairs at (7, 10) on 3F (we are currently at (9, 11))
path_to_stairs_3f = [
    (8, 11),
    (7, 11),
    (7, 10)
]

print("Walking to West stairs on 3F...")
if walk_path(path_to_stairs_3f):
    print("Warping to 2F...")
    time.sleep(2.0) # wait for warp animation
    print("Arrived on 2F. Position:", get_pos())
    mgba.take_screenshot()
    
    # 2. On 2F, walk to East stairs at (15, 11)
    # Let's try direct coordinates first, pathfinder will handle it.
    path_on_2f = [
        (15, 11)
    ]
    print("Walking to East stairs on 2F (State B)...")
    if walk_path(path_on_2f):
        print("Reached East stairs on 2F! Warping to 3F...")
        time.sleep(2.0)
        print("Arrived on 3F (East side). Position:", get_pos())
        mgba.take_screenshot()
    else:
        print("Failed to reach East stairs on 2F.")
        mgba.take_screenshot()
else:
    print("Failed to reach stairs on 3F.")
    mgba.take_screenshot()
