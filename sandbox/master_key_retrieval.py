import mgba
import time

def handle_battle():
    # If we are in a battle, we need to run.
    # We can check if a battle is active by pressing B or looking at coordinates,
    # but the simplest way is to try running a run sequence: Down, Right, A.
    print("Encountered battle or text! Attempting to escape/dismiss...")
    mgba.press_buttons(["B", "sleep 500", "Down", "Right", "A", "sleep 1000", "B"])

def step_to(direction, tx, ty):
    pos = mgba.get_coordinates()
    print(f"Current pos: {pos}. Pressing {direction} to reach ({tx}, {ty})...")
    mgba.press_buttons([direction])
    time.sleep(0.4)
    new_pos = mgba.get_coordinates()
    
    # If we didn't move, it could be a battle or text or wall.
    if new_pos == pos:
        print("Did not move. Attempting to clear battle/text...")
        handle_battle()
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            # Try pressing button again
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
    # We start at (11, 12) on Cinnabar Island.
    # 1. Walk to Mansion entrance at (6, 3) and enter.
    print("--- STEP 1: Entering Mansion ---")
    island_path = [
        ("Up", 11, 11),
        ("Up", 11, 10),
        ("Up", 11, 9),
        ("Up", 11, 8),
        ("Up", 11, 7),
        ("Up", 11, 6),
        ("Up", 11, 5),
        ("Up", 11, 4),
        ("Up", 11, 3),
        ("Left", 10, 3),
        ("Left", 9, 3),
        ("Left", 8, 3),
        ("Left", 7, 3),
        ("Left", 6, 3),
        ("Up", 6, 2), # Enter door (should land inside at (5, 27) on 1F)
    ]
    if not follow_path(island_path):
        return False
        
    time.sleep(1.5) # Wait for transition
    pos = mgba.get_coordinates()
    print(f"Inside Mansion 1F. Position: {pos}")
    if pos['x'] != 5 or pos['y'] != 27:
        print("Error: Not at Mansion 1F entrance!")
        mgba.take_screenshot()
        return False
        
    # 2. On 1F, walk to stairs at (7, 10)
    print("--- STEP 2: Walking to 2F stairs on 1F ---")
    path_to_stairs_1f = [
        ("Up", 5, 26), ("Up", 5, 25), ("Up", 5, 24), ("Up", 5, 23), ("Up", 5, 22),
        ("Up", 5, 21), ("Up", 5, 20), ("Up", 5, 19), ("Up", 5, 18), ("Up", 5, 17),
        ("Up", 5, 16), ("Up", 5, 15), ("Up", 5, 14), ("Up", 5, 13), ("Up", 5, 12),
        ("Up", 5, 11), ("Up", 5, 10),
        ("Right", 6, 10), ("Right", 7, 10),
        ("Up", 7, 9), # Step onto stairs to warp to 2F (should land at (7, 11) on 2F)
    ]
    if not follow_path(path_to_stairs_1f):
        return False
        
    time.sleep(1.5) # Wait for transition
    pos = mgba.get_coordinates()
    print(f"On Mansion 2F. Position: {pos}")
    
    # 3. On 2F, go to 3F via stairs at (7, 10)
    print("--- STEP 3: Ascending to 3F ---")
    # Landed at (7, 11). Just step Up onto the stairs at (7, 10).
    path_to_stairs_2f = [
        ("Up", 7, 10), # Step onto stairs to warp to 3F (should land at (7, 11) on 3F)
    ]
    if not follow_path(path_to_stairs_2f):
        return False
        
    time.sleep(1.5) # Wait for transition
    pos = mgba.get_coordinates()
    print(f"On Mansion 3F. Position: {pos}")
    
    # 4. On 3F, walk to Mewtwo switch at (12, 11)
    print("--- STEP 4: Walking to 3F Switch ---")
    # Landed at (7, 11)
    path_to_switch_3f = [
        ("Right", 8, 11),
        ("Right", 9, 11),
        ("Down", 9, 12),
        ("Right", 10, 12),
        ("Right", 11, 12),
        ("Up", 11, 11),
    ]
    if not follow_path(path_to_switch_3f):
        return False
        
    # Face Right and press A to toggle switch to State B
    print("Toggling 3F switch to State B...")
    mgba.press_buttons(["Right", "sleep 200", "A", "sleep 500", "B"])
    print("Switch toggled!")
    
    # Take screenshot to verify we are there
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    run_master_route()
