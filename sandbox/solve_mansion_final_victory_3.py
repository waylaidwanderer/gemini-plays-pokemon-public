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

# 1. Walk to switch at (12, 12) on 3F in State A
path_to_switch = [
    (1, 13),
    (4, 13),
    (4, 9),
    (9, 9),
    (9, 12),
    (12, 12)
]

print("Walking to center-left Mewtwo switch at (12, 12) on 3F...")
if walk_path(path_to_switch):
    print("Reached (12, 12). Facing Up and toggling Mewtwo switch to State B...")
    mgba.press_buttons(["Up"])
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
    
    # 2. Walk to balcony landing (20, 15) in State B
    path_to_balcony = [
        (11, 12),
        (11, 10),
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
    if walk_path(path_to_balcony):
        print("Reached balcony landing successfully! Dropping to B1F...")
        mgba.take_screenshot()
        # Step Down to (20, 18) and Left to drop
        mgba.press_buttons(["Down", "sleep 400", "Down", "sleep 400", "Down", "sleep 400", "Left"])
        time.sleep(3.0)
        print("Dropped! B1F Position:", get_pos())
        mgba.take_screenshot()
    else:
        print("Failed to reach balcony landing on 3F.")
        mgba.take_screenshot()
else:
    print("Failed to reach Mewtwo switch on 3F.")
    mgba.take_screenshot()
