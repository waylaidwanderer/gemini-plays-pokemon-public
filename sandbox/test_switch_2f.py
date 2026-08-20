import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

print("Testing 2F Mewtwo switch from:", get_pos())

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

# 1. Test Side (12, 11) facing Right
print("\n--- Testing (12, 11) facing Right ---")
path_to_left_side = [
    (16, 10), (16, 9), (16, 8), (16, 7),
    (15, 7), (14, 7), (13, 7), (12, 7),
    (12, 8), (12, 9), (12, 10), (12, 11)
]

success_left = True
for (tx, ty) in path_to_left_side:
    if not step_to_closed_loop(tx, ty):
        success_left = False
        break

if success_left:
    print("Reached (12, 11). Facing Right...")
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    # Check if dialogue is open by pressing Down (which is walkable to 12, 12)
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    p = get_pos()
    if p == {'x': 12, 'y': 11}:
        print("-> SUCCESS! (12, 11) facing Right successfully opened the switch textbox.")
        # Clear dialogue
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        mgba.press_buttons(["B"])
        time.sleep(0.4)
    else:
        print("-> FAILED. We walked to:", p)
else:
    print("Could not reach (12, 11)")

# 2. Test Side (13, 12) facing Up
print("\n--- Testing (13, 12) facing Up ---")
# From (12, 11) or (12, 12), walk to (13, 12)
path_to_bottom_side = [
    (12, 12), (13, 12)
]
success_bottom = True
for (tx, ty) in path_to_bottom_side:
    if not step_to_closed_loop(tx, ty):
        success_bottom = False
        break

if success_bottom:
    print("Reached (13, 12). Facing Up...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    # Check if dialogue is open by pressing Down (which is walkable to 13, 13)
    # Wait, on 2F is (13, 13) walkable? Yes, pink floor.
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    p = get_pos()
    if p == {'x': 13, 'y': 12}:
        print("-> SUCCESS! (13, 12) facing Up successfully opened the switch textbox.")
        # Clear dialogue
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        mgba.press_buttons(["B"])
        time.sleep(0.4)
    else:
        print("-> FAILED. We walked to:", p)
else:
    print("Could not reach (13, 12)")
