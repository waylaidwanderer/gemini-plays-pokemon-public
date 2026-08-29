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
        else:
            time.sleep(0.2)
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
    print("walk_to_balcony_v2: Starting...")
    pos = mgba.get_coordinates()
    print(f"Current pos: {pos}")
    
    path = [
        (11, 7), (12, 7),
        (12, 8), (12, 9), (12, 10), (12, 11), (12, 12), (12, 13), (12, 14), (12, 15), (12, 16),
        (13, 16), (14, 16), (15, 16), (16, 16),
        (16, 17), (16, 18),
        (17, 18), (18, 18), (19, 18)
    ]
    
    pos_tuple = (pos['x'], pos['y'])
    if pos_tuple in path:
        idx = path.index(pos_tuple)
        path = path[idx+1:]
        print(f"Sliced path to start from index {idx+1}: {path}")
    
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
