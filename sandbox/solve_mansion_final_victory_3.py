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
    
    # Current position is (23, 5) on 3F (State B)
    path_to_switch = [
        # 1. Walk Up Column 23 to Row 3
        ("Up", 23, 4),
        ("Up", 23, 3),
        
        # 2. Walk Left along Row 3 to Column 11
        ("Left", 22, 3),
        ("Left", 21, 3),
        ("Left", 20, 3),
        ("Left", 19, 3),
        ("Left", 18, 3),
        ("Left", 17, 3),
        ("Left", 16, 3),
        ("Left", 15, 3),
        ("Left", 14, 3),
        ("Left", 13, 3),
        ("Left", 12, 3),
        ("Left", 11, 3),
        
        # 3. Walk Down Column 11 to Row 7
        ("Down", 11, 4),
        ("Down", 11, 5),
        ("Down", 11, 6),
        ("Down", 11, 7),
        
        # 4. Walk Right to Column 12 (bypasses Row 8 rubble on Column 11)
        ("Right", 12, 7),
        
        # 5. Walk Down Column 12 to Row 11
        ("Down", 12, 8),
        ("Down", 12, 9),
        ("Down", 12, 10),
        ("Down", 12, 11),
        
        # 6. Walk Left to Column 11
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
            ("Right", 12, 12),
            ("Right", 13, 12),
            ("Right", 14, 12),
            ("Right", 15, 12),
            ("Right", 16, 12),
            ("Right", 17, 12),
            ("Right", 18, 12),
            ("Right", 19, 12),
            ("Right", 20, 12),
            ("Right", 21, 12),
            ("Right", 22, 12),
            ("Right", 23, 12),
            ("Right", 24, 12),
            ("Down", 24, 13), # Gate is OPEN in State A!
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
