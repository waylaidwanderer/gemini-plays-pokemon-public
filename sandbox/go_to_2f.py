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
    print(f"At {pos}. Moving {direction} to ({tx}, {ty})...")
    mgba.press_buttons([direction])
    time.sleep(0.4)
    new_pos = mgba.get_coordinates()
    
    if new_pos == pos:
        print("Did not move. Attempting to escape battle or clear text...")
        handle_battle()
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            print("Retrying movement step...")
            mgba.press_buttons([direction])
            time.sleep(0.4)
            new_pos = mgba.get_coordinates()
            
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

def run_all():
    print("Dismissing Grimer battle intro...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Dismiss sending out SHELLBY text
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    
    # Select RUN
    print("Fleeing battle...")
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(3.0) # wait for escape
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Overworld pos after escape:", pos)
    
    # 2. Ascend to 3F. We are at (7, 10) or (7, 11) on 2F
    if pos['x'] == 7 and pos['y'] == 10:
        print("Standing on stairs. Stepping off to (7, 11) to reset warp...")
        mgba.press_buttons(["Down"])
        time.sleep(0.5)
        pos = mgba.get_coordinates()
        print("Position:", pos)
        
    if pos['x'] == 7 and pos['y'] == 11:
        print("Stepping Up onto (7, 10) stairs to warp to 3F...")
        mgba.press_buttons(["Up"])
        time.sleep(2.0) # wait for warp
        
    pos = mgba.get_coordinates()
    print("Warp complete! Position on 3F:", pos)
    
    # We land at (7, 11) on 3F in State A.
    # 3. Walk to the pit at (22, 6) on 3F
    print("Walking to the pit at (22, 6)...")
    path_to_pit = [
        ("Right", 8, 11),
        ("Right", 9, 11),
        ("Right", 10, 11), # OPEN in State A!
        ("Right", 11, 11),
        ("Up", 11, 10),
        ("Up", 11, 9),
        ("Up", 11, 8),
        ("Up", 11, 7),
        ("Up", 11, 6),
        ("Right", 12, 6),
        ("Right", 13, 6),
        ("Right", 14, 6),
        ("Right", 15, 6),
        ("Right", 16, 6),
        ("Right", 17, 6),
        ("Right", 18, 6),
        ("Right", 19, 6),
        ("Right", 20, 6),
        ("Right", 21, 6),
        ("Right", 22, 6), # PIT fall to 2F!
    ]
    if not follow_path(path_to_pit):
        return False
        
    print("Warp completed! Landed on 2F!")
    time.sleep(2.0)
    final_pos = mgba.get_coordinates()
    print("Landed on 2F! Position:", final_pos)
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    run_all()
