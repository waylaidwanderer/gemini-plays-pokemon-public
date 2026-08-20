import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

print("Starting 3F balcony route from:", get_pos())

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

# Route to balcony
path = [
    # Right to (7, 12)
    (3, 12), (4, 12), (5, 12), (6, 12), (7, 12),
    # Down to (7, 13)
    (7, 13),
    # Right to (9, 13)
    (8, 13), (9, 13),
    # Up to (9, 10)
    (9, 12), (9, 11), (9, 10),
    # Right to (11, 10)
    (10, 10), (11, 10),
    # Up to (11, 5)
    (11, 9), (11, 8), (11, 7), (11, 6), (11, 5),
    # Right to (21, 5)
    (12, 5), (13, 5), (14, 5), (15, 5), (16, 5), (17, 5), (18, 5), (19, 5), (20, 5), (21, 5),
    # Up to (21, 3)
    (21, 4), (21, 3),
    # Right to (26, 3)
    (22, 3), (23, 3), (24, 3), (25, 3), (26, 3),
    # Down to (26, 5)
    (26, 4), (26, 5),
    # Left to (24, 5)
    (25, 5), (24, 5),
    # Down to (24, 7)
    (24, 6), (24, 7),
    # Right to (26, 7)
    (25, 7), (26, 7),
    # Down to (26, 12)
    (26, 8), (26, 9), (26, 10), (26, 11), (26, 12),
    # Left to (25, 12)
    (25, 12),
    # Down to (25, 14)
    (25, 13), (25, 14),
    # Left to (22, 14)
    (24, 14), (23, 14), (22, 14),
    # Left and Down to doorway at (21, 15)
    (21, 14), (21, 15),
    # Step Left to landing (20, 15)
    (20, 15),
    # Down column 20 to row 18
    (20, 16), (20, 17), (20, 18),
    # Step Left onto (19, 18) to drop!
    (19, 18)
]

success = True
for (tx, ty) in path:
    if not step_to(tx, ty):
        print(f"Failed at step ({tx}, {ty})")
        success = False
        break

if success:
    print("Dropped! Current pos after drop:", get_pos())
    mgba.take_screenshot()
