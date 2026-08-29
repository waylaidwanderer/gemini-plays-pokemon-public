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
        if not step_one(None, target_x, target_y): # automatic direction
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
    
    # Path to (2, 6)
    path = [
        (26, 5), (26, 4), (26, 3), (26, 2), (26, 1),
        (25, 1), (24, 1), (23, 1), (22, 1), (21, 1), (20, 1), (19, 1), (18, 1), (17, 1), (16, 1), (15, 1), (14, 1), (13, 1), (12, 1), (11, 1), (10, 1), (9, 1), (8, 1), (7, 1), (6, 1), (5, 1), (4, 1),
        (4, 2), (4, 3), (4, 4), (4, 5),
        (3, 5), (3, 6), (2, 6)
    ]
    
    pos_tuple = (pos['x'], pos['y'])
    if pos_tuple in path:
        idx = path.index(pos_tuple)
        path = path[idx+1:]
        print(f"Sliced path: {path}")
        
    if not walk_path(path):
        print("Failed to reach (2, 6)")
        return
        
    print("Reached (2, 6). Facing UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    # Let's interact with the switch step-by-step and take screenshots!
    print("Interacting with the switch...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    img1 = mgba.take_screenshot()
    print(f"Pressed A (1). Screenshot saved to: {img1}")
    
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    img2 = mgba.take_screenshot()
    print(f"Pressed A (2). Screenshot saved to: {img2}")
    
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    img3 = mgba.take_screenshot()
    print(f"Pressed A (3). Screenshot saved to: {img3}")
    
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    img4 = mgba.take_screenshot()
    print(f"Pressed A (4). Screenshot saved to: {img4}")
    
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    img5 = mgba.take_screenshot()
    print(f"Pressed A (5). Screenshot saved to: {img5}")
    
if __name__ == "__main__":
    main()
