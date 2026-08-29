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
    
    if pos_after['y'] < 0 or pos_after['y'] > 18:
        print(f"move_safe_battle: FELL THROUGH PITFALL! Current: {pos_after}")
        return True
        
    attempts = 0
    while (pos_after['x'] != target_x or pos_after['y'] != target_y) and attempts < 4:
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
                
        print(f"move_safe_battle: Retrying step '{step}'...")
        mgba.press_buttons([step])
        time.sleep(0.4)
        pos_before = pos_after
        pos_after = mgba.get_coordinates()
        attempts += 1
        
    return pos_after['x'] == target_x and pos_after['y'] == target_y

def main():
    print("probe_3f_east_state_b_more: Starting from (27, 5)...")
    
    # 1. Walk Right to (28, 5)
    if not move_safe_battle("Right", 28, 5): return
    
    # 2. Test Down to (28, 6)
    print("Testing (28, 6)...")
    if not move_safe_battle("Down", 28, 6):
        print("Blocked. (28, 6) is solid.")
    else:
        # Test Down to (28, 7)
        print("Testing (28, 7)...")
        if not move_safe_battle("Down", 28, 7):
            print("Blocked. (28, 7) is solid.")
        else:
            # Walk back
            move_safe_battle("Up", 28, 6)
            move_safe_battle("Up", 28, 5)
            
    print("Completed probing of Column 28.")

if __name__ == "__main__":
    main()
