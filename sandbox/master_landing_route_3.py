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
    print("Starting absolute master route to B1F starting from (26, 3)...")
    pos = mgba.get_coordinates()
    print("Current position:", pos)
    
    # We should be at (26, 3) on 3F
    if pos != {'x': 26, 'y': 3}:
        print("Warning: not at (26, 3). Re-aligning...")
        if pos['y'] != 3:
            step_to("Down" if pos['y'] < 3 else "Up", pos['x'], 3)
        pos = mgba.get_coordinates()
        if pos['x'] != 26:
            step_to("Left" if pos['x'] > 26 else "Right", 26, 3)
            
    # 1. Walk from (26, 3) to switch at (2, 12) on 3F in State B
    print("--- 3F (State B): Walking to switch at (2, 12) ---")
    path_to_switch = [
        ("Left", 25, 3),
        ("Left", 24, 3),
        ("Left", 23, 3),
        ("Left", 22, 3),
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
        ("Left", 12, 5), # Bypasses Column 11 Row 8 rubble via Column 12!
        ("Down", 12, 6),
        ("Down", 12, 7),
        ("Down", 12, 8),
        ("Down", 12, 9),
        ("Down", 12, 10),
        ("Left", 11, 10),
        ("Left", 10, 10), # Column 10 Row 10 is OPEN!
        ("Left", 9, 10),
        ("Down", 9, 11),
        ("Left", 8, 11),
        ("Left", 7, 11),
        ("Left", 6, 11),
        ("Left", 5, 11),
        ("Left", 4, 11),
        ("Down", 4, 12),
        ("Down", 4, 13),
        ("Left", 3, 13),
        ("Left", 2, 13),
        ("Up", 2, 12),
    ]
    if not follow_path(path_to_switch):
        mgba.take_screenshot()
        return
        
    # Toggle switch to State A
    print("Facing Up to toggle switch...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    print("Toggling switch to State A...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"]) # YES
    time.sleep(1.0)
    mgba.press_buttons(["B"]) # Close dialogue
    time.sleep(1.0)
    
    # 2. Walk to East Balcony drop on 3F (State A)
    print("--- 3F (State A): Walking to East Balcony drop ---")
    path_to_drop_a = [
        ("Down", 2, 13),
        ("Right", 3, 13),
        ("Right", 4, 13),
        ("Up", 4, 12),
        ("Up", 4, 11),
        ("Right", 5, 11),
        ("Right", 6, 11),
        ("Right", 7, 11),
        ("Right", 8, 11),
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
