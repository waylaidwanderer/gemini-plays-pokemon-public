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
            # Maybe it was just a turn in place. Try pressing direction again!
            mgba.press_buttons([direction])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
            
            if new_pos == pos:
                print("Still did not move. Checking for battle...")
                handle_battle()
                time.sleep(0.5)
                # Try moving again
                mgba.press_buttons([direction])
                time.sleep(0.5)
                new_pos = mgba.get_coordinates()
        else:
            # We moved to an unexpected tile. Try to step in the direction of the target.
            print(f"We are at unexpected position {new_pos}. Retrying {direction}...")
            pos = new_pos
            mgba.press_buttons([direction])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
        attempts += 1
        
    return new_pos == {'x': tx, 'y': ty}

def main():
    print("Starting route to true 3F Mewtwo switch at (10, 5)...")
    
    path = [
        # 1. Walk Down to (2, 13)
        ("Down", 2, 11),
        ("Down", 2, 12),
        ("Down", 2, 13),
        # 2. Walk Right to (7, 13) (through Column 8 gap)
        ("Right", 3, 13),
        ("Right", 4, 13),
        ("Right", 5, 13),
        ("Right", 6, 13),
        ("Right", 7, 13),
        # 3. Walk Up to (7, 11)
        ("Up", 7, 12),
        ("Up", 7, 11),
        # 4. Walk Right to (10, 11)
        ("Right", 8, 11), # Wait, is (8, 11) blocked? Let's check!
        # Oh, wait! Earlier we found (8, 11) is blocked!
        # Let's check: can we walk along Row 13 instead?
        # Yes! Row 13 is open all the way to column 10!
        # So we should walk Right along Row 13 to (10, 13) instead!
    ]
    
    # Correct path:
    # 1. Down to (2, 13)
    # 2. Right to (10, 13)
    # 3. Up to (10, 6)
    
    path = [
        ("Down", 2, 11),
        ("Down", 2, 12),
        ("Down", 2, 13),
        
        ("Right", 3, 13),
        ("Right", 4, 13),
        ("Right", 5, 13),
        ("Right", 6, 13),
        ("Right", 7, 13),
        ("Right", 8, 13),
        ("Right", 9, 13),
        ("Right", 10, 13),
        
        ("Up", 10, 12),
        ("Up", 10, 11),
        ("Up", 10, 10),
        ("Up", 10, 9),
        ("Up", 10, 8),
        ("Up", 10, 7),
        ("Up", 10, 6),
    ]
    
    success = True
    for direction, tx, ty in path:
        if not step_to(direction, tx, ty):
            print(f"Failed to reach ({tx}, {ty})!")
            success = False
            break
            
    if success:
        print("Successfully reached (10, 6)! Facing Up towards the switch at (10, 5)...")
        # Ensure we are facing Up and interact
        mgba.press_buttons(["Up", "A"])
        time.sleep(1.0)
        
        mgba.take_screenshot()
        
        print("Pressing A to select YES and confirm switch activation...")
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
        mgba.take_screenshot()
        print("Done!")
    else:
        mgba.take_screenshot()

if __name__ == "__main__":
    main()
