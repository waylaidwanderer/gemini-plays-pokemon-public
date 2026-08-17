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

def go_down_to_1f():
    print("Starting descent from Roof at:", get_pos())
    
    # 1. Roof -> 5F
    # Walk to (15, 3) and UP to (15, 2)
    if not walk_to_target(15, 3):
        return False
    print("Stepping UP into stairs...")
    press_and_wait("Up", 1.0)
    print("Arrived on 5F at:", get_pos())
    
    # 2. 5F -> 4F (DOWN escalator at 16, 1)
    if not walk_to_target(16, 2):
        return False
    print("Stepping UP into DOWN escalator...")
    press_and_wait("Up", 1.0)
    print("Arrived on 4F at:", get_pos())
    
    # 3. 4F -> 3F (DOWN escalator at 16, 1)
    print("Stepping UP into DOWN escalator...")
    press_and_wait("Up", 1.0)
    print("Arrived on 3F at:", get_pos())
    
    # 4. 3F -> 2F (DOWN escalator at 16, 1)
    print("Stepping UP into DOWN escalator...")
    press_and_wait("Up", 1.0)
    print("Arrived on 2F at:", get_pos())
    
    # 5. 2F -> 1F (DOWN escalator at 16, 1)
    print("Stepping UP into DOWN escalator...")
    press_and_wait("Up", 1.0)
    print("Arrived on 1F at:", get_pos())
    
    # 6. Exit 1F to Celadon City
    # Walk DOWN 5 steps to (16, 7)
    print("Walking down to 1F exit...")
    for _ in range(5):
        press_and_wait("Down", 0.3)
    time.sleep(1.0)
    print("Final outside position:", get_pos())

go_down_to_1f()
