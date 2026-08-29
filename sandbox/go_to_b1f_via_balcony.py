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
    print("go_to_b1f_via_balcony: Starting...")
    pos = mgba.get_coordinates()
    print(f"Start pos: {pos}")
    
    # Complete, continuous path from (19, 16) to balcony drop at (19, 18)
    path = [
        # 1. Walk Right along Row 16 to Column 24
        (20, 16), (21, 16), (22, 16), (23, 16), (24, 16),
        # 2. Walk Up Column 24 to Row 3
        (24, 15), (24, 14), (24, 13), (24, 12), (24, 11), (24, 10), (24, 9), (24, 8), (24, 7), (24, 6), (24, 5), (24, 4), (24, 3),
        # 3. Walk Left along Row 3 to Column 10
        (23, 3), (22, 3), (21, 3), (20, 3), (19, 3), (18, 3), (17, 3), (16, 3), (15, 3), (14, 3), (13, 3), (12, 3), (11, 3), (10, 3),
        # 4. Walk Down Column 10 to Row 16
        (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10), (10, 11), (10, 12), (10, 13), (10, 14), (10, 15), (10, 16),
        # 5. Walk Right along Row 16 to Column 16
        (11, 16), (12, 16), (13, 16), (14, 16), (15, 16), (16, 16),
        # 6. Walk Down Column 16 to the balcony grass
        (16, 17), (16, 18),
        # 7. Walk Right along Row 18 (balcony grass) to Column 19
        (17, 18), (18, 18), (19, 18)
    ]
    
    pos_tuple = (pos['x'], pos['y'])
    if pos_tuple in path:
        start_idx = path.index(pos_tuple)
        path = path[start_idx+1:]
        
    print(f"Walking path to balcony: {path}")
    res = walk_path(path)
    if res == "WARPED":
        print("Warped unexpectedly on path!")
        return
    elif not res:
        print("Walking to balcony failed.")
        return
        
    # We are at (19, 18) on the balcony grass. Let's walk Down to trigger the fall!
    print("At (19, 18). Stepping Down to trigger balcony drop...")
    mgba.press_buttons(["Down"])
    time.sleep(1.0)
    
    pos_end = mgba.get_coordinates()
    print(f"Position after drop attempt: {pos_end}")
    if pos_end['y'] != 18:
        print("SUCCESSFULLY FELL TO B1F!!!")
    else:
        print("Failed to drop.")

if __name__ == "__main__":
    main()
