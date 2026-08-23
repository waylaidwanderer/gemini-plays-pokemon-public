import mgba
import time

def walk_to_1f():
    path = [
        # Up Column 18 to Row 3
        (18, 5), (18, 4), (18, 3),
        # Left Row 3 to Column 12
        (17, 3), (16, 3), (15, 3), (14, 3), (13, 3), (12, 3),
        # Down Column 12 to Row 11
        (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (12, 9), (12, 10), (12, 11),
        # Left Row 11 to Column 7
        (11, 11), (10, 11), (9, 11), (8, 11), (7, 11),
        # Up to stairs at (7, 10)
        (7, 10)
    ]
    
    print("Walking 2F East -> 1F West...")
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
            
    print("Reached stairs at (7, 10)! Stepping UP to warp back to 1F West...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    final_pos = mgba.get_coordinates()
    print("Position after warp:", final_pos)
    mgba.take_screenshot()
    return True

walk_to_1f()
