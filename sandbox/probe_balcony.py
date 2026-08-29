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
    print("probe_balcony_v4: Starting...")
    pos = mgba.get_coordinates()
    print(f"Start pos: {pos}")
    
    # We are at (19, 16).
    # 1. Walk back to (24, 13) on 3F East
    path_back = [
        # Right to Column 24
        (20, 16), (21, 16), (22, 16), (23, 16), (24, 16),
        # Up Column 24 to Row 13
        (24, 15), (24, 14), (24, 13),
        # Up to Row 11
        (24, 12), (24, 11),
        # Left along Row 11 to Column 16
        (23, 11), (22, 11), (21, 11), (20, 11), (19, 11), (18, 11), (17, 11), (16, 11)
    ]
    
    pos_tuple = (pos['x'], pos['y'])
    if pos_tuple in path_back:
        start_idx = path_back.index(pos_tuple)
        path_back = path_back[start_idx+1:]
        
    print(f"Walking path back and to (16, 11): {path_back}")
    if not walk_path(path_back):
        print("Failed to walk to (16, 11).")
        return
        
    # 2. Try to walk Down Column 16 to (16, 17) to drop!
    print("Trying to walk Down Column 16 to (16, 17)...")
    for y in range(12, 18):
        res = step_one("Down", 16, y)
        if res == "WARPED" or mgba.get_coordinates()['y'] > 17:
            print("SUCCESSFULLY FELL OR TRANSITIONED ON COLUMN 16!!!")
            time.sleep(1.0)
            print(f"Landed at: {mgba.get_coordinates()}")
            return
        elif not res:
            print(f"Blocked moving Down Column 16 at Row {y}.")
            break
            
    print(f"Ending position: {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
