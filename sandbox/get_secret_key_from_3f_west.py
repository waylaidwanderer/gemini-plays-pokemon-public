import mgba
import time

def handle_battle():
    print("Coordinates did not change. Battle or obstacle detected! Attempting to flee/clear...")
    # Attempt to flee by pressing Down, Right, A on the fight menu
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    # Clear "Escaped safely!" text or dismiss other dialogues
    mgba.press_buttons(["B", "sleep 100", "B", "sleep 100", "B"])
    time.sleep(1.0)

def navigate_to_targets(targets):
    target_idx = 0
    stuck_count = 0
    last_pos = None
    
    while target_idx < len(targets):
        current_pos = mgba.get_coordinates()
        target = targets[target_idx]
        print(f"Current Position: {current_pos}, Target: {target}")
        
        # Check if we reached the current target
        if current_pos['x'] == target[0] and current_pos['y'] == target[1]:
            print(f"Reached target {target}!")
            target_idx += 1
            stuck_count = 0
            if target_idx >= len(targets):
                break
            target = targets[target_idx]
        
        # Check if we got warped/stairs transitioned
        if last_pos and (abs(current_pos['x'] - last_pos['x']) > 2 or abs(current_pos['y'] - last_pos['y']) > 2):
            print(f"Warp detected! New position is {current_pos}")
            return True # Warp occurred, return control to caller
            
        dx = target[0] - current_pos['x']
        dy = target[1] - current_pos['y']
        
        if dx < 0:
            direction = "Left"
        elif dx > 0:
            direction = "Right"
        elif dy < 0:
            direction = "Up"
        elif dy > 0:
            direction = "Down"
        else:
            target_idx += 1
            continue
            
        print(f"Stepping {direction} towards {target}...")
        mgba.press_buttons([direction])
        time.sleep(0.35)
        
        new_pos = mgba.get_coordinates()
        if new_pos == current_pos:
            stuck_count += 1
            if stuck_count >= 2:
                handle_battle()
                stuck_count = 0
        else:
            stuck_count = 0
            
        last_pos = current_pos
        time.sleep(0.1)
    return False

# Starting position: (7, 10) on 3F West (State A)
pos = mgba.get_coordinates()
print("Starting from position on 3F West:", pos)

if pos['x'] == 7 and pos['y'] == 10:
    # Step 1: Cross 3F West to 3F East stairs at (15, 11)
    print("1. Crossing 3F West to 3F East...")
    targets_3f = [(12, 10), (12, 6), (19, 6), (19, 11), (15, 11)]
    navigate_to_targets(targets_3f)
time.sleep(1.5)

# Land on 2F East at (16, 11) (or similar)
pos_2f_east = mgba.get_coordinates()
print("Position on 2F East:", pos_2f_east)

# Step 2: Toggle switch to State B
if pos_2f_east['x'] == 16 and pos_2f_east['y'] == 11:
    print("2. Walking to 2F East switch at (12, 11)...")
    navigate_to_targets([(12, 11)])
    time.sleep(1.0)
    
    pos_switch = mgba.get_coordinates()
    if pos_switch['x'] == 12 and pos_switch['y'] == 11:
        print("Facing Right towards statue switch...")
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
        print("Toggling switch to State B...")
        mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "B", "sleep 200"])
        time.sleep(1.0)
        
        # Step 3: Walk back to East stairs at (15, 11) and warp to 3F East (State B)
        print("3. Walking back to East stairs...")
        navigate_to_targets([(15, 11)])
time.sleep(1.5)

# Land on 3F East at (16, 11) (State B)
pos_3f_east_b = mgba.get_coordinates()
print("Position on 3F East (State B):", pos_3f_east_b)

# Step 4: Walk to the balcony and drop to B1F East
if pos_3f_east_b['x'] == 16 and pos_3f_east_b['y'] == 11:
    print("4. Walking to balcony and dropping...")
    targets_balcony = [(21, 11), (21, 15), (20, 15), (20, 18), (19, 18)]
    navigate_to_targets(targets_balcony)
time.sleep(2.0)

# Land on B1F East at (19, 16)
pos_b1f = mgba.get_coordinates()
print("Position on B1F East:", pos_b1f)

# Step 5: Walk to Column 10 Row 5 and then Left to Column 1 Row 5
if pos_b1f['x'] == 19 and pos_b1f['y'] == 16:
    print("5. Walking to B1F West NORTH room via open gate...")
    targets_b1f = [(10, 16), (10, 5), (1, 5)]
    navigate_to_targets(targets_b1f)
time.sleep(1.0)

# Step 6: Retrieve Secret Key at (1, 4)
pos_key = mgba.get_coordinates()
print("Position near Secret Key:", pos_key)
if pos_key['x'] == 1 and pos_key['y'] == 5:
    print("6. Facing UP and retrieving Secret Key...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    mgba.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B", "sleep 200"])
    time.sleep(1.0)

print("Coordinates at end of script:", mgba.get_coordinates())
mgba.take_screenshot()
