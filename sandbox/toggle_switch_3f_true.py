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
    print("Starting route from (10, 7) to true 3F switch stand position (2, 12) via Column 12...")
    
    path = [
        # 1. Walk Right to (12, 7)
        ("Right", 11, 7),
        ("Right", 12, 7),
        
        # 2. Walk Down Column 12 to (12, 13)
        ("Down", 12, 8),
        ("Down", 12, 9),
        ("Down", 12, 10),
        ("Down", 12, 11),
        ("Down", 12, 12),
        ("Down", 12, 13),
        
        # 3. Walk Left along Row 13 to (2, 13)
        ("Left", 11, 13),
        ("Left", 10, 13),
        ("Left", 9, 13),
        ("Left", 8, 13),
        ("Left", 7, 13),
        ("Left", 6, 13),
        ("Left", 5, 13),
        ("Left", 4, 13),
        ("Left", 3, 13),
        ("Left", 2, 13),
        
        # 4. Walk Up to (2, 12)
        ("Up", 2, 12),
    ]
    
    success = True
    for direction, tx, ty in path:
        if not step_to(direction, tx, ty):
            print(f"Failed to reach ({tx}, {ty})!")
            success = False
            break
            
    if success:
        print("Successfully reached (2, 12)! Toggling switch at (2, 11) using Gen 1 timing...")
        # Face Up, wait, press A, wait, press A to confirm, wait, press B to clear
        mgba.press_buttons(["Up", "sleep 250", "A", "sleep 600", "A", "sleep 600", "B"])
        time.sleep(2.0)
        
        mgba.take_screenshot()
        print("Done!")
    else:
        mgba.take_screenshot()

if __name__ == "__main__":
    main()
