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

# Step 1: Step off the stairs to (7, 11) and walk to (2, 11)
print("Walking to switch on 3F West...")
targets = [(7, 11), (2, 11)]
navigate_to_targets(targets)

time.sleep(1.0)
pos = mgba.get_coordinates()
print("Position at switch target:", pos)

if pos['x'] == 2 and pos['y'] == 11:
    # Face UP towards (2, 10)
    print("Facing Up towards the switch...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # Press A to interact and Yes to press the switch
    print("Interacting with switch...")
    mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "B", "sleep 200"])
    time.sleep(1.0)

time.sleep(1.0)
print("Final Position:", mgba.get_coordinates())
mgba.take_screenshot()
