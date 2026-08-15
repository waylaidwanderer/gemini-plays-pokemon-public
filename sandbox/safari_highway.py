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
    
    # Check where we currently are to skip completed phases
    pos = get_pos()
    if pos is None:
        pos = handle_textbox_or_battle()
        
    # We could be in Center or Area 1 (East)
    # Let's check map by checking coordinates.
    # Center map has coordinates up to (29, 25), and starting at (15, 25).
    # Area 1 (East) has different coordinates or similar, but let's check position.
    # Currently we are at (5, 22) which is Area 1 (East).
    
    in_area1 = False
    if pos is not None:
        # If we are at (5, 22) or we know we are in Area 1, we skip step 1.
        # Let's check if x <= 20 and we are in Area 1.
        # To be robust, let's just inspect if we are at (5, 22)
        if pos == (5, 22) or (pos[0] < 21 and pos[1] == 22):
            in_area1 = True
            
    if not in_area1:
        # Step 1: Navigate Center starting at (15, 25) or (28, 14)
        if pos is not None and pos[0] >= 27 and pos[1] >= 11:
            print("Handling starting from Column 28 Row 14 detour...")
            navigate_to(27, 14)
            navigate_to(27, 10)
        else:
            print("Standard Center start...")
            navigate_to(15, 22)
            navigate_to(27, 22)
            navigate_to(27, 10)
            
        print("\n--- Navigating to (29, 10) in Center ---")
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
    print("\n--- STEP 2a: Navigating to (4, 22) in Area 1 (East) ---")
    navigate_to(4, 22)
    
    print("\n--- STEP 2b: Navigating to (4, 24) in Area 1 (East) ---")
    navigate_to(4, 24)
    
    print("\n--- STEP 2c: Navigating to (20, 24) in Area 1 (East) ---")
    navigate_to(20, 24)
    
    print("\n--- STEP 2d: Navigating to (20, 26) in Area 1 (East) ---")
    navigate_to(20, 26)
    
    print("\n--- STEP 2e: Navigating to (0, 26) in Area 1 (East) ---")
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
