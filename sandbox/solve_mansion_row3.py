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
    print(f"At {pos}. Moving {direction} to ({tx}, {ty})...")
    mgba.press_buttons([direction])
    time.sleep(0.4)
    new_pos = mgba.get_coordinates()
    
    if new_pos == pos:
        print("Did not move. Attempting to escape battle or clear text...")
        handle_battle()
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            print("Retrying movement step...")
            mgba.press_buttons([direction])
            time.sleep(0.4)
            new_pos = mgba.get_coordinates()
            
    return new_pos['x'] == tx and new_pos['y'] == ty

def follow_path(path):
    for d, tx, ty in path:
        attempts = 0
        while not step_to(d, tx, ty):
            attempts += 1
            if attempts > 5:
                print(f"Failed to move to ({tx}, {ty}) after 5 attempts.")
                mgba.take_screenshot()
                return False
    return True

def run_main():
    print("Navigating from (12, 11) to west switch at (2, 12)...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # Path to (2, 12)
    path_to_switch = [
        ("Left", 11, 11),
        ("Left", 10, 11), # OPEN in State A!
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
    if not follow_path(path_to_switch):
        return False
        
    print("At (2, 12). Toggling switch at (2, 11) to State B...")
    mgba.press_buttons(["Up", "sleep 200", "A", "sleep 500", "A", "sleep 500", "B"])
    time.sleep(1.0)
    
    # Path back to Row 3 and then across to Column 26
    path_back_to_row3 = [
        ("Down", 2, 13),
        ("Right", 3, 13),
        ("Up", 3, 12),
        ("Up", 3, 11),
        ("Up", 3, 10),
        ("Up", 3, 9),
        ("Up", 3, 8),
        ("Up", 3, 7),
        ("Up", 3, 6),
        ("Up", 3, 5),
        ("Up", 3, 4),
        ("Up", 3, 3), # Row 3
        # Walk RIGHT along Row 3 to Column 26
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
        ("Right", 22, 3),
        ("Right", 23, 3),
        ("Right", 24, 3),
        ("Right", 25, 3),
        ("Right", 26, 3),
    ]
    if not follow_path(path_back_to_row3):
        return False
        
    # Walk DOWN column 26 to row 5, then left to row 5, then down column 24 to the drop at (24, 14)
    path_to_drop = [
        ("Down", 26, 4),
        ("Down", 26, 5),
        ("Left", 25, 5),
        ("Left", 24, 5),
        # Walk DOWN column 24 to the drop at (24, 14)
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
    if not follow_path(path_to_drop):
        return False
        
    print("At (24, 14). Dropping off balcony...")
    mgba.press_buttons(["Left"])
    time.sleep(3.0) # Wait for fall transition
    
    final_pos = mgba.get_coordinates()
    print("Landing position on 1F:", final_pos)
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    run_main()
