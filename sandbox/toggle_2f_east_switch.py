import mgba
import time
from PIL import Image

def handle_any_menu_or_battle():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file)
    img_std = img.resize((160, 144), Image.Resampling.NEAREST)
    
    black_or_white = 0
    total_pixels = 0
    for y in range(115, 140):
        for x in range(10, 150):
            r, g, b = img_std.getpixel((x, y))
            total_pixels += 1
            is_bw = (r < 50 and g < 50 and b < 50) or (r > 200 and g > 200 and b > 200)
            if is_bw:
                black_or_white += 1
                
    percentage = black_or_white / total_pixels
    if percentage > 0.90:
        print(f"Menu/Dialogue detected! (B/W: {percentage*100:.2f}%)")
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        
        # Check if still in battle
        scr_file2 = mgba.take_screenshot()
        img2 = Image.open(scr_file2)
        img_std2 = img2.resize((160, 144), Image.Resampling.NEAREST)
        black_or_white2 = 0
        for y in range(115, 140):
            for x in range(10, 150):
                r, g, b = img_std2.getpixel((x, y))
                is_bw = (r < 50 and g < 50 and b < 50) or (r > 200 and g > 200 and b > 200)
                if is_bw:
                    black_or_white2 += 1
        percentage2 = black_or_white2 / total_pixels
        
        if percentage2 > 0.90:
            print("Still in battle. Running...")
            mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
            time.sleep(1.5)
            # Dismiss run text
            for _ in range(4):
                mgba.press_buttons(["B"])
                time.sleep(0.3)
        return True
    return False

def walk_step(direction, expected_coords, retries=15):
    for i in range(retries):
        if handle_any_menu_or_battle():
            pos = mgba.get_coordinates()
            if pos == expected_coords:
                return True
        mgba.press_buttons([direction])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            print(f"Moved {direction}, current position: {pos}")
            return True
        print(f"Blocked or battle! Retrying {direction} to {expected_coords} (attempt {i+1}/{retries}), current: {pos}")
        time.sleep(0.3)
    return False

# Current is (14, 7) on 2F East
print("Walking to 2F West switch standing position (2, 12)...")
success = True

steps_to_switch = [
    ("Left", {"x": 13, "y": 7}),
    ("Left", {"x": 12, "y": 7}),
    ("Down", {"x": 12, "y": 8}),
    ("Down", {"x": 12, "y": 9}),
    ("Down", {"x": 12, "y": 10}),
    ("Down", {"x": 12, "y": 11}),
    ("Left", {"x": 11, "y": 11}),
    ("Left", {"x": 10, "y": 11}),
    ("Left", {"x": 9, "y": 11}),
    ("Left", {"x": 8, "y": 11}),
    ("Left", {"x": 7, "y": 11}),
    ("Left", {"x": 6, "y": 11}),
    ("Left", {"x": 5, "y": 11}),
    ("Left", {"x": 4, "y": 11}),
    ("Left", {"x": 3, "y": 11}),
    ("Left", {"x": 2, "y": 11}),
    ("Down", {"x": 2, "y": 12}),
]

for d, c in steps_to_switch:
    if not walk_step(d, c):
        success = False
        break

if success:
    print("At (2, 12) on 2F West! Facing UP to toggle switch to State A...")
    mgba.press_buttons(["Up"])
    time.sleep(0.3)
    mgba.press_buttons(["A"]) # "A secret switch!"
    time.sleep(0.8)
    mgba.press_buttons(["A"]) # select YES
    time.sleep(0.8)
    mgba.press_buttons(["A"]) # "Pressed it!"
    time.sleep(0.8)
    print("Successfully toggled switch to State A!")
    
    # Run finish_mansion_from_2f_west.py to complete the quest!
    print("Now executing finish_mansion_from_2f_west.py...")
    exec(open("finish_mansion_from_2f_west.py").read())
else:
    print("Failed to navigate to switch.")
