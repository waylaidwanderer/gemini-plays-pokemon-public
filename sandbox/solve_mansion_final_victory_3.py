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
    # Run option: Down, Right, A
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

# 1. Walk to switch at (2, 11) from current (7, 11) on 3F
path_to_switch = [
    (8, 11),
    (8, 9),
    (1, 9),
    (1, 11)
]

print("Walking to switch...")
if walk_path(path_to_switch):
    print("Reached (1, 11). Facing Right and toggling switch to State B...")
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    
    # Toggle switch to State B
    mgba.press_buttons([
        "A", "sleep 1000",
        "A", "sleep 1000",
        "Up", "sleep 1000",
        "A", "sleep 1000",
        "B", "sleep 500",
        "B"
    ])
    time.sleep(3.0)
    print("Switch toggled. Position:", get_pos())
    mgba.take_screenshot()
    
    # 2. Walk to (9, 10) in State B
    path_to_9_10 = [
        (1, 9),
        (9, 9),
        (9, 10)
    ]
    print("Walking to (9, 10) in State B...")
    if walk_path(path_to_9_10):
        print("Reached (9, 10) successfully! Position:", get_pos())
        mgba.take_screenshot()
    else:
        print("Failed to reach (9, 10).")
        mgba.take_screenshot()
else:
    print("Failed to reach switch on 3F.")
    mgba.take_screenshot()
