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
    print("test_row_6: Navigating to Row 6...")
    # Currently at (2, 13)
    
    # 1. Walk Right to (6, 13)
    for x in range(3, 7):
        if not step_one("Right", x, 13): return
        
    # 2. Walk Up to (6, 8)
    # Note: avoid trainer if blocking, but let's see. Trainer is currently at (7, 11) or nearby.
    for y in range(12, 7, -1):
        if not step_one("Up", 6, y):
            print(f"Failed to move UP to row {y}. Checking if trainer is blocking...")
            pos = mgba.get_coordinates()
            print(f"Current position: {pos}")
            return
            
    # 3. Walk Left to (5, 8)
    if not step_one("Left", 5, 8): return
    
    # 4. Walk Up to (5, 6)
    if not step_one("Up", 5, 7): return
    if not step_one("Up", 5, 6): return
    
    print("Succeeded in reaching (5, 6) without falling! We are above the pitfall.")
    
    # 5. Test walkability of (6, 6)
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
        
        # Walk back to (5, 6) if successful
        if success2:
            step_one("Left", 6, 6)
            step_one("Left", 5, 6)
        else:
            step_one("Left", 5, 6)

if __name__ == "__main__":
    main()
