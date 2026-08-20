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

def interact_with_timing(direction):
    # Press direction to face, wait 250ms, press A, wait 600ms, press A, wait 600ms, press B
    print(f"Interacting facing {direction}...")
    mgba.press_buttons([direction, "sleep 250", "A", "sleep 600", "A", "sleep 600", "B"])
    time.sleep(2.5)

def main():
    print("Starting brute-force 3F switch toggle search around (2, 11)...")
    
    # Currently at (10, 11)
    # Walk to (2, 13) via Row 13
    path_to_row13 = [
        ("Down", 10, 12),
        ("Down", 10, 13),
        ("Left", 9, 13),
        ("Left", 8, 13),
        ("Left", 7, 13),
        ("Left", 6, 13),
        ("Left", 5, 13),
        ("Left", 4, 13),
        ("Left", 3, 13),
        ("Left", 2, 13),
    ]
    
    for direction, tx, ty in path_to_row13:
        if not step_to(direction, tx, ty):
            print(f"Failed to reach ({tx}, {ty}) on way to Row 13!")
            return
            
    # Position is (2, 13)
    
    # --- TEST 1: (2, 12) facing UP ---
    if step_to("Up", 2, 12):
        interact_with_timing("Up")
        
    # --- TEST 2: (1, 11) facing RIGHT ---
    # From (2, 12), walk Left to (1, 12) then Up to (1, 11)
    if step_to("Left", 1, 12) and step_to("Up", 1, 11):
        interact_with_timing("Right")
        
    # --- TEST 3: (2, 10) facing DOWN ---
    # From (1, 11), walk Right to (2, 11) then Up to (2, 10)
    # Wait, (2, 11) is walkable.
    if step_to("Right", 2, 11) and step_to("Up", 2, 10):
        interact_with_timing("Down")
        
    # --- TEST 4: (3, 11) facing LEFT ---
    # From (2, 10), walk Down to (2, 11) then Right to (3, 11)
    # Wait, is (3, 11) walkable? Let's check.
    # Column 3 has statues on even rows, pink carpet on odd rows, so (3, 11) should be walkable.
    if step_to("Down", 2, 11) and step_to("Right", 3, 11):
        interact_with_timing("Left")
        
    # Now walk back to (10, 11) to test if we succeeded!
    # From (3, 11), walk Down to (3, 13) then Right to (10, 13) then Up to (10, 11)
    path_back = [
        ("Down", 3, 12),
        ("Down", 3, 13),
        ("Left", 2, 13), # Just to align with Column 2
        ("Right", 3, 13),
        ("Right", 4, 13),
        ("Right", 5, 13),
        ("Right", 6, 13),
        ("Right", 7, 13),
        ("Right", 8, 13),
        ("Right", 9, 13),
        ("Right", 10, 13),
        ("Up", 10, 12),
        ("Up", 10, 11),
    ]
    
    for direction, tx, ty in path_back:
        step_to(direction, tx, ty)
        
    # Check if gate at (10, 11) is CLOSED
    pos = mgba.get_coordinates()
    if pos == {'x': 10, 'y': 11}:
        print("At (10, 11). Attempting to walk Right to (11, 11) to test gate...")
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
        pos_test = mgba.get_coordinates()
        if pos_test == {'x': 11, 'y': 11}:
            print("TEST RESULT: Gate is still OPEN. Brute-force failed to find switch at (2, 11).")
            mgba.press_buttons(["Left"])
            time.sleep(0.5)
        else:
            print("TEST RESULT: GATE IS CLOSED!!! SUCCESS!!! One of the positions successfully toggled the switch to State B!")
    else:
        print("Failed to reach (10, 11) for testing.")
        
    mgba.take_screenshot()

if __name__ == "__main__":
    main()
