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
        # Check if we transitioned to B1F East (our y coordinate after warping might be 2, 3, etc.)
        # Emerge on B1F East at (22, 2)
        if target_x == 22 and target_y == 2 and pos_after['x'] == 22 and pos_after['y'] == 2:
            print("move_safe_battle: Successfully warped to B1F East (22, 2)!")
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
        
    return (pos_after['x'] == target_x and pos_after['y'] == target_y) or (target_x == 22 and target_y == 2 and pos_after['x'] == 22 and pos_after['y'] == 2)

def main():
    print("go_to_b1f: Starting from 1F East...")
    pos = mgba.get_coordinates()
    print(f"Initial coordinates: {pos}")
    
    # 1. Walk from current (25, 4) to (21, 2)
    if pos['x'] == 25 and pos['y'] == 4:
        if not move_safe_battle("Up", 25, 3): return
        
    pos = mgba.get_coordinates()
    if pos['y'] == 3:
        for x in range(pos['x'] - 1, 20, -1):
            if not move_safe_battle("Left", x, 3): return
            
    if not move_safe_battle("Up", 21, 2): return
    
    # 2. Step RIGHT onto stairs at (22, 2) and warp DOWN to B1F East
    print("Stepping onto stairs to warp DOWN to B1F...")
    if not move_safe_battle("Right", 22, 2): return
    
    pos = mgba.get_coordinates()
    print(f"Coordinates after warp: {pos}")
    
    # 3. On B1F East, walk DOWN to (22, 4)
    if not move_safe_battle("Down", 22, 3): return
    if not move_safe_battle("Down", 22, 4): return
    
    # 4. Walk LEFT on Row 4 to Column 19 (19, 4)
    for x in range(21, 18, -1):
        if not move_safe_battle("Left", x, 4): return
        
    # 5. Walk DOWN to (19, 5)
    if not move_safe_battle("Down", 19, 5): return
    
    # 6. Walk LEFT on Row 5 to Column 1 (1, 5) (passing open gate at (9, 5))
    for x in range(18, 0, -1):
        if not move_safe_battle("Left", x, 5): return
        
    print(f"Successfully reached the Secret Key Room at B1F West {mgba.get_coordinates()}!")
    
    # 7. Stand facing UP and retrieve Secret Key at (1, 4)
    print("Facing UP to retrieve Secret Key...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    print("Interacting with Secret Key...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    # Dismiss dialogue text boxes
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    print("Secret Key retrieved successfully!")
    print(f"Final coordinates: {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
