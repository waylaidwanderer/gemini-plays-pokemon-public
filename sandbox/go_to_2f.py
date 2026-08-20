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
    print("Backing out of move menu to main battle menu...")
    mgba.press_buttons(["B"])
    time.sleep(1.0)
    
    # We should be back on the main battle menu, cursor on FIGHT.
    # FIGHT is top-left. RUN is bottom-right.
    # Press Down, Right, A to run from battle!
    print("Running from Koffing battle...")
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(3.0) # wait for escape
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Overworld pos after escape:", pos)
    
    # We should land at (26, 4). Walk Left to (23, 4), Down to (23, 6), Left into pit at (22, 6)
    path = [
        ("Left", 25, 4),
        ("Left", 24, 4),
        ("Left", 23, 4),
        ("Down", 23, 5),
        ("Down", 23, 6),
        ("Left", 22, 6), # PIT fall to 2F!
    ]
    if not follow_path(path):
        return False
        
    print("Pit reached! Warping...")
    time.sleep(2.0) # wait for fall animation
    
    final_pos = mgba.get_coordinates()
    print("Landed on 2F! Coordinates:", final_pos)
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    run_all()
