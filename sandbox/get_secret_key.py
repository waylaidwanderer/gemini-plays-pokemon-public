import mgba
import time

def move_to(tx, ty):
    current = mgba.get_coordinates()
    print(f"Navigating from {current} to ({tx}, {ty})...")
    
    attempts_stuck = 0
    while current != {'x': tx, 'y': ty}:
        cx, cy = current['x'], current['y']
        
        # Determine next button to press
        if cx < tx:
            btn = "Right"
        elif cx > tx:
            btn = "Left"
        elif cy < ty:
            btn = "Down"
        elif cy > ty:
            btn = "Up"
            
        mgba.press_buttons([btn])
        time.sleep(0.4)
        
        new_pos = mgba.get_coordinates()
        if new_pos == current:
            # Position did not change. We might be in a battle or hitting a wall!
            attempts_stuck += 1
            print(f"Stuck at {current} (attempt {attempts_stuck}). Trying to clear/flee...")
            
            # 1. Try to flee from battle: Down, Right, A
            mgba.press_buttons(["Down", "Right", "A"])
            time.sleep(1.0)
            
            # 2. Press B to clear "Got away safely!" or any dialogue
            mgba.press_buttons(["B"])
            time.sleep(0.5)
            
            # 3. Press B again to be sure
            mgba.press_buttons(["B"])
            time.sleep(0.5)
            
            new_pos = mgba.get_coordinates()
            if new_pos == current and attempts_stuck > 3:
                # If we are still stuck after 3 attempts, we might be hitting a wall. Break to avoid infinite loop.
                print(f"CRITICAL: Physically blocked at {current} while trying to reach ({tx}, {ty})!")
                break
        else:
            attempts_stuck = 0
            current = new_pos
            print(f"Moved to: {current}")

def execute_master_route():
    print("Starting B1F Secret Key Master Routine...")
    
    # We are currently at (10, 1) in State A
    # Step 1: Walk Down Column 10 to Row 11
    move_to(10, 11)
    
    # Step 2: Walk Left to (3, 11)
    move_to(3, 11)
    
    # Step 3: Walk to (1, 11) via Row 12 to bypass the statue
    move_to(3, 12)
    move_to(1, 12)
    move_to(1, 11)
    
    # Step 4: Turn Right and toggle switch to State B
    print("At (1, 11). Facing Right to toggle switch...")
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    # Clear dialogue
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    print(f"Current position after switch toggle: {mgba.get_coordinates()}")
    
    # Step 5: Walk to (5, 13) via Row 13 in State B
    move_to(1, 13)
    move_to(5, 13)
    
    # Step 6: Walk UP Column 5 to (5, 8)
    move_to(5, 8)
    
    # Step 7: Walk Left to (4, 8)
    move_to(4, 8)
    
    # Step 8: Walk UP Column 4 to (4, 5) (through open gates (4,7) and (4,6)!)
    move_to(4, 5)
    
    # Step 9: Walk Left to (1, 5)
    move_to(1, 5)
    
    # Step 10: Stand at (1, 5) facing UP and press A to retrieve Secret Key
    print("At (1, 5). Facing Up to retrieve Secret Key...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    # Clear dialogue
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    print(f"Retrieval attempt finished. Final position: {mgba.get_coordinates()}")
    scr = mgba.take_screenshot()
    print(f"Screenshot at end: {scr}")

execute_master_route()
