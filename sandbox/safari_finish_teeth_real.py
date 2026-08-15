import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def handle_textbox_or_battle():
    print("Coordinates are None. Handling potential battle or dialog...")
    # Clear text boxes with B
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 150"])
    
    # Try to RUN
    print("Attempting to RUN from battle...")
    bridge.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1000"])
    
    # Clear post-flee text
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 150"])
        
    pos = get_pos()
    print(f"Coordinates after battle handling: {pos}")
    return pos

def walk_step_robust(direction):
    pos = get_pos()
    if pos is None:
        return handle_textbox_or_battle()
        
    print(f"Walking {direction} from {pos}")
    bridge.press_buttons([direction, "sleep 450"])
    
    new_pos = get_pos()
    if new_pos is None:
        return handle_textbox_or_battle()
        
    if new_pos != pos:
        return new_pos
        
    print("Position didn't change, pressing B...")
    bridge.press_buttons(["B", "sleep 200"])
    new_pos = get_pos()
    if new_pos is None:
        return handle_textbox_or_battle()
    if new_pos != pos:
        return new_pos
        
    return handle_textbox_or_battle()

def navigate_to(tx, ty):
    stuck_count = 0
    while True:
        pos = get_pos()
        if pos is None:
            handle_textbox_or_battle()
            continue
            
        if pos == (tx, ty):
            print(f"Arrived at waypoint ({tx}, {ty})")
            break
            
        print(f"Current: {pos}, Target: ({tx}, {ty})")
        if pos[0] < tx:
            direction = "Right"
        elif pos[0] > tx:
            direction = "Left"
        elif pos[1] < ty:
            direction = "Down"
        elif pos[1] > ty:
            direction = "Up"
            
        new_pos = walk_step_robust(direction)
        if new_pos == pos:
            stuck_count += 1
            if stuck_count > 3:
                print("Stuck! Clearing with B...")
                bridge.press_buttons(["B", "sleep 500"])
                stuck_count = 0
        else:
            stuck_count = 0
        time.sleep(0.4)

def main():
    print("Executing Legendary Ground-Level Golden Route to Gold Teeth...")
    # Starting at (15, 25) inside Safari Zone Center
    
    # Step 1: Walk LEFT to (14, 25)
    print("\n--- STEP 1: Walking LEFT to (14, 25) ---")
    walk_step_robust("Left")
    
    # Step 2: Walk DOWN to (14, 26)
    print("\n--- STEP 2: Walking DOWN to (14, 26) ---")
    walk_step_robust("Down")
    
    # Step 3: Navigate LEFT along Row 26 to (0, 26)
    print("\n--- STEP 3: Navigating to (0, 26) ---")
    navigate_to(0, 26)
    
    # Step 4: Step LEFT to transition to Area 3 (West) at (29, 26)
    print("\n--- STEP 4: Transitioning to Area 3 (West) ---")
    bridge.press_buttons(["Left", "sleep 1000"])
    time.sleep(1.0)
    
    pos = get_pos()
    if pos is None:
         pos = handle_textbox_or_battle()
    print(f"Position in Area 3: {pos}")
    
    # Step 5: Navigate to (19, 26)
    print("\n--- STEP 5: Navigating to (19, 26) ---")
    navigate_to(19, 26)
    
    # Step 6: Stand facing UP and press A to pick up the Gold Teeth!
    print("\n--- STEP 6: Facing UP and picking up Gold Teeth ---")
    bridge.press_buttons(["Up", "sleep 500"])
    bridge.press_buttons(["A", "sleep 1500"])
    
    # Print final position to verify
    pos = get_pos()
    print(f"Final position: {pos}")

if __name__ == "__main__":
    main()
