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
    
    # We are at (18, 19) in Area 3 (West) on the ground level
    # Step 1: Navigate to (21, 18) (ground below East Stairs)
    print("\n--- STEP 1: Navigating to (21, 18) ---")
    navigate_to(21, 18)
    
    # Step 2: Climb completely onto the flat top of Plateau at (21, 16)
    print("\n--- STEP 2: Climbing onto flat top of Plateau at (21, 16) ---")
    walk_step_robust("Up")  # to (21, 17)
    walk_step_robust("Up")  # to (21, 16)
    pos = get_pos()
    print(f"Position on Plateau: {pos}")
    
    # Step 3: Navigate across flat top of Plateau to (6, 16)
    print("\n--- STEP 3: Navigating to (6, 16) on Plateau ---")
    navigate_to(6, 16)
    
    # Step 4: Walk DOWN to descend West Stairs onto ground at (6, 20)
    print("\n--- STEP 4: Descending West Stairs ---")
    walk_step_robust("Down")  # to (6, 17)
    walk_step_robust("Down")  # to (6, 18)
    walk_step_robust("Down")  # to (6, 19) (stair tile)
    walk_step_robust("Down")  # to (6, 20) (ground level)
    pos = get_pos()
    print(f"Position on Ground: {pos}")
    
    # Step 5: Navigate to (19, 26) on the Row 26 Highway
    print("\n--- STEP 5: Navigating to (19, 26) ---")
    navigate_to(19, 26)
    
    # Step 6: Stand facing UP and press A to pick up the Gold Teeth!
    print("\n--- STEP 6: Facing UP and picking up Gold Teeth ---")
    bridge.press_buttons(["Up", "sleep 500"])
    bridge.press_buttons(["A", "sleep 1500"])
    
    pos = get_pos()
    print(f"Final position: {pos}")

if __name__ == "__main__":
    main()
