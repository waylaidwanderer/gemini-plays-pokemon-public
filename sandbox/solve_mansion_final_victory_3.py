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
    print("Starting master victory route via Row 3 from (21, 6)...")
    
    # We are currently at (21, 6) on 3F (State B)
    path = [
        # 1. Walk Up Column 21 to Row 3
        ("Up", 21, 5),
        ("Up", 21, 4),
        ("Up", 21, 3),
        
        # 2. Walk Right along Row 3 to Column 24
        ("Right", 22, 3),
        ("Right", 23, 3),
        ("Right", 24, 3),
        
        # 3. Walk Down Column 24 to the balcony drop at (24, 14)
        ("Down", 24, 4),
        ("Down", 24, 5),
        ("Down", 24, 6),
        ("Down", 24, 7),
        ("Down", 24, 8),
        ("Down", 24, 9),
        ("Down", 24, 10),
        ("Down", 24, 11),
        ("Down", 24, 12),
        ("Down", 24, 13),
        ("Down", 24, 14),
    ]
    
    success = True
    for direction, tx, ty in path:
        if not step_to(direction, tx, ty):
            print(f"Failed to reach ({tx}, {ty})!")
            success = False
            break
            
    if success:
        print("At (24, 14). Dropping off balcony...")
        # Step Left to drop
        mgba.press_buttons(["Left"])
        time.sleep(3.0) # Wait for drop animation/warp
        
        pos_landing = mgba.get_coordinates()
        print("Landed on 1F! Current position:", pos_landing)
        mgba.take_screenshot()
    else:
        mgba.take_screenshot()

if __name__ == "__main__":
    main()
