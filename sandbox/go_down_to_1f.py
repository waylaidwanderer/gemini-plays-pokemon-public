import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def walk_to_target(target_x, target_y):
    print(f"Walking to ({target_x}, {target_y})...")
    for step in range(25):
        cx, cy = get_pos()
        if cx == target_x and cy == target_y:
            print(f"Arrived at ({cx}, {cy})")
            return True
            
        dx = target_x - cx
        dy = target_y - cy
        
        if dx != 0:
            btn = "Right" if dx > 0 else "Left"
            press_and_wait(btn, 0.3)
        elif dy != 0:
            btn = "Down" if dy > 0 else "Up"
            press_and_wait(btn, 0.3)
            
        # Verify we moved
        nx, ny = get_pos()
        if nx == cx and ny == cy:
            print(f"BUMPED at ({cx}, {cy}) trying to go to ({target_x}, {target_y})!")
            return False
            
    return False

def go_down_to_1f_perfect():
    print("Starting descent from 5F at:", get_pos())
    
    # 1. Close text box
    print("Closing text box...")
    press_and_wait("B", 0.5)
    
    # 2. 5F -> 4F (DOWN escalator at 16, 1)
    print("--- 5F to 4F ---")
    if not walk_to_target(16, 2):
        return False
    print("Stepping UP into DOWN escalator on 5F...")
    press_and_wait("Up", 1.0)
    time.sleep(0.5)
    print("Arrived on 4F at:", get_pos())
    
    # 3. 4F -> 3F (DOWN escalator at 16, 1)
    print("--- 4F to 3F ---")
    if not walk_to_target(16, 2):
        return False
    print("Stepping UP into DOWN escalator on 4F...")
    press_and_wait("Up", 1.0)
    time.sleep(0.5)
    print("Arrived on 3F at:", get_pos())
    
    # 4. 3F -> 2F (DOWN escalator at 16, 1)
    print("--- 3F to 2F ---")
    if not walk_to_target(16, 2):
        return False
    print("Stepping UP into DOWN escalator on 3F...")
    press_and_wait("Up", 1.0)
    time.sleep(0.5)
    print("Arrived on 2F at:", get_pos())
    
    # 5. 2F -> 1F (DOWN escalator at 16, 1)
    print("--- 2F to 1F ---")
    if not walk_to_target(16, 2):
        return False
    print("Stepping UP into DOWN escalator on 2F...")
    press_and_wait("Up", 1.0)
    time.sleep(0.5)
    print("Arrived on 1F at:", get_pos())
    
    # 6. Exit 1F to Celadon City
    print("--- Exiting 1F ---")
    # Walk Left 8 steps on Row 2 to Column 8 (8, 2)
    if not walk_to_target(8, 2):
        return False
    # Walk Down 5 steps to Row 7 (8, 7)
    if not walk_to_target(8, 7):
        return False
        
    print("Stepping DOWN to exit the store...")
    press_and_wait("Down", 1.5) # Longer wait for map transition
    
    # Verify outside
    final_x, final_y = get_pos()
    print("Final position outside:", (final_x, final_y))
    if final_y > 7 or final_x == 10:
        print("SUCCESS! Successfully exited the Department Store!")
        mgba.take_screenshot()
        return True
    else:
        print("FAILED to exit the store. We are at:", (final_x, final_y))
        mgba.take_screenshot()
        return False

go_down_to_1f_perfect()
