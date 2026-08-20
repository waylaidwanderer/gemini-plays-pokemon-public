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
    
    # 1. Walk from (10, 12) to Mansion entrance (6, 3) via Column 14 (Eastern Road next to ocean)
    if pos == {'x': 10, 'y': 12}:
        path_to_mansion = [
            ("Right", 11, 12), ("Right", 12, 12), ("Right", 13, 12), ("Right", 14, 12),
            ("Up", 14, 11), ("Up", 14, 10), ("Up", 14, 9), ("Up", 14, 8), ("Up", 14, 7), ("Up", 14, 6), ("Up", 14, 5), ("Up", 14, 4), ("Up", 14, 3),
            ("Left", 13, 3), ("Left", 12, 3), ("Left", 11, 3), ("Left", 10, 3), ("Left", 9, 3), ("Left", 8, 3), ("Left", 7, 3), ("Left", 6, 3),
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
    
    # 2. Path on 1F to stairs at (7, 10):
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
    
    # 3. Stairs from 2F to 3F are at (7, 10)
    if pos == {'x': 7, 'y': 11}:
        if not step_to("Up", 7, 10):
            return
    
    time.sleep(1.5)
    pos = mgba.get_coordinates()
    print("Inside Mansion 3F! Position:", pos)
    
    # 4. Walk to the west-side switch at (2, 11) on 3F (State A)
    if pos == {'x': 7, 'y': 11}:
        path_to_switch = [
            ("Left", 6, 11),
            ("Left", 5, 11),
            ("Left", 4, 11),
            ("Left", 3, 11),
            ("Left", 2, 11),
            ("Down", 2, 12),
        ]
        for d, tx, ty in path_to_switch:
            if not step_to(d, tx, ty):
                return
                
    pos = mgba.get_coordinates()
    print("Reached switch! Position:", pos)
    
    # 5. Face UP and press A to toggle switch at (2, 11)
    if pos == {'x': 2, 'y': 12}:
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        
        # Toggle switch to State B
        print("Toggling 3F switch to State B...")
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        mgba.press_buttons(["A"]) # YES
        time.sleep(1.0)
        mgba.press_buttons(["B"]) # Dismiss
        time.sleep(1.0)
        
    # 6. Walk to Balcony Drop at (20, 18) on 3F (State B)
    pos = mgba.get_coordinates()
    if pos == {'x': 2, 'y': 12}:
        print("Walking to the Balcony Drop...")
        path_to_balcony = [
            ("Right", 3, 12),
            ("Up", 3, 11), ("Up", 3, 10), ("Up", 3, 9), ("Up", 3, 8), ("Up", 3, 7), ("Up", 3, 6), ("Up", 3, 5), ("Up", 3, 4), ("Up", 3, 3),
            ("Right", 4, 3), ("Right", 5, 3), ("Right", 6, 3), ("Right", 7, 3), ("Right", 8, 3), ("Right", 9, 3), ("Right", 10, 3), ("Right", 11, 3), ("Right", 12, 3), ("Right", 13, 3), ("Right", 14, 3), ("Right", 15, 3), ("Right", 16, 3), ("Right", 17, 3), ("Right", 18, 3), ("Right", 19, 3), ("Right", 20, 3), ("Right", 21, 3),
            ("Down", 21, 4), ("Down", 21, 5), ("Down", 21, 6), ("Down", 21, 7), ("Down", 21, 8), ("Down", 21, 9), ("Down", 21, 10), ("Down", 21, 11), ("Down", 21, 12), ("Down", 21, 13), ("Down", 21, 14), ("Down", 21, 15),
            ("Left", 20, 15),
            ("Down", 20, 16), ("Down", 20, 17), ("Down", 20, 18),
        ]
        for d, tx, ty in path_to_balcony:
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
