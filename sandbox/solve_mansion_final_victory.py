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
    
    # We are at (7, 11) on 3F inside Mansion in State B.
    # Let's walk to the pit at (25, 6)!
    if pos == {'x': 7, 'y': 11}:
        path_to_pit = [
            ("Up", 7, 10),
            ("Right", 8, 10), ("Right", 9, 10), ("Right", 10, 10),
            ("Up", 10, 9), ("Up", 10, 8), ("Up", 10, 7), ("Up", 10, 6), ("Up", 10, 5),
            ("Right", 11, 5), ("Right", 12, 5),
            ("Right", 13, 5), ("Right", 14, 5), ("Right", 15, 5), ("Right", 16, 5), ("Right", 17, 5), ("Right", 18, 5), ("Right", 19, 5), ("Right", 20, 5), ("Right", 21, 5), # Gate (21, 5) is OPEN in State B!
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
    
    # Walk to B1F stairs on 1F (usually walking UP from landing area)
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
