import mgba
import time
from PIL import Image, ImageChops

def has_dialogue_opened():
    # Compare screen before and after pressing A
    # First, take screenshot before
    img1_path = mgba.take_screenshot()
    img1 = Image.open(img1_path)
    
    # Press A
    mgba.press_buttons(["A"])
    time.sleep(0.4)
    
    # Take screenshot after
    img2_path = mgba.take_screenshot()
    img2 = Image.open(img2_path)
    
    # Compare bottom 4 rows of tiles (y from 112 to 144)
    w, h = img1.size
    y_start = int(112 / 144 * h)
    
    crop1 = img1.crop((0, y_start, w, h))
    crop2 = img2.crop((0, y_start, w, h))
    
    diff = ImageChops.difference(crop1, crop2)
    bbox = diff.getbbox()
    
    if bbox is not None:
        # Screen changed! This means dialogue opened!
        print("Dialogue box detected!")
        # Press B to dismiss
        mgba.press_buttons(["B"])
        time.sleep(0.3)
        return True
    return False

def test_tile(x, y, face_dir):
    current = mgba.get_coordinates()
    print(f"Testing from ({x}, {y}) facing {face_dir}...")
    
    # Walk to (x, y)
    # We are currently at some position on Column 12
    pos = mgba.get_coordinates()
    while pos['y'] != y:
        dy = y - pos['y']
        direction = "Down" if dy > 0 else "Up"
        mgba.press_buttons([direction])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        
    # Face the correct direction
    mgba.press_buttons([face_dir])
    time.sleep(0.4)
    
    if has_dialogue_opened():
        print(f"SUCCESS: Switch is located next to ({x}, {y}) facing {face_dir}!")
        return True
    return False

def main():
    print("Starting switch location probe on 3F West...")
    # We are currently at (12, 11)
    # Let's test the following combinations:
    # 1. Stand at (12, 9) facing Right (towards 13, 9)
    # 2. Stand at (12, 11) facing Right (towards 13, 11)
    # 3. Stand at (12, 10) facing Right (towards 13, 10)
    # 4. Stand at (12, 11) facing Down (towards 12, 12)
    # 5. Stand at (12, 10) facing Up (towards 12, 9)
    
    tests = [
        (12, 9, "Right"),
        (12, 11, "Right"),
        (12, 10, "Right"),
        (12, 11, "Down"),
        (12, 10, "Up")
    ]
    
    for x, y, face_dir in tests:
        if test_tile(x, y, face_dir):
            print("FOUND IT!")
            return
            
    print("None of the tested combinations triggered a dialogue.")

if __name__ == "__main__":
    main()
