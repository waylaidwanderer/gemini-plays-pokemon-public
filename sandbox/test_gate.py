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

def test_column_8():
    # We are at (4, 10)
    pos = mgba.get_coordinates()
    print(f"test_column_8: Starting at {pos}")
    
    # 1. Walk down to (4, 12)
    move_safe_battle("Down", 4, 11)
    move_safe_battle("Down", 4, 12)
    
    # 2. Walk right to (8, 12) -> wait, (8, 12) is the planter!
    # So we walk right to Column 6 Row 12, then Column 6 Row 13, then Column 8 Row 13, then Column 8 Row 10
    move_safe_battle("Right", 5, 12)
    move_safe_battle("Right", 6, 12)
    move_safe_battle("Down", 6, 13)
    move_safe_battle("Right", 7, 13)
    move_safe_battle("Right", 8, 13)
    move_safe_battle("Up", 8, 12) # wait, is (8, 12) planter? Let's check (8, 11) instead
    move_safe_battle("Up", 8, 11)
    move_safe_battle("Up", 8, 10)
    
    # Test (8, 9)
    pos = mgba.get_coordinates()
    print(f"test_column_8: Testing Column 8 Row 9 (8, 9) from {pos}...")
    success = move_safe_battle("Up", 8, 9)
    if success:
        print("test_column_8: Column 8 Row 9 is OPEN!")
    else:
        print("test_column_8: Column 8 Row 9 is CLOSED.")
        
    # Test (9, 9) if we can walk right to (9, 10)
    move_safe_battle("Right", 9, 10)
    print("test_column_8: Testing Column 9 Row 9 (9, 9)...")
    success9 = move_safe_battle("Up", 9, 9)
    if success9:
        print("test_column_8: Column 9 Row 9 is OPEN!")
    else:
        print("test_column_8: Column 9 Row 9 is CLOSED.")

if __name__ == "__main__":
    test_column_8()
