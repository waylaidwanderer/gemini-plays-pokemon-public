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

# Step 1: Walk to the Cinnabar Lab exit at (2, 7) and step Down
print("Exiting Cinnabar Lab...")
targets_exit_lab = [(2, 7)]
navigate_to_targets(targets_exit_lab)

time.sleep(0.5)
# Step DOWN to walk out of the Lab
print("Stepping Down out of the Lab...")
mgba.press_buttons(["Down"])
time.sleep(1.5)

# We should be on Cinnabar Island at (6, 10)
pos = mgba.get_coordinates()
print("Position on Cinnabar Island:", pos)

if pos['x'] == 6 and pos['y'] == 10:
    # Step 2: Walk to the Pokemon Mansion entrance at (6, 3) bypassing the Lab door at (6, 9)
    print("Walking to Pokemon Mansion entrance...")
    targets_mansion = [
        (7, 10),  # Step Right to Column 7
        (7, 4),   # Step Up to Row 4
        (6, 4),   # Step Left to Column 6
        (6, 3)    # Step Up onto Mansion entrance warp!
    ]
    navigate_to_targets(targets_mansion)

time.sleep(1.5)
final_pos = mgba.get_coordinates()
print("Final Position after warping into Mansion:", final_pos)
mgba.take_screenshot()
