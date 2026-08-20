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
    print("Starting final mansion victory route from (7, 11)...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Start position on 3F:", pos)
    
    # Path from (7, 11) to switch position (11, 11)
    path_to_switch = [
        ("Right", 8, 11),
        ("Right", 9, 11),
        ("Right", 10, 11), # OPEN in State A!
        ("Right", 11, 11),
    ]
    if not follow_path(path_to_switch):
        return False
        
    print("At (11, 11). Toggling switch at (12, 11) to State B...")
    mgba.press_buttons(["Right", "sleep 200", "A", "sleep 500", "A", "sleep 500", "B"])
    time.sleep(1.0)
    
    # Path to the balcony drop at (24, 14) via Row 5
    path_to_drop = [
        # Walk UP column 11 to Row 5
        ("Up", 11, 10),
        ("Up", 11, 9),
        ("Up", 11, 8),
        ("Up", 11, 7),
        ("Up", 11, 6),
        ("Up", 11, 5),
        # Walk RIGHT along Row 5 to Column 24
        ("Right", 12, 5),
        ("Right", 13, 5),
        ("Right", 14, 5),
        ("Right", 15, 5),
        ("Right", 16, 5),
        ("Right", 17, 5),
        ("Right", 18, 5),
        ("Right", 19, 5),
        ("Right", 20, 5),
        ("Right", 21, 5), # OPEN in State B!
        ("Right", 22, 5),
        ("Right", 23, 5),
        ("Right", 24, 5),
        # Walk DOWN column 24 to Row 14
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
