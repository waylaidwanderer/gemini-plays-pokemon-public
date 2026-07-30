import mgba
import time

def walk_to(target_x, target_y):
    print(f"Attempting to walk to ({target_x}, {target_y})")
    pos = mgba.get_coordinates()
    print(f"Starting at: {pos}")
    
    # We want to walk step-by-step to target
    while pos['x'] != target_x or pos['y'] != target_y:
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
            # Try once more, if still blocked, exit so the model can handle it
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

# Main navigation path to the cuttable bush at (35, 32)
success = True
# 1. Down column 10 to Row 22
success = success and walk_to(10, 22)
# 2. Right along Row 22 to column 22
success = success and walk_to(22, 22)
# 3. Down column 22 to Row 31
success = success and walk_to(22, 31)
# 4. Right along Row 31 to column 35
success = success and walk_to(35, 31)
# 5. Down to (35, 32) (cuttable bush)
success = success and walk_to(35, 32)

if success:
    print("Path navigation complete!")
else:
    print("Path navigation was interrupted.")
