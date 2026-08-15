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
    print("Executing Safari Return Route via Plateau...")
    # We are at (5, 21) inside Area 3 (West) on ground level
    
    # Step 1: Navigate to (6, 20) (West Stairs base)
    print("\n--- STEP 1: Navigating to (6, 20) ---")
    navigate_to(6, 21)
    navigate_to(6, 20)
    
    # Step 2: Climb West Stairs by walking UP onto Plateau flat top at (6, 16)
    print("\n--- STEP 2: Climbing Plateau at (6, 16) ---")
    walk_step_robust("Up")  # to (6, 19) (stair tile)
    walk_step_robust("Up")  # to (6, 18)
    walk_step_robust("Up")  # to (6, 17)
    walk_step_robust("Up")  # to (6, 16) (flat top)
    pos = get_pos()
    print(f"Current Position on Plateau: {pos}")
    
    # Step 3: Navigate across Plateau to (21, 16)
    print("\n--- STEP 3: Navigating across Plateau to (21, 16) ---")
    navigate_to(21, 16)
    
    # Step 4: Walk DOWN to descend East Stairs onto ground at (21, 18)
    print("\n--- STEP 4: Descending East Stairs ---")
    walk_step_robust("Down")  # to (21, 17) (stair tile)
    walk_step_robust("Down")  # to (21, 18) (ground level)
    pos = get_pos()
    print(f"Current Position on ground: {pos}")
    
    # Step 5: Navigate to (29, 23) (East transition)
    print("\n--- STEP 5: Navigating to (29, 23) ---")
    navigate_to(21, 23)
    navigate_to(29, 23)
    
    # Step 6: Step RIGHT to transition to Safari Zone Center
    print("\n--- STEP 6: Transitioning to Safari Zone Center ---")
    bridge.press_buttons(["Right", "sleep 1000"])
    time.sleep(1.0)
    
    pos = get_pos()
    if pos is None:
         pos = handle_textbox_or_battle()
    print(f"Final Position in Center: {pos}")

if __name__ == "__main__":
    main()
