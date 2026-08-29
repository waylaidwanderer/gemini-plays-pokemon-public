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
        # Check if we fell (which we don't expect until we reach the drop point!)
        if target_x == 26 and target_y == 3 and pos_after['y'] == 4:
            print("move_safe_battle: Fell through pitfall at (26, 3)!")
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
        
    return (pos_after['x'] == target_x and pos_after['y'] == target_y) or (target_x == 26 and target_y == 3 and pos_after['y'] == 4)

def main():
    print("solve_mansion_3f: Starting from (26, 5)...")
    pos = mgba.get_coordinates()
    
    # 1. Walk Up to (26, 3)
    if not move_safe_battle("Up", 26, 4): return
    if not move_safe_battle("Up", 26, 3): return
    
    # 2. Walk Left to (20, 3)
    for x in range(25, 19, -1):
        if not move_safe_battle("Left", x, 3): return
        
    # 3. Walk Down to (20, 4) -> Left to (19, 4) -> Down to (19, 6)
    if not move_safe_battle("Down", 20, 4): return
    if not move_safe_battle("Left", 19, 4): return
    if not move_safe_battle("Down", 19, 5): return
    if not move_safe_battle("Down", 19, 6): return
    
    # 4. Walk Left Row 6 to (10, 6)
    for x in range(18, 9, -1):
        if not move_safe_battle("Left", x, 6): return
        
    # 5. Walk Down to (10, 11)
    for y in range(7, 12):
        if not move_safe_battle("Down", 10, y): return
        
    # 6. Walk Left Row 11 to Column 3 (3, 11)
    for x in range(9, 2, -1):
        if not move_safe_battle("Left", x, 11): return
        
    # 7. Walk Down to (3, 12) -> Left to (2, 12)
    if not move_safe_battle("Down", 3, 12): return
    if not move_safe_battle("Left", 2, 12): return
    
    # 8. Face UP and toggle switch to State B
    print("Facing UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    print("Toggling switch to State B...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # 9. Walk back to Column 10 Row 11
    if not move_safe_battle("Right", 3, 12): return
    if not move_safe_battle("Up", 3, 11): return
    for x in range(4, 11):
        if not move_safe_battle("Right", x, 11): return
        
    # 10. Walk Up Column 10 to Row 6 (10, 6)
    for y in range(10, 5, -1):
        if not move_safe_battle("Up", 10, y): return
        
    # 11. Walk Right Row 6 to Column 19 (19, 6)
    for x in range(11, 20):
        if not move_safe_battle("Right", x, 6): return
        
    # 12. Walk Up Column 19 to Row 4 (19, 4)
    for y in [5, 4]:
        if not move_safe_battle("Up", 19, y): return
        
    # 13. Walk Right to (20, 4) then UP to (20, 3)
    if not move_safe_battle("Right", 20, 4): return
    if not move_safe_battle("Up", 20, 3): return
    
    # 14. Walk Right Row 3 to Column 25 (25, 3)
    for x in range(21, 26):
        if not move_safe_battle("Right", x, 3): return
        
    print(f"Successfully reached (25, 3) in State B! Coordinates: {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
