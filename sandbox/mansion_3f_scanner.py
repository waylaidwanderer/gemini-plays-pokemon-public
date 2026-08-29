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
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    mgba.press_buttons(["B"])
    time.sleep(1.0)

def step_one(direction, target_x, target_y):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        if is_in_battle():
            handle_battle_escape()
            mgba.press_buttons([direction])
            time.sleep(0.4)
            pos_after = mgba.get_coordinates()
            
    # Warp/Fall check
    if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 2 or abs(pos_after['y'] - pos_before['y']) > 2):
        print(f"WARPED/FELL! Landed at: {pos_after} from {pos_before}")
        return "WARPED"
        
    if pos_after['x'] == target_x and pos_after['y'] == target_y:
        return "SUCCESS"
    else:
        return "BLOCKED"

def walk_to(target_x, target_y):
    pos = mgba.get_coordinates()
    while pos['x'] != target_x or pos['y'] != target_y:
        dx = target_x - pos['x']
        dy = target_y - pos['y']
        
        if dx > 0:
            res = step_one("Right", pos['x'] + 1, pos['y'])
        elif dx < 0:
            res = step_one("Left", pos['x'] - 1, pos['y'])
        elif dy > 0:
            res = step_one("Down", pos['x'], pos['y'] + 1)
        elif dy < 0:
            res = step_one("Up", pos['x'], pos['y'] - 1)
            
        if res == "WARPED":
            return "WARPED"
        elif res == "BLOCKED":
            return "BLOCKED"
        pos = mgba.get_coordinates()
    return "SUCCESS"

def main():
    print("mansion_3f_scanner_v2: Starting scan of Rows 8, 9, 10...")
    pos = mgba.get_coordinates()
    
    # We are currently at (23, 7).
    # Walk to and scan:
    # Row 8: (23, 8), (26, 8), (27, 8)
    # Row 9: (23, 9), (26, 9), (27, 9)
    # Row 10: (23, 10), (24, 10), (25, 10), (26, 10), (27, 10)
    # We will try to walk to all of these systematically.
    scan_points = [
        (23, 8), (23, 9), (23, 10),
        (24, 10), (25, 10), (26, 10), (27, 10),
        (27, 9), (27, 8),
        (26, 8), (26, 9)
    ]
    
    for target in scan_points:
        res = walk_to(target[0], target[1])
        if res == "WARPED":
            print("FOUND THE PITFALL!!!")
            return
            
    print("Scan complete. No pitfall found.")

if __name__ == "__main__":
    main()
