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
    print("Executing Safari Zone Complete Highway Route to Gold Teeth...")
    
    # Step 1: Navigate Center starting at (15, 25)
    print("\n--- STEP 1a: Navigating to (15, 22) in Center ---")
    navigate_to(15, 22)
    
    print("\n--- STEP 1b: Navigating to (28, 22) in Center ---")
    navigate_to(28, 22)
    
    print("\n--- STEP 1c: Navigating to (28, 10) in Center ---")
    navigate_to(28, 10)
    
    print("\n--- STEP 1d: Navigating to (29, 10) in Center ---")
    navigate_to(29, 10)
    
    # Transition to Area 1 (East)
    print("Transitioning to Area 1...")
    bridge.press_buttons(["Right", "sleep 1000"])
    time.sleep(1.0)
    
    pos = get_pos()
    if pos is None:
         pos = handle_textbox_or_battle()
    print(f"Position in Area 1 (East): {pos}")
    
    # Step 2: Navigate to (20, 26) in Area 1 (East)
    print("\n--- STEP 2a: Navigating to (20, 22) in Area 1 (East) ---")
    navigate_to(20, 22)
    
    print("\n--- STEP 2b: Navigating to (20, 26) in Area 1 (East) ---")
    navigate_to(20, 26)
    
    print("\n--- STEP 2c: Navigating to (0, 26) in Area 1 (East) ---")
    navigate_to(0, 26)
    
    # Transition to Center Row 26
    print("Transitioning to Center Row 26...")
    bridge.press_buttons(["Left", "sleep 1000"])
    time.sleep(1.0)
    
    pos = get_pos()
    if pos is None:
         pos = handle_textbox_or_battle()
    print(f"Position in Center Row 26: {pos}")
    
    # Step 3: Navigate LEFT to transition to Area 3 (West) at Row 26
    print("\n--- STEP 3: Navigating to Area 3 Row 26 ---")
    navigate_to(0, 26)
    print("Transitioning to Area 3 Row 26...")
    bridge.press_buttons(["Left", "sleep 1000"])
    time.sleep(1.0)
    
    pos = get_pos()
    if pos is None:
         pos = handle_textbox_or_battle()
    print(f"Position in Area 3 Row 26: {pos}")
    
    # Step 4: Navigate to (19, 26) on the Row 26 Highway
    print("\n--- STEP 4: Navigating to (19, 26) ---")
    navigate_to(19, 26)
    
    # Step 5: Stand facing UP and press A to pick up the Gold Teeth!
    print("\n--- STEP 5: Facing UP and picking up Gold Teeth ---")
    bridge.press_buttons(["Up", "sleep 500"])
    bridge.press_buttons(["A", "sleep 1500"])
    
    pos = get_pos()
    print(f"Final position: {pos}")

if __name__ == "__main__":
    main()
