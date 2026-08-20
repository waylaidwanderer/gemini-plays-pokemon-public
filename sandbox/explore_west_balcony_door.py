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
            # Check if we merely turned in place (Gen 1 turning mechanics)
            print("Did not move. Retrying once to handle turning in place...")
            mgba.press_buttons([direction])
            time.sleep(0.4)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                print("Still did not move. Checking for battle or text...")
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
    
    # Path to West Wing (3, 11) crossing Column 22 on Row 3 and Column 10 gate on Row 5
    path = [
        ("Up", 24, 10),
        ("Right", 25, 10),
        ("Right", 26, 10),
        ("Up", 26, 9),
        ("Up", 26, 8),
        ("Up", 26, 7),
        ("Up", 26, 6),
        ("Up", 26, 5),
        ("Up", 26, 4),
        ("Up", 26, 3),
        ("Left", 25, 3),
        ("Left", 24, 3),
        ("Left", 23, 3),
        ("Left", 22, 3), # Cross Column 22!
        ("Left", 21, 3),
        ("Down", 21, 4),
        ("Down", 21, 5), # Gate (21, 5) is OPEN in State B!
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
        ("Down", 11, 6),
        ("Down", 11, 7),
        ("Down", 11, 8),
        ("Down", 11, 9),
        ("Down", 11, 10),
        ("Down", 11, 11),
        ("Left", 10, 11),
        ("Left", 9, 11),
        ("Left", 8, 11),
        ("Left", 7, 11),
        ("Left", 6, 11),
        ("Left", 5, 11),
        ("Left", 4, 11),
        ("Left", 3, 11),
    ]
    
    print("Walking back to west wing...")
    if not follow_path(path):
        return
        
    mgba.take_screenshot()
    print("Successfully reached west wing at (3, 11)!")

if __name__ == "__main__":
    main()
