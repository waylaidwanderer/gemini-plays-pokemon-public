import mgba
import time

def handle_battle():
    print("Coordinates did not change. Likely a battle! Attempting to flee...")
    # Gen 1 Battle Menu: FIGHT is top-left, RUN is bottom-right.
    # We press Down, Right, A to select RUN.
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.0)
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)

def walk_step(tx, ty, direction):
    attempts = 0
    while attempts < 30:
        pos = mgba.get_coordinates()
        if pos['x'] == tx and pos['y'] == ty:
            return True
            
        mgba.press_buttons([direction])
        time.sleep(0.55)
        new_pos = mgba.get_coordinates()
        
        if new_pos == pos:
            print(f"Bumped at {pos} going {direction}. Attempting battle escape...")
            handle_battle()
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
        else:
            if new_pos['x'] == tx and new_pos['y'] == ty:
                return True
        attempts += 1
    return False

def walk_to(tx, ty):
    pos = mgba.get_coordinates()
    print(f"Walking from {pos} to ({tx}, {ty})...")
    
    attempts = 0
    while pos['x'] != tx or pos['y'] != ty:
        dx = tx - pos['x']
        dy = ty - pos['y']
        
        # Decide direction
        if dx < 0:
            direction = "Left"
        elif dx > 0:
            direction = "Right"
        elif dy < 0:
            direction = "Up"
        elif dy > 0:
            direction = "Down"
        else:
            break
            
        pos_before = pos
        mgba.press_buttons([direction])
        time.sleep(0.55)  # Safe sleep to prevent false bumps
        pos = mgba.get_coordinates()
        
        if pos == pos_before:
            print(f"BUMPED at {pos} going {direction} towards ({tx}, {ty})")
            time.sleep(0.5)
            pos = mgba.get_coordinates()
            if pos == pos_before:
                print("Coordinates still the same. Likely in battle! Attempting to flee...")
                handle_battle()
                time.sleep(0.5)
                pos = mgba.get_coordinates()
                if pos == pos_before:
                    print("Still stuck. Exiting.")
                    return False
        attempts += 1
        if attempts > 40:
            print("Too many walk attempts. Exiting.")
            return False
    return True

# --- THE ULTIMATE VICTORY ROUTE ---

# Current position is (24, 11) on 2F East in State B.
pos = mgba.get_coordinates()
print("Starting Ultimate Victory script from:", pos)

if pos['x'] == 24 and pos['y'] == 11:
    print("--- PHASE 1: WALKING TO 2F EAST STAIRS ---")
    path_to_stairs = [
        (24, 12, 'Down'),
        (24, 13, 'Down'),
        (24, 14, 'Down'),
        (24, 15, 'Down'),
        (24, 16, 'Down'),
        (23, 16, 'Left'),
        (22, 16, 'Left'),
        (21, 16, 'Left'),
        (20, 16, 'Left'),
        (20, 17, 'Down'),
        (20, 18, 'Down'),
        (19, 18, 'Left'),
        (18, 18, 'Left'),
        (17, 18, 'Left'),
        (16, 18, 'Left'),
        (15, 18, 'Left'),
        (15, 17, 'Up'),
        (15, 16, 'Up'),
        (15, 15, 'Up'),
        (15, 14, 'Up'),
        (15, 13, 'Up'),
        (15, 12, 'Up'),
        (15, 11, 'Up'),
    ]
    for target in path_to_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach target at ({tx}, {ty})")
            exit()
            
    print("At (15, 11) on 2F East. Stepping UP to warp to 3F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)

# We land on 3F East (State B)
pos = mgba.get_coordinates()
print("Position on 3F East:", pos)

if pos['y'] == 11 or pos['y'] == 10:
    print("--- PHASE 2: WALKING TO 3F WEST SWITCH ---")
    if not walk_to(15, 6): exit()
    if not walk_to(12, 6): exit()
    if not walk_to(12, 11): exit()
    if not walk_to(2, 11): exit()
    if not walk_to(2, 12): exit()

# Toggle 3F West switch to State A
pos = mgba.get_coordinates()
if pos['x'] == 2 and pos['y'] == 12:
    print("At (2, 12) on 3F West. Facing UP to toggle switch to State A...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    mgba.press_buttons(["A", "sleep 300", "A", "sleep 500", "B"])
    time.sleep(1.5)

# Walk to 3F East balcony in State A and drop
pos = mgba.get_coordinates()
if pos['x'] == 2 and pos['y'] == 12:
    print("--- PHASE 3: WALKING TO 3F EAST BALCONY IN STATE A ---")
    if not walk_to(2, 11): exit()
    if not walk_to(12, 11): exit()
    if not walk_to(12, 6): exit()
    if not walk_to(19, 6): exit()
    if not walk_to(19, 16): exit()
    
    print("At (19, 16) on 3F East. Stepping Left to drop from balcony...")
    mgba.press_buttons(["Left"])
    time.sleep(3.0)

# Land on B1F East South in State A
pos_b1f = mgba.get_coordinates()
print("Position after drop:", pos_b1f)

if pos_b1f['x'] == 19 and pos_b1f['y'] == 16:
    print("--- PHASE 4: WALKING TO B1F WEST SWITCH IN STATE A ---")
    if not walk_to(10, 16): exit()
    if not walk_to(10, 11): exit()
    if not walk_to(2, 11): exit()
    if not walk_to(2, 12): exit()

# Toggle B1F West switch to State B
pos_b1f = mgba.get_coordinates()
if pos_b1f['x'] == 2 and pos_b1f['y'] == 12:
    print("At (2, 12) on B1F West. Facing UP to toggle switch to State B...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    mgba.press_buttons(["A", "sleep 300", "A", "sleep 500", "B"])
    time.sleep(1.5)

# Walk to Secret Key in State B
pos_b1f = mgba.get_coordinates()
if pos_b1f['x'] == 2 and pos_b1f['y'] == 12:
    print("--- PHASE 5: WALKING TO SECRET KEY ROOM ---")
    if not walk_to(2, 11): exit()
    if not walk_to(10, 11): exit()
    if not walk_to(10, 5): exit()
    if not walk_to(1, 5): exit()

# Retrieve Secret Key
pos_key = mgba.get_coordinates()
if pos_key['x'] == 1 and pos_key['y'] == 5:
    print("--- PHASE 6: RETRIEVING SECRET KEY ---")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    mgba.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B"])
    time.sleep(1.5)

print("Final coordinates after Ultimate Victory sequence:", mgba.get_coordinates())
mgba.take_screenshot()
