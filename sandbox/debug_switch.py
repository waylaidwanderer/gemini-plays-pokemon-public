import mgba
import time

def handle_battle():
    print("Coordinates did not change. Battle or obstacle detected! Attempting to flee...")
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
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
        
        if current_pos['x'] == target[0] and current_pos['y'] == target[1]:
            print(f"Reached target {target}!")
            target_idx += 1
            stuck_count = 0
            if target_idx >= len(targets):
                break
            target = targets[target_idx]
        
        if last_pos and (abs(current_pos['x'] - last_pos['x']) > 2 or abs(current_pos['y'] - last_pos['y']) > 2):
            print(f"Warp detected! New position is {current_pos}")
            return True
            
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

# Starting from (20, 7) on 3F East
pos = mgba.get_coordinates()
print("Starting position:", pos)

# Step 1: Walk to (12, 11) on 3F
print("Walking to (12, 11)...")
targets = [(19, 7), (12, 7), (12, 11)]
navigate_to_targets(targets)

# Step 2: Check if there is a Mewtwo statue switch at (12, 11)
pos_switch = mgba.get_coordinates()
print("Position near switch:", pos_switch)
if pos_switch['x'] == 12 and pos_switch['y'] == 11:
    print("Testing interaction at (12, 11)...")
    # Face Right towards (13, 11) where the Mewtwo statue might be
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    
    # Try interacting with A
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Check if a text box is on screen (we will take a screenshot to verify)
    print("Taking screenshot after interaction...")
    mgba.take_screenshot()
