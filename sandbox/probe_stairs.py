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
        
        direction = ""
        if dx > 0: direction = "Right"
        elif dx < 0: direction = "Left"
        elif dy > 0: direction = "Down"
        elif dy < 0: direction = "Up"
        
        if not step_one(direction, target_x, target_y):
            return False
    return True

def main():
    print("probe_stairs_via_col12: Starting...")
    pos = mgba.get_coordinates()
    print(f"Current position: {pos}")
    
    # Path from (10, 10) to Column 12, then Row 1, then (22, 1)
    path = [
        # Right to Column 12
        (11, 10), (12, 10),
        # Up Column 12 to Row 1
        (12, 9), (12, 8), (12, 7), (12, 6), (12, 5), (12, 4), (12, 3), (12, 2), (12, 1),
        # Right along Row 1 to Column 22
        (13, 1), (14, 1), (15, 1), (16, 1), (17, 1), (18, 1), (19, 1), (20, 1), (21, 1), (22, 1)
    ]
    
    pos_tuple = (pos['x'], pos['y'])
    if pos_tuple in path:
        start_idx = path.index(pos_tuple)
        path = path[start_idx+1:]
        
    print(f"Walking path: {path}")
    if not walk_path(path):
        print("Walking to stairs failed.")
        return
        
    # We are at (22, 1) on 2F East.
    print("Arrived at stairs (22, 1). Testing warp...")
    
    # Step Left to (21, 1)
    print("Stepping Left to (21, 1)...")
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    print(f"Position: {mgba.get_coordinates()}")
    
    # Step Right onto (22, 1) to trigger warp
    print("Stepping Right to (22, 1) to test warp...")
    mgba.press_buttons(["Right"])
    time.sleep(1.0)
    print(f"Position after warp attempt: {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
