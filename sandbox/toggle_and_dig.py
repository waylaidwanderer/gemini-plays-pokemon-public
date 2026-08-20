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
    print("Starting bypass walk along column 1 from (3, 13)...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # We are at (3, 13). Walk Left to (2, 13), Left to (1, 13), Up to (1, 12), Up to (1, 11)
    path = [
        ("Left", 2, 13),
        ("Left", 1, 13),
        ("Up", 1, 12),
        ("Up", 1, 11),
    ]
    if not follow_path(path):
        return False
        
    # Face Right and press A to toggle switch to State B
    print("At (1, 11). Facing Right and toggling switch at (2, 11)...")
    mgba.press_buttons(["Right", "sleep 300", "A", "sleep 500", "A", "sleep 500", "B"])
    time.sleep(1.0)
    
    pos = mgba.get_coordinates()
    print("Coordinates after switch toggle:", pos)
    mgba.take_screenshot()
    
    # Now use DIG using Paras (TRUFFLE)
    print("Opening Start menu...")
    mgba.press_buttons(["Start"])
    time.sleep(1.0)
    
    # From POKeDEX (default) to POKeMON: Down, then A
    print("Navigating to POKeMON...")
    mgba.press_buttons(["Down", "A"])
    time.sleep(1.5)
    
    # In POKeMON list, move Down to select TRUFFLE (second in party)
    print("Selecting TRUFFLE...")
    mgba.press_buttons(["Down", "A"])
    time.sleep(1.5)
    
    # Select DIG (Option 1)
    print("Executing DIG...")
    mgba.press_buttons(["A"])
    time.sleep(4.0) # Wait for escape animation and overworld to load
    
    final_pos = mgba.get_coordinates()
    print("Position after DIG:", final_pos)
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    run_all()
