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

def drop():
    # We are at (20, 3)
    pos = mgba.get_coordinates()
    print(f"drop: Starting at {pos}")
    
    # Walk RIGHT to (26, 3)
    for x in range(21, 27):
        # We might fall down before reaching 26 if the pit is on column 25 or 26
        # Let's check coordinates after every step!
        pos_before = mgba.get_coordinates()
        if pos_before['y'] != 3:
            # We fell! (y is now probably 4 or we are on 1F)
            print(f"drop: We fell! Position is now: {pos_before}")
            return
            
        success = move_safe_battle("Right", x, 3)
        if not success:
            # If we fell, the coordinates might have changed but not to the target (x, 3).
            # Let's check our current position
            pos_after = mgba.get_coordinates()
            if pos_after['y'] != 3:
                print(f"drop: We fell during move! Position: {pos_after}")
                return
            else:
                print(f"drop: Failed to walk Right to Column {x} Row 3.")
                return

    # If we reached (26, 3) without falling, step Right/Down to drop!
    print("drop: Reached (26, 3) without falling. Stepping Right...")
    mgba.press_buttons(["Right"])
    time.sleep(1.0)
    pos = mgba.get_coordinates()
    print(f"drop: Position after Right: {pos}")
    
    if pos['y'] == 3:
        print("drop: Still on 3F. Stepping Down...")
        mgba.press_buttons(["Down"])
        time.sleep(1.0)
        pos = mgba.get_coordinates()
        print(f"drop: Position after Down: {pos}")

if __name__ == "__main__":
    drop()
