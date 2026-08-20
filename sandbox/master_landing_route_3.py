import mgba
import time

def handle_battle():
    print("Encountered battle or text! Escaping...")
    # Safe escape sequence: press B twice to close any menus/text,
    # then Down, Right to guarantee we hover RUN, then A to select RUN.
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300", "Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1000", "B"])

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

def follow_path(path):
    for direction, tx, ty in path:
        if not step_to(direction, tx, ty):
            print(f"Failed to reach ({tx}, {ty})!")
            return False
    return True

def main():
    print("Starting absolute master route to B1F starting from (24, 5)...")
    pos = mgba.get_coordinates()
    print("Current position:", pos)
    
    # We should be at (24, 5) on 3F
    if pos != {'x': 24, 'y': 5}:
        print("Warning: not at (24, 5). Re-aligning...")
        if pos['y'] != 5:
            step_to("Down" if pos['y'] < 5 else "Up", pos['x'], 5)
        pos = mgba.get_coordinates()
        if pos['x'] != 24:
            step_to("Left" if pos['x'] > 24 else "Right", 24, 5)
            
    # Walk the State B path on 3F to the East Balcony drop
    print("--- 3F (State B): Walking to East Balcony drop ---")
    path_to_drop = [
        ("Down", 24, 6),
        ("Down", 24, 7),
        ("Right", 25, 7),
        ("Right", 26, 7),
        ("Down", 26, 8),
        ("Down", 26, 9),
        ("Down", 26, 10),
        ("Down", 26, 11),
        ("Down", 26, 12),
        ("Left", 25, 12),
        ("Down", 25, 13),
        ("Down", 25, 14),
        ("Left", 24, 14),
        ("Left", 23, 14),
        ("Left", 22, 14),
        ("Down", 22, 15),
        ("Left", 21, 15), # Enter balcony doorway
        ("Left", 20, 15), # Onto balcony
    ]
    if not follow_path(path_to_drop):
        mgba.take_screenshot()
        return
        
    print("At (20, 15). Stepping Left to drop...")
    mgba.press_buttons(["Left"])
    time.sleep(3.0) # wait for falling warp
    
    landing_pos = mgba.get_coordinates()
    print("Landed! Position:", landing_pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
