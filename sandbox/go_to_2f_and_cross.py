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
        
        if not step_one(direction, target_x, target_y):
            return False
    return True

def main():
    print("go_to_2f_and_cross: Starting...")
    pos = mgba.get_coordinates()
    print(f"Current position: {pos}")
    
    # 1. Walk on 3F from (7, 10) to stairs at (22, 2)
    path_to_stairs = [
        # Down to Row 11
        (7, 11),
        # Right to Column 12
        (8, 11), (9, 11), (10, 11), (11, 11), (12, 11),
        # Up to Row 6
        (12, 10), (12, 9), (12, 8), (12, 7), (12, 6),
        # Right to Column 20
        (13, 6), (14, 6), (15, 6), (16, 6), (17, 6), (18, 6), (19, 6), (20, 6),
        # Up to Row 3
        (20, 5), (20, 4), (20, 3),
        # Right to Column 22
        (21, 3), (22, 3),
        # Up to Row 2
        (22, 2)
    ]
    
    # Filter the path to start from where we currently are
    if pos in path_to_stairs:
        start_idx = path_to_stairs.index(pos)
        remaining_path = path_to_stairs[start_idx+1:]
    else:
        # If we are at (7, 10), start from the beginning
        remaining_path = path_to_stairs
        
    print(f"Walking remaining path to stairs: {remaining_path}")
    if not walk_path(remaining_path):
        print("Walking to stairs failed.")
        return
        
    # Take stairs to 2F East
    print("Stepping onto stairs to warp to 2F East...")
    mgba.press_buttons(["Up"])
    time.sleep(1.0)
    pos_2f = mgba.get_coordinates()
    print(f"Arrived on 2F! Position: {pos_2f}")

if __name__ == "__main__":
    main()
