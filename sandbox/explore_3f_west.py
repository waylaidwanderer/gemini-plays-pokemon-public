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
    if 0.90 < percentage < 0.999:
        print("Battle/dialogue detected! Pressing B...")
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
        
        if 0.90 < percentage2 < 0.999:
            print("Still in battle. Running...")
            mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
            time.sleep(1.5)
            # Clear escape texts
            for _ in range(4):
                mgba.press_buttons(["B"])
                time.sleep(0.3)
        return True
    return False

def try_step(direction):
    curr = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.4)
    handle_any_menu_or_battle()
    new_pos = mgba.get_coordinates()
    if new_pos != curr:
        print(f"Successfully moved {direction} to {new_pos}")
        return True
    else:
        print(f"Blocked moving {direction} from {curr}")
        return False

# Try walking to Column 1 first
print("Exploring from", mgba.get_coordinates())
try_step("Left")
try_step("Left")
try_step("Up")
try_step("Up")
try_step("Right")
try_step("Right")
try_step("Right")
try_step("Right")
try_step("Right")

print("Final position after exploration:", mgba.get_coordinates())
