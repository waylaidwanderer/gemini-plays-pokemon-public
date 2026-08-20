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
    # Start at (9, 12) on Cinnabar Island.
    # 1. Walk Right to column 19, then Up to row 3, then Left to column 6, then enter.
    print("--- STEP 1: Walking to Mansion via East Road Column 19 ---")
    island_path = [
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
        # Now walk Up column 19 as far as possible
        ("Up", 19, 11),
        ("Up", 19, 10),
        ("Up", 19, 9),
        ("Up", 19, 8),
        ("Up", 19, 7),
        ("Up", 19, 6),
        ("Up", 19, 5),
        ("Up", 19, 4),
        ("Up", 19, 3),
        # Walk Left to the Mansion door
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
        ("Up", 6, 2), # Enter Mansion door (should land inside at (5, 27) on 1F)
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
        ("Right", 6, 10),
    ]
    if not follow_path(path_to_stairs_1f):
        return False
        
    # Step Right to (7, 10) to warp to 2F
    print("Stepping onto 1F stairs...")
    mgba.press_buttons(["Right"])
    time.sleep(1.5)
    pos = mgba.get_coordinates()
    print(f"On Mansion 2F. Position: {pos}")
    
    # 3. On 2F, go to 3F via stairs at (7, 10)
    print("--- STEP 3: Ascending to 3F ---")
    if pos['x'] == 7 and pos['y'] == 11:
        print("Landed at (7, 11) on 2F. Stepping Up to warp to 3F...")
        if not step_to("Up", 7, 10):
            return False
    elif pos['x'] == 7 and pos['y'] == 10:
        print("Landed at (7, 10) on 2F. Stepping Down and back Up to warp to 3F...")
        if not step_to("Down", 7, 11):
            return False
        if not step_to("Up", 7, 10):
            return False
            
    time.sleep(1.5) # Wait for transition
    pos = mgba.get_coordinates()
    print(f"On Mansion 3F. Position: {pos}")
    
    # 4. On 3F (State A), walk to Mewtwo switch at (12, 11)
    print("--- STEP 4: Walking to 3F Switch ---")
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
    
    pos = mgba.get_coordinates()
    print(f"Position after switch toggle: {pos}")
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    run_master_route()
