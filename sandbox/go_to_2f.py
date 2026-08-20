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
    print("Dismissing 'SHELLBY is already out!'...")
    mgba.press_buttons(["B"])
    time.sleep(1.0)
    
    # Press B again to exit the Pokemon party list and return to main fight menu
    print("Exiting Pokemon menu...")
    mgba.press_buttons(["B"])
    time.sleep(1.0)
    
    # We are in the main fight menu, cursor on POKEMON.
    # From POKEMON (top-right): Down moves to RUN (bottom-right).
    print("Running from battle...")
    mgba.press_buttons(["Down", "A"])
    time.sleep(3.0) # wait for escape
    
    # Ensure overworld is clean
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Overworld position after escape:", pos)
    
    # We should be at (7, 13). Walk Up column 7 to (7, 10) stairs
    path = [
        ("Up", 7, 12),
        ("Up", 7, 11),
        ("Up", 7, 10),
    ]
    if not follow_path(path):
        return False
        
    print("Successfully stepped onto stairs! Warping...")
    time.sleep(2.0)
    
    final_pos = mgba.get_coordinates()
    print("Final position on 2F:", final_pos)
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    run_all()
