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
            
    return pos_after['x'] == target_x and pos_after['y'] == target_y

def main():
    print("test_row_7_east: Starting from current position...")
    pos = mgba.get_coordinates()
    print(f"Start coordinates: {pos}")
    
    # We are at (18, 6)
    # Test Column 19 Row 7
    print("Testing DOWN Column 19...")
    if step_one("Right", 19, 6):
        success = step_one("Down", 19, 7)
        pos = mgba.get_coordinates()
        print(f"  At (19, 7)? {'YES' if success else 'NO'}. Position: {pos}")
        if success:
            # Backtrack
            step_one("Up", 19, 6)
            step_one("Left", 18, 6)
            return
            
    # Test Column 20 Row 7
    print("Testing DOWN Column 20...")
    if step_one("Right", 20, 6):
        success = step_one("Down", 20, 7)
        pos = mgba.get_coordinates()
        print(f"  At (20, 7)? {'YES' if success else 'NO'}. Position: {pos}")
        if success:
            # Backtrack
            step_one("Up", 20, 6)
            step_one("Left", 19, 6)
            step_one("Left", 18, 6)
            return
            
    # Test Column 21 Row 7
    print("Testing DOWN Column 21...")
    if step_one("Right", 21, 6):
        success = step_one("Down", 21, 7)
        pos = mgba.get_coordinates()
        print(f"  At (21, 7)? {'YES' if success else 'NO'}. Position: {pos}")
        if success:
            # Backtrack
            step_one("Up", 21, 6)
            step_one("Left", 20, 6)
            step_one("Left", 19, 6)
            step_one("Left", 18, 6)
            return

    # Go back to (18, 6)
    pos = mgba.get_coordinates()
    if pos['x'] != 18 or pos['y'] != 6:
        print(f"Restoring to (18, 6). Current: {pos}")
        if pos['y'] == 6:
            for x in range(pos['x'] - 1, 17, -1):
                step_one("Left", x, 6)

if __name__ == "__main__":
    main()
