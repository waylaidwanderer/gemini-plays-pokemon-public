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

# 1. Walk to stairs on 3F and go down to 2F
path_3f = [
    (9, 10),
    (8, 10),
    (7, 10)
]
print("Walking to West stairs on 3F...")
if walk_path(path_3f):
    print("Warped down to 2F!")
    time.sleep(2.0)
    print("Position on 2F:", get_pos())
    mgba.take_screenshot()
    
    # 2. Walk to switch at (12, 11) on 2F (State B)
    path_2f_switch = [
        (12, 10),
        (12, 11)
    ]
    print("Walking to switch on 2F...")
    if walk_path(path_2f_switch):
        print("At (12, 11). Facing Right and toggling switch to State A...")
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        
        # Toggle switch to State A (only A, A, B, B)
        mgba.press_buttons([
            "A", "sleep 1000",
            "A", "sleep 1000",
            "B", "sleep 500",
            "B"
        ])
        time.sleep(3.0)
        print("Toggled! Position after toggle:", get_pos())
        mgba.take_screenshot()
        
        # 3. Test if row 7 is open to the East in State A
        # Let's walk to (12, 7) first
        path_test = [
            (12, 10),
            (12, 7)
        ]
        if walk_path(path_test):
            print("At (12, 7). Trying to walk Right towards (16, 7) to test row 7...")
            # Walk Right step by step
            for i in range(4):
                pos_before = get_pos()
                success, pos_after = step_dir("Right")
                print(f"Step {i+1}: from {pos_before} to {pos_after}")
                if not success:
                    print("Blocked at row 7!")
                    break
            print("Final test position reached:", get_pos())
            mgba.take_screenshot()
        else:
            print("Failed to reach (12, 7).")
    else:
        print("Failed to reach switch on 2F.")
else:
    print("Failed to reach stairs on 3F.")
