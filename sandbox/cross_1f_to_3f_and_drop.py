import mgba
import time

def cross_1f_to_3f():
    # We are at (7, 10) on 1F West.
    path_1f = [
        # Step Left off the warp
        (6, 10),
        # Step Down
        (6, 11),
        # Walk Right along Row 11 to Column 12
        (7, 11), (8, 11), (9, 11), (10, 11), (11, 11), (12, 11),
        # Walk Up Column 12 to Row 6
        (12, 10), (12, 9), (12, 8), (12, 7), (12, 6),
        # Walk Right along Row 6 to Column 17
        (13, 6), (14, 6), (15, 6), (16, 6), (17, 6),
        # Walk Down through the open shutter gate at (17, 7)
        (17, 7), (17, 8), (17, 9), (17, 10),
        # Walk Right to stairs at (18, 10)
        (18, 10)
    ]
    
    print("Walking 1F West -> 1F East -> 2F East in State B...")
    for target in path_1f:
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
        time.sleep(0.35)
        
        new_pos = mgba.get_coordinates()
        if new_pos == {'x': target[0], 'y': target[1]}:
            print(f"Reached {target}")
        else:
            print(f"FAILED to reach {target}. We are at {new_pos}.")
            mgba.take_screenshot()
            return False
            
    print("Reached stairs at (18, 10)! Stepping DOWN to warp to 2F East...")
    mgba.press_buttons(["Down"])
    time.sleep(1.0)
    
    pos_2f = mgba.get_coordinates()
    print("Coordinates on 2F East:", pos_2f)
    
    # Check if we successfully warped to 2F East (should be near (18, 11))
    if pos_2f['y'] < 9:
        print("Error: Did not warp to 2F East South!")
        mgba.take_screenshot()
        return False
        
    # Now walk on 2F East South to 3F East stairs at (15, 11)
    path_2f = [
        # Walk Left to stairs at (15, 11)
        (17, 11), (16, 11), (15, 11)
    ]
    
    print("Walking on 2F East South...")
    for target in path_2f:
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
        time.sleep(0.35)
        
        new_pos = mgba.get_coordinates()
        if new_pos == {'x': target[0], 'y': target[1]}:
            print(f"Reached {target}")
        else:
            print(f"FAILED to reach {target}. We are at {new_pos}.")
            mgba.take_screenshot()
            return False
            
    print("Reached stairs at (15, 11)! Stepping UP to warp to 3F East...")
    mgba.press_buttons(["Up"])
    time.sleep(1.0)
    
    pos_3f = mgba.get_coordinates()
    print("Final coordinates on 3F East:", pos_3f)
    mgba.take_screenshot()
    return True

cross_1f_to_3f()
