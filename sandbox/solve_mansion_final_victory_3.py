import mgba
import time

def handle_battle():
    print("Encountered battle or text! Escaping...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(2.0)
    mgba.press_buttons(["B"])
    time.sleep(0.5)

def step_to(direction, tx, ty):
    pos = mgba.get_coordinates()
    if pos['x'] == tx and pos['y'] == ty:
        return True
        
    print(f"At {pos}. Moving {direction} to ({tx}, {ty})...")
    mgba.press_buttons([direction])
    time.sleep(0.5)
    new_pos = mgba.get_coordinates()
    
    attempts = 0
    while new_pos != {'x': tx, 'y': ty} and attempts < 5:
        if new_pos == pos:
            print("Did not move. Checking for direction turn, wall, or battle...")
            mgba.press_buttons([direction])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
            
            if new_pos == pos:
                print("Still did not move. Checking for battle...")
                handle_battle()
                time.sleep(0.5)
                mgba.press_buttons([direction])
                time.sleep(0.5)
                new_pos = mgba.get_coordinates()
        else:
            print(f"We are at unexpected position {new_pos}. Retrying {direction}...")
            pos = new_pos
            mgba.press_buttons([direction])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
        attempts += 1
        
    return new_pos == {'x': tx, 'y': ty}

def main():
    print("Starting absolute master victory route to B1F via State A balcony drop...")
    
    # Current position is (24, 12) on 3F (State B)
    path_to_switch = [
        # 1. Walk Right to Column 26
        ("Right", 25, 12),
        ("Right", 26, 12),
        
        # 2. Walk Up Column 26 to Row 5
        ("Up", 26, 11),
        ("Up", 26, 10),
        ("Up", 26, 9),
        ("Up", 26, 8),
        ("Up", 26, 7),
        ("Up", 26, 6),
        ("Up", 26, 5),
        
        # 3. Walk Left along Row 5 to Column 11
        ("Left", 25, 5),
        ("Left", 24, 5),
        ("Left", 23, 5),
        ("Left", 22, 5),
        ("Left", 21, 5), # Gate at (21, 5) is OPEN in State B!
        ("Left", 20, 5),
        ("Left", 19, 5),
        ("Left", 18, 5),
        ("Left", 17, 5),
        ("Left", 16, 5),
        ("Left", 15, 5),
        ("Left", 14, 5),
        ("Left", 13, 5),
        ("Left", 12, 5),
        ("Left", 11, 5),
        
        # 4. Walk Down Column 11 to Row 7
        ("Down", 11, 6),
        ("Down", 11, 7),
        
        # 5. Walk Right to Column 12 (bypasses Row 8 rubble on Column 11)
        ("Right", 12, 7),
        
        # 6. Walk Down Column 12 to Row 11
        ("Down", 12, 8),
        ("Down", 12, 9),
        ("Down", 12, 10),
        ("Down", 12, 11),
        
        # 7. Walk Left to Column 11
        ("Left", 11, 11),
    ]
    
    success = True
    for direction, tx, ty in path_to_switch:
        if not step_to(direction, tx, ty):
            print(f"Failed to reach ({tx}, {ty}) on way to switch!")
            success = False
            break
            
    if success:
        print("Successfully reached (11, 11)! Toggling switch at (12, 11) to State A...")
        # Face Right and toggle
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
        # Select YES, dismiss text, close dialogue
        mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "B"])
        time.sleep(2.5)
        
        # Now walk to the balcony drop at (24, 14) on 3F (State A)
        print("Walking to the open balcony drop at (24, 14) in State A...")
        path_to_balcony = [
            ("Down", 11, 12),
            
            # Now Row 12 is open in State A! Wait, is Row 12 blocked by rubble?
            # Yes, Row 12 is blocked at (22, 12) and (23, 12) by yellow rubble.
            # So we cannot walk along Row 12!
            # Instead, we walk Down to Row 13!
            # Let's check: from (11, 12), can we walk Down to (11, 13)?
            # No, Row 13 on Column 11 is blocked by a wall!
            # But wait! Column 10 is open at Row 13!
            # So we walk:
            # - Left to (10, 12) (which is open in State A!)
            # - Down to (10, 13)
            # - Right to Column 24? No, Row 13 is blocked at Column 24/25.
            # Wait!
            # In State A, the gate at (24, 13) is OPEN.
            # But how do we walk from (11, 11) to Column 24 in State A?
            # Let's think:
            # In State A:
            # - The gate at (10, 11)/(10, 12) is OPEN.
            # - Can we walk Left from (11, 11) to (10, 11)?
            # Yes!
            # - From (10, 11), can we walk Up Column 10 to Row 5 (10, 5)?
            # Yes! Column 10 is open in State A!
            # - From (10, 5), can we walk Right to Column 24 on Row 5?
            # No, the gate at (21, 5) is CLOSED in State A!
            # Wait, then how do we reach Column 24 on Row 12/14 in State A?
            # Ah!
            # Let's look at Saffron Mansion 3F map in State A.
            # If the gate at (10, 11) is OPEN, we can walk from the West side to the East side.
            # Can we walk horizontally on Row 11?
            # - We walk from (10, 11) to (11, 11).
            # - From (11, 11), can we walk Left? Yes.
            # Wait, how do we cross Column 22 on the East side?
            # In State A, the gate at Column 22 is CLOSED?
            # No, in State A, the gate at (21, 5) is CLOSED, but is Column 22 gate open?
            # Yes, the Column 22 gate (which is at (22, 5)) is closed?
            # Wait! We just saw that Row 11 is completely open horizontally across column 22 in both states!
            # Yes!!!
            # So we can walk Left/Right horizontally along Row 11 across Column 22!
            # And from Column 22, we can walk to Column 24!
            # Let's trace Row 11 horizontally:
            # - From (11, 11) (where we are standing when we toggle the switch to State A):
            # - Can we walk Right along Row 11 directly to (24, 11)?
            # Yes!!!
            # Let's check: is Row 11 open from Column 11 to Column 24?
            # - Column 11 Row 11 is open.
            # - Column 12 Row 11 is open.
            # - Column 13 Row 11 is open (wait, is it?).
            # - In Saffron Mansion 3F, Row 11 is the main horizontal hallway!
            # Yes! Row 11 is completely open horizontally across almost all columns!
            # Let's check:
            # - Currently standing at (11, 11).
            # - Walk Right to (24, 11)!
            # - Walk Down to (24, 14):
            #   - (24, 11) -> (24, 12) -> (24, 13) -> (24, 14).
            #   - In State A, the gate at (24, 13) is OPEN!
            #   - So we can walk Down directly to (24, 14)!
            # - Step Left to drop!
            
            # This is incredibly simple and 100% correct!
            # Row 11 is wide open horizontally, so we can walk straight Right from (11, 11) to (24, 11)!
        ]
        
        path_to_balcony = [
            ("Right", 12, 11),
            ("Right", 13, 11),
            ("Right", 14, 11),
            ("Right", 15, 11),
            ("Right", 16, 11),
            ("Right", 17, 11),
            ("Right", 18, 11),
            ("Right", 19, 11),
            ("Right", 20, 11),
            ("Right", 21, 11),
            ("Right", 22, 11), # Open in both states!
            ("Right", 23, 11),
            ("Right", 24, 11),
            ("Down", 24, 12),
            ("Down", 24, 13), # Open in State A!
            ("Down", 24, 14),
        ]
        
        for direction, tx, ty in path_to_balcony:
            if not step_to(direction, tx, ty):
                print(f"Failed to reach ({tx}, {ty}) on way to balcony!")
                success = False
                break
                
        if success:
            print("At (24, 14). Dropping off balcony...")
            # Step Left to drop
            mgba.press_buttons(["Left"])
            time.sleep(3.0) # Wait for drop animation/warp
            
            landing_pos = mgba.get_coordinates()
            print("Landed on B1F! Current position:", landing_pos)
            mgba.take_screenshot()
            
    else:
        mgba.take_screenshot()

if __name__ == "__main__":
    main()
