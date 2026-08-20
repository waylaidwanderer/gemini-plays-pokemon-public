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
    
    # Walk Left from (25, 10) to (3, 10) on 3F (State B)
    # Bypassing the pillar at (8, 10) by walking around it if needed
    # Wait, let's see if column 8 has a pillar on row 10.
    # Yes, we verified column 8 has a pillar on row 10!
    # So we must bypass column 8 by walking Down to row 13, Left, then back Up!
    # Let's trace the bypass:
    # Walk Left to (10, 10) -> Down to (10, 13) -> Left to (7, 13) -> Up to (7, 10) -> Left to (3, 10).
    path = [
        ("Left", 24, 10),
        ("Left", 23, 10),
        ("Left", 22, 10),
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
        ("Down", 10, 11),
        ("Down", 10, 12),
        ("Down", 10, 13),
        ("Left", 9, 13),
        ("Left", 8, 13),
        ("Left", 7, 13),
        ("Up", 7, 12),
        ("Up", 7, 11),
        ("Up", 7, 10),
        ("Left", 6, 10),
        ("Left", 5, 10),
        ("Left", 4, 10),
        ("Left", 3, 10),
    ]
    
    print("Walking around pillar to the west wing...")
    if not follow_path(path):
        return
        
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
