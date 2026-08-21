import mgba
import time

def handle_battle():
    print("Coordinates did not change. Battle or obstacle detected! Attempting to flee...")
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    mgba.press_buttons(["B", "sleep 100", "B", "sleep 100", "B"])
    time.sleep(1.0)

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
                print("Coordinates still the same. Likely in battle! Exiting script so player can handle it.")
                return False
        attempts += 1
        if attempts > 40:
            print("Too many walk attempts. Exiting.")
            return False
    return True

# --- THE DEFINITIVE MASTER SOLUTION SEQUENCE ---
pos = mgba.get_coordinates()
print("Starting definitive master run:", pos)

# 1. Clear textbox
mgba.press_buttons(["B"])
time.sleep(1.0)
pos = mgba.get_coordinates()

# Walk to 3F West switch in State A
if pos['x'] == 12 and pos['y'] == 10:
    if not walk_to(12, 11): exit()
    if not walk_to(3, 11): exit()
    if not walk_to(3, 12): exit()
    if not walk_to(2, 12): exit()

# 2. Toggle 3F West switch to State B
pos = mgba.get_coordinates()
if pos['x'] == 2 and pos['y'] == 12:
    print("At (2, 12) on 3F West. Facing UP to toggle switch...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    mgba.press_buttons(["A", "sleep 300", "A", "sleep 500", "B"])
    time.sleep(1.5)

# 3. Walk to the 3F East balcony in State B and drop
pos = mgba.get_coordinates()
if pos['x'] == 2 and pos['y'] == 12:
    if not walk_to(3, 12): exit()
    if not walk_to(3, 11): exit()
    # In State B, Column 10 gate is open
    if not walk_to(10, 11): exit()
    if not walk_to(10, 5): exit()
    if not walk_to(19, 5): exit()
    if not walk_to(19, 16): exit()
    
    print("At (19, 16). Stepping Left to drop from balcony in State B...")
    mgba.press_buttons(["Left"])
    time.sleep(3.0)

# 4. Land on B1F East in State B. Head to B1F East switch and toggle to State A
pos_b1f = mgba.get_coordinates()
print("Position after drop:", pos_b1f)
if pos_b1f['x'] == 19 and pos_b1f['y'] == 16:
    # Walk Down 4 steps, Left 7 steps to (12, 20)
    if not walk_to(19, 20): exit()
    if not walk_to(12, 20): exit()
    
    print("At (12, 20) on B1F East. Facing Left to toggle switch...")
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    mgba.press_buttons(["A", "sleep 300", "A", "sleep 500", "B"])
    time.sleep(1.5)

# 5. Head from B1F East to B1F West in State A
pos_b1f = mgba.get_coordinates()
if pos_b1f['x'] == 12 and pos_b1f['y'] == 20:
    if not walk_to(19, 20): exit()
    if not walk_to(19, 16): exit()
    # In State A, the Column 18 gate is open
    if not walk_to(10, 16): exit()
    if not walk_to(10, 11): exit()
    if not walk_to(3, 11): exit()
    if not walk_to(3, 12): exit()
    if not walk_to(2, 12): exit()

# 6. Toggle B1F West switch back to State B
pos_b1f = mgba.get_coordinates()
if pos_b1f['x'] == 2 and pos_b1f['y'] == 12:
    print("At (2, 12) on B1F West. Facing UP to toggle switch to State B...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    mgba.press_buttons(["A", "sleep 300", "A", "sleep 500", "B"])
    time.sleep(1.5)

# 7. Walk to the Secret Key room standing at (1, 5)
pos_b1f = mgba.get_coordinates()
if pos_b1f['x'] == 2 and pos_b1f['y'] == 12:
    if not walk_to(3, 12): exit()
    if not walk_to(3, 11): exit()
    if not walk_to(10, 11): exit()
    if not walk_to(10, 5): exit()
    if not walk_to(1, 5): exit()

# 8. Retrieve the Secret Key at (1, 4)
pos_key = mgba.get_coordinates()
if pos_key['x'] == 1 and pos_key['y'] == 5:
    print("At (1, 5). Facing UP and retrieving Secret Key...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    mgba.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B", "sleep 200"])
    time.sleep(1.0)

print("Final position at end of script:", mgba.get_coordinates())
mgba.take_screenshot()
