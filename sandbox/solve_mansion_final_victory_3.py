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
    print("Starting absolute master victory route to B1F...")
    
    # Current position is (24, 7) on 3F
    path_to_switch = [
        # 1. Walk Up Column 24 to Row 5
        ("Up", 24, 6),
        ("Up", 24, 5),
        
        # 2. Walk Right to Column 26
        ("Right", 25, 5),
        ("Right", 26, 5),
        
        # 3. Walk Down Column 26 to Row 12
        ("Down", 26, 6),
        ("Down", 26, 7),
        ("Down", 26, 8),
        ("Down", 26, 9),
        ("Down", 26, 10),
        ("Down", 26, 11),
        ("Down", 26, 12),
        
        # 4. Walk Left along Row 12 to Column 11
        ("Left", 25, 12),
        ("Left", 24, 12),
        ("Left", 23, 12),
        ("Left", 22, 12),
        ("Left", 21, 12),
        ("Left", 20, 12),
        ("Left", 19, 12),
        ("Left", 18, 12),
        ("Left", 17, 12),
        ("Left", 16, 12),
        ("Left", 15, 12),
        ("Left", 14, 12),
        ("Left", 13, 12),
        ("Left", 12, 12),
        ("Left", 11, 12),
        
        # 5. Walk Up to (11, 11)
        ("Up", 11, 11),
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
