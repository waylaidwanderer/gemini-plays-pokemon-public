import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

print("Starting toggle to State A and gate test. Starting pos:", get_pos())

def handle_battle():
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.05)
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.2)
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.05)

def step_to_closed_loop(tx, ty):
    for attempt in range(12):
        c = get_pos()
        if c['x'] == tx and c['y'] == ty:
            return True
        dx = tx - c['x']
        dy = ty - c['y']
        btn = None
        if abs(dx) >= abs(dy):
            if dx > 0: btn = "Right"
            else: btn = "Left"
        else:
            if dy > 0: btn = "Down"
            else: btn = "Up"
        mgba.press_buttons([btn])
        time.sleep(0.4)
        after = get_pos()
        if after == c:
            handle_battle()
            after_retry = get_pos()
            if after_retry == c:
                return False
    return get_pos() == {'x': tx, 'y': ty}

# 1. Walk back to (1, 11)
path_to_switch = [
    (11, 6), (11, 11), (3, 11), (3, 12), (1, 12), (1, 11)
]
success_walk = True
for (tx, ty) in path_to_switch:
    if not step_to_closed_loop(tx, ty):
        success_walk = False
        break

if success_walk:
    print("Reached switch station (1, 11). Turning Right...")
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    
    # Toggle to State A (interact, YES, clear)
    print("Toggling switch to State A...")
    mgba.press_buttons([
        "A", "sleep 1200",
        "Up", "sleep 400",
        "A", "sleep 1500",
        "B", "sleep 400",
        "B"
    ])
    time.sleep(5.0)
    print("Toggle complete! Pos:", get_pos())
    
    # 2. Walk to (20, 6)
    path_back = [
        (1, 12), (3, 12), (3, 11), (11, 11), (11, 6), (20, 6)
    ]
    success_back = True
    for (tx, ty) in path_back:
        if not step_to_closed_loop(tx, ty):
            success_back = False
            break
            
    if success_back:
        print("Reached (20, 6). Testing gate at (20, 5)...")
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        print("Pos after testing Up at (20, 5):", get_pos())
        mgba.take_screenshot()
    else:
        print("Failed to walk back to (20, 6)")
else:
    print("Failed to reach (1, 11)")
