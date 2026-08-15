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

def try_move(direction):
    pos = get_pos()
    new_pos = walk_step_robust(direction)
    if new_pos == pos:
        return False, new_pos
    return True, new_pos

def main():
    print("Probing eastern ground level via Row 14 bypass...")
    # Stand at (17, 23).
    # Step 1: Walk UP Column 17 to Row 14: (17, 14)
    # Wait, can we walk UP Column 17 past the Plateau?
    # No, Column 17 Rows 15-18 has the Plateau!
    # So we cannot walk UP Column 17 directly!
    # But we can walk:
    # 1. LEFT to Column 15 Row 23: (15, 23)
    # 2. UP to Column 15 Row 14: (15, 14) (this is the ground corridor!)
    # 3. RIGHT to Column 29 Row 14: (29, 14)
    # 4. DOWN to Column 29 Row 23: (29, 23)
    # 5. LEFT along Row 23 to Column 22: (22, 23)
    print("\n--- STEP 1: Navigating to Column 15 Row 14 ---")
    navigate_to(15, 23)
    navigate_to(15, 14)
    
    print("\n--- STEP 2: Navigating to Column 29 Row 14 ---")
    navigate_to(29, 14)
    
    print("\n--- STEP 3: Navigating to Column 29 Row 23 ---")
    navigate_to(29, 23)
    
    # Step 4: Walk LEFT along Row 23 and probe DOWN on Columns 28 to 22
    print("\n--- STEP 4: Probing DOWN on Columns 28 to 22 ---")
    for col in range(28, 21, -1):
        navigate_to(col, 23)
        print(f"\nProbing DOWN at Column {get_pos()[0]} Row {get_pos()[1]}...")
        success, p = try_move("Down")
        if success:
            print(f"SUCCESS! Walked DOWN to {p}")
            # Try to walk DOWN again
            success2, p2 = try_move("Down")
            if success2:
                print(f"SUCCESS! Walked DOWN to {p2}")
                walk_step_robust("Up")
            walk_step_robust("Up")
        else:
            print("DOWN is BLOCKED")
            
    print(f"Final position: {get_pos()}")

if __name__ == "__main__":
    main()
