import mgba
import time

def handle_battle():
    print("Encountered battle or text! Escaping...")
    # Highly robust escape sequence: press B twice to clear submenus,
    # then Down, Right to highlight RUN, then A to select RUN.
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
    print("Starting master landing route to B1F via State B balcony drop...")
    pos = mgba.get_coordinates()
    print("Current position:", pos)
    
    # 1. Walk Left to (2, 12) on 3F in State A
    print("--- STEP 1: Walking to switch at (2, 12) ---")
    path_to_switch = []
    curr_x = pos['x']
    while curr_x > 2:
        curr_x -= 1
        path_to_switch.append(("Left", curr_x, 12))
        
    if not follow_path(path_to_switch):
        print("Failed to reach switch position.")
        mgba.take_screenshot()
        return
        
    # 2. Toggle switch at (2, 11) to State B
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
    
    # 3. Walk to balcony drop at (24, 14) in State B
    print("--- STEP 3: Walking to balcony drop on 3F (State B) ---")
    path_to_drop = [
        ("Right", 3, 12),
        ("Up", 3, 11),
        ("Up", 3, 10),
        ("Up", 3, 9),
        ("Up", 3, 8),
        ("Up", 3, 7),
        ("Up", 3, 6),
        ("Up", 3, 5),
        ("Up", 3, 4),
        ("Up", 3, 3),
        ("Right", 4, 3),
        ("Right", 5, 3),
        ("Right", 6, 3),
        ("Right", 7, 3),
        ("Right", 8, 3),
        ("Right", 9, 3),
        ("Right", 10, 3),
        ("Right", 11, 3),
        ("Right", 12, 3),
        ("Right", 13, 3),
        ("Right", 14, 3),
        ("Right", 15, 3),
        ("Right", 16, 3),
        ("Right", 17, 3),
        ("Right", 18, 3),
        ("Right", 19, 3),
        ("Right", 20, 3),
        ("Right", 21, 3),
        ("Down", 21, 4),
        ("Down", 21, 5), # Gate (21, 5) is OPEN in State B!
        ("Down", 21, 6),
        ("Down", 21, 7),
        ("Down", 21, 8),
        ("Down", 21, 9),
        ("Down", 21, 10),
        ("Down", 21, 11),
        ("Down", 21, 12),
        ("Down", 21, 13),
        ("Down", 21, 14),
        ("Right", 22, 14),
        ("Right", 23, 14),
        ("Right", 24, 14),
    ]
    if not follow_path(path_to_drop):
        print("Failed to reach balcony drop point.")
        mgba.take_screenshot()
        return
        
    print("At (24, 14). Dropping off balcony...")
    # Step Left to drop
    mgba.press_buttons(["Left"])
    time.sleep(3.0) # Wait for drop animation/warp
    
    landing_pos = mgba.get_coordinates()
    print("Landed! Current position:", landing_pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
