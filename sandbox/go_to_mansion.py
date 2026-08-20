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
            print("Did not move. Checking for battle or text...")
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
    
    # Path to Pokémon Mansion
    # 1. Walk Up column 19 to row 6
    # 2. Walk Left along row 6 to column 15 (bypassing Gym building)
    # 3. Walk Up column 15 to row 3
    # 4. Walk Left along row 3 to column 6 (Mansion entrance)
    path = [
        ("Up", 19, 11),
        ("Up", 19, 10),
        ("Up", 19, 9),
        ("Up", 19, 8),
        ("Up", 19, 7),
        ("Up", 19, 6),
        ("Left", 18, 6),
        ("Left", 17, 6),
        ("Left", 16, 6),
        ("Left", 15, 6),
        ("Up", 15, 5),
        ("Up", 15, 4),
        ("Up", 15, 3),
        ("Left", 14, 3),
        ("Left", 13, 3),
        ("Left", 12, 3),
        ("Left", 11, 3),
        ("Left", 10, 3),
        ("Left", 9, 3),
        ("Left", 8, 3),
        ("Left", 7, 3),
        ("Left", 6, 3), # Mansion Entrance warp
    ]
    
    print("Walking to Pokémon Mansion entrance...")
    if not follow_path(path):
        return
        
    time.sleep(2.0) # Wait for warp
    pos = mgba.get_coordinates()
    print("Inside Mansion 1F:", pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
