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
    # Press B to dismiss any text
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # Press Down, Right, A to select RUN
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    
    # Press B to dismiss "Got away safely!"
    mgba.press_buttons(["B"])
    time.sleep(1.0)

def move_safe_battle(step, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"move_safe_battle: Moving '{step}' to ({target_x}, {target_y}). Current: {pos_before}")
    mgba.press_buttons([step])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    
    attempts = 0
    while (pos_after['x'] != target_x or pos_after['y'] != target_y) and attempts < 4:
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
        
    arrived = (pos_after['x'] == target_x and pos_after['y'] == target_y)
    print(f"move_safe_battle: Arrived: {arrived}. Final position: {pos_after}")
    return arrived

def main():
    # We are currently at (22, 7) on 3F East facing UP
    print("solve_mansion_3f: Starting...")
    
    # 1. Walk Left to (19, 7)
    for x in [21, 20, 19]:
        move_safe_battle("Left", x, 7)
        
    # 2. Walk UP Column 19 to (19, 6)
    move_safe_battle("Up", 19, 6)
    
    # 3. Walk LEFT Row 6 to (10, 6)
    for x in range(18, 9, -1):
        move_safe_battle("Left", x, 6)
        
    # 4. Walk DOWN Column 10 to (10, 10)
    for y in [7, 8, 9, 10]:
        move_safe_battle("Down", 10, y)
        
    # 5. Walk LEFT Row 10 to (1, 10)
    for x in range(9, 0, -1):
        move_safe_battle("Left", x, 10)
        
    # 6. Walk down to (1, 12) and right to (2, 12)
    move_safe_battle("Down", 1, 11)
    move_safe_battle("Down", 1, 12)
    move_safe_battle("Right", 2, 12)
    
    # 7. Toggle switch to State A
    print("At switch. Toggling to State A...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # 8. Walk back to (1, 10)
    move_safe_battle("Left", 1, 12)
    move_safe_battle("Up", 1, 11)
    move_safe_battle("Up", 1, 10)
    
    # 9. Walk back to Column 10 Row 10
    for x in range(2, 11):
        move_safe_battle("Right", x, 10)
        
    # 10. Walk back UP to Row 6
    for y in [9, 8, 7, 6]:
        move_safe_battle("Up", 10, y)
        
    # 11. Walk RIGHT Row 6 to (19, 6)
    for x in range(11, 20):
        move_safe_battle("Right", x, 6)
        
    # 12. Walk UP Column 19 to Row 4
    for y in [5, 4]:
        move_safe_battle("Up", 19, y)
        
    # 13. Walk RIGHT to (20, 4) and UP to (20, 3)
    move_safe_battle("Right", 20, 4)
    move_safe_battle("Up", 20, 3)
    
    # 14. Walk RIGHT to (26, 3)
    for x in range(21, 27):
        move_safe_battle("Right", x, 3)
        
    # 15. Walk DOWN to (26, 5)
    move_safe_battle("Down", 26, 4)
    move_safe_battle("Down", 26, 5)
    
    # 16. Test DOWN to (26, 6) in State A!
    print("Testing (26, 6) in State A...")
    pos_down = move_safe_battle("Down", 26, 6)
    if pos_down:
        print(f"Succeeded stepping into (26, 6)! Pos: {mgba.get_coordinates()}")
    else:
        print("(26, 6) is still solid in State A.")
        
    # 17. Walk UP to (26, 3) -> LEFT to (22, 3) and test stairs (22, 2) in State A!
    pos = mgba.get_coordinates()
    if pos['y'] == 5:
        move_safe_battle("Up", 26, 4)
        move_safe_battle("Up", 26, 3)
        for x in range(25, 21, -1):
            move_safe_battle("Left", x, 3)
        print("Testing stairs at (22, 2) in State A...")
        pos_up = move_safe_battle("Up", 22, 2)
        if pos_up:
            print(f"Succeeded stepping onto stairs (22, 2)! Pos: {pos_up}")
        else:
            print("Stairs (22, 2) are still solid/blocked in State A.")

if __name__ == "__main__":
    main()
