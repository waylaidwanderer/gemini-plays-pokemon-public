import mgba
import time
from PIL import Image, ImageChops

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
        return True
    else:
        mgba.press_buttons(["Start"])
        time.sleep(0.25)
        return False

def handle_battle_escape():
    print("ESCAPING BATTLE...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    mgba.press_buttons(["B"])
    time.sleep(1.0)

def step_one(direction, target_x, target_y):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        if is_in_battle():
            handle_battle_escape()
            mgba.press_buttons([direction])
            time.sleep(0.4)
            pos_after = mgba.get_coordinates()
            
    # Pitfall check
    if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 2 or abs(pos_after['y'] - pos_before['y']) > 2):
        print(f"FELL THROUGH PITFALL! Landed at: {pos_after}")
        return False
        
    return pos_after['x'] == target_x and pos_after['y'] == target_y

def main():
    print("test_row_6_from_5_8: Dismissing battle text...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print(f"Start coordinates: {pos}")
    
    # We are at (5, 8)
    # Walk Up to (5, 5)
    path = [
        ("Up", 5, 7),
        ("Up", 5, 6),
        ("Up", 5, 5),
    ]
    
    for direction, tx, ty in path:
        if not step_one(direction, tx, ty):
            print(f"Failed at step '{direction}' to ({tx}, {ty})")
            return
            
    print("Succeeded in reaching (5, 5) without falling! We are above the pitfall.")
    
    # 5. Test walkability of (6, 5) (Mewtwo statue/table is at (10, 5) but Row 5 is open!)
    # Let's walk Right on Row 5 or Row 6!
    # Let's try to walk right on Row 6 first from (5, 6):
    print("Moving Down to (5, 6) to test Row 6...")
    if not step_one("Down", 5, 6): return
    
    print("Testing RIGHT to (6, 6) (rubble)...")
    success = step_one("Right", 6, 6)
    pos = mgba.get_coordinates()
    print(f"At (6, 6)? {'YES' if success else 'NO'}. Current: {pos}")
    
    if success:
        # Test (7, 6)
        print("Testing RIGHT to (7, 6) (rubble)...")
        success2 = step_one("Right", 7, 6)
        pos = mgba.get_coordinates()
        print(f"At (7, 6)? {'YES' if success2 else 'NO'}. Current: {pos}")
        
        # Test (8, 6)
        if success2:
            print("Testing RIGHT to (8, 6) (rubble)...")
            success3 = step_one("Right", 8, 6)
            pos = mgba.get_coordinates()
            print(f"At (8, 6)? {'YES' if success3 else 'NO'}. Current: {pos}")
            
            if success3:
                # Test (9, 6) (rubble)
                print("Testing RIGHT to (9, 6) (rubble)...")
                success4 = step_one("Right", 9, 6)
                pos = mgba.get_coordinates()
                print(f"At (9, 6)? {'YES' if success4 else 'NO'}. Current: {pos}")
                
                if success4:
                    # Test (10, 6) (pink/white floor!)
                    print("Testing RIGHT to (10, 6) (floor)...")
                    success5 = step_one("Right", 10, 6)
                    pos = mgba.get_coordinates()
                    print(f"At (10, 6)? {'YES' if success5 else 'NO'}. Current: {pos}")
                    
                    if success5:
                        print("SUCCESS!!! Row 6 is completely walkable from Column 5 to Column 10!")
                        print("We can now easily cross to 3F East!")
                    else:
                        step_one("Left", 8, 6)
                        step_one("Left", 7, 6)
                        step_one("Left", 6, 6)
                        step_one("Left", 5, 6)
                else:
                    step_one("Left", 7, 6)
                    step_one("Left", 6, 6)
                    step_one("Left", 5, 6)
            else:
                step_one("Left", 6, 6)
                step_one("Left", 5, 6)
        else:
            step_one("Left", 5, 6)

if __name__ == "__main__":
    main()
