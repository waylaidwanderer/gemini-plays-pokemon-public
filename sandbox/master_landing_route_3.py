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
    print("Starting absolute master route to B1F starting from (8, 11) in State A...")
    
    # Dismiss 'Got away safely!' text if any
    mgba.press_buttons(["B"])
    time.sleep(1.0)
    
    pos = mgba.get_coordinates()
    print("Current position:", pos)
    
    # We should be at (8, 11) on 3F
    if pos != {'x': 8, 'y': 11}:
        print("Warning: not at (8, 11). Re-aligning...")
        if pos['y'] != 11:
            step_to("Down" if pos['y'] < 11 else "Up", pos['x'], 11)
        pos = mgba.get_coordinates()
        if pos['x'] != 8:
            step_to("Left" if pos['x'] > 8 else "Right", 8, 11)
            
    # 1. Walk the State A path directly to the East Balcony drop
    print("--- 3F (State A): Walking directly to East Balcony drop ---")
    path_to_drop_a = [
        ("Right", 9, 11),
        ("Right", 10, 11), # Column 10 Row 11 is OPEN in State A!
        ("Right", 11, 11),
        ("Right", 12, 11),
        ("Up", 12, 10),
        ("Up", 12, 9),
        ("Up", 12, 8),
        ("Up", 12, 7),
        ("Up", 12, 6),
        ("Right", 13, 6),
        ("Right", 14, 6),
        ("Right", 15, 6),
        ("Right", 16, 6),
        ("Right", 17, 6),
        ("Right", 18, 6),
        ("Right", 19, 6),
        ("Right", 20, 6),
        ("Right", 21, 6),
        ("Right", 22, 6),
        ("Right", 23, 6),
        ("Right", 24, 6),
        ("Down", 24, 7),
        ("Down", 24, 8),
        ("Down", 24, 9),
        ("Down", 24, 10),
        ("Down", 24, 11),
        ("Down", 24, 12),
        ("Down", 24, 13), # Gate at (24, 13) is OPEN in State A!
        ("Down", 24, 14),
        ("Left", 23, 14),
        ("Left", 22, 14),
        ("Down", 22, 15),
        ("Left", 21, 15), # Enter balcony doorway
        ("Left", 20, 15), # Inside balcony doorway
        ("Down", 20, 16),
        ("Down", 20, 17), # Gate (20, 17) is OPEN in State A!
        ("Down", 20, 18), # Onto balcony
    ]
    if not follow_path(path_to_drop_a):
        mgba.take_screenshot()
        return
        
    print("At (20, 18). Stepping Left to drop...")
    mgba.press_buttons(["Left"])
    time.sleep(3.0) # wait for falling warp
    
    landing_pos = mgba.get_coordinates()
    print("Landed! Position:", landing_pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
