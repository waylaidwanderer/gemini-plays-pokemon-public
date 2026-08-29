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
    # We are at (3, 11) on 3F West with Start menu open
    print("go_to_b1f_via_balcony: Starting...")
    
    # 1. Dismiss Start menu (press B)
    mgba.press_buttons(["B"])
    time.sleep(1.0)
    
    # 2. Walk DOWN to (3, 12)
    pos = mgba.get_coordinates()
    success = move_safe_battle("Down", 3, 12)
    if not success: return
    
    # 3. Walk LEFT to (2, 12)
    success = move_safe_battle("Left", 2, 12)
    if not success: return
    
    # 4. Toggle switch to State A (standing at 2, 12 facing UP)
    print("At switch (2, 12). Toggling to State A...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # 5. Walk LEFT to (1, 12)
    success = move_safe_battle("Left", 1, 12)
    if not success: return
    
    # 6. Walk RIGHT along Row 12 to Column 19 (open in State A!)
    for x in range(2, 20):
        success = move_safe_battle("Right", x, 12)
        if not success: return
        
    # 7. Walk DOWN Column 19 to Row 18
    for y in range(13, 19):
        success = move_safe_battle("Down", 19, y)
        if not success: return
        
    # 8. Step DOWN to jump over the balcony!
    print("At balcony (19, 18). Jumping down...")
    mgba.press_buttons(["Down"])
    time.sleep(1.5)
    mgba.press_buttons(["Down"])
    time.sleep(1.5)
    
    print(f"Arrived at B1F East! Current position: {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
