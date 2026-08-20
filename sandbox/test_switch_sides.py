import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

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

print("Testing switch interaction sides...")

# 1. Test side (1, 11) facing Right
print("\n--- Testing (1, 11) facing Right ---")
if step_to_closed_loop(1, 11):
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    # Press Down to see if we walk or if we are in a menu
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    p = get_pos()
    if p == {'x': 1, 'y': 11}:
        print("-> SUCCESS! (1, 11) facing Right successfully opened the textbox.")
        # Clear textbox
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        mgba.press_buttons(["B"])
        time.sleep(0.4)
    else:
        print("-> FAILED. We walked to:", p)
else:
    print("Could not reach (1, 11)")

# 2. Test side (2, 12) facing Up
print("\n--- Testing (2, 12) facing Up ---")
if step_to_closed_loop(2, 12):
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    # Press Down to see if we walk or if we are in a menu
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    p = get_pos()
    if p == {'x': 2, 'y': 12}:
        print("-> SUCCESS! (2, 12) facing Up successfully opened the textbox.")
        # Clear textbox
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        mgba.press_buttons(["B"])
        time.sleep(0.4)
    else:
        print("-> FAILED. We walked to:", p)
else:
    print("Could not reach (2, 12)")
