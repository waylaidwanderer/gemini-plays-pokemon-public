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
    if pos['x'] == tx and pos['y'] == ty:
        return True
        
    print(f"At {pos}. Moving {direction} to ({tx}, {ty})...")
    mgba.press_buttons([direction])
    time.sleep(0.6) # Safe delay for perfect GBC emulation on bike
    new_pos = mgba.get_coordinates()
    
    attempts = 0
    while new_pos != {'x': tx, 'y': ty} and attempts < 2:
        if new_pos == pos:
            # If we didn't move, it might be turning in place. Let's press the button again once!
            print("Did not move. Retrying direction once...")
            mgba.press_buttons([direction])
            time.sleep(0.6)
            new_pos = mgba.get_coordinates()
            
            # If still didn't move, we are blocked by a wall or battle. 
            # If so, do NOT run blind escape macro. Just return False to let us handle it!
            if new_pos == pos:
                print(f"Blocked! Cannot move {direction} to ({tx}, {ty}) from {pos}.")
                return False
        else:
            print(f"Unexpected pos {new_pos}. Correcting...")
            pos = new_pos
            mgba.press_buttons([direction])
            time.sleep(0.6)
            new_pos = mgba.get_coordinates()
        attempts += 1
        
    return new_pos == {'x': tx, 'y': ty}

def main():
    pos = mgba.get_coordinates()
    print("Starting at:", pos)
    
    # 1. Exit the Lab from (3, 3)
    # Path: Down to (3, 7) -> Down to warp outside to (6, 10)
    if pos['y'] < 7 and pos['x'] == 3:
        path_exit_lab = [
            ("Down", 3, 4),
            ("Down", 3, 5),
            ("Down", 3, 6),
            ("Down", 3, 7),
        ]
        for d, tx, ty in path_exit_lab:
            if not step_to(d, tx, ty):
                return
        
        # Warp outside by pressing Down at (3, 7)
        print("Pressing Down at (3, 7) to warp outside...")
        mgba.press_buttons(["Down"])
        time.sleep(2.0)
        
    time.sleep(1.0)
    pos = mgba.get_coordinates()
    print("Outside Lab! Position:", pos)
    
    # 2. Walk to Mansion entrance (6, 3) via Eastern Road (Column 11)
    if pos == {'x': 6, 'y': 10}:
        path_to_mansion = [
            ("Down", 6, 11),
            ("Right", 7, 11), ("Right", 8, 11), ("Right", 9, 11), ("Right", 10, 11), ("Right", 11, 11),
            ("Up", 11, 10), ("Up", 11, 9), ("Up", 11, 8), ("Up", 11, 7), ("Up", 11, 6), ("Up", 11, 5), ("Up", 11, 4), ("Up", 11, 3),
            ("Left", 10, 3), ("Left", 9, 3), ("Left", 8, 3), ("Left", 7, 3), ("Left", 6, 3),
        ]
        for d, tx, ty in path_to_mansion:
            if not step_to(d, tx, ty):
                return
                
    # Step UP to enter Mansion
    pos = mgba.get_coordinates()
    if pos == {'x': 6, 'y': 3}:
        print("Entering Mansion...")
        mgba.press_buttons(["Up"])
        time.sleep(2.5)
        
    pos = mgba.get_coordinates()
    print("Inside Mansion 1F! Position:", pos)
    
    # 3. Path on 1F to stairs at (7, 10):
    if pos['y'] > 20 and pos['x'] == 5:
        path_1f = [
            ("Up", 5, 26), ("Up", 5, 25), ("Up", 5, 24), ("Up", 5, 23), ("Up", 5, 22),
            ("Right", 6, 22), ("Right", 7, 22),
            ("Up", 7, 21), ("Up", 7, 20), ("Up", 7, 19), ("Up", 7, 18), ("Up", 7, 17),
            ("Up", 7, 16), ("Up", 7, 15), ("Up", 7, 14), ("Up", 7, 13), ("Up", 7, 12),
            ("Up", 7, 11), ("Up", 7, 10), # Stairs to 2F
        ]
        for d, tx, ty in path_1f:
            if not step_to(d, tx, ty):
                return
                
    time.sleep(1.5)
    pos = mgba.get_coordinates()
    print("Inside Mansion 2F! Position:", pos)
    
    # 4. Stairs from 2F to 3F are at (7, 10)
    if pos == {'x': 7, 'y': 11}:
        if not step_to("Up", 7, 10):
            return
    
    time.sleep(1.5)
    pos = mgba.get_coordinates()
    print("Inside Mansion 3F! Position:", pos)
    
    # 5. Walk straight to (11, 11) on 3F
    if pos == {'x': 7, 'y': 11}:
        path_3f = [
            ("Right", 8, 11),
            ("Right", 9, 11),
            ("Right", 10, 11), # Gate at (10, 11) is OPEN in State A
            ("Right", 11, 11),
        ]
        for d, tx, ty in path_3f:
            if not step_to(d, tx, ty):
                return
                
    pos = mgba.get_coordinates()
    print("Reached switch landing! Position:", pos)
    
    # 6. Face Right to look at (12, 11)
    if pos == {'x': 11, 'y': 11}:
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
        
        # Toggle switch to State B
        print("Toggling switch to State B...")
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        mgba.press_buttons(["A"]) # YES
        time.sleep(1.0)
        mgba.press_buttons(["B"]) # Dismiss
        time.sleep(1.0)
    
    # 7. Walk to Pit on 3F (State B)
    pos = mgba.get_coordinates()
    if pos == {'x': 11, 'y': 11}:
        print("Walking to the Pit...")
        path_to_pit = [
            ("Up", 11, 10),
            ("Right", 12, 10),
            ("Up", 12, 9), ("Up", 12, 8), ("Up", 12, 7), ("Up", 12, 6), ("Up", 12, 5),
            ("Right", 13, 5), ("Right", 14, 5), ("Right", 15, 5), ("Right", 16, 5), ("Right", 17, 5),
            ("Right", 18, 5), ("Right", 19, 5), ("Right", 20, 5), ("Right", 21, 5), # Gate (21, 5) is OPEN in State B!
            ("Up", 21, 4), ("Up", 21, 3),
            ("Right", 22, 3), ("Right", 23, 3), ("Right", 24, 3), ("Right", 25, 3), ("Right", 26, 3),
            ("Down", 26, 4), ("Down", 26, 5), ("Down", 26, 6),
        ]
        for d, tx, ty in path_to_pit:
            if not step_to(d, tx, ty):
                return
                
        print("At (26, 6). Stepping Left onto the pit at (25, 6)...")
        mgba.press_buttons(["Left"])
        time.sleep(3.0) # Wait for falling animation
        
    pos = mgba.get_coordinates()
    print("Landed on 1F! Position:", pos)
    mgba.take_screenshot()
    
    # 8. Walk to B1F stairs on 1F (usually walking UP from landing area)
    if pos['x'] == 25 and pos['y'] == 6:
        print("Walking onto B1F stairs...")
        for _ in range(5):
            mgba.press_buttons(["Up"])
            time.sleep(0.5)
            
        pos = mgba.get_coordinates()
        print("Final position on B1F:", pos)
        mgba.take_screenshot()

if __name__ == "__main__":
    main()
