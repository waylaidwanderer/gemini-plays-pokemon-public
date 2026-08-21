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

# 1. Walk to (12, 12) on 2F
path = [
    (12, 7),
    (12, 12)
]

print("Walking to switch on 2F...")
if walk_path(path):
    print("Reached (12, 12). Facing Up and interacting with Mewtwo switch...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    # Switch Interaction:
    # 1. Press A to trigger prompt: "A secret switch! Press it?"
    # 2. Wait, the Gen 1 Mewtwo statue prompt defaults to "NO" or "YES"?
    # Let's press A, then press Up to move cursor to YES (just in case), then A, then B.
    # Let's do this sequentially to be extremely safe.
    mgba.press_buttons([
        "A", "sleep 1000", # open textbox
        "Up", "sleep 500",  # move cursor to YES (if it defaults to NO)
        "A", "sleep 1000", # confirm YES
        "B", "sleep 500",  # close dialogue
        "B"
    ])
    time.sleep(3.0)
    print("Mewtwo switch toggled. Position:", get_pos())
    mgba.take_screenshot()
else:
    print("Failed to reach switch.")
    mgba.take_screenshot()
