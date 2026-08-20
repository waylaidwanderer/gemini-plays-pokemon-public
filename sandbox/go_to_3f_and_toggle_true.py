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
    time.sleep(0.5)
    new_pos = mgba.get_coordinates()
    
    attempts = 0
    while new_pos != {'x': tx, 'y': ty} and attempts < 3:
        if new_pos == pos:
            print("Did not move. Retrying...")
            mgba.press_buttons([direction])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                print("Checking for battle...")
                handle_battle()
                time.sleep(0.5)
                mgba.press_buttons([direction])
                time.sleep(0.5)
                new_pos = mgba.get_coordinates()
        else:
            print(f"Unexpected pos {new_pos}. Correcting...")
            pos = new_pos
            mgba.press_buttons([direction])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
        attempts += 1
        
    return new_pos == {'x': tx, 'y': ty}

def main():
    pos = mgba.get_coordinates()
    print("Starting at:", pos)
    
    # 1. Walk from (5, 7) to Mansion entrance (6, 3) avoiding the Lab door
    path_to_mansion = [
        ("Up", 5, 6),
        ("Up", 5, 5),
        ("Up", 5, 4),
        ("Up", 5, 3),
        ("Right", 6, 3), # Mansion entrance
    ]
    
    for d, tx, ty in path_to_mansion:
        step_to(d, tx, ty)
        
    print("Entering Mansion...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    
    pos = mgba.get_coordinates()
    print("Inside Mansion 1F! Position:", pos)
    
    # 2. Path on 1F to stairs at (7, 10):
    path_1f = [
        ("Up", 5, 26), ("Up", 5, 25), ("Up", 5, 24), ("Up", 5, 23), ("Up", 5, 22),
        ("Right", 6, 22), ("Right", 7, 22),
        ("Up", 7, 21), ("Up", 7, 20), ("Up", 7, 19), ("Up", 7, 18), ("Up", 7, 17),
        ("Up", 7, 16), ("Up", 7, 15), ("Up", 7, 14), ("Up", 7, 13), ("Up", 7, 12),
        ("Up", 7, 11), ("Up", 7, 10), # Stairs to 2F
    ]
    for d, tx, ty in path_1f:
        step_to(d, tx, ty)
        
    time.sleep(1.0)
    pos = mgba.get_coordinates()
    print("Inside Mansion 2F! Position:", pos)
    
    # 3. Stairs from 2F to 3F are at (7, 10)
    step_to("Up", 7, 10)
    
    time.sleep(1.0)
    pos = mgba.get_coordinates()
    print("Inside Mansion 3F! Position:", pos)
    
    # 4. Walk straight to (11, 11) on 3F
    path_3f = [
        ("Right", 8, 11),
        ("Right", 9, 11),
        ("Right", 10, 11), # Gate at (10, 11) is OPEN in State A
        ("Right", 11, 11),
    ]
    for d, tx, ty in path_3f:
        step_to(d, tx, ty)
        
    pos = mgba.get_coordinates()
    print("Reached switch landing! Position:", pos)
    
    # 5. Face Right to look at (12, 11)
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    
    # 6. Toggle switch to State B
    print("Toggling switch to State B...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"]) # YES
    time.sleep(1.0)
    mgba.press_buttons(["B"]) # Dismiss
    time.sleep(1.0)
    
    # 7. Walk to Pit on 3F (State B)
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
        step_to(d, tx, ty)
        
    print("At (26, 6). Stepping Left onto the pit at (25, 6)...")
    mgba.press_buttons(["Left"])
    time.sleep(3.0) # Wait for falling animation
    
    pos = mgba.get_coordinates()
    print("Landed on 1F! Position:", pos)
    mgba.take_screenshot()
    
    # Walk to B1F stairs (usually walking UP from landing area)
    print("Walking onto B1F stairs...")
    for _ in range(5):
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        
    pos = mgba.get_coordinates()
    print("Final position on B1F:", pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
