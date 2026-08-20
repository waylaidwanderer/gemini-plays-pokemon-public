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

def run_main():
    print("Testing Row 15 horizontal crossing starting from (24, 15)...")
    # Walk Left from (24, 15) to see how far we can go
    for i in range(15):
        pos_before = mgba.get_coordinates()
        mgba.press_buttons(["Left"])
        time.sleep(0.4)
        pos_after = mgba.get_coordinates()
        print(f"Step {i+1}: position is {pos_after}")
        if pos_before == pos_after:
            # Handle battle or text
            handle_battle()
            time.sleep(0.5)
            pos_after = mgba.get_coordinates()
            if pos_before == pos_after:
                print("Row 15 BLOCKED at column:", pos_after['x'])
                break
                
    # If we made it to column 11, we are in the west wing!
    pos_final = mgba.get_coordinates()
    print("Final position of Row 15 test:", pos_final)
    mgba.take_screenshot()
    
    if pos_final['x'] <= 11:
        print("SUCCESS! Row 15 is open to the west wing!")
        return True
        
    # If Row 15 is blocked, let's walk back to (24, 15) and test Row 16!
    print("Row 15 was blocked. Returning to (24, 15)...")
    # Walk Right back to column 24
    for i in range(24 - pos_final['x']):
        mgba.press_buttons(["Right"])
        time.sleep(0.4)
        handle_battle()
        
    print("At column 24 on row 15. Stepping Down to (24, 16)...")
    if not step_to("Down", 24, 16):
        print("Failed to step Down to (24, 16)!")
        return False
        
    print("Testing Row 16 horizontal crossing starting from (24, 16)...")
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
                print("Row 16 BLOCKED at column:", pos_after['x'])
                break
                
    pos_final_16 = mgba.get_coordinates()
    print("Final position of Row 16 test:", pos_final_16)
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    run_main()
