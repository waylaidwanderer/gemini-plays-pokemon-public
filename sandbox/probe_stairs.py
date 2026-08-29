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
    print("probe_stairs: Walking to 2F East stairs...")
    pos = mgba.get_coordinates()
    # Path from current (9, 11) to (22, 1) on 2F East
    # We can go UP to Row 1, then RIGHT to (22, 1)
    path = []
    for y in range(10, 0, -1):
        path.append((9, y))
    for x in range(10, 23):
        path.append((x, 1))
        
    if not walk_path(path):
        print("Walking to stairs failed.")
        return
        
    # We are at (22, 1). Let's test stepping off and back onto (22, 1) to see if we can warp!
    # Stand at (21, 1), step Right to (22, 1)
    print("Testing warp at (22, 1) from the Left side...")
    pos_before = mgba.get_coordinates()
    mgba.press_buttons(["Left"]) # Step to (21, 1)
    time.sleep(0.4)
    print(f"Position at (21, 1): {mgba.get_coordinates()}")
    
    mgba.press_buttons(["Right"]) # Step onto (22, 1)
    time.sleep(1.0)
    print(f"Position after stepping Right onto (22, 1): {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
