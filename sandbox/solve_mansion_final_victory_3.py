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
    print("Starting final balcony drop from (26, 6) on 3F...")
    
    # Current position is (26, 6)
    path = [
        # 1. Walk Down Column 26 to Row 14
        ("Down", 26, 7),
        ("Down", 26, 8),
        ("Down", 26, 9),
        ("Down", 26, 10),
        ("Down", 26, 11),
        ("Down", 26, 12),
        ("Down", 26, 13),
        ("Down", 26, 14),
        
        # 2. Walk Left to (24, 14)
        ("Left", 25, 14),
        ("Left", 24, 14),
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
        time.sleep(3.0) # Wait for warp animation
        
        pos_landing = mgba.get_coordinates()
        print("Landed on 1F! Current position:", pos_landing)
        mgba.take_screenshot()
    else:
        mgba.take_screenshot()

if __name__ == "__main__":
    main()
