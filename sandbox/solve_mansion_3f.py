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
    
    # Check if we fell through the pitfall (landing on 1F East inside the fenced room)
    # Landing at 1F East (25, 6)
    if target_x == 26 and target_y == 6 and pos_after['x'] == 25 and pos_after['y'] == 6:
        print("move_safe_battle: Successfully fell through the pitfall to 1F East (25, 6)!")
        return True
        
    attempts = 0
    while (pos_after['x'] != target_x or pos_after['y'] != target_y) and attempts < 6:
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
        
    return (pos_after['x'] == target_x and pos_after['y'] == target_y) or (target_x == 26 and target_y == 6 and pos_after['x'] == 25 and pos_after['y'] == 6)

def main():
    print("solve_mansion_3f: Starting from (5, 11) on 3F West...")
    
    # 1. Walk Down to (5, 13)
    if not move_safe_battle("Down", 5, 12): return
    if not move_safe_battle("Down", 5, 13): return
    
    # 2. Walk Left to (2, 13)
    for x in range(4, 1, -1):
        if not move_safe_battle("Left", x, 13): return
        
    # 3. Walk Up to (2, 12)
    if not move_safe_battle("Up", 2, 12): return
    
    # 4. Face UP towards switch
    print("Facing UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # 5. Toggle switch to State B
    print("Toggling switch to State B...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # 6. Walk Down to (2, 13)
    if not move_safe_battle("Down", 2, 13): return
    
    # 7. Walk Right along Row 13 to Column 10 (10, 13)
    for x in range(3, 11):
        if not move_safe_battle("Right", x, 13): return
        
    # 8. Walk Up Column 10 to Row 6 (10, 6)
    for y in range(12, 5, -1):
        if not move_safe_battle("Up", 10, y): return
        
    # 9. Walk Right Row 6 to Column 19 (19, 6)
    for x in range(11, 20):
        if not move_safe_battle("Right", x, 6): return
        
    # 10. Walk Up Column 19 to Row 4 (19, 4)
    for y in [5, 4]:
        if not move_safe_battle("Up", 19, y): return
        
    # 11. Walk Right to (20, 4) then UP to (20, 3)
    if not move_safe_battle("Right", 20, 4): return
    if not move_safe_battle("Up", 20, 3): return
    
    # 12. Walk Right Row 3 to Column 26 (26, 3)
    for x in range(21, 27):
        if not move_safe_battle("Right", x, 3): return
        
    # 13. Walk Down Column 26 to Row 6 (26, 6) (which is the pitfall!)
    if not move_safe_battle("Down", 26, 4): return
    if not move_safe_battle("Down", 26, 5): return
    
    print("Stepping onto pitfall at (26, 6)...")
    if move_safe_battle("Down", 26, 6):
        print(f"Successfully dropped! Current pos: {mgba.get_coordinates()}")
    else:
        print("Failed to drop.")

if __name__ == "__main__":
    main()
