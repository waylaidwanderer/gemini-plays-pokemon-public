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
    print("Executing Real Safari Golden Route to Gold Teeth...")
    
    # We are at (9, 14) in Area 3 (West)
    # Step 1: Walk LEFT to Column 0 Row 14 to transition to Center
    print("\n--- STEP 1: Transitioning to Safari Zone Center ---")
    navigate_to(0, 14)
    # Give a step LEFT to transition
    bridge.press_buttons(["Left", "sleep 1000"])
    time.sleep(1.0)
    
    pos = get_pos()
    if pos is None:
         pos = handle_textbox_or_battle()
    print(f"Position in Center: {pos}")
    
    # Step 2: Navigate to (0, 11) in Center
    print("\n--- STEP 2: Navigating to (0, 11) in Center ---")
    navigate_to(0, 11)
    # Give a step LEFT to transition to Area 3 (East side)
    bridge.press_buttons(["Left", "sleep 1000"])
    time.sleep(1.0)
    
    pos = get_pos()
    if pos is None:
         pos = handle_textbox_or_battle()
    print(f"Position in Area 3 (East): {pos}")
    
    # Step 3: Navigate to (21, 18) (below East Stairs)
    print("\n--- STEP 3: Navigating to (21, 18) ---")
    navigate_to(21, 18)
    
    # Step 4: Climb East Stairs by walking UP onto (21, 17)
    print("\n--- STEP 4: Climbing onto Plateau at (21, 17) ---")
    walk_step_robust("Up")
    pos = get_pos()
    print(f"Position on Plateau: {pos}")
    
    # Step 5: Walk to (6, 18) on Plateau
    print("\n--- STEP 5: Navigating to (6, 18) on Plateau ---")
    # Walk left to Column 19
    navigate_to(19, 17)
    # Down to Row 18
    navigate_to(19, 18)
    # Left to Column 6
    navigate_to(6, 18)
    
    # Step 6: Descend West Stairs by walking DOWN onto (6, 19)
    print("\n--- STEP 6: Descending West Stairs ---")
    walk_step_robust("Down")
    pos = get_pos()
    print(f"Position on ground: {pos}")
    
    # Step 7: Navigate to (19, 26) on Row 26 Highway
    print("\n--- STEP 7: Navigating to (19, 26) ---")
    navigate_to(19, 26)
    
    # Step 8: Stand facing UP and press A to pick up the teeth!
    print("\n--- STEP 8: Stand facing UP and press A ---")
    bridge.press_buttons(["Up", "sleep 500"])
    bridge.press_buttons(["A", "sleep 1500"])
    
    pos = get_pos()
    print(f"Final position: {pos}")

if __name__ == "__main__":
    main()
