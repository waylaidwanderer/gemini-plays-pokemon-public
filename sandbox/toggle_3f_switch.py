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
    print("Currently at on 3F:", mgba.get_coordinates())
    
    # Walk to (2, 12) from (12, 11)
    path = [
        ("Left", 11, 11),
        ("Left", 10, 11),
        ("Left", 9, 11),
        ("Left", 8, 11),
        ("Left", 7, 11),
        ("Left", 6, 11),
        ("Left", 5, 11),
        ("Left", 4, 11),
        ("Left", 3, 11),
        ("Down", 3, 12),
        ("Left", 2, 12),
    ]
    
    if not follow_path(path):
        return
        
    print("At 3F Switch at (2, 12). Toggling...")
    # Face Up (towards statue at 2, 11) and press A
    mgba.press_buttons(["Up", "sleep 200", "A", "sleep 500", "A", "sleep 500", "B"])
    time.sleep(2.0)
    
    # Verify State B is toggled by checking coordinates
    pos = mgba.get_coordinates()
    print("After toggle position:", pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
