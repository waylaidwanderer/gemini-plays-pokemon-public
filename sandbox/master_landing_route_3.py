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
    print("Starting absolute master route to B1F from current position...")
    pos = mgba.get_coordinates()
    print("Current position:", pos)
    
    # We should be at (10, 11) on 1F
    if pos != {'x': 10, 'y': 11}:
        print("Warning: not at (10, 11). Re-aligning...")
        if pos['y'] != 11:
            step_to("Down" if pos['y'] < 11 else "Up", pos['x'], 11)
        pos = mgba.get_coordinates()
        if pos['x'] != 10:
            step_to("Left" if pos['x'] > 10 else "Right", 10, 11)
            
    # 1. Walk Left to (7, 11) and ascend to 2F
    print("--- 1F: Walking to stairs at (7, 10) ---")
    path_to_stairs_1f = [
        ("Left", 9, 11),
        ("Left", 8, 11),
        ("Left", 7, 11),
        ("Up", 7, 10), # Ascend to 2F
    ]
    if not follow_path(path_to_stairs_1f):
        mgba.take_screenshot()
        return
        
    time.sleep(1.5) # wait for transition
    pos = mgba.get_coordinates()
    print("Position on 2F:", pos)
    
    # 2. Ascend to 3F (stairs are at same location 7, 10)
    print("--- 2F: Ascending to 3F ---")
    if pos == {'x': 7, 'y': 11}:
        if not step_to("Up", 7, 10):
            print("Failed to ascend to 3F.")
            mgba.take_screenshot()
            return
            
    time.sleep(1.5) # wait for transition
    pos = mgba.get_coordinates()
    print("Position on 3F:", pos)
    
    # 3. Walk to switch at (2, 11) on 3F (State A)
    print("--- 3F: Walking to switch at (2, 12) ---")
    path_to_switch = [
        ("Down", 7, 12),
        ("Left", 6, 12),
        ("Left", 5, 12),
        ("Left", 4, 12),
        ("Left", 3, 12),
        ("Left", 2, 12),
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
    
    # 4. Walk to East Balcony drop on 3F (State B)
    print("--- 3F (State B): Walking to East Balcony drop ---")
    path_to_drop = [
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
        ("Right", 10, 10), # Column 10 Row 10 is OPEN in State B!
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
        ("Up", 21, 4),
        ("Up", 21, 3),
        ("Right", 22, 3),
        ("Right", 23, 3),
        ("Right", 24, 3),
        ("Right", 25, 3),
        ("Right", 26, 3),
        ("Down", 26, 4),
        ("Down", 26, 5),
        ("Left", 25, 5),
        ("Left", 24, 5),
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
