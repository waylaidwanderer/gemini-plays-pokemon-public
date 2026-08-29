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
        # Check if we fell (landing at (25, 6) on 1F East)
        if target_x == 26 and target_y == 6 and pos_after['x'] == 25 and pos_after['y'] == 6:
            print("move_safe_battle: Successfully fell through the pit!")
            break
        # General fall check: if we are at (25, 6) or any other 1F location
        # On 1F, coordinates of the fenced room are (25, 6), (26, 4) etc.
        # But wait, is our map actually changed? Yes.
            
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
            else:
                print("move_safe_battle: Unexpected overworld movement.")
                
        print(f"move_safe_battle: Retrying step '{step}'...")
        mgba.press_buttons([step])
        time.sleep(0.4)
        pos_before = pos_after
        pos_after = mgba.get_coordinates()
        attempts += 1
        
    return True

def main():
    print("probe_3f_east: Starting from (26, 5)...")
    
    # Let's test going Left to (25, 5) then Down to (25, 6)
    print("Testing (25, 6) via (25, 5)...")
    if move_safe_battle("Left", 25, 5):
        # Now try to step Down to (25, 6)
        print("Stepping Down to (25, 6)...")
        mgba.press_buttons(["Down"])
        time.sleep(1.0)
        pos = mgba.get_coordinates()
        print(f"Position after stepping Down: {pos}")
        if pos['x'] != 25 or pos['y'] != 6:
            print("We must have fell or moved elsewhere!")
            return
        # Walk back Up if we didn't fall
        move_safe_battle("Up", 25, 5)
        move_safe_battle("Right", 26, 5)
        
    # Let's test going Right to (27, 5) then Down to (27, 6)
    print("Testing (27, 6) via (27, 5)...")
    if move_safe_battle("Right", 27, 5):
        # Now try to step Down to (27, 6)
        print("Stepping Down to (27, 6)...")
        mgba.press_buttons(["Down"])
        time.sleep(1.0)
        pos = mgba.get_coordinates()
        print(f"Position after stepping Down: {pos}")
        if pos['x'] != 27 or pos['y'] != 6:
            print("We must have fell or moved elsewhere!")
            return
        # Walk back Up if we didn't fall
        move_safe_battle("Up", 27, 5)
        move_safe_battle("Left", 26, 5)
        
    print("Probing completed. No pitfall found on (25, 6) or (27, 6).")

if __name__ == "__main__":
    main()
