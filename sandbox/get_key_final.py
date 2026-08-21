import mgba
import time

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
            # If we bump, it's either a battle or wall. Let's wait a bit and check
            time.sleep(0.5)
            pos = mgba.get_coordinates()
            if pos == pos_before:
                print("Coordinates still the same. Likely in battle! Exiting script so player can handle it.")
                return False
        attempts += 1
        if attempts > 40:
            print("Too many walk attempts. Exiting.")
            return False
    return True

# --- STAGE 2: SUPER-ROBUST RETRIEVAL SEQUENCE ---
pos = mgba.get_coordinates()
print("Current position:", pos)

if pos['x'] == 21 and pos['y'] == 6:
    # 1. Walk UP to (21, 3)
    if not walk_to(21, 3): exit()
    # 2. Walk Left to (19, 3)
    if not walk_to(19, 3): exit()
    # 3. Walk Down to (19, 16)
    if not walk_to(19, 16): exit()
    
    # 4. Drop off balcony by stepping Left to (18, 16)
    print("At (19, 16). Stepping Left to drop from balcony...")
    mgba.press_buttons(["Left"])
    time.sleep(3.0)

pos_b1f = mgba.get_coordinates()
print("Landed on B1F! Position:", pos_b1f)

# Step 2: Navigate B1F to B1F West switch stand tile at (2, 12)
if pos_b1f['x'] == 19 and pos_b1f['y'] == 16:
    # Walk to (10, 16)
    if not walk_to(10, 16): exit()
    # Walk UP Column 10 to Row 11 (10, 11)
    if not walk_to(10, 11): exit()
    # Walk Left along Row 11 to Column 3 (3, 11)
    if not walk_to(3, 11): exit()
    # Walk Down to (3, 12)
    if not walk_to(3, 12): exit()
    # Walk Left to Column 2 (2, 12)
    if not walk_to(2, 12): exit()

# Step 3: Toggle B1F switch to State B
pos_switch = mgba.get_coordinates()
if pos_switch['x'] == 2 and pos_switch['y'] == 12:
    print("At (2, 12) on B1F West. Facing UP to toggle switch...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    print("Toggling Mewtwo statue switch to State B...")
    mgba.press_buttons(["A", "sleep 300", "A", "sleep 500", "B"])
    time.sleep(1.5)

# Step 4: Walk to the Secret Key room standing at (1, 5)
pos_b1f = mgba.get_coordinates()
if pos_b1f['x'] == 2 and pos_b1f['y'] == 12:
    # Walk to (3, 12)
    if not walk_to(3, 12): exit()
    # Walk to (3, 11)
    if not walk_to(3, 11): exit()
    # Walk to (10, 11)
    if not walk_to(10, 11): exit()
    # Walk to (10, 5)
    if not walk_to(10, 5): exit()
    # Walk to (1, 5)
    if not walk_to(1, 5): exit()

# Step 5: Retrieve the Secret Key at (1, 4)
pos_key = mgba.get_coordinates()
if pos_key['x'] == 1 and pos_key['y'] == 5:
    print("At (1, 5). Facing UP and retrieving Secret Key...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    mgba.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B", "sleep 200"])
    time.sleep(1.0)

print("Final position at end of script:", mgba.get_coordinates())
mgba.take_screenshot()
