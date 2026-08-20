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
    print("Starting drop script from (23, 11)...")
    # Path to (24, 14)
    path_to_balcony = [
        ("Right", 24, 11),
        ("Down", 24, 12),
        ("Down", 24, 13),
        ("Down", 24, 14),
    ]
    if not follow_path(path_to_balcony):
        return False
        
    print("Reached (24, 14). Testing balcony drop by walking Left...")
    # First turn Left
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    print("Position after turning Left:", mgba.get_coordinates())
    
    # Take a step Left
    mgba.press_buttons(["Left"])
    time.sleep(3.0) # wait for warp/drop
    
    pos = mgba.get_coordinates()
    print("Position after walking Left:", pos)
    mgba.take_screenshot()
    
    if pos['x'] != 24 or pos['y'] != 14:
        print("Successfully dropped!")
        return True
        
    # If Left didn't drop, try walking Down from (24, 14)
    print("Left step did not drop. Trying Down step...")
    mgba.press_buttons(["Down"])
    time.sleep(3.0) # wait for drop
    
    pos_down = mgba.get_coordinates()
    print("Position after walking Down:", pos_down)
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    run_main()
