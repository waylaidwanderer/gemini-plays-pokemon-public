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
    # We start at (11, 9) on 3F West
    print("go_to_b1f_via_balcony: Starting...")
    
    # 1. Walk down Column 11 to Row 11
    pos = mgba.get_coordinates()
    while pos['y'] < 11:
        success = move_safe_battle("Down", 11, pos['y'] + 1)
        if not success: return
        pos = mgba.get_coordinates()
        
    # 2. Walk LEFT Row 11 to Column 1 (bypassing warp at (7, 10))
    while pos['x'] > 1:
        success = move_safe_battle("Left", pos['x'] - 1, 11)
        if not success: return
        pos = mgba.get_coordinates()
        
    # 3. Walk to switch at (2, 12)
    success = move_safe_battle("Down", 1, 12)
    if not success: return
    success = move_safe_battle("Right", 2, 12)
    if not success: return
    
    # 4. Toggle switch to State A
    print("At switch. Toggling to State A...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # 5. Walk back to (1, 11)
    pos = mgba.get_coordinates()
    success = move_safe_battle("Left", 1, 12)
    if not success: return
    success = move_safe_battle("Up", 1, 11)
    if not success: return
    pos = mgba.get_coordinates()
    
    # 6. Walk RIGHT Row 11 to Column 19 (which is open in State A!)
    while pos['x'] < 19:
        success = move_safe_battle("Right", pos['x'] + 1, 11)
        if not success: return
        pos = mgba.get_coordinates()
        
    # 7. Walk DOWN Column 19 to Row 18
    while pos['y'] < 18:
        success = move_safe_battle("Down", 19, pos['y'] + 1)
        if not success: return
        pos = mgba.get_coordinates()
        
    # 8. Step DOWN to jump over the balcony!
    print("At balcony (19, 18). Jumping down...")
    mgba.press_buttons(["Down"])
    time.sleep(1.5)
    mgba.press_buttons(["Down"])
    time.sleep(1.5)
    
    print(f"Arrived at B1F East! Current position: {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
