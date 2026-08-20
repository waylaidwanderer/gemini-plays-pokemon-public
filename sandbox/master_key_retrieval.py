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
    # We are currently at (22, 7) on 3F (State B).
    pos = mgba.get_coordinates()
    print(f"Starting at: {pos}")
    if pos['x'] != 22 or pos['y'] != 7:
        print("Error: Not at (22, 7)!")
        return False
        
    # Walk around the partition walls and rubble to reach the balcony drop on 3F
    print("--- STEP 1: Walking to balcony drop on 3F (State B) ---")
    path_to_drop_3f = [
        ("Left", 21, 7),
        ("Left", 20, 7),
        ("Left", 19, 7),
        ("Left", 18, 7),
        ("Up", 18, 6),
        ("Up", 18, 5),
        ("Up", 18, 4), # Row 4 is open across columns 18-21
        ("Right", 19, 4),
        ("Right", 20, 4),
        ("Right", 21, 4),
        ("Up", 21, 3), # Row 3 is open across columns 20-25
        ("Right", 22, 3),
        ("Right", 23, 3),
        ("Right", 24, 3),
        ("Right", 25, 3),
        ("Down", 25, 4),
        ("Down", 25, 5),
        ("Down", 25, 6),
        ("Down", 25, 7),
        ("Down", 25, 8), # Passable railing
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
    print("--- STEP 2: Dropping to 1F B1F stairs ---")
    mgba.press_buttons(["Left"])
    time.sleep(1.5)
    
    pos = mgba.get_coordinates()
    print(f"Landed on 1F! Position: {pos}")
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    run_master_route()
