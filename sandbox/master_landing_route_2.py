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
    print("Dismissing 'Got away safely!' text if any...")
    mgba.press_buttons(["B"])
    time.sleep(1.0)
    
    pos = mgba.get_coordinates()
    print("Current position after dismissing text:", pos)
    
    # We should be at (12, 12) or near it.
    if pos['y'] == 13:
        if not step_to("Up", pos['x'], 12):
            print("Failed to walk Up to row 12.")
            mgba.take_screenshot()
            return
            
    pos = mgba.get_coordinates()
    # Now walk Right along Row 12 to Column 24
    path_to_balcony = []
    curr_x = pos['x']
    while curr_x < 24:
        curr_x += 1
        path_to_balcony.append(("Right", curr_x, 12))
        
    path_to_balcony.append(("Down", 24, 13))
    path_to_balcony.append(("Down", 24, 14))
    
    print("Walking path to balcony drop at (24, 14)...")
    if not follow_path(path_to_balcony):
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
