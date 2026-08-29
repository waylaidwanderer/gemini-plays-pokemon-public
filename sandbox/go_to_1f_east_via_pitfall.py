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
        print("is_in_battle: TRUE (Stable screen on Start)")
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
        # Check if we fell (which is expected at the very end of the route!)
        # If the target is (26, 6) but we are suddenly on 1F (y coordinate would be like 6, but map or x might change)
        # Wait, if we fell, pos_after['x'] might be 25 and pos_after['y'] might be 6 on 1F.
        # So we should break if our coordinates are totally different or if we detected we fell.
        # On 1F East, landing is (25, 6).
        if target_x == 26 and target_y == 6 and pos_after['x'] == 25 and pos_after['y'] == 6:
            print("move_safe_battle: Successfully fell through the pit to 1F East (25, 6)!")
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
        
    return pos_after

def main():
    print("go_to_1f_east_via_pitfall: Starting...")
    pos = mgba.get_coordinates()
    print(f"Initial coordinates: {pos}")
    
    # We are at (6, 12). Let's go Left to Column 1.
    for x in range(5, 0, -1):
        pos = move_safe_battle("Left", x, 12)
        
    # Walk Up Column 1 to Row 6
    for y in range(11, 5, -1):
        pos = move_safe_battle("Up", 1, y)
        
    # Walk Right Row 6 to Column 19
    for x in range(2, 20):
        pos = move_safe_battle("Right", x, 6)
        
    # Walk Up Column 19 to Row 4
    for y in [5, 4]:
        pos = move_safe_battle("Up", 19, y)
        
    # Walk Right to (20, 4) then UP to (20, 3)
    pos = move_safe_battle("Right", 20, 4)
    pos = move_safe_battle("Up", 20, 3)
    
    # Walk Right Row 3 to Column 26
    for x in range(21, 27):
        pos = move_safe_battle("Right", x, 3)
        
    # Walk Down Column 26 to Row 6 (pitfall at (26, 6) drops us to 1F East at (25, 6))
    pos = move_safe_battle("Down", 26, 4)
    pos = move_safe_battle("Down", 26, 5)
    
    print("Stepping onto the pitfall at (26, 6)...")
    pos = move_safe_battle("Down", 26, 6)
    
    print(f"Landing position: {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
