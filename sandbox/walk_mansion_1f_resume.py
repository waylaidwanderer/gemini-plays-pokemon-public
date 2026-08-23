import mgba
import time

def walk_mansion_1f_resume():
    # Remaining path to avoid the Column 13 Row 7 wall
    path = [
        # Right Row 11 from (7, 11) to (12, 11)
        (8, 11), (9, 11), (10, 11), (11, 11), (12, 11),
        # Up Column 12 to Row 6
        (12, 10), (12, 9), (12, 8), (12, 7), (12, 6),
        # Right Row 6 to Column 18
        (13, 6), (14, 6), (15, 6), (16, 6), (17, 6), (18, 6),
        # Down Column 18 to Row 10
        (18, 7), (18, 8), (18, 9), (18, 10)
    ]
    
    print("Resuming 1F West -> 2F East walk...")
    for target in path:
        pos = mgba.get_coordinates()
        dx = target[0] - pos['x']
        dy = target[1] - pos['y']
        
        if abs(dx) + abs(dy) != 1:
            print(f"Error: Target {target} is not adjacent to current position {pos}")
            return False
            
        if dx == 1: btn = "Right"
        elif dx == -1: btn = "Left"
        elif dy == 1: btn = "Down"
        elif dy == -1: btn = "Up"
        
        mgba.press_buttons([btn])
        time.sleep(0.35)  # Safe 0.35s sleep
        
        new_pos = mgba.get_coordinates()
        if new_pos == {'x': target[0], 'y': target[1]}:
            print(f"Reached {target}")
        else:
            print(f"FAILED to reach {target}. We are at {new_pos}.")
            mgba.take_screenshot()
            return False
            
    print("Reached stairs at (18, 10)! Stepping DOWN to warp to 2F East...")
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    
    final_pos = mgba.get_coordinates()
    print("Position after warp:", final_pos)
    mgba.take_screenshot()
    return True

walk_mansion_1f_resume()
