import mgba
import time

def handle_battle():
    print("Encountered battle or text! Attempting to escape/dismiss...")
    mgba.press_buttons(["B", "sleep 300", "Down", "sleep 100", "Right", "sleep 100", "A", "sleep 1000", "B"])

def step_to(direction, tx, ty):
    pos = mgba.get_coordinates()
    if pos['x'] == tx and pos['y'] == ty:
        return True
        
    print(f"Current pos: {pos}. Pressing {direction} to reach ({tx}, {ty})...")
    mgba.press_buttons([direction])
    time.sleep(0.4)
    new_pos = mgba.get_coordinates()
    
    attempts = 0
    while new_pos != {'x': tx, 'y': ty} and attempts < 10:
        if new_pos == pos:
            print("Did not move. Retrying once to handle turning...")
            mgba.press_buttons([direction])
            time.sleep(0.4)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                print("Checking for battle or text...")
                handle_battle()
                time.sleep(0.5)
                mgba.press_buttons([direction])
                time.sleep(0.4)
                new_pos = mgba.get_coordinates()
        else:
            print(f"Unexpected position {new_pos}. Correcting...")
            pos = new_pos
            mgba.press_buttons([direction])
            time.sleep(0.4)
            new_pos = mgba.get_coordinates()
        attempts += 1
        
    return new_pos == {'x': tx, 'y': ty}

def follow_path(path):
    for d, tx, ty in path:
        if not step_to(d, tx, ty):
            print(f"Failed to move to ({tx}, {ty}).")
            mgba.take_screenshot()
            return False
    return True

def main():
    print("Currently at:", mgba.get_coordinates())
    
    # 1. Walk from (19, 16) on the East Balcony back inside and to Saffron Row 10
    path = [
        ("Right", 20, 16),
        ("Up", 20, 15),
        ("Right", 21, 15),
        ("Right", 22, 15),
        ("Up", 22, 14),
        ("Up", 22, 13),
        ("Up", 22, 12),
        ("Up", 22, 11),
        ("Up", 22, 10),
    ]
    
    print("Walking back inside to (22, 10)...")
    if not follow_path(path):
        return
        
    # 2. Walk Left to (10, 10)
    path_left = [
        ("Left", 21, 10),
        ("Left", 20, 10),
        ("Left", 19, 10),
        ("Left", 18, 10),
        ("Left", 17, 10),
        ("Left", 16, 10),
        ("Left", 15, 10),
        ("Left", 14, 10),
        ("Left", 13, 10),
        ("Left", 12, 10),
        ("Left", 11, 10),
        ("Left", 10, 10),
    ]
    
    print("Walking Left to (10, 10)...")
    if not follow_path(path_left):
        return
        
    # Take screenshot of the center-west area
    mgba.take_screenshot()
    
    # 3. Walk Left to column 3
    path_west = [
        ("Left", 9, 10),
        ("Left", 8, 10),
        ("Left", 7, 10),
        ("Left", 6, 10),
        ("Left", 5, 10),
        ("Left", 4, 10),
        ("Left", 3, 10),
    ]
    
    print("Walking Left to west wing at (3, 10)...")
    if not follow_path(path_west):
        return
        
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
