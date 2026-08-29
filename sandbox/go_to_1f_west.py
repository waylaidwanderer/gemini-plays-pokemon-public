from PIL import Image, ImageChops
import mgba
import time

def is_in_battle():
    img1_path = mgba.take_screenshot()
    img1 = Image.open(img1_path)
    mgba.press_buttons(["Start"])
    time.sleep(0.2)
    img2_path = mgba.take_screenshot()
    img2 = Image.open(img2_path)
    diff = ImageChops.difference(img1, img2)
    bbox = diff.getbbox()
    if bbox is None:
        print("is_in_battle: TRUE")
        return True
    else:
        print("is_in_battle: FALSE. Closing menu...")
        mgba.press_buttons(["Start"])
        time.sleep(0.2)
        return False

def handle_battle_escape():
    print("handle_battle_escape: ESCAPING BATTLE...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    mgba.press_buttons(["B"])
    time.sleep(1.0)

def move_safe_battle(step, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"move_safe_battle: Moving '{step}' to ({target_x}, {target_y}). Current: {pos_before}")
    mgba.press_buttons([step])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    
    attempts = 0
    while (pos_after['x'] != target_x or pos_after['y'] != target_y) and attempts < 6:
        if pos_before == pos_after:
            print("move_safe_battle: Position did not change. Checking battle...")
            if is_in_battle():
                handle_battle_escape()
            else:
                print("move_safe_battle: Turn-in-place or wall. Bailing...")
                return False
        else:
            print(f"move_safe_battle: Moved but to {pos_after} instead of target ({target_x}, {target_y}). Checking battle...")
            if is_in_battle():
                handle_battle_escape()
            else:
                print("move_safe_battle: Unexpected overworld movement.")
                
        print(f"move_safe_battle: Retrying step '{step}'...")
        mgba.press_buttons([step])
        time.sleep(0.4)
        pos_before = pos_after
        pos_after = mgba.get_coordinates()
        attempts += 1
        
    return pos_after['x'] == target_x and pos_after['y'] == target_y

def main():
    print("go_to_1f_west: Starting...")
    
    # We are at (20, 2)
    if not move_safe_battle("Down", 20, 3): return
    if not move_safe_battle("Down", 20, 4): return
    if not move_safe_battle("Left", 19, 4): return
    if not move_safe_battle("Down", 19, 5): return
    if not move_safe_battle("Down", 19, 6): return
    
    # Try to walk LEFT on Row 6 as far as possible to see if Column 18 is open!
    print("Attempting to walk LEFT along Row 6 to Column 5...")
    for x in range(18, 4, -1):
        if not move_safe_battle("Left", x, 6):
            print(f"Blocked at Column {x}!")
            return
            
    print(f"Successfully reached 1F West at {mgba.get_coordinates()}!")

if __name__ == "__main__":
    main()
