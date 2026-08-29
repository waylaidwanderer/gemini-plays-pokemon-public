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
            
    return pos_after['x'] == target_x and pos_after['y'] == target_y

def main():
    print("probe_around: Walking from (7, 10) to (1, 10) on 3F West...")
    pos = mgba.get_coordinates()
    print(f"Start: {pos}")
    
    # Path to (1, 10)
    path = [
        ("Left", 6, 10),
        ("Left", 5, 10),
        ("Left", 4, 10),
        ("Down", 4, 11),
        ("Down", 4, 12),
        ("Down", 4, 13),
        ("Left", 3, 13),
        ("Left", 2, 13),
        ("Left", 1, 13),
        ("Up", 1, 12),
        ("Up", 1, 11),
        ("Up", 1, 10),
    ]
    
    for d, tx, ty in path:
        if not step_one(d, tx, ty):
            print(f"Failed at step '{d}' to ({tx}, {ty})")
            return
            
    print(f"Succeeded! Current coordinates: {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
