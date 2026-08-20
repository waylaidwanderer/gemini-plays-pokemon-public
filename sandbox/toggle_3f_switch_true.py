import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

print("Starting toggle sequence from:", get_pos())

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

# Path to (1, 11)
path = [
    # Walk Left along row 6 to column 11
    (20, 6), (19, 6), (18, 6), (17, 6), (16, 6), (15, 6), (14, 6), (13, 6), (12, 6), (11, 6),
    # Down column 11 to row 11
    (11, 7), (11, 8), (11, 9), (11, 10), (11, 11),
    # Left through open gate at (10, 11)
    (10, 11), (9, 11), (8, 11), (7, 11), (6, 11), (5, 11), (4, 11), (3, 11),
    # Down to (3, 12)
    (3, 12),
    # Left to (1, 12)
    (2, 12), (1, 12),
    # Up to (1, 11)
    (1, 11)
]

success = True
for (tx, ty) in path:
    if not step_to(tx, ty):
        print(f"Failed at step ({tx}, {ty})")
        success = False
        break

if success:
    print("Successfully reached (1, 11). Turning Right to face the switch...")
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    print("Interacting with A...")
    mgba.press_buttons(["A"])
    time.sleep(0.6)
    # Select YES
    mgba.press_buttons(["A"])
    time.sleep(0.6)
    # Clear dialogue
    mgba.press_buttons(["B"])
    time.sleep(0.4)
    mgba.press_buttons(["B"])
    time.sleep(0.4)
    print("Toggle complete! Position:", get_pos())
    mgba.take_screenshot()
