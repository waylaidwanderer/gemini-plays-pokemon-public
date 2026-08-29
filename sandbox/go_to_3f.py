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
            
    # Warp check
    if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 2 or abs(pos_after['y'] - pos_before['y']) > 2):
        print(f"WARPED! Landed at: {pos_after}")
        return True
        
    return pos_after['x'] == target_x and pos_after['y'] == target_y

def main():
    print("go_to_3f: Moving back to 3F West...")
    pos = mgba.get_coordinates()
    print(f"Start: {pos}")
    
    # 1. Walk Left to (12, 6)
    if pos['y'] == 6 and pos['x'] > 12:
        print("Walking left along Row 6 to Column 12...")
        for x in range(pos['x'] - 1, 11, -1):
            if not step_one("Left", x, 6): return
            
    pos = mgba.get_coordinates()
    # 2. Walk Down Column 12 to Row 11 (12, 11)
    if pos['x'] == 12 and pos['y'] < 11:
        print("Walking down Column 12 to Row 11...")
        for y in range(pos['y'] + 1, 12):
            if not step_one("Down", 12, y): return
            
    pos = mgba.get_coordinates()
    # 3. Walk Left to (7, 11)
    if pos['x'] == 12 and pos['y'] == 11:
        print("Walking left to Column 7...")
        for x in range(11, 6, -1):
            if not step_one("Left", x, 11): return
            
    pos = mgba.get_coordinates()
    # 4. Step UP onto stairs at (7, 10) to warp to 3F West
    if pos['x'] == 7 and pos['y'] == 11:
        print("Stepping onto stairs...")
        mgba.press_buttons(["Up"])
        time.sleep(1.5) # Wait for map transition to 3F West
        
    print(f"Landed on 3F West? Position: {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
