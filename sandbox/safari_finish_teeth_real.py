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
    print("Executing Super-Optimized Ground Route to Gold Teeth...")
    
    # We are at (15, 24) in Area 3 (West) on the ground level
    # Step 1: Navigate to (15, 23)
    print("\n--- STEP 1: Navigating to (15, 23) ---")
    navigate_to(15, 23)
    
    # Step 2: Navigate to (8, 23)
    print("\n--- STEP 2: Navigating to (8, 23) ---")
    navigate_to(8, 23)
    
    # Step 3: Jump DOWN over the ledge at Row 24/25
    print("\n--- STEP 3: Jumping DOWN over Row 24 Ledge ---")
    walk_step_robust("Down")  # to (8, 24) (stair/ledge tile)
    walk_step_robust("Down")  # jumps over ledge to (8, 26)
    
    pos = get_pos()
    print(f"Position after jump: {pos}")
    
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
