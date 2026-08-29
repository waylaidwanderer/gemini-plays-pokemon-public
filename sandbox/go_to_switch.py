import mgba
import time
from PIL import Image, ImageChops

def is_in_battle():
    img1_path = mgba.take_screenshot()
    img1 = Image.open(img1_path)
    mgba.press_buttons(["Start"])
    time.sleep(0.25)
    img2_path = mgba.take_screenshot()
    img2 = Image.open(img2_path)
    diff = ImageChops.difference(img1, img2)
    bbox = diff.getbbox()
    if bbox is None:
        return True
    else:
        mgba.press_buttons(["Start"])
        time.sleep(0.25)
        return False

def handle_battle_escape():
    print("ESCAPING BATTLE...")
    # Spam B first to clear text
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    # Press Down, Right, A to RUN
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    # Press B to dismiss any run failure or text
    mgba.press_buttons(["B"])
    time.sleep(0.5)

def step_one(direction, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"Moving {direction} to ({target_x}, {target_y}). Current: {pos_before}")
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        if is_in_battle():
            handle_battle_escape()
            # Retry after escape
            mgba.press_buttons([direction])
            time.sleep(0.4)
            pos_after = mgba.get_coordinates()
            
    if pos_after['x'] == target_x and pos_after['y'] == target_y:
        return True
    else:
        print(f"Failed to move to ({target_x}, {target_y}). Ended up at: {pos_after}")
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
            # Check if we got into a battle that we couldn't escape or if we were blocked
            return False
    return True

def main():
    print("Starting walk path to switch...")
    # Let's define the path from (1, 8) to (2, 12)
    path = [
        (1, 7),
        (2, 7),
        (3, 7),
        (3, 6),
        (3, 5),
        (3, 4),
        (4, 4),
        # Wait, let's see if we can go UP on Column 4 to Row 2
        (4, 3),
        (4, 2),
        # Walk RIGHT along Row 2 to Column 10
        (5, 2),
        (6, 2),
        (7, 2),
        (8, 2),
        (9, 2),
        (10, 2),
        # Walk DOWN Column 10 to Row 11
        (10, 3),
        (10, 4),
        (10, 5),
        (10, 6),
        (10, 7),
        (10, 8),
        (10, 9),
        (10, 10),
        (10, 11),
        # Walk LEFT along Row 11 to Column 2
        (9, 11),
        (8, 11),
        (7, 11),
        (6, 11),
        (5, 11),
        (4, 11),
        (3, 11),
        (2, 11),
        # Walk DOWN to (2, 12)
        (2, 12)
    ]
    
    success = walk_path(path)
    if success:
        print("ARRIVED AT SWITCH AT (2, 12)!")
        # Face UP
        mgba.press_buttons(["Up"])
        time.sleep(0.3)
    else:
        print("FAILED to walk path.")

if __name__ == "__main__":
    main()
