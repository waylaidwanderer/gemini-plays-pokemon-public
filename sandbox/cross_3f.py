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

def cross():
    # We are at (10, 6)
    pos = mgba.get_coordinates()
    print(f"cross: Starting at {pos}")
    
    # Walk RIGHT on Row 6 to Column 21
    # Note: Column 19 Row 6 might be open directly, but let's go to Column 21 and back to 19 to be 100% safe
    # from the previous known-good route.
    for x in range(11, 22):
        if not move_safe_battle("Right", x, 6):
            print(f"cross: Failed to walk Right on Row 6 to Column {x}")
            return
            
    # Walk LEFT to Column 19
    for x in [20, 19]:
        if not move_safe_battle("Left", x, 6):
            return
            
    # Walk UP Column 19 to Row 3
    for y in [5, 4, 3]:
        if not move_safe_battle("Up", 19, y):
            return
            
    # Walk RIGHT on Row 3 to Column 26
    for x in range(20, 27):
        if not move_safe_battle("Right", x, 3):
            return
            
    print(f"cross: Successfully reached (26, 3). Current pos: {mgba.get_coordinates()}")

if __name__ == "__main__":
    cross()
