import mgba
import time

def walk_step(direction, target_x, target_y):
    pos = mgba.get_coordinates()
    print(f"Standing at {pos}. Pressing {direction} to ({target_x}, {target_y})...")
    mgba.press_buttons([direction])
    time.sleep(0.4)
    new_pos = mgba.get_coordinates()
    print(f"Now at {new_pos}.")
    if new_pos['x'] == target_x and new_pos['y'] == target_y:
        return True
    else:
        # If blocked, try to dismiss text/battle first
        print("Failed to reach target. Attempting to clear text/battle...")
        mgba.press_buttons(["B"])
        time.sleep(0.5)
        # Try once more
        mgba.press_buttons([direction])
        time.sleep(0.4)
        new_pos = mgba.get_coordinates()
        if new_pos['x'] == target_x and new_pos['y'] == target_y:
            return True
        print(f"INTERRUPTED! Got stuck at {new_pos}")
        mgba.take_screenshot()
        return False

def go_to_2f():
    print("Walking from 1F entrance at (5, 27) to 2F stairs...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # 1. Walk straight Up column 5 to row 10
    path = []
    for row in range(26, 9, -1):
        path.append(("Up", 5, row))
        
    # 2. Walk Right to (7, 10)
    path.append(("Right", 6, 10))
    path.append(("Right", 7, 10))
    
    # Execute the path
    for d, tx, ty in path:
        if not walk_step(d, tx, ty):
            return False
            
    # Step onto the stairs at (7, 10) (usually UP)
    print("At stairs (7, 10). Pressing Up to warp to 2F...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0) # Wait for warp
    
    final_pos = mgba.get_coordinates()
    print("Position after warp attempt:", final_pos)
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    go_to_2f()
