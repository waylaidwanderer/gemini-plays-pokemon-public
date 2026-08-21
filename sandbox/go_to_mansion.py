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

# We are at (17, 12) on Cinnabar Island.
# Walk to Pokemon Mansion entrance via East road (Column 18):
print("Walking to Pokemon Mansion entrance via East road (Column 18)...")
targets = [
    (18, 12), # Step Right to Column 18
    (18, 3),  # Walk Up to Row 3
    (6, 3),   # Walk Left to Column 6
    (6, 2)    # Step UP onto Mansion entrance warp!
]
navigate_to_targets(targets)

time.sleep(1.5)
final_pos = mgba.get_coordinates()
print("Final Position after warping into Mansion:", final_pos)
mgba.take_screenshot()
