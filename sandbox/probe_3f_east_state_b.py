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
    
    # Check if we fell (which will change map/state or coordinates, or we warp)
    # If the coordinate y is no longer in the range [3, 5] on 3F, we fell!
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
    print("probe_3f_east_state_b: Starting from (10, 7)...")
    
    # 1. Walk UP to (10, 6)
    if not move_safe_battle("Up", 10, 6): return
    
    # 2. Walk Right Row 6 to Column 19 (19, 6)
    for x in range(11, 20):
        if not move_safe_battle("Right", x, 6): return
        
    # 3. Walk Up Column 19 to Row 4 (19, 4)
    for y in [5, 4]:
        if not move_safe_battle("Up", 19, y): return
        
    # 4. Walk Right to (20, 4) then UP to (20, 3)
    if not move_safe_battle("Right", 20, 4): return
    if not move_safe_battle("Up", 20, 3): return
    
    # 5. Walk Right Row 3 to Column 25 (25, 3)
    for x in range(21, 26):
        if not move_safe_battle("Right", x, 3): return
        
    print("Successfully reached 3F East at (25, 3). Now probing all potential pitfalls...")
    
    # Let's test walking to various tiles on 3F East.
    # We will try to walk onto Row 4, Row 5, and Row 6 on Columns 25, 26, 27.
    # Note: If we fall, the script will output "FELL THROUGH PITFALL!" and terminate.
    
    # Test (25, 4)
    print("Testing (25, 4)...")
    if not move_safe_battle("Down", 25, 4): return
    
    # Test (25, 5)
    print("Testing (25, 5)...")
    if not move_safe_battle("Down", 25, 5): return
    
    # Test (25, 6)
    print("Testing (25, 6)...")
    if not move_safe_battle("Down", 25, 6):
        print("Blocked. (25, 6) is solid.")
    else:
        # Walk back
        move_safe_battle("Up", 25, 5)
        
    # Walk to (26, 5)
    print("Moving to (26, 5)...")
    if not move_safe_battle("Right", 26, 5): return
    
    # Test (26, 6)
    print("Testing (26, 6)...")
    if not move_safe_battle("Down", 26, 6):
        print("Blocked. (26, 6) is solid.")
    else:
        # Walk back
        move_safe_battle("Up", 26, 5)
        
    # Walk to (27, 5)
    print("Moving to (27, 5)...")
    if not move_safe_battle("Right", 27, 5): return
    
    # Test (27, 6)
    print("Testing (27, 6)...")
    if not move_safe_battle("Down", 27, 6):
        print("Blocked. (27, 6) is solid.")
    else:
        # Walk back
        move_safe_battle("Up", 27, 5)
        
    print("Probing of Row 6 completed. Let's see if we fall at Row 7 or Row 4/5...")
    
if __name__ == "__main__":
    main()
