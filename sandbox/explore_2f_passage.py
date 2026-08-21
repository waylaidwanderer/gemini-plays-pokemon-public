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

# Step 1: Go back to 2F West via stairs at (7, 10)
print("Going down to 2F West...")
targets_to_stairs = [(7, 11), (7, 10)]
navigate_to_targets(targets_to_stairs)

time.sleep(1.0)
pos = mgba.get_coordinates()
print("Position after trying to warp to 2F:", pos)

# Step 2: From 2F West, test walking to 2F East
# If we successfully warped, we are at (7, 11) on 2F West.
# Let's walk Right from (7, 11) to (14, 11) to see where we get blocked!
if pos['y'] == 11 and pos['x'] == 7:
    print("We are on 2F West! Testing horizontal passage to the East...")
    test_path = [(8, 11), (9, 11), (10, 11), (11, 11), (12, 11), (13, 11), (14, 11)]
    navigate_to_targets(test_path)
    
time.sleep(1.0)
print("Final Position:", mgba.get_coordinates())
mgba.take_screenshot()
