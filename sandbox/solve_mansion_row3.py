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
    print("Navigating to Column 23, Row 3...")
    path = [
        # 1. Walk Right to (24, 16)
        ("Right", 20, 16),
        ("Right", 21, 16),
        ("Right", 22, 16),
        ("Right", 23, 16),
        ("Right", 24, 16),
        # 2. Walk UP column 24 to row 11
        ("Up", 24, 15),
        ("Up", 24, 14),
        ("Up", 24, 13),
        ("Up", 24, 12),
        ("Up", 24, 11),
        # 3. Walk Left to (23, 11)
        ("Left", 23, 11),
        # 4. Walk UP column 23 to row 3
        ("Up", 23, 10),
        ("Up", 23, 9),
        ("Up", 23, 8),
        ("Up", 23, 7),
        ("Up", 23, 6),
        ("Up", 23, 5),
        ("Up", 23, 4),
        ("Up", 23, 3),
    ]
    if not follow_path(path):
        return False
        
    print("Reached (23, 3). Testing Left horizontal crossing on Row 3...")
    for i in range(15):
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
                print("Row 3 blocked at column:", pos_after['x'])
                break
                
    pos_final = mgba.get_coordinates()
    print("Final position of Row 3 test:", pos_final)
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    run_main()
