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
    print("Starting final victory balcony drop route in State B from (9, 11)...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Start position:", pos)
    
    # Path from (9, 11) to the drop at (24, 14) via Row 3 and Row 5 (since we are already in State B)
    path = [
        # 1. Walk Left to Column 6
        ("Left", 8, 11),
        ("Left", 7, 11),
        ("Left", 6, 11),
        # 2. Walk UP column 6 to Row 3
        ("Up", 6, 10),
        ("Up", 6, 9),
        ("Up", 6, 8),
        ("Up", 6, 7),
        ("Up", 6, 6),
        ("Up", 6, 5),
        ("Up", 6, 4),
        ("Up", 6, 3),
        # 3. Walk RIGHT along Row 3 to Column 26
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
        # 4. Walk DOWN column 26 to Row 5
        ("Down", 26, 4),
        ("Down", 26, 5),
        # 5. Walk LEFT along Row 5 to Column 24
        ("Left", 25, 5),
        ("Left", 24, 5),
        # 6. Walk DOWN column 24 to the drop at (24, 14)
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
    
    if not follow_path(path):
        return False
        
    print("At (24, 14). Dropping off balcony...")
    mgba.press_buttons(["Left"])
    time.sleep(3.0) # wait for warp/drop
    
    final_pos = mgba.get_coordinates()
    print("Landing position on 1F:", final_pos)
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    run_main()
