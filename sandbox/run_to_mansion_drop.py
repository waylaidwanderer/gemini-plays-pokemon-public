import mgba
import time

def handle_battle():
    print("Encountered battle or text! Attempting to escape/dismiss...")
    mgba.press_buttons(["B", "sleep 300", "Down", "sleep 100", "Right", "sleep 100", "A", "sleep 1000", "B"])

def step_to(direction, tx, ty):
    pos = mgba.get_coordinates()
    if pos['x'] == tx and pos['y'] == ty:
        return True
        
    print(f"Current pos: {pos}. Pressing {direction} to reach ({tx}, {ty})...")
    mgba.press_buttons([direction])
    time.sleep(0.4)
    new_pos = mgba.get_coordinates()
    
    attempts = 0
    while new_pos != {'x': tx, 'y': ty} and attempts < 10:
        if new_pos == pos:
            print("Did not move. Checking for battle or text...")
            handle_battle()
            time.sleep(0.5)
            mgba.press_buttons([direction])
            time.sleep(0.4)
            new_pos = mgba.get_coordinates()
        else:
            print(f"Unexpected position {new_pos}. Correcting...")
            pos = new_pos
            mgba.press_buttons([direction])
            time.sleep(0.4)
            new_pos = mgba.get_coordinates()
        attempts += 1
        
    return new_pos == {'x': tx, 'y': ty}

def follow_path(path):
    for d, tx, ty in path:
        if not step_to(d, tx, ty):
            print(f"Failed to move to ({tx}, {ty}).")
            mgba.take_screenshot()
            return False
    return True

def main():
    print("Starting automated run to Mansion B1F via State B balcony drop...")
    
    # 1. Path from our current position (19, 4) to Mansion Entrance (6, 3)
    path_to_mansion = [
        ("Left", 18, 4),
        ("Left", 17, 4),
        ("Left", 16, 4),
        ("Left", 15, 4),
        ("Left", 14, 4),
        ("Left", 13, 4),
        ("Left", 12, 4),
        ("Left", 11, 4),
        ("Left", 10, 4),
        ("Left", 9, 4),
        ("Left", 8, 4),
        ("Left", 7, 4),
        ("Left", 6, 4),
        ("Up", 6, 3), # Warp into Mansion 1F
    ]
    
    print("Walking to Pokémon Mansion entrance...")
    if not follow_path(path_to_mansion):
        return
        
    time.sleep(2.0) # Wait for Mansion 1F warp
    pos = mgba.get_coordinates()
    print("Inside Mansion 1F:", pos)
    
    # 2. Walk from 1F landing (5, 27) to 1F stairs (7, 10)
    path_to_1f_stairs = [
        ("Up", 5, 26),
        ("Up", 5, 25),
        ("Up", 5, 24),
        ("Up", 5, 23),
        ("Up", 5, 22),
        ("Up", 5, 21),
        ("Up", 5, 20),
        ("Up", 5, 19),
        ("Up", 5, 18),
        ("Up", 5, 17),
        ("Up", 5, 16),
        ("Up", 5, 15),
        ("Up", 5, 14),
        ("Up", 5, 13),
        ("Up", 5, 12),
        ("Up", 5, 11),
        ("Right", 6, 11),
        ("Right", 7, 11),
        ("Up", 7, 10), # Warp to 2F
    ]
    
    print("Walking to Mansion 2F stairs...")
    if not follow_path(path_to_1f_stairs):
        return
        
    time.sleep(2.0) # Wait for 2F warp
    pos = mgba.get_coordinates()
    print("Inside Mansion 2F:", pos)
    
    # 3. Walk from 2F landing (7, 11) to 3F stairs (7, 10)
    # Since we are already in State A, we can go directly to 3F!
    path_to_2f_stairs = [
        ("Up", 7, 10), # Warp to 3F
    ]
    
    print("Walking to Mansion 3F stairs...")
    if not follow_path(path_to_2f_stairs):
        return
        
    time.sleep(2.0) # Wait for 3F warp
    pos = mgba.get_coordinates()
    print("Inside Mansion 3F:", pos)
    
    # 4. On 3F (State A), walk to switch at (12, 11)
    path_to_3f_switch = [
        ("Right", 8, 11),
        ("Right", 9, 11),
        ("Down", 9, 12),
        ("Right", 10, 12),
        ("Right", 11, 12),
        ("Up", 11, 11),
    ]
    
    print("Walking to 3F switch...")
    if not follow_path(path_to_3f_switch):
        return
        
    print("Toggling 3F switch to State B...")
    # Face Right and press A
    mgba.press_buttons(["Right", "sleep 200", "A", "sleep 500", "A", "sleep 500", "B"])
    time.sleep(2.0)
    
    # 5. On 3F (State B), walk to the balcony drop at (24, 14) via Row 5
    path_to_balcony = [
        ("Up", 11, 10),
        ("Up", 11, 9),
        ("Up", 11, 8),
        ("Up", 11, 7),
        ("Up", 11, 6),
        ("Up", 11, 5),
        ("Right", 12, 5),
        ("Right", 13, 5),
        ("Right", 14, 5),
        ("Right", 15, 5),
        ("Right", 16, 5),
        ("Right", 17, 5),
        ("Right", 18, 5),
        ("Right", 19, 5),
        ("Right", 20, 5),
        ("Right", 21, 5), # Gate is OPEN in State B!
        ("Right", 22, 5),
        ("Right", 23, 5),
        ("Right", 24, 5),
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
    
    print("Walking to 3F balcony drop...")
    if not follow_path(path_to_balcony):
        return
        
    print("Dropping off the balcony...")
    mgba.press_buttons(["Left"])
    time.sleep(3.0) # Wait for drop animation/warp
    
    pos = mgba.get_coordinates()
    print("Landed! Coordinates:", pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
