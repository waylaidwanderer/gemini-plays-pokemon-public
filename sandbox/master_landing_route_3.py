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
    print("Starting absolute master route to B1F starting from (21, 16) in State A...")
    pos = mgba.get_coordinates()
    print("Current position:", pos)
    
    # We should be at (21, 16) on 3F
    if pos != {'x': 21, 'y': 16}:
        print("Warning: not at (21, 16). Re-aligning...")
        if pos['y'] != 16:
            step_to("Down" if pos['y'] < 16 else "Up", pos['x'], 16)
        pos = mgba.get_coordinates()
        if pos['x'] != 21:
            step_to("Left" if pos['x'] > 21 else "Right", 21, 16)
            
    # 1. Walk from (21, 16) to switch at (2, 12) on 3F in State A
    print("--- 3F (State A): Walking to switch at (2, 12) ---")
    path_to_switch = [
        ("Up", 21, 15),
        ("Up", 21, 14),
        ("Up", 21, 13),
        ("Up", 21, 12),
        ("Up", 21, 11),
        ("Up", 21, 10),
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
        
    # Toggle switch to State B
    print("Facing Up to toggle switch...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    print("Toggling switch to State B...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"]) # YES
    time.sleep(1.0)
    mgba.press_buttons(["B"]) # Close dialogue
    time.sleep(1.0)
    
    # 2. Walk to East Balcony drop on 3F (State B)
    print("--- 3F (State B): Walking to East Balcony drop ---")
    path_to_drop_b = [
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
        ("Right", 10, 10), # Column 10 Row 10 is OPEN!
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
        ("Right", 21, 5), # Gate (21, 5) is OPEN in State B!
        ("Down", 21, 6),
        ("Down", 21, 7),
        ("Down", 21, 8),
        ("Down", 21, 9),
        ("Down", 21, 10),
        ("Down", 21, 11),
        ("Down", 21, 12),
        ("Down", 21, 13),
        ("Down", 21, 14),
        ("Down", 21, 15), # Enter balcony doorway
        ("Left", 20, 15), # Inside balcony doorway
        ("Down", 20, 16),
        ("Down", 20, 17), # Gate (20, 17) is OPEN in State B!
        ("Down", 20, 18), # Onto balcony
    ]
    if not follow_path(path_to_drop_b):
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
