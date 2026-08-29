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
        # Check if we warped to 2F West (landing at (5, 11) or (5, 10))
        if target_x == 5 and target_y == 10 and pos_after['x'] == 5 and pos_after['y'] == 11:
            print("move_safe_battle: Successfully warped to 2F West!")
            break
            
        if pos_before == pos_after:
            print("move_safe_battle: Position did not change. Checking battle...")
            if is_in_battle():
                handle_battle_escape()
            else:
                print("move_safe_battle: Turn-in-place or wall. Retrying...")
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
        
    return (pos_after['x'] == target_x and pos_after['y'] == target_y) or (target_x == 5 and target_y == 10 and pos_after['x'] == 5 and pos_after['y'] == 11)

def main():
    print("go_to_1f_west: Starting from (17, 6)...")
    pos = mgba.get_coordinates()
    print(f"Initial coordinates: {pos}")
    
    # 1. Walk Left Row 6 to Column 6
    for x in range(pos['x'] - 1, 5, -1):
        if not move_safe_battle("Left", x, 6): return
        
    # 2. Walk Down Column 6 to Row 10 (6, 10)
    for y in range(7, 11):
        if not move_safe_battle("Down", 6, y): return
        
    # 3. Step Left to (5, 10) and warp UP to 2F West
    print("Stepping onto stairs to warp UP to 2F West...")
    if move_safe_battle("Left", 5, 10):
        print(f"Coordinates after warp: {mgba.get_coordinates()}")
    else:
        print("Warp failed.")

if __name__ == "__main__":
    main()
