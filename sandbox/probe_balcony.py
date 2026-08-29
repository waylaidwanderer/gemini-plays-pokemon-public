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
    print("probe_balcony_v3: Starting...")
    pos = mgba.get_coordinates()
    print(f"Start pos: {pos}")
    
    # We are at (19, 16)
    # Walk Left to Column 16, then Down to the balcony
    path = [
        # Walk Left to (16, 16)
        (18, 16), (17, 16), (16, 16),
        # Walk Down to (16, 18)
        (16, 17), (16, 18),
        # Walk Right to (19, 18)
        (17, 18), (18, 18), (19, 18)
    ]
    
    res = walk_path(path)
    if res == "WARPED":
        print("Warped from path!")
        return
    elif not res:
        print("Failed on path.")
        return
        
    # We are at (19, 18). Let's go DOWN to trigger the balcony fall!
    print("Trying to go Down from (19, 18) to trigger balcony fall...")
    res = step_one("Down", 19, 19)
    if res == "WARPED" or mgba.get_coordinates()['y'] != 18:
        print("SUCCESSFULLY FELL FROM BALCONY TO B1F!!!")
        time.sleep(1.0)
        print(f"Landed at: {mgba.get_coordinates()}")
    else:
        print(f"Failed to drop. Current pos: {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
