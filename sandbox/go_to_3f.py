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

def run_main():
    print("Starting corrected route to 3F stairs from (6, 13)...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    path = [
        ("Up", 6, 12),
        ("Up", 6, 11),
        ("Up", 6, 10),
        ("Right", 7, 10), # Stairs!
    ]
    if not follow_path(path):
        return False
        
    print("At (7, 10) on 2F. Ascending to 3F...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0) # Wait for warp
    
    pos = mgba.get_coordinates()
    print("Position after warp:", pos)
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    run_main()
