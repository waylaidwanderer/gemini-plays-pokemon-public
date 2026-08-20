import mgba
import time

def handle_battle():
    print("Encountered battle or text! Escaping...")
    # Advance any initial text
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    # Move to RUN and press A
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
    print("Starting final mansion victory route from (26, 5)...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Start position:", pos)
    
    # Complete path from (26, 5) to the switch at (11, 11) via Row 3
    path_to_switch = [
        # 1. Walk UP column 26 to Row 3
        ("Up", 26, 4),
        ("Up", 26, 3),
        # 2. Walk LEFT along Row 3 to Column 11
        ("Left", 25, 3),
        ("Left", 24, 3),
        ("Left", 23, 3),
        ("Left", 22, 3),
        ("Left", 21, 3),
        ("Left", 20, 3),
        ("Left", 19, 3),
        ("Left", 18, 3),
        ("Left", 17, 3),
        ("Left", 16, 3),
        ("Left", 15, 3),
        ("Left", 14, 3),
        ("Left", 13, 3),
        ("Left", 12, 3),
        ("Left", 11, 3),
        # 3. Walk DOWN column 11 to Row 11
        ("Down", 11, 4),
        ("Down", 11, 5),
        ("Down", 11, 6),
        ("Down", 11, 7),
        ("Down", 11, 8),
        ("Down", 11, 9),
        ("Down", 11, 10),
        ("Down", 11, 11),
    ]
    
    if not follow_path(path_to_switch):
        return False
        
    # Toggle switch to State B
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
        
    # Step Left to drop to 1F B1F stairs
    print("At (24, 14). Dropping off balcony...")
    mgba.press_buttons(["Left"])
    time.sleep(3.0) # wait for fall transition
    
    final_pos = mgba.get_coordinates()
    print("Landing position on 1F:", final_pos)
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    run_main()
