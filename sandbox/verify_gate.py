import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

print("Starting gate verification from:", get_pos())

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

# Walk from (1, 10) to (3, 11) via row 12
path_to_test = [(1, 11), (1, 12), (2, 12), (3, 12), (3, 11)]
for (tx, ty) in path_to_test:
    step_to_closed_loop(tx, ty)

# Now try to walk Right towards column 11
print("Position before gate test:", get_pos())
# We will step Right repeatedly. If gate is closed, we will get blocked.
# Gate is at column 10 (between x=9 and x=11 on row 11)
for i in range(10):
    c = get_pos()
    print(f"Step {i+1}. Current pos: {c}. Pressing Right...")
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    after = get_pos()
    if after == c:
        print("Blocked on Right press! Checking for battle...")
        handle_battle()
        after_retry = get_pos()
        if after_retry == c:
            print("STILL BLOCKED. The gate is indeed CLOSED (State B)!")
            break
    if after['x'] >= 11:
        print("We crossed column 10! Current pos:", after)
        print("The gate is OPEN (State A)!")
        break
