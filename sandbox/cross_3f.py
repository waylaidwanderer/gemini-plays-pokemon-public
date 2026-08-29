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
        return True
    else:
        mgba.press_buttons(["Start"])
        time.sleep(0.2)
        return False

def handle_battle_escape():
    print("handle_battle_escape: ESCAPING BATTLE!")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    mgba.press_buttons(["B"])
    time.sleep(1.0)

def move_safe_battle(step, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"move_safe_battle: Attempting to move '{step}' to ({target_x}, {target_y}). Current: {pos_before}")
    mgba.press_buttons([step])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    
    attempts = 0
    while (pos_after['x'] != target_x or pos_after['y'] != target_y) and attempts < 6:
        if pos_before == pos_after:
            print("move_safe_battle: Position did not change. Checking for battle...")
            if is_in_battle():
                handle_battle_escape()
            else:
                print("move_safe_battle: Overworld turn-in-place or obstruction. Retrying...")
        else:
            print(f"move_safe_battle: Moved to {pos_after} instead of target ({target_x}, {target_y}). Checking battle...")
            if is_in_battle():
                handle_battle_escape()
                
        print(f"move_safe_battle: Retrying step '{step}'...")
        mgba.press_buttons([step])
        time.sleep(0.4)
        pos_before = pos_after
        pos_after = mgba.get_coordinates()
        attempts += 1
        
    arrived = (pos_after['x'] == target_x and pos_after['y'] == target_y)
    print(f"move_safe_battle: Arrived: {arrived}. Final position: {pos_after}")
    return arrived

def test_row_3():
    # We are at (19, 4)
    pos = mgba.get_coordinates()
    print(f"test_row_3: Starting at {pos}")
    
    # 1. Walk right to (20, 4) and try to walk UP to (20, 3)
    move_safe_battle("Right", 20, 4)
    print("test_row_3: Testing Column 20 Row 3 (20, 3)...")
    success20 = move_safe_battle("Up", 20, 3)
    if success20:
        print("test_row_3: Column 20 Row 3 is OPEN!")
        return 20
    else:
        print("test_row_3: Column 20 Row 3 is CLOSED.")
        
    # 2. Walk right to (21, 4) and try to walk UP to (21, 3)
    # Note: we are currently back at (20, 4) if UP failed
    move_safe_battle("Right", 21, 4)
    print("test_row_3: Testing Column 21 Row 3 (21, 3)...")
    success21 = move_safe_battle("Up", 21, 3)
    if success21:
        print("test_row_3: Column 21 Row 3 is OPEN!")
        return 21
    else:
        print("test_row_3: Column 21 Row 3 is CLOSED.")
        
    return None

if __name__ == "__main__":
    test_row_3()
