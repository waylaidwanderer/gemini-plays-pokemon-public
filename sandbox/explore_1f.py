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

# Step 1: Walk from (3, 12) on 2F West to (5, 10) to warp DOWN to 1F West
print("Going down to 1F West...")
targets_to_1f = [(5, 12), (5, 10)]
navigate_to_targets(targets_to_1f)

time.sleep(1.0)
pos = mgba.get_coordinates()
print("Position after trying to warp to 1F:", pos)

# Step 2: From 1F West landing (which is at (5, 11)), walk to (16, 7) on 1F East
# Wait! Let's check our actual position.
if pos['y'] == 11 and pos['x'] == 5:
    print("We are on 1F West! Walking to 1F East...")
    cross_targets = [(12, 11), (12, 7), (16, 7)]
    navigate_to_targets(cross_targets)

time.sleep(1.0)
print("Final Position:", mgba.get_coordinates())
mgba.take_screenshot()
