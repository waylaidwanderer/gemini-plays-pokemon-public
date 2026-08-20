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
            # We didn't move. In Gen 1, if we just turned, new_pos can equal pos.
            # So we check if we face the correct direction by pressing it again.
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
    
    # 1. Walk from (12, 11) to (2, 12) on 3F (State A)
    path_to_switch = [
        ("Down", 12, 12),
        ("Left", 11, 12),
        ("Left", 10, 12),
        ("Left", 9, 12),
        ("Left", 8, 12),
        ("Left", 7, 12),
        ("Left", 6, 12),
        ("Left", 5, 12),
        ("Left", 4, 12),
        ("Left", 3, 12),
        ("Left", 2, 12),
    ]
    
    print("Walking to west-side 3F switch...")
    if not follow_path(path_to_switch):
        return
        
    # 2. Toggle the switch at (2, 11) to State B
    print("At (2, 12). Facing Up and toggling switch to State B...")
    mgba.press_buttons(["Up", "sleep 200", "A", "sleep 500", "A", "sleep 500", "B"])
    time.sleep(2.0)
    
    # 3. Walk to the balcony drop at (24, 14) via the State B horizontal crossing
    path_to_balcony = [
        ("Right", 3, 12),
        ("Right", 4, 12),
        ("Right", 5, 12),
        ("Right", 6, 12),
        ("Right", 7, 12),
        ("Down", 7, 13),
        ("Right", 8, 13),
        ("Right", 9, 13),
        ("Up", 9, 12),
        ("Up", 9, 11),
        ("Up", 9, 10),
        ("Right", 10, 10),
        ("Right", 11, 10),
        ("Up", 11, 9),
        ("Up", 11, 8),
        ("Up", 11, 7),
        ("Up", 11, 6),
        ("Up", 11, 5),
        ("Right", 12, 5),
        ("Right", 13, 5),
        ("Right", 14, 5),
        ("Right", 15, 5),
        ("Right", 16, 5),
        ("Right", 17, 5),
        ("Right", 18, 5),
        ("Right", 19, 5),
        ("Right", 20, 5),
        ("Right", 21, 5), # Gate is OPEN in State B!
        ("Right", 22, 5),
        ("Right", 23, 5),
        ("Right", 24, 5),
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
    
    print("Walking to balcony drop...")
    if not follow_path(path_to_balcony):
        return
        
    print("At (24, 14). Dropping off the balcony...")
    mgba.press_buttons(["Left"])
    time.sleep(3.0) # Wait for drop animation/warp
    
    pos = mgba.get_coordinates()
    print("Landed! Coordinates:", pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
