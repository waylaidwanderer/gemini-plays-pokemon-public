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
    if pos['x'] == tx and pos['y'] == ty:
        return True
        
    print(f"At {pos}. Moving {direction} to ({tx}, {ty})...")
    mgba.press_buttons([direction])
    time.sleep(0.5)
    new_pos = mgba.get_coordinates()
    
    attempts = 0
    while new_pos != {'x': tx, 'y': ty} and attempts < 5:
        if new_pos == pos:
            print("Did not move. Checking for direction turn, wall, or battle...")
            mgba.press_buttons([direction])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
            
            if new_pos == pos:
                print("Still did not move. Checking for battle...")
                handle_battle()
                time.sleep(0.5)
                mgba.press_buttons([direction])
                time.sleep(0.5)
                new_pos = mgba.get_coordinates()
        else:
            print(f"We are at unexpected position {new_pos}. Retrying {direction}...")
            pos = new_pos
            mgba.press_buttons([direction])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
        attempts += 1
        
    return new_pos == {'x': tx, 'y': ty}

def main():
    print("Starting route to (11, 11) to toggle 3F switch...")
    
    # We are currently at (2, 11) on 3F
    path = [
        # 1. Move Down to (2, 13)
        ("Down", 2, 12),
        ("Down", 2, 13),
        
        # 2. Move Right to (10, 13)
        ("Right", 3, 13),
        ("Right", 4, 13),
        ("Right", 5, 13),
        ("Right", 6, 13),
        ("Right", 7, 13),
        ("Right", 8, 13),
        ("Right", 9, 13),
        ("Right", 10, 13),
        
        # 3. Move Up to (10, 11)
        ("Up", 10, 12),
        ("Up", 10, 11),
        
        # 4. Move Right to (11, 11)
        ("Right", 11, 11),
    ]
    
    success = True
    for direction, tx, ty in path:
        if not step_to(direction, tx, ty):
            print(f"Failed to reach ({tx}, {ty})!")
            success = False
            break
            
    if success:
        print("Successfully reached (11, 11)! Toggling switch at (12, 11) facing Right with Gen 1 timing...")
        # Face Right, wait 250ms, press A, wait 600ms, press A, wait 600ms, press B
        mgba.press_buttons(["Right", "sleep 250", "A", "sleep 600", "A", "sleep 600", "B"])
        time.sleep(2.5)
        
        # Take screenshot of toggle result
        mgba.take_screenshot()
        
        # Now let's test if the gate at (10, 11) is CLOSED (State B)
        print("Testing if gate is CLOSED by stepping Left to (10, 11)...")
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
        
        pos_after = mgba.get_coordinates()
        print("Coordinates after attempting Left:", pos_after)
        
        if pos_after == {'x': 10, 'y': 11}:
            print("GATE IS OPEN! Switch toggle failed.")
            # Move back Right to (11, 11)
            mgba.press_buttons(["Right"])
            time.sleep(0.5)
        else:
            print("GATE IS CLOSED! SWITCH TOGGLE SUCCESSFUL!!! Global state is now State B!")
            
        mgba.take_screenshot()
    else:
        mgba.take_screenshot()

if __name__ == "__main__":
    main()
