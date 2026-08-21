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
    # Run from battle
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
                print(f"  Blocked at {c} trying to move {btn}! Exiting script.")
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

# 1. Walk from current (13, 12) on 2F (State B) to West stairs at (7, 10)
path_2f = [
    (12, 12),
    (12, 10),
    (7, 10)
]

print("Walking to West stairs on 2F (State B)...")
if walk_path(path_2f):
    print("Reached West stairs! Warping up to 3F...")
    time.sleep(2.0) # wait for warp
    print("Arrived on 3F. Position:", get_pos())
    mgba.take_screenshot()
    
    # 2. On 3F (State B), walk to (9, 10)
    path_3f = [
        (9, 11),
        (9, 10)
    ]
    print("Walking to (9, 10) on 3F...")
    if walk_path(path_3f):
        print("Reached (9, 10)! Testing if we can walk Right to (10, 10)...")
        success, pos = step_dir("Right")
        if success:
            print("Walked Right to (10, 10)! Pos:", pos)
            mgba.take_screenshot()
            
            # Try walking Right to (11, 10)
            success2, pos2 = step_dir("Right")
            if success2:
                print("Walked Right to (11, 10)! East side reached!")
                # Walk to balcony landing
                path_balcony = [
                    (11, 5),
                    (20, 5),
                    (20, 3),
                    (21, 3),
                    (25, 3),
                    (25, 7),
                    (26, 7),
                    (26, 12),
                    (25, 12),
                    (25, 14),
                    (21, 14),
                    (21, 15),
                    (20, 15)
                ]
                print("Walking to balcony landing on 3F...")
                if walk_path(path_balcony):
                    print("Reached balcony landing! Dropping to B1F...")
                    mgba.take_screenshot()
                    mgba.press_buttons(["Down", "sleep 400", "Down", "sleep 400", "Down", "sleep 400", "Left"])
                    time.sleep(3.0)
                    print("Dropped! B1F Position:", get_pos())
                    mgba.take_screenshot()
                else:
                    print("Failed to reach balcony landing.")
                    mgba.take_screenshot()
            else:
                print("Blocked trying to move from (10, 10) to (11, 10).")
                mgba.take_screenshot()
        else:
            print("Blocked trying to move from (9, 10) to (10, 10).")
            mgba.take_screenshot()
    else:
        print("Failed to reach (9, 10) on 3F.")
        mgba.take_screenshot()
else:
    print("Failed to reach West stairs on 2F.")
    mgba.take_screenshot()
