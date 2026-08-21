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

# Starting from (12, 11) on 3F
pos = mgba.get_coordinates()
print("Starting position:", pos)

# Step 1: Walk to the 3F West switch at (2, 11) (via 3, 11 -> 3, 12 -> 2, 12)
print("Walking to 3F West switch at (2, 11)...")
# We walk along Row 11 to Column 3, then Down to Row 12, then Left to Column 2
targets_to_switch = [(3, 11), (3, 12), (2, 12)]
navigate_to_targets(targets_to_switch)

# Step 2: Interact with the 3F West switch
pos_switch = mgba.get_coordinates()
print("Position near 3F West switch:", pos_switch)
if pos_switch['x'] == 2 and pos_switch['y'] == 12:
    print("Facing Up towards Mewtwo statue switch...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    print("Toggling the switch...")
    # Press A, then select YES (A), then dismiss with B
    mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "B", "sleep 200"])
    time.sleep(1.0)
    
    # Step 3: Walk back to 3F East and try walking Down Column 19
    print("Walking back to 3F East and testing Column 19...")
    targets_test = [(3, 12), (3, 11), (12, 11), (12, 6), (19, 6), (19, 11)]
    navigate_to_targets(targets_test)

print("Coordinates at end of script:", mgba.get_coordinates())
mgba.take_screenshot()
