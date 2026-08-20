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

def escape_and_go_to_stairs():
    print("Backing out of move menu to main battle menu...")
    mgba.press_buttons(["B"])
    time.sleep(1.0)
    
    print("Running from battle...")
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(3.0) # wait for escape
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Overworld pos after escape:", pos)
    
    # We land somewhere on 3F east side (around row 10 column 24).
    # Let's walk west along row 11 to the west stairs at (7, 10).
    # Since we are in State A, the gate at (10, 11) is OPEN!
    # Path: Walk to row 11 column 24, then west to (7, 11), then test stairs at (7, 10)
    
    # Walk to row 11 first
    curr = mgba.get_coordinates()
    if curr['y'] != 11:
        step_to("Down", curr['x'], 11)
        
    curr = mgba.get_coordinates()
    # Path west from current column to (7, 11)
    path_to_stairs = []
    for col in range(curr['x'] - 1, 6, -1):
        path_to_stairs.append(("Left", col, 11))
        
    if not follow_path(path_to_stairs):
        return False
        
    # We are at (7, 11) on 3F. Let's test how to warp Down to 2F.
    # We'll try walking Up to (7, 10) first (which we stood on earlier).
    # If that doesn't warp, we'll try walking Up to (7, 9) and then Down onto (7, 10)!
    print("At (7, 11). Walking Up to (7, 10)...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0) # wait for warp
    
    pos3 = mgba.get_coordinates()
    print("Position after walking Up:", pos3)
    
    if pos3['x'] == 7 and pos3['y'] == 10:
        # We did not warp. Let's walk Up to (7, 9) and Down to (7, 10)
        print("At (7, 10). Walking Up to (7, 9)...")
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        print("Position:", mgba.get_coordinates())
        
        print("Walking Down onto (7, 10) stairs...")
        mgba.press_buttons(["Down"])
        time.sleep(2.0) # wait for warp
        
        final_pos = mgba.get_coordinates()
        print("Final position after Down warp attempt:", final_pos)
        mgba.take_screenshot()
    else:
        print("Warp occurred!")
        mgba.take_screenshot()

if __name__ == "__main__":
    escape_and_go_to_stairs()
