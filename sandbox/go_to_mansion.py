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

# Step 1: Walk out of the Pokémon Center
print("Exiting Pokémon Center...")
# We are at (3, 7) inside the Center, door is at (3, 8)
mgba.press_buttons(["Down"])
time.sleep(1.5) # wait for warp

# We should land on Cinnabar Island at (15, 12)
pos = mgba.get_coordinates()
print("Position on Cinnabar Island:", pos)

if pos['x'] == 15 and pos['y'] == 12:
    # Step 2: Walk to the Pokémon Mansion entrance door at (12, 3) via Column 19
    print("Walking to Pokémon Mansion entrance via Column 19...")
    targets = [
        (19, 12),  # Walk Right along Row 12 to Column 19
        (19, 3),   # Walk Up Column 19 to Row 3 (bypassing Gym/Mart/Center!)
        (12, 3),   # Walk Left Row 3 to Column 12 (the Mansion entrance!)
        (12, 2)    # Step UP onto the warp to enter the Mansion!
    ]
    navigate_to_targets(targets)

time.sleep(1.5)
final_pos = mgba.get_coordinates()
print("Final Position inside Mansion:", final_pos)
mgba.take_screenshot()
