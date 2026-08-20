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
    print("Starting corrected 3F switch toggle sequence...")
    
    # 1. We are currently at (12, 11). Move Left to (11, 11)
    if not step_to("Left", 11, 11):
        print("Failed to reach (11, 11)!")
        mgba.take_screenshot()
        return
        
    print("Successfully reached (11, 11). Turning face Right...")
    # 2. Press raw "Right" to turn in place
    mgba.press_buttons(["Right"])
    time.sleep(0.5) # Wait for turn animation to complete
    
    # 3. Toggle the switch at (12, 11)
    print("Pressing A to interact with the switch at (12, 11)...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    mgba.take_screenshot()
    
    # Press A to select YES, press A to dismiss, press B to close
    print("Pressing A to select YES on switch...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    print("Pressing A to dismiss text...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    print("Pressing B to close dialogue...")
    mgba.press_buttons(["B"])
    time.sleep(1.0)
    
    mgba.take_screenshot()
    
    # 4. Now test if the gate at (10, 11) is CLOSED (State B)
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

if __name__ == "__main__":
    main()
