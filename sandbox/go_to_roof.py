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
    for step in range(20):
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

def go_to_roof_verified():
    # Start on 2F at (14, 2) with textbox open
    print("Starting from:", get_pos())
    
    # 1. Close text box
    print("Closing text box...")
    press_and_wait("B", 0.5)
    
    # 2. 2F -> 3F (UP stairs at 16, 1)
    print("--- 2F to 3F ---")
    if not walk_to_target(16, 2):
        return False
    print("Stepping UP into stairs...")
    press_and_wait("Up", 1.0)
    print("Arrived on 3F at:", get_pos())
    
    # 3. 3F -> 4F (UP stairs at 12, 1)
    print("--- 3F to 4F ---")
    if not walk_to_target(12, 2):
        return False
    print("Stepping UP into stairs...")
    press_and_wait("Up", 1.0)
    print("Arrived on 4F at:", get_pos())
    
    # 4. 4F -> 5F (UP stairs at 16, 1)
    print("--- 4F to 5F ---")
    if not walk_to_target(16, 2):
        return False
    print("Stepping UP into stairs...")
    press_and_wait("Up", 1.0)
    print("Arrived on 5F at:", get_pos())
    
    # 5. 5F -> Roof (UP stairs at 12, 1)
    print("--- 5F to Roof ---")
    if not walk_to_target(12, 2):
        return False
    print("Stepping UP into stairs...")
    press_and_wait("Up", 1.0)
    
    # Verify we are on the Roof
    final_x, final_y = get_pos()
    print("Final position:", (final_x, final_y))
    if final_x == 15 and final_y == 3:
        print("SUCCESS! Successfully arrived on the Roof!")
        return True
    else:
        print("FAILED to reach the Roof. We are at:", (final_x, final_y))
        return False

go_to_roof_verified()
