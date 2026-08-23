import mgba
import time

def walk_mansion_1f():
    # Adjusted route to avoid the Column 13 Row 7 wall by going via Row 6
    path = [
        # Up Column 5 from (5, 27) to (5, 11)
        (5, 26), (5, 25), (5, 24), (5, 23), (5, 22), (5, 21), (5, 20), (5, 19), (5, 18), (5, 17), (5, 16), (5, 15), (5, 14), (5, 13), (5, 12), (5, 11),
        # Right Row 11 to (12, 11)
        (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11), (12, 11),
        # Up Column 12 to Row 6
        (12, 10), (12, 9), (12, 8), (12, 7), (12, 6),
        # Right Row 6 to Column 18
        (13, 6), (14, 6), (15, 6), (16, 6), (17, 6), (18, 6),
        # Down Column 18 to Row 10
        (18, 7), (18, 8), (18, 9), (18, 10)
    ]
    
    print("Starting 1F West -> 2F East walk...")
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
        time.sleep(0.35)  # Slightly longer sleep for safety
        
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

walk_mansion_1f()
