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
    # We are currently at (13, 12) on 2F (State B).
    pos = mgba.get_coordinates()
    print(f"Starting at: {pos}")
    if pos['x'] != 13 or pos['y'] != 12:
        print("Error: Not at (13, 12)!")
        return False
        
    # 1. On 2F (State B), walk to (18, 8) stairs via Row 5 (Northeast Gate is OPEN!)
    print("--- STEP 1: Walking to 3F stairs on 2F (State B) ---")
    path_to_stairs_2f = [
        ("Left", 12, 12),
        ("Left", 11, 12),
        ("Up", 11, 11),
        ("Up", 11, 10),
        ("Up", 11, 9),
        ("Up", 11, 8),
        ("Up", 11, 7),
        ("Up", 11, 6),
        ("Up", 11, 5),
        ("Right", 12, 5),
        ("Right", 13, 5),
        ("Right", 14, 5),
        ("Right", 15, 5), # Northeast Gate OPEN in State B!
        ("Right", 16, 5),
        ("Right", 17, 5),
        ("Right", 18, 5),
        ("Down", 18, 6),
        ("Down", 18, 7),
    ]
    if not follow_path(path_to_stairs_2f):
        return False
        
    # Step Down onto (18, 8) stairs to warp to 3F
    print("Stepping onto 2F stairs...")
    mgba.press_buttons(["Down"])
    time.sleep(1.5)
    pos = mgba.get_coordinates()
    print(f"On Mansion 3F. Position: {pos}")
    
    # 2. On 3F (State B), walk to the balcony drop at (24, 14)
    print("--- STEP 2: Walking to balcony drop on 3F (State B) ---")
    path_to_drop_3f = [
        ("Up", 18, 7),
        ("Up", 18, 6),
        ("Up", 18, 5),
        ("Up", 18, 4),
        ("Up", 18, 3),
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
    print("--- STEP 3: Dropping to 1F B1F stairs ---")
    mgba.press_buttons(["Left"])
    time.sleep(1.5)
    
    pos = mgba.get_coordinates()
    print(f"Landed on 1F! Position: {pos}")
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    run_master_route()
