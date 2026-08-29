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
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    mgba.press_buttons(["B"])
    time.sleep(1.0)

def move_safe_battle(step, target_x, target_y):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([step])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    attempts = 0
    while (pos_after['x'] != target_x or pos_after['y'] != target_y) and attempts < 3:
        if pos_before == pos_after:
            time.sleep(1.0)
            if is_in_battle():
                handle_battle_escape()
            else:
                return False
        else:
            time.sleep(1.0)
            if is_in_battle():
                handle_battle_escape()
        mgba.press_buttons([step])
        time.sleep(0.4)
        pos_after = mgba.get_coordinates()
        attempts += 1
    return pos_after['x'] == target_x and pos_after['y'] == target_y

def test_gates():
    # We are at (1, 10)
    pos = mgba.get_coordinates()
    print(f"test_gates: Starting at {pos}")
    
    # 1. Test Column 3
    print("test_gates: Moving to (3, 10)...")
    if move_safe_battle("Right", 2, 10):
        # Wait, is (2, 10) open? (2, 10) has the Mewtwo statue head!
        # Ah! Is (2, 10) blocked by the statue head?
        # Let's see if we can move to (2, 10). If (2, 10) is blocked, we walk Down to (1, 11) -> Right to (3, 11) -> Up to (3, 10)
        pass
    
    # Let's do the safe path to (3, 10):
    # (1, 10) -> (1, 11) -> (3, 11) -> (3, 10)
    move_safe_battle("Down", 1, 11)
    move_safe_battle("Right", 2, 11)
    move_safe_battle("Right", 3, 11)
    move_safe_battle("Up", 3, 10)
    
    pos = mgba.get_coordinates()
    print(f"test_gates: Now at {pos}. Testing Column 3 Row 9 (3, 9)...")
    success3 = move_safe_battle("Up", 3, 9)
    if success3:
        print("test_gates: Column 3 Row 9 is OPEN!")
        return 3
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
        return 4
    else:
        print("test_gates: Column 4 Row 9 is CLOSED.")
        
    return None

if __name__ == "__main__":
    test_gates()
