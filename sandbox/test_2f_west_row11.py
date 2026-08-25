import mgba
import time
from PIL import Image

def handle_any_menu_or_battle():
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
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        return True
    return False

def walk_step(direction, expected_coords, retries=5):
    for i in range(retries):
        handle_any_menu_or_battle()
        mgba.press_buttons([direction])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            print(f"Moved {direction}, current position: {pos}")
            return True
        print(f"Blocked! Retrying {direction} to {expected_coords}, current: {pos}")
        time.sleep(0.2)
    return False

# Currently at (4, 12) on 2F West
# Walk UP to (4, 11), LEFT to (3, 11), LEFT to (2, 11)
success = walk_step("Up", {"x": 4, "y": 11})
if success:
    success = walk_step("Left", {"x": 3, "y": 11})
if success:
    print("Reached (3, 11)! Testing if (2, 11) is open...")
    if walk_step("Left", {"x": 2, "y": 11}):
        print("(2, 11) is OPEN! Toggling switch facing UP...")
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        mgba.press_buttons(["A"])
        time.sleep(1.5)
        mgba.press_buttons(["A"]) # YES
        time.sleep(1.5)
        mgba.press_buttons(["A"]) # Dismiss
        time.sleep(1.5)
        print("Toggled! Current position:", mgba.get_coordinates())
    else:
         print("(2, 11) is CLOSED!")
