import mgba
import time
from PIL import Image, ImageChops

def is_in_battle():
    # Only check if we are in battle by comparing screen after Start press
    # but wait, let's just make it extremely robust.
    # If the screen has the dialogue border, we are in battle or menu.
    # But even simpler: if we get into a battle, our coordinates won't change
    # and we can just use a simple escape routine if we bump repeatedly.
    img1_path = mgba.take_screenshot()
    img1 = Image.open(img1_path)
    mgba.press_buttons(["Start"])
    time.sleep(0.3)
    img2_path = mgba.take_screenshot()
    img2 = Image.open(img2_path)
    diff = ImageChops.difference(img1, img2)
    bbox = diff.getbbox()
    if bbox is None:
        # Screen didn't change with Start, we are likely in battle
        print("is_in_battle: TRUE")
        return True
    else:
        # Screen changed, close the menu
        print("is_in_battle: FALSE")
        mgba.press_buttons(["Start"])
        time.sleep(0.3)
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
    
    attempts = 0
    while (pos_after['x'] != target_x or pos_after['y'] != target_y) and attempts < 3:
        print(f"step_one: Failed to reach ({target_x}, {target_y}). Current: {pos_after}. Checking battle...")
        if is_in_battle():
            handle_battle_escape()
        mgba.press_buttons([direction])
        time.sleep(0.4)
        pos_after = mgba.get_coordinates()
        attempts += 1
        
    return pos_after['x'] == target_x and pos_after['y'] == target_y

def main():
    print("probe_around: Walking from (5, 11) to (1, 10)...")
    pos = mgba.get_coordinates()
    print(f"Start: {pos}")
    
    # 1. Down to (5, 13)
    if pos['x'] == 5 and pos['y'] == 11:
        if not step_one("Down", 5, 12): return
        if not step_one("Down", 5, 13): return
        
    pos = mgba.get_coordinates()
    # 2. Left to (1, 13)
    if pos['y'] == 13 and pos['x'] > 1:
        for x in range(pos['x'] - 1, 0, -1):
            if not step_one("Left", x, 13): return
            
    pos = mgba.get_coordinates()
    # 3. Up to (1, 10)
    if pos['x'] == 1 and pos['y'] > 10:
        for y in range(pos['y'] - 1, 9, -1):
            if not step_one("Up", 1, y): return
            
    print(f"Succeeded! Landed at: {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
