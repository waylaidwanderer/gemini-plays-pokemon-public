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
    print("Navigating to Row 20 via Column 24...")
    path_to_row20 = [
        # 1. Walk Right along row 16 to column 24
        ("Right", 20, 16),
        ("Right", 21, 16),
        ("Right", 22, 16),
        ("Right", 23, 16),
        ("Right", 24, 16),
        # 2. Walk Down column 24 to row 20
        ("Down", 24, 17),
        ("Down", 24, 18),
        ("Down", 24, 19),
        ("Down", 24, 20),
    ]
    if not follow_path(path_to_row20):
        return False
        
    print("Reached (24, 20). Walking Left along Row 20...")
    # Walk Left from column 24 as far as we can go
    for i in range(25):
        pos_before = mgba.get_coordinates()
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        pos_after = mgba.get_coordinates()
        print(f"Step {i+1}: position is {pos_after}")
        if pos_before == pos_after:
            handle_battle()
            time.sleep(0.5)
            pos_after = mgba.get_coordinates()
            if pos_before == pos_after:
                print("Row 20 blocked at column:", pos_after['x'])
                break
                
    pos_final = mgba.get_coordinates()
    print("Final position of Row 20 test:", pos_final)
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    run_main()
