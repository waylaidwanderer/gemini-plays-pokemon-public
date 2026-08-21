import mgba
import time

def navigate_to_targets(targets):
    target_idx = 0
    last_pos = None
    
    while target_idx < len(targets):
        current_pos = mgba.get_coordinates()
        target = targets[target_idx]
        print(f"Current Position: {current_pos}, Target: {target}")
        
        if current_pos['x'] == target[0] and current_pos['y'] == target[1]:
            print(f"Reached target {target}!")
            target_idx += 1
            if target_idx >= len(targets):
                break
            target = targets[target_idx]
        
        # Check if we got warped
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
        
        last_pos = current_pos
        time.sleep(0.1)

# Step 1: Walk out of Cinnabar Lab
print("Walking to Lab exit...")
exit_targets = [(3, 5), (3, 7), (2, 7)]
navigate_to_targets(exit_targets)

time.sleep(0.5)
print("Stepping Down onto exit warp...")
mgba.press_buttons(["Down"])
time.sleep(1.5) # wait for warp

# We should land on Cinnabar Island at (3, 12)
pos = mgba.get_coordinates()
print("Position on Cinnabar Island:", pos)

if pos['x'] == 3 and pos['y'] == 12:
    # Step 2: Walk to the Pokemon Mansion entrance door at (12, 3)
    print("Walking to Pokemon Mansion entrance...")
    targets_mansion = [
        (15, 12),  # Walk Right along Row 12 to Column 15
        (15, 5),   # Walk Up Column 15 to Row 5
        (12, 5),   # Walk Left Row 5 to Column 12
        (12, 2)    # Walk Up Column 12 to Row 2 (warp inside!)
    ]
    navigate_to_targets(targets_mansion)

time.sleep(1.5)
final_pos = mgba.get_coordinates()
print("Final Position inside Mansion:", final_pos)
mgba.take_screenshot()
