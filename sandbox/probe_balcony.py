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
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    mgba.press_buttons(["Down", "sleep 250", "Right", "sleep 250", "A", "sleep 1000", "B"])
    time.sleep(1.5)

def step_one(direction, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"Moving {direction} to ({target_x}, {target_y}). Current: {pos_before}")
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        if is_in_battle():
            handle_battle_escape()
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
        
        # Fall check
        pos_before = mgba.get_coordinates()
        if not step_one(direction, target_x, target_y):
            pos_after = mgba.get_coordinates()
            if abs(pos_after['x'] - pos_before['x']) > 2 or abs(pos_after['y'] - pos_before['y']) > 2:
                print(f"WARPED/FELL! Landed at {pos_after}")
                return "WARPED"
            return False
            
        pos_after = mgba.get_coordinates()
        if abs(pos_after['x'] - pos_before['x']) > 2 or abs(pos_after['y'] - pos_before['y']) > 2:
            print(f"WARPED/FELL! Landed at {pos_after}")
            return "WARPED"
    return True

def main():
    print("probe_balcony: Starting...")
    pos = mgba.get_coordinates()
    print(f"Start pos: {pos}")
    
    # Path to (26, 11) on 3F East
    # We are at (20, 5)
    path = [
        # Up to Row 3
        (20, 4), (20, 3),
        # Right to Column 26
        (21, 3), (22, 3), (23, 3), (24, 3), (25, 3), (26, 3),
        # Down to Row 11
        (26, 4), (26, 5), (26, 6), (26, 7), (26, 8), (26, 9), (26, 10), (26, 11)
    ]
    
    if not walk_path(path):
        print("Failed to reach (26, 11).")
        return
        
    # We are at (26, 11). Let's see how far south we can go on Column 26!
    print("Trying to go Down Column 26 as far as possible...")
    for y in range(12, 20):
        if not step_one("Down", 26, y):
            print(f"Blocked moving Down at Row {y}.")
            break
            
    pos_now = mgba.get_coordinates()
    print(f"Current position: {pos_now}")
    
    # Try to go Left as far as possible
    print("Trying to go Left...")
    for x in range(pos_now['x'] - 1, 15, -1):
        res = step_one("Left", x, pos_now['y'])
        if res == "WARPED":
            return
        elif not res:
            print(f"Blocked moving Left at Column {x}.")
            break
            
    print(f"Final probing position: {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
