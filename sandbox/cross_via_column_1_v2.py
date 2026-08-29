from PIL import Image, ImageChops
import mgba
import time

def is_in_battle():
    img1_path = mgba.take_screenshot()
    img1 = Image.open(img1_path)
    mgba.press_buttons(["Start"])
    time.sleep(0.25)
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
        time.sleep(0.25)
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
    
    # Check if we fell (landing coordinates shift drastically)
    if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 2 or abs(pos_after['y'] - pos_before['y']) > 2):
        print(f"move_safe_battle: FELL THROUGH PIT! Current: {pos_after}")
        return True
        
    attempts = 0
    while (pos_after['x'] != target_x or pos_after['y'] != target_y) and attempts < 6:
        if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 2 or abs(pos_after['y'] - pos_before['y']) > 2):
            print(f"move_safe_battle: FELL THROUGH PIT! Current: {pos_after}")
            return True
            
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
        
    return pos_after['x'] == target_x and pos_after['y'] == target_y

def main():
    print("cross_via_column_1_v2: Starting from current position (2, 13)...")
    pos = mgba.get_coordinates()
    
    # 1. Walk Left to (1, 13)
    if pos['x'] == 2 and pos['y'] == 13:
        if not move_safe_battle("Left", 1, 13): return
        
    pos = mgba.get_coordinates()
    # 2. Walk Up Column 1 to (1, 6)
    if pos['x'] == 1 and pos['y'] > 6:
        for y in range(pos['y'] - 1, 5, -1):
            if not move_safe_battle("Up", 1, y): return
            
    pos = mgba.get_coordinates()
    # 3. Walk Right on Row 6 to Column 19 (19, 6)
    if pos['y'] == 6 and pos['x'] < 19:
        for x in range(pos['x'] + 1, 20):
            if not move_safe_battle("Right", x, 6): return
            
    pos = mgba.get_coordinates()
    # 4. Walk Up Column 19 to Row 4 (19, 4)
    if pos['x'] == 19 and pos['y'] > 4:
        for y in range(pos['y'] - 1, 3, -1):
            if not move_safe_battle("Up", 19, y): return
            
    pos = mgba.get_coordinates()
    # 5. Walk Right to (20, 4) then UP to (20, 3)
    if pos['x'] == 19 and pos['y'] == 4:
        if not move_safe_battle("Right", 20, 4): return
        if not move_safe_battle("Up", 20, 3): return
        
    pos = mgba.get_coordinates()
    # 6. Walk Right Row 3 to Column 26 (26, 3)
    if pos['y'] == 3 and pos['x'] < 26:
        for x in range(pos['x'] + 1, 27):
            if not move_safe_battle("Right", x, 3):
                # Check if we fell through
                pos = mgba.get_coordinates()
                if pos['y'] != 3:
                    print(f"Fell through pit while walking Row 3! Landed at: {pos}")
                    return
                    
    pos = mgba.get_coordinates()
    # 7. Walk Down Column 26 to Row 6 (26, 6) to trigger pitfall if we didn't fall yet
    if pos['x'] == 26 and pos['y'] == 3:
        for y in range(4, 7):
            if not move_safe_battle("Down", 26, y):
                pos = mgba.get_coordinates()
                if pos['y'] != y:
                    print(f"Fell through pit at y={y}! Landed at: {pos}")
                    return
                    
    print(f"Script complete. Current coordinates: {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
