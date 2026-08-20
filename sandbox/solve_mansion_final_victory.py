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
    
    # We are at (21, 6) on 3F inside Mansion in State A.
    # 1. Walk from (21, 6) to (11, 11) to access the switch at (12, 11)
    if pos == {'x': 21, 'y': 6}:
        path_to_switch = [
            ("Left", 20, 6), ("Left", 19, 6), ("Left", 18, 6), ("Left", 17, 6), ("Left", 16, 6), ("Left", 15, 6), ("Left", 14, 6), ("Left", 13, 6), ("Left", 12, 6),
            ("Down", 12, 7), ("Down", 12, 8), ("Down", 12, 9), ("Down", 12, 10),
            ("Left", 11, 10),
            ("Down", 11, 11),
        ]
        for d, tx, ty in path_to_switch:
            if not step_to(d, tx, ty):
                return
                
    pos = mgba.get_coordinates()
    print("At switch landing! Position:", pos)
    
    # 2. Face RIGHT and press A to toggle switch at (12, 11)
    if pos == {'x': 11, 'y': 11}:
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
        
    # 3. Walk to the Pit at (25, 6) in State B
    pos = mgba.get_coordinates()
    if pos == {'x': 11, 'y': 11}:
        print("Walking to the Pit...")
        path_to_pit = [
            ("Up", 11, 10),
            ("Right", 12, 10),
            ("Up", 12, 9), ("Up", 12, 8), ("Up", 12, 7), ("Up", 12, 6),
            ("Right", 13, 6), ("Right", 14, 6), ("Right", 15, 6), ("Right", 16, 6), ("Right", 17, 6), ("Right", 18, 6), ("Right", 19, 6), ("Right", 20, 6), ("Right", 21, 6),
            ("Up", 21, 5), ("Up", 21, 4), ("Up", 21, 3), # Gate at (21, 5) is OPEN in State B!
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
    
    # 4. Walk to B1F stairs on 1F
    if pos['y'] > 15:
        print("Walking onto B1F stairs...")
        for _ in range(5):
            mgba.press_buttons(["Up"])
            time.sleep(0.5)
            
        pos = mgba.get_coordinates()
        print("Final position on B1F:", pos)
        mgba.take_screenshot()

if __name__ == "__main__":
    main()
