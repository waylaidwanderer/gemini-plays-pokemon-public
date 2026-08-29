import mgba
import time

def step_one(direction, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"Moving {direction} to ({target_x}, {target_y}). Current: {pos_before}")
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        print("Blocked or in battle. Attempting run...")
        mgba.press_buttons(["Down", "sleep 250", "Right", "sleep 250", "A", "sleep 1000", "B"])
        time.sleep(2.0)
        # Try moving again
        mgba.press_buttons([direction])
        time.sleep(0.4)
        pos_after = mgba.get_coordinates()
        
    if pos_after['x'] == target_x and pos_after['y'] == target_y:
        return True
    return False

def walk_path(coords):
    for target_x, target_y in coords:
        pos = mgba.get_coordinates()
        dx = target_x - pos['x']
        dy = target_y - pos['y']
        
        if abs(dx) + abs(dy) > 1:
            print(f"Error: Step to ({target_x}, {target_y}) is too far from current {pos}")
            return False
            
        direction = ""
        if dx > 0: direction = "Right"
        elif dx < 0: direction = "Left"
        elif dy > 0: direction = "Down"
        elif dy < 0: direction = "Up"
        
        # Check if we fell through a pit during the walk!
        # If coordinates change drastically, it means we warped/fell!
        pos_before = mgba.get_coordinates()
        if not step_one(direction, target_x, target_y):
            pos_now = mgba.get_coordinates()
            if abs(pos_now['x'] - pos_before['x']) > 2 or abs(pos_now['y'] - pos_before['y']) > 2:
                print(f"WARPED/FELL! Landed at {pos_now}")
                return "WARPED"
            return False
            
        # Double check warp/fall after a successful-looking step
        pos_after = mgba.get_coordinates()
        if abs(pos_after['x'] - pos_before['x']) > 2 or abs(pos_after['y'] - pos_before['y']) > 2:
            print(f"WARPED/FELL! Landed at {pos_after}")
            return "WARPED"
            
    return True

def main():
    print("go_to_b1f: Starting...")
    pos = mgba.get_coordinates()
    print(f"Current position: {pos}")
    
    # We are on 2F East.
    # Path back to 2F East stairs at (22, 1)
    if pos['x'] == 12 and pos['y'] >= 1:
        # Walk Up Column 12 to Row 1
        path_2f = []
        for y in range(pos['y'] - 1, 0, -1):
            path_2f.append((12, y))
        # Walk Right along Row 1 to Column 22
        for x in range(13, 23):
            path_2f.append((x, 1))
            
        print(f"Walking back to 2F East stairs: {path_2f}")
        if not walk_path(path_2f):
            print("Walking on 2F East failed.")
            return
            
        # Stepping onto stairs to warp to 3F East
        print("Stepping onto stairs to warp to 3F East...")
        mgba.press_buttons(["Up"])
        time.sleep(1.0)
        pos = mgba.get_coordinates()
        print(f"Arrived on 3F! Position: {pos}")
        
    # Now we are on 3F East (or should be).
    pos = mgba.get_coordinates()
    # Path on 3F East to the pitfall at (26, 6)
    # The stairs are at (22, 2) or (22, 1)
    # Walk to (22, 3) -> (26, 3) -> (26, 6)
    path_3f = [
        (22, 3),
        (23, 3), (24, 3), (25, 3), (26, 3),
        (26, 4), (26, 5), (26, 6)
    ]
    
    pos_tuple = (pos['x'], pos['y'])
    if pos_tuple in path_3f:
        start_idx = path_3f.index(pos_tuple)
        path_3f = path_3f[start_idx+1:]
        
    print(f"Walking on 3F East to pitfall: {path_3f}")
    res = walk_path(path_3f)
    if res == "WARPED":
        print("SUCCESSFULLY FELL TO 1F EAST!!!")
        time.sleep(1.0)
        print(f"Landed at: {mgba.get_coordinates()}")
    elif res:
        # If we successfully walked but didn't warp automatically, let's step on (26, 6)
        print(f"Arrived at end of path on 3F. Position: {mgba.get_coordinates()}")
    else:
        print("Failed to walk 3F East path.")

if __name__ == "__main__":
    main()
