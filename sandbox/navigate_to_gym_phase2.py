import mgba
import time

def walk_to(target_x, target_y):
    print(f"Attempting to walk to ({target_x}, {target_y})")
    pos = mgba.get_coordinates()
    print(f"Starting at: {pos}")
    
    # We want to walk step-by-step to target
    while pos['x'] != target_x or pos['y'] != target_y:
        # Check if map transitioned (e.g. coordinates jumped suddenly, or we entered Gym)
        # If we are inside the Gym, the y-coordinate might be smaller or we might be at a different x
        # Let's check if we are no longer in the overworld target region
        # Gym coordinates are typically within x=[0,10], y=[0,17]
        # Overworld path is at y >= 28 or x >= 5
        if pos['y'] < 20 and pos['x'] < 15:
            # We likely entered the Gym!
            print("Map transition detected! We are probably inside the Gym.")
            return True
            
        # Determine next direction
        dx = target_x - pos['x']
        dy = target_y - pos['y']
        
        button = None
        if dy > 0:
            button = "Down"
        elif dy < 0:
            button = "Up"
        elif dx > 0:
            button = "Right"
        elif dx < 0:
            button = "Left"
            
        if not button:
            break
            
        print(f"Pressing {button}...")
        mgba.press_buttons([button])
        time.sleep(0.1) # small pause
        
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            # We didn't move! Maybe blocked by NPC or wall.
            print(f"BLOCKED! Still at {pos}. Waiting 500ms...")
            time.sleep(0.5)
            # Try once more, if still blocked, exit
            mgba.press_buttons([button])
            time.sleep(0.1)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                print(f"STUCK at {pos}! Exiting navigation.")
                return False
                
        pos = new_pos
        print(f"Current position: {pos}")
        
    print(f"Successfully reached ({target_x}, {target_y})!")
    return True

success = True
# 1. Walk Down to (35, 34)
success = success and walk_to(35, 34)
# 2. Walk Left to (5, 34)
success = success and walk_to(5, 34)
# 3. Walk Up to (5, 28)
success = success and walk_to(5, 28)
# 4. Walk Right to (12, 28)
success = success and walk_to(12, 28)
# 5. Walk Up into the Gym at (12, 27)
if success:
    print("Attempting to enter the Gym door...")
    mgba.press_buttons(["Up"])
    time.sleep(1.0)
    final_pos = mgba.get_coordinates()
    print(f"Final position: {final_pos}")
