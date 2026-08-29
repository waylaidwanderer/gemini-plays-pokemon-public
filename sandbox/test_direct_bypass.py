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
        print(f"WARPED/FELL! Landed at: {pos_after}")
        return True
        
    return pos_after['x'] == target_x and pos_after['y'] == target_y

def main():
    print("Starting direct 2F bypass test...")
    pos = mgba.get_coordinates()
    print(f"Current pos: {pos}")
    
    # Walk DOWN Column 9 directly to Row 15 (9, 15)
    if pos['x'] == 9 and pos['y'] < 15:
        print("Walking down Column 9 to Row 15...")
        for y in range(pos['y'] + 1, 16):
            if not step_one("Down", 9, y):
                print(f"Failed to walk DOWN to (9, {y}).")
                return
        pos = mgba.get_coordinates()

    # Attempt to walk RIGHT along Row 15 directly to Column 12 (12, 15)
    if pos['y'] == 15 and pos['x'] < 12:
        print("Attempting to walk right on Row 15 directly to Column 12...")
        for x in range(pos['x'] + 1, 13):
            if not step_one("Right", x, 15):
                print(f"Failed to walk RIGHT to ({x}, 15).")
                return
        pos = mgba.get_coordinates()

    # Walk UP Column 12 directly to Row 3 (12, 3)
    if pos['x'] == 12 and pos['y'] > 3:
        print("Walking up Column 12 to Row 3...")
        for y in range(pos['y'] - 1, 2, -1):
            if not step_one("Up", 12, y):
                print(f"Failed to walk UP to (12, {y}).")
                return
        pos = mgba.get_coordinates()

    print(f"Success! Arrived at: {pos}")

if __name__ == "__main__":
    main()
