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

def test_gates():
    # We are at (1, 10)
    pos = mgba.get_coordinates()
    print(f"test_gates: Starting at {pos}")
    
    # Let's do the safe path to (3, 10):
    # (1, 10) -> (1, 11) -> (2, 11) -> (3, 11) -> (3, 10)
    move_safe_battle("Down", 1, 11)
    move_safe_battle("Right", 2, 11)
    move_safe_battle("Right", 3, 11)
    move_safe_battle("Up", 3, 10)
    
    pos = mgba.get_coordinates()
    print(f"test_gates: Now at {pos}. Testing Column 3 Row 9 (3, 9)...")
    success3 = move_safe_battle("Up", 3, 9)
    if success3:
        print("test_gates: Column 3 Row 9 is OPEN!")
        # Step back down to (3, 10)
        move_safe_battle("Down", 3, 10)
    else:
        print("test_gates: Column 3 Row 9 is CLOSED.")
        
    # 2. Test Column 4
    # From (3, 10) -> (4, 10)
    print("test_gates: Moving to (4, 10)...")
    move_safe_battle("Right", 4, 10)
    pos = mgba.get_coordinates()
    print(f"test_gates: Now at {pos}. Testing Column 4 Row 9 (4, 9)...")
    success4 = move_safe_battle("Up", 4, 9)
    if success4:
        print("test_gates: Column 4 Row 9 is OPEN!")
        # Step back down to (4, 10)
        move_safe_battle("Down", 4, 10)
    else:
        print("test_gates: Column 4 Row 9 is CLOSED.")
        
    return None

if __name__ == "__main__":
    test_gates()
