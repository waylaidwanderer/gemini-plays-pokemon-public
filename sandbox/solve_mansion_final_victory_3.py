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
    print("Starting master victory route: pit drop at (24, 5)...")
    
    # We are currently at (24, 12) on 3F
    path = [
        # 1. Walk Right to (26, 12)
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
        
        # 3. Walk Left to (24, 5) -> Pit Drop!
        ("Left", 25, 5),
        ("Left", 24, 5),
    ]
    
    success = True
    for direction, tx, ty in path:
        if not step_to(direction, tx, ty):
            print(f"Failed to reach ({tx}, {ty})!")
            success = False
            break
            
    if success:
        print("At (24, 5). Falling through pit...")
        time.sleep(3.0) # Wait for drop animation/warp
        
        pos_landing = mgba.get_coordinates()
        print("Landed on 1F! Current position:", pos_landing)
        mgba.take_screenshot()
    else:
        mgba.take_screenshot()

if __name__ == "__main__":
    main()
