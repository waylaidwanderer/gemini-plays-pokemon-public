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

def run_to_pit_east():
    print("Walking Left into the pit from (24, 6)...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # Path: Left to (23, 6), Left into pit at (22, 6)
    path = [
        ("Left", 23, 6),
        ("Left", 22, 6) # PIT fall!
    ]
    if not follow_path(path):
        return False
        
    print("Pit reached! Warping...")
    time.sleep(2.0) # Wait for fall animation
    
    final_pos = mgba.get_coordinates()
    print("Landed on 2F! Coordinates:", final_pos)
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    run_to_pit_east()
