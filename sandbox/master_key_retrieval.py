import mgba
import time

def handle_battle():
    print("Encountered battle or text! Attempting to escape/dismiss...")
    mgba.press_buttons(["B", "sleep 300", "Down", "Right", "A", "sleep 1000", "B"])

def step_to(direction, tx, ty):
    pos = mgba.get_coordinates()
    print(f"Current pos: {pos}. Pressing {direction} to reach ({tx}, {ty})...")
    mgba.press_buttons([direction])
    time.sleep(0.4)
    new_pos = mgba.get_coordinates()
    
    if new_pos == pos:
        print("Did not move. Attempting to clear battle/text...")
        handle_battle()
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            print("Trying again...")
            mgba.press_buttons([direction])
            time.sleep(0.4)
            new_pos = mgba.get_coordinates()
            
    print(f"New pos: {new_pos}")
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

def run_master_route():
    # We are currently at (4, 13) on 3F (State B).
    pos = mgba.get_coordinates()
    print(f"Starting at: {pos}")
    if pos['x'] != 4 or pos['y'] != 13:
        print("Error: Not at (4, 13)!")
        return False
        
    # Walk to the balcony drop on 3F (State B)
    print("--- STEP 4: Walking to balcony drop on 3F (State B) ---")
    path_to_drop_3f = [
        ("Left", 3, 13),
        ("Up", 3, 12),
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
        ("Right", 22, 3),
        ("Right", 23, 3),
        ("Right", 24, 3),
        ("Right", 25, 3),
        ("Down", 25, 4),
        ("Down", 25, 5),
        ("Down", 25, 6),
        ("Down", 25, 7),
        ("Down", 25, 8),
        ("Down", 25, 9),
        ("Down", 25, 10),
        ("Down", 25, 11),
        ("Down", 25, 12),
        ("Down", 25, 13),
        ("Down", 25, 14),
        ("Left", 24, 14),
    ]
    if not follow_path(path_to_drop_3f):
        return False
        
    # Drop to 1F B1F stairs!
    print("--- STEP 5: Dropping to 1F B1F stairs ---")
    mgba.press_buttons(["Left"])
    time.sleep(1.5)
    
    pos = mgba.get_coordinates()
    print(f"Landed on 1F! Position: {pos}")
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    run_master_route()
