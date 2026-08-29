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
    print("debug_switch: Walking to switch to take dialogue screenshot...")
    # Sliced path from (26, 6) to (2, 6) via Row 1
    path = [
        (26, 5), (26, 4), (26, 3), (26, 2), (26, 1),
        (25, 1), (24, 1), (23, 1), (22, 1), (21, 1), (20, 1), (19, 1), (18, 1), (17, 1), (16, 1), (15, 1), (14, 1), (13, 1), (12, 1), (11, 1), (10, 1), (9, 1), (8, 1), (7, 1), (6, 1), (5, 1), (4, 1),
        (4, 2), (4, 3), (4, 4), (4, 5),
        (3, 5), (3, 6), (2, 6)
    ]
    
    if not walk_path(path):
        print("Failed to reach (2, 6)")
        return
        
    print("Reached (2, 6). Facing UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    # Interacting and taking a screenshot of the prompt!
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Take screenshot of the YES/NO prompt!
    screenshot = mgba.take_screenshot()
    print(f"Captured prompt screenshot: {screenshot}")
    
    # Keep it there so we can see it on the next overworld frame!
    
if __name__ == "__main__":
    main()
