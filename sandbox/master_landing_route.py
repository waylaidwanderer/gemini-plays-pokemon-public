import mgba
import time

def handle_battle():
    print("Encountered battle or text! Escaping...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(2.0)
    mgba.press_buttons(["B"])
    time.sleep(0.5)

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
    print("Starting master landing route to B1F...")
    pos = mgba.get_coordinates()
    print("Current position:", pos)
    
    # We are currently at (1, 13) on 3F. Let's walk to the switch.
    # From (1, 13) to (1, 11):
    path_to_switch = [
        ("Up", 1, 12),
        ("Up", 1, 11),
    ]
    if not follow_path(path_to_switch):
        print("Failed to reach switch area.")
        mgba.take_screenshot()
        return

    print("Facing Right to toggle switch...")
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    
    # Interact with the Mewtwo statue switch to toggle to State A (Default)
    print("Toggling switch to State A...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"]) # YES
    time.sleep(1.0)
    mgba.press_buttons(["B"]) # Close dialogue
    time.sleep(1.0)
    
    # Walk to the balcony drop at (24, 14) on 3F in State A
    print("Walking to the balcony drop at (24, 14)...")
    path_to_balcony = [
        ("Down", 1, 12),
        ("Down", 1, 13),
        ("Right", 2, 13),
        ("Right", 3, 13),
        ("Right", 4, 13),
        ("Up", 4, 12),
        ("Up", 4, 11),
        ("Up", 4, 10),
        ("Right", 5, 10),
        ("Right", 6, 10),
        ("Right", 7, 10),
        ("Down", 7, 11),
        ("Down", 7, 12),
        ("Right", 8, 12),
        ("Right", 9, 12),
        ("Right", 10, 12),
        ("Right", 11, 12),
        ("Right", 12, 12),
        ("Right", 13, 12),
        ("Right", 14, 12),
        ("Right", 15, 12),
        ("Right", 16, 12),
        ("Right", 17, 12),
        ("Right", 18, 12),
        ("Right", 19, 12),
        ("Right", 20, 12),
        ("Right", 21, 12),
        ("Right", 22, 12),
        ("Right", 23, 12),
        ("Right", 24, 12),
        ("Down", 24, 13), # Gate is OPEN in State A!
        ("Down", 24, 14),
    ]
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
