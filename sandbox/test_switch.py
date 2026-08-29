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
    print("test_switch: Executing switch-testing sequence...")
    # Currently at (1, 12)
    
    # 1. Down to (1, 13)
    if not step_one("Down", 1, 13):
        print("Failed to move to (1, 13)")
        return
        
    # 2. Right to (2, 13)
    if not step_one("Right", 2, 13):
        print("Failed to move to (2, 13)")
        return
        
    # 3. Try Up to (2, 12)
    print("Testing UP to (2, 12)...")
    success = step_one("Up", 2, 12)
    pos = mgba.get_coordinates()
    print(f"At (2, 12)? {'YES' if success else 'NO'}. Position: {pos}")
    
    # 4. If we failed, let's print out what is walkable from (2, 13)
    if not success:
        print("Trying to walk UP again to be absolutely sure...")
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        if pos['x'] == 2 and pos['y'] == 12:
            print("Succeeded on second try!")
            success = True
            
    if success:
        print("Standing at (2, 12). Facing UP towards Mewtwo switch...")
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        print("Interacting with switch...")
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        print("Switch interact complete. Checking coordinates:")
        print(mgba.get_coordinates())
    else:
        print("Unable to reach (2, 12). The gate at (2, 12) is CLOSED!")

if __name__ == "__main__":
    main()
