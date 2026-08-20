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
    time.sleep(0.6) # Safe delay for GBC emulation on bike
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
    
    # 1. Walk to the west-side switch at (1, 11) from our current position on 3F
    if pos == {'x': 1, 'y': 12}:
        path_to_switch = [
            ("Up", 1, 11),
        ]
        for d, tx, ty in path_to_switch:
            if not step_to(d, tx, ty):
                return
    elif pos == {'x': 1, 'y': 13}:
        path_to_switch = [
            ("Up", 1, 12),
            ("Up", 1, 11),
        ]
        for d, tx, ty in path_to_switch:
            if not step_to(d, tx, ty):
                return
                
    pos = mgba.get_coordinates()
    print("Reached switch landing! Position:", pos)
    
    # 2. Face RIGHT and press A to toggle switch at (2, 11)
    if pos == {'x': 1, 'y': 11}:
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
        
        # Toggle switch to State B
        print("Toggling 3F switch to State B...")
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        mgba.press_buttons(["A"]) # YES
        time.sleep(1.0)
        mgba.press_buttons(["B"]) # Dismiss
        time.sleep(1.0)
        
    # 3. Walk to Balcony Drop at (20, 18) on 3F (State B)
    pos = mgba.get_coordinates()
    if pos == {'x': 1, 'y': 11} or pos == {'x': 4, 'y': 10}:
        print("Walking to the Balcony Drop...")
        path_to_balcony = [
            ("Down", 4, 11), ("Down", 4, 12), ("Down", 4, 13),
            ("Right", 5, 13),
            ("Up", 5, 12), ("Up", 5, 11), ("Up", 5, 10), ("Up", 5, 9), ("Up", 5, 8), ("Up", 5, 7), ("Up", 5, 6), ("Up", 5, 5), ("Up", 5, 4), ("Up", 5, 3),
            ("Right", 6, 3), ("Right", 7, 3), ("Right", 8, 3), ("Right", 9, 3), ("Right", 10, 3), ("Right", 11, 3), ("Right", 12, 3), ("Right", 13, 3), ("Right", 14, 3), ("Right", 15, 3), ("Right", 16, 3), ("Right", 17, 3), ("Right", 18, 3), ("Right", 19, 3), ("Right", 20, 3), ("Right", 21, 3),
            ("Down", 21, 4), ("Down", 21, 5), ("Down", 21, 6), ("Down", 21, 7), ("Down", 21, 8), ("Down", 21, 9), ("Down", 21, 10), ("Down", 21, 11), ("Down", 21, 12), ("Down", 21, 13), ("Down", 21, 14), ("Down", 21, 15),
            ("Left", 20, 15),
            ("Down", 20, 16), ("Down", 20, 17), ("Down", 20, 18),
        ]
        # If we are starting from (4, 10), we only need the steps after (4, 10)
        actual_path = []
        skip = (pos == {'x': 4, 'y': 10})
        for d, tx, ty in path_to_balcony:
            if skip:
                if tx == 4 and ty == 10:
                    skip = False
                actual_path.append((d, tx, ty))
            else:
                actual_path.append((d, tx, ty))
                
        # Wait, if we start at (1, 11), we need the full path, but with a different start
        if pos == {'x': 1, 'y': 11}:
            full_path = [
                ("Down", 1, 12),
                ("Down", 1, 13),
                ("Right", 2, 13), ("Right", 3, 13), ("Right", 4, 13),
            ] + path_to_balcony
            actual_path = full_path
            
        for d, tx, ty in actual_path:
            if not step_to(d, tx, ty):
                return
                
        print("At (20, 18). Dropping from balcony...")
        mgba.press_buttons(["Left"])
        time.sleep(3.0) # Wait for falling animation
        
    pos = mgba.get_coordinates()
    print("Landed on B1F! Current position:", pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
