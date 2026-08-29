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
    # Mash B to clear transition
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    # Run from battle
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
        pos_before = mgba.get_coordinates()
        dx = target_x - pos_before['x']
        dy = target_y - pos_before['y']
        
        direction = ""
        if dx > 0: direction = "Right"
        elif dx < 0: direction = "Left"
        elif dy > 0: direction = "Down"
        elif dy < 0: direction = "Up"
        
        if not step_one(direction, target_x, target_y):
            pos_after = mgba.get_coordinates()
            if abs(pos_after['x'] - pos_before['x']) > 2 or abs(pos_after['y'] - pos_before['y']) > 2:
                print(f"WARPED/FELL! Landed at {pos_after}")
                return "WARPED"
            return False
    return True

def main():
    print("walk_to_balcony: Starting...")
    pos = mgba.get_coordinates()
    print(f"Current pos: {pos}")
    
    path = [
        (25, 10), (26, 10),
        (26, 9), (26, 8), (26, 7), (26, 6), (26, 5), (26, 4), (26, 3),
        (25, 3), (24, 3), (23, 3), (22, 3), (21, 3), (20, 3), (19, 3), (18, 3), (17, 3), (16, 3), (15, 3), (14, 3), (13, 3), (12, 3), (11, 3), (10, 3),
        (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10), (10, 11), (10, 12), (10, 13), (10, 14), (10, 15), (10, 16),
        (11, 16), (12, 16), (13, 16), (14, 16), (15, 16), (16, 16),
        (16, 17), (16, 18),
        (17, 18), (18, 18), (19, 18)
    ]
    
    res = walk_path(path)
    if res == "WARPED":
        print("Warped unexpectedly on path!")
        return
    elif not res:
        print("Walking to balcony failed.")
        return
        
    print("At (19, 18). Stepping Down to trigger balcony drop...")
    mgba.press_buttons(["Down"])
    time.sleep(1.0)
    
    pos_end = mgba.get_coordinates()
    print(f"Position after drop attempt: {pos_end}")
    if pos_end['y'] != 18 or pos_end['x'] != 19:
        print("SUCCESSFULLY FELL TO B1F!!!")
    else:
        print("Failed to drop.")

if __name__ == "__main__":
    main()
