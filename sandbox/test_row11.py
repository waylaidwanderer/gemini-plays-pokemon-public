import mgba
import time

def handle_battle():
    print("Encountered battle or text! Escaping...")
    # Advance any initial text
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    # Move to RUN and press A
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
    print("Walking Down to row 11 from (23, 6)...")
    path_to_row11 = [
        ("Down", 23, 7),
        ("Down", 23, 8),
        ("Down", 23, 9),
        ("Down", 23, 10),
        ("Down", 23, 11),
    ]
    if not follow_path(path_to_row11):
        return False
        
    print("Reached (23, 11). Testing Left movements along Row 11...")
    # Since we need to turn first in Gen 1, we will try walking Left multiple times
    for i in range(15):
        pos_before = mgba.get_coordinates()
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        pos_after = mgba.get_coordinates()
        print(f"Step {i+1}: position is {pos_after}")
        if pos_before == pos_after:
            # Let's handle battle just in case
            handle_battle()
            time.sleep(0.5)
            pos_after = mgba.get_coordinates()
            if pos_before == pos_after:
                print("BLOCKED at row 11! Cannot walk Left further.")
                mgba.take_screenshot()
                break
                
    mgba.take_screenshot()

if __name__ == "__main__":
    run_main()
