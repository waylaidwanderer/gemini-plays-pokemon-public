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
    print("Navigating down to 2F Northwest Switch room...")
    # Stand on (6, 10) and walk Left to (5, 10) to warp
    mgba.press_buttons(["Left"])
    time.sleep(2.0) # Wait for warp
    
    pos = mgba.get_coordinates()
    print("Position on 2F after warp:", pos)
    
    # We should land at (5, 11) on 2F. Let's walk to (2, 12)
    path = [
        ("Left", 4, 11),
        ("Left", 3, 11),
        ("Down", 3, 12),
        ("Left", 2, 12),
    ]
    if not follow_path(path):
        return False
        
    print("At (2, 12) on 2F. Pressing UP to face statue...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    print("Pressing A to toggle switch...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    print("Taking screenshot to see if text box opened...")
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)
    
    # Dismiss any text box if it opened
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    return True

if __name__ == "__main__":
    run_main()
