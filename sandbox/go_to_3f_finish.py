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
    print("handle_battle_escape: ESCAPING BATTLE...")
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

def main():
    # We are at (5, 12) on 2F West with Start menu open
    print("go_to_3f_finish: Starting...")
    
    # Dismiss menu
    mgba.press_buttons(["B"])
    time.sleep(1.0)
    
    pos = mgba.get_coordinates()
    print(f"go_to_3f_finish: Start pos: {pos}")
    
    # 1. Walk UP Column 5 to Row 11
    while pos['y'] > 11:
        pos = move_test_or_step("Up", 5, pos['y'] - 1)
        
    # 2. Walk RIGHT to (7, 11)
    pos = move_test_or_step("Right", 6, 11)
    pos = move_test_or_step("Right", 7, 11)
    
    # 3. Warp UP to 3F West!
    print("go_to_3f_finish: Warping UP to 3F West...")
    mgba.press_buttons(["Up"])
    time.sleep(1.0)
    
    pos = mgba.get_coordinates()
    print(f"go_to_3f_finish: Position on 3F West: {pos}")
    
    # 4. Walk down to (7, 11) (safe from warp)
    pos = move_test_or_step("Down", 7, 11)
    
    # 5. Walk right along Row 11 to Column 10 (10, 11)
    while pos['x'] < 10:
        pos = move_test_or_step("Right", pos['x'] + 1, 11)
        
    # 6. Walk UP Column 10 to Row 6 (10, 6)
    while pos['y'] > 6:
        pos = move_test_or_step("Up", 10, pos['y'] - 1)
        
    # 7. Walk right on Row 6 to (19, 6)
    while pos['x'] < 19:
        pos = move_test_or_step("Right", pos['x'] + 1, 6)
        
    # 8. Walk UP Column 19 to Row 4 (19, 4)
    while pos['y'] > 4:
        pos = move_test_or_step("Up", 19, pos['y'] - 1)
        
    # 9. Walk to (20, 4) then UP to (20, 3)
    pos = move_test_or_step("Right", 20, 4)
    pos = move_test_or_step("Up", 20, 3)
    
    # 10. Walk RIGHT to (25, 3)
    while pos['x'] < 25:
        pos = move_test_or_step("Right", pos['x'] + 1, 3)
        
    print(f"go_to_3f_finish: Successfully reached 3F East at {mgba.get_coordinates()}")

def move_test_or_step(step, target_x, target_y):
    # Use move_safe_battle but wrap it
    success = move_safe_battle(step, target_x, target_y)
    if not success:
        print(f"CRITICAL: Failed to move '{step}' to ({target_x}, {target_y})")
    return mgba.get_coordinates()

if __name__ == "__main__":
    main()
