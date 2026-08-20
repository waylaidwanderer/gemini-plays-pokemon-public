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
    # We are currently at (21, 4) on 3F (State A).
    pos = mgba.get_coordinates()
    print(f"Starting at: {pos}")
    if pos['x'] != 21 or pos['y'] != 4:
        print("Error: Not at (21, 4)!")
        return False
        
    # 1. Walk back to the switch at (2, 11) on 3F to toggle back to State B!
    print("--- STEP 1: Walking back to 3F switch at (2, 11) ---")
    path_to_switch = [
        ("Up", 21, 3),
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
        ("Left", 10, 3),
        ("Left", 9, 3),
        ("Left", 8, 3),
        ("Left", 7, 3),
        ("Left", 6, 3),
        ("Left", 5, 3),
        ("Left", 4, 3),
        ("Left", 3, 3),
        ("Down", 3, 4),
        ("Down", 3, 5),
        ("Down", 3, 6),
        ("Down", 3, 7),
        ("Down", 3, 8),
        ("Down", 3, 9),
        ("Down", 3, 10),
        ("Down", 3, 11),
        ("Down", 3, 12),
        ("Left", 2, 12),
    ]
    if not follow_path(path_to_switch):
        return False
        
    # Toggle switch to State B
    print("Toggling 3F switch to State B...")
    mgba.press_buttons(["Up", "sleep 200", "A", "sleep 500", "A", "sleep 500", "B"])
    print("Switch toggled!")
    
    # 2. Walk to the balcony drop on 3F (State B)
    print("--- STEP 2: Walking to balcony drop on 3F (State B) ---")
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
