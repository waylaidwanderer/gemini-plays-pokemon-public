import mgba
import time

def cross_2f_east():
    path = [
        # Up Column 12 from (12, 11) to (12, 3)
        (12, 10), (12, 9), (12, 8), (12, 7), (12, 6), (12, 5), (12, 4), (12, 3),
        # Right Row 3 to Column 18
        (13, 3), (14, 3), (15, 3), (16, 3), (17, 3), (18, 3),
        # Down Column 18 to Row 11
        (18, 4), (18, 5), (18, 6), (18, 7), (18, 8), (18, 9), (18, 10), (18, 11),
        # Left Row 11 to Column 15
        (17, 11), (16, 11), (15, 11)
    ]
    
    print("Starting 2F West -> 2F East -> 3F East walk...")
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
            
    print("Reached stairs at (15, 11)! Stepping UP to warp to 3F East...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    final_pos = mgba.get_coordinates()
    print("Position after warp:", final_pos)
    mgba.take_screenshot()
    return True

cross_2f_east()
