import mgba
import time

def handle_battle():
    print("Coordinates did not change. Battle or obstacle detected! Attempting to flee/clear...")
    mgba.press_buttons(["B", "sleep 100", "B", "sleep 100", "Down", "Right", "A", "sleep 1500", "B", "sleep 200", "B"])
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
            break
            
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

# Step 1: Walk to 1F West stairs to warp to 2F West
print("Walking to 1F West stairs...")
targets_1f = [(6, 10), (7, 10)]
navigate_to_targets(targets_1f)

time.sleep(1.5)
pos = mgba.get_coordinates()
print("Position on 2F West:", pos)

# We land at (7, 11) on 2F West.
# Step 2: Step back onto the stairs at (7, 10) to warp to 3F West
if pos['x'] == 7 and pos['y'] == 11:
    print("Stepping onto stairs to warp to 3F West...")
    mgba.press_buttons(["Up"])
    time.sleep(1.5)
    
pos_3f = mgba.get_coordinates()
print("Position on 3F West:", pos_3f)

# We land at (7, 11) on 3F West.
# Step 3: Cross 3F West to 3F East stairs at (15, 11)
if pos_3f['x'] == 7 and pos_3f['y'] == 11:
    print("Crossing 3F West to 3F East...")
    targets_3f = [(12, 11), (12, 6), (19, 6), (19, 11), (15, 11)]
    navigate_to_targets(targets_3f)
    
time.sleep(1.5)
pos_2f_east = mgba.get_coordinates()
print("Position on 2F East:", pos_2f_east)

# We land on 2F East at (16, 11).
# Step 4: Toggle the Mewtwo statue switch to State B
if pos_2f_east['x'] == 16 and pos_2f_east['y'] == 11:
    print("Walking to 2F East switch...")
    targets_2f_switch = [(12, 11)]
    navigate_to_targets(targets_2f_switch)
    
    time.sleep(1.0)
    pos_switch = mgba.get_coordinates()
    if pos_switch['x'] == 12 and pos_switch['y'] == 11:
        print("Facing Right towards statue switch...")
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
        
        print("Toggling switch to State B...")
        mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "B", "sleep 200"])
        time.sleep(1.0)
        
        # Step 5: Walk back to stairs at (15, 11) and warp up to 3F East
        print("Walking to East stairs...")
        targets_2f_stairs = [(15, 11)]
        navigate_to_targets(targets_2f_stairs)

time.sleep(1.5)
pos_3f_east_b = mgba.get_coordinates()
print("Position on 3F East (State B):", pos_3f_east_b)

# We land on 3F East (State B) at (16, 11).
# Step 6: Walk to the balcony and drop to B1F East
if pos_3f_east_b['x'] == 16 and pos_3f_east_b['y'] == 11:
    print("Walking to balcony and dropping...")
    targets_balcony = [(21, 11), (21, 15), (20, 15), (20, 18), (19, 18)]
    navigate_to_targets(targets_balcony)

time.sleep(2.0)
pos_b1f = mgba.get_coordinates()
print("Position on B1F East:", pos_b1f)
mgba.take_screenshot()
