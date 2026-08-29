import mgba
import time
from PIL import Image

def step_one(direction, target_x, target_y):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    if pos_after['x'] == target_x and pos_after['y'] == target_y:
        return True
    return False

def walk_path(coords):
    for target_x, target_y in coords:
        pos_before = mgba.get_coordinates()
        dx = target_x - pos_before['x']
        dy = target_y - pos_before['y']
        direction = "Right" if dx > 0 else "Left" if dx < 0 else "Down" if dy > 0 else "Up"
        if not step_one(direction, target_x, target_y):
            return False
    return True

def main():
    print("debug_switch: Starting...")
    pos = mgba.get_coordinates()
    print(f"Current pos: {pos}")
    
    # Sliced path from (26, 1) to (2, 6) via Row 1
    path = [
        (25, 1), (24, 1), (23, 1), (22, 1), (21, 1), (20, 1), (19, 1), (18, 1), (17, 1), (16, 1), (15, 1), (14, 1), (13, 1), (12, 1), (11, 1), (10, 1), (9, 1), (8, 1), (7, 1), (6, 1), (5, 1), (4, 1),
        (4, 2), (4, 3), (4, 4), (4, 5),
        (3, 5), (3, 6), (2, 6)
    ]
    
    pos_tuple = (pos['x'], pos['y'])
    if pos_tuple in path:
        idx = path.index(pos_tuple)
        path = path[idx+1:]
        print(f"Sliced path to start from index {idx+1}: {path}")
        
    if not walk_path(path):
        print("Failed to reach (2, 6)")
        return
        
    print("Reached (2, 6). Facing UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    # Step-by-step switch interaction with screenshots!
    print("Interacting with switch step 1...")
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    s0 = mgba.take_screenshot()
    print(f"Saved step 1 screenshot to: {s0}")
    
    print("Interacting with switch step 2...")
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    s1 = mgba.take_screenshot()
    print(f"Saved step 2 screenshot to: {s1}")
    
    print("Interacting with switch step 3 (UP)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    s2 = mgba.take_screenshot()
    print(f"Saved step 3 (UP) screenshot to: {s2}")
    
    print("Interacting with switch step 4...")
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    s3 = mgba.take_screenshot()
    print(f"Saved step 4 screenshot to: {s3}")
    
    print("Interacting with switch step 5...")
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    s4 = mgba.take_screenshot()
    print(f"Saved step 5 screenshot to: {s4}")
    
    print("Interacting with switch step 6...")
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    s5 = mgba.take_screenshot()
    print(f"Saved step 6 screenshot to: {s5}")

if __name__ == "__main__":
    main()
