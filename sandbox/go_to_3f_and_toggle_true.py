import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

print("Starting route to 3F switch from:", get_pos())

def handle_battle():
    print("Battle or block! Clearing screens...")
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    # Run from battle
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.2)
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.1)

def step_to(tx, ty):
    for attempt in range(12):
        c = get_pos()
        if c['x'] == tx and c['y'] == ty:
            print(f"Reached: ({tx}, {ty})")
            return True
        dx = tx - c['x']
        dy = ty - c['y']
        
        btn = None
        if dx > 0:
            btn = "Right"
        elif dx < 0:
            btn = "Left"
        elif dy > 0:
            btn = "Down"
        elif dy < 0:
            btn = "Up"
            
        print(f"Standing at {c}. Pressing {btn} to reach ({tx}, {ty})...")
        mgba.press_buttons([btn])
        time.sleep(0.4)
        
        after = get_pos()
        if after == c:
            print("Blocked! Handling battle or obstacles...")
            handle_battle()
            after_retry = get_pos()
            if after_retry == c:
                print(f"STILL BLOCKED at {c} trying to reach ({tx}, {ty}). Aborting step.")
                return False
    return False

# Route to (2, 12)
# We are currently at (16, 7). Let's go Left to (11, 7)
path = [
    (15, 7), (14, 7), (13, 7), (12, 7), (11, 7),
    # Down column 11 to row 11
    (11, 8), (11, 9), (11, 10), (11, 11),
    # Left through the gate at (10, 11)
    (10, 11), (9, 11), (8, 11), (7, 11), (6, 11), (5, 11), (4, 11), (3, 11), (2, 11),
    # Down to (2, 12)
    (2, 12)
]

success = True
for (tx, ty) in path:
    if not step_to(tx, ty):
        print(f"Failed to reach step: ({tx}, {ty})")
        success = False
        break

if success:
    print("Successfully reached switch tile (2, 12). Interacting with switch...")
    # Face UP
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    # Interact
    mgba.press_buttons(["A"])
    time.sleep(0.8)
    # Clear dialogue if any
    for _ in range(3):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    print("Done! Position:", get_pos())
    mgba.take_screenshot()
else:
    print("Failed to reach (2, 12).")
