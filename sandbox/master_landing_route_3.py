import mgba
import time

def handle_battle():
    print("Encountered battle or text! Escaping...")
    # Safe escape sequence: press B twice to close any menus/text,
    # then Down, Right to guarantee we hover RUN, then A to select RUN.
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300", "Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1000", "B"])

def step_to_test(direction, tx, ty):
    pos = mgba.get_coordinates()
    if pos['x'] == tx and pos['y'] == ty:
        return True
        
    print(f"At {pos}. Attempting to move {direction} to ({tx}, {ty})...")
    mgba.press_buttons([direction])
    time.sleep(0.5)
    new_pos = mgba.get_coordinates()
    
    if new_pos == pos:
        # Check if we merely turned in place
        print("Did not move. Pressing direction again...")
        mgba.press_buttons([direction])
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        
        if new_pos == pos:
            # We are blocked! Could be battle or solid obstacle
            print("Still did not move. Checking for battle/text...")
            # Try to press B to dismiss any dialogue/battle
            mgba.press_buttons(["B"])
            time.sleep(0.5)
            # Check coordinates again
            new_pos = mgba.get_coordinates()
            if new_pos != pos:
                print("Coordinates changed after B press!")
                return new_pos['x'] == tx and new_pos['y'] == ty
                
            # If still same, let's see if we are in a battle
            print("Attempting to run from possible battle...")
            handle_battle()
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
            
    print(f"Result position: {new_pos}")
    return new_pos['x'] == tx and new_pos['y'] == ty

def main():
    print("Starting master landing route 3 with empirical wall checking...")
    pos = mgba.get_coordinates()
    print("Current position:", pos)
    
    # 1. Walk Left to (2, 13)
    print("--- STEP 1: Walking to (2, 13) ---")
    path_to_switch = [
        ("Left", 4, 13),
        ("Left", 3, 13),
        ("Left", 2, 13),
        ("Up", 2, 12),
    ]
    for d, tx, ty in path_to_switch:
        if not step_to_test(d, tx, ty):
            print(f"Failed to reach ({tx}, {ty}) on way to switch.")
            mgba.take_screenshot()
            return
            
    # 2. Toggle switch at (2, 11) to State B
    print("Facing Up to toggle switch...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    print("Toggling switch to State B...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"]) # YES
    time.sleep(1.0)
    mgba.press_buttons(["B"]) # Close dialogue
    time.sleep(1.0)
    
    # 3. Empirically test if we can walk Right to (3, 12)
    print("--- STEP 3: Testing if (3, 12) is walkable ---")
    if step_to_test("Right", 3, 12):
        print("SUCCESS: (3, 12) is WALKABLE!")
        # We can continue along the standard Column 3 path
        path_to_drop = [
            ("Up", 3, 11),
            ("Up", 3, 10),
            ("Up", 3, 9),
            ("Up", 3, 8),
            ("Up", 3, 7),
            ("Up", 3, 6),
            ("Up", 3, 5),
            ("Up", 3, 4),
            ("Up", 3, 3),
        ]
    else:
        print("BLOCKED: (3, 12) is solid/blocked! Attempting bypass via Row 13...")
        # Bypass via Row 13 to Column 3 (wait, (3, 12) is blocked, can we walk vertically past it?)
        # Let's check Column 2 vertically: (2, 12) -> (2, 11) -> (2, 10)
        # Wait, let's try walking Up to (2, 11) or (2, 10) first to see if Column 2 is open!
        # If Column 2 is open vertically to Row 10: (2, 12) -> (2, 11) -> (2, 10) -> (3, 10)?
        # Let's write a bypass route that walks Down to (2, 13), Right to (3, 13), Right to (4, 13), then Up to Row 12, etc.
        # But wait! If Column 3 is blocked at Row 12, we can't walk Up Column 3 anyway!
        # Let's test Column 2 or other paths if (3, 12) is blocked.
        # For now, let's just log the failure and stop so we can analyze the screenshot!
        mgba.take_screenshot()
        return

    # If the standard column 3 path is open, continue to drop
    path_to_drop += [
        ("Right", 4, 3),
        ("Right", 5, 3),
        ("Right", 6, 3),
        ("Right", 7, 3),
        ("Right", 8, 3),
        ("Right", 9, 3),
        ("Right", 10, 3),
        ("Right", 11, 3),
        ("Right", 12, 3),
        ("Right", 13, 3),
        ("Right", 14, 3),
        ("Right", 15, 3),
        ("Right", 16, 3),
        ("Right", 17, 3),
        ("Right", 18, 3),
        ("Right", 19, 3),
        ("Right", 20, 3),
        ("Right", 21, 3),
        ("Down", 21, 4),
        ("Down", 21, 5), # Gate (21, 5) is OPEN in State B!
        ("Down", 21, 6),
        ("Down", 21, 7),
        ("Down", 21, 8),
        ("Down", 21, 9),
        ("Down", 21, 10),
        ("Down", 21, 11),
        ("Down", 21, 12),
        ("Down", 21, 13),
        ("Down", 21, 14),
        ("Right", 22, 14),
        ("Right", 23, 14),
        ("Right", 24, 14),
    ]
    
    print("Walking path to balcony drop...")
    if not follow_path(path_to_drop):
        print("Failed to reach balcony drop point.")
        mgba.take_screenshot()
        return
        
    print("At (24, 14). Dropping off balcony...")
    # Step Left to drop
    mgba.press_buttons(["Left"])
    time.sleep(3.0) # Wait for drop animation/warp
    
    landing_pos = mgba.get_coordinates()
    print("Landed! Current position:", landing_pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
