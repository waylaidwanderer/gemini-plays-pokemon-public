import mgba
import time
from PIL import Image

def handle_any_menu_or_battle():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file)
    img_std = img.resize((160, 144), Image.Resampling.NEAREST)
    
    # We first press B to exit any move sub-menu we might be in
    mgba.press_buttons(["B"])
    time.sleep(0.3)
    
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file)
    img_std = img.resize((160, 144), Image.Resampling.NEAREST)
    
    black_or_white = 0
    total_pixels = 0
    for y in range(115, 140):
        for x in range(10, 150):
            r, g, b = img_std.getpixel((x, y))[:3]
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
                r, g, b = img_std2.getpixel((x, y))[:3]
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
        time.sleep(0.45)
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            print(f"Moved {direction}, current position: {pos}")
            return True
        print(f"Blocked or battle! Retrying {direction} to {expected_coords} (attempt {i+1}/{retries}), current: {pos}")
        time.sleep(0.3)
    return False

def run_steps(steps):
    for d, c in steps:
        if not walk_step(d, c):
            return False
    return True

print("Running test_switch_found.py...")

# 1. Escape battle if needed
handle_any_menu_or_battle()

pos = mgba.get_coordinates()
print("Position after battle escape:", pos)

# Walk to (1, 11) from (2, 12)
if pos == {"x": 2, "y": 12}:
    if not run_steps([
        ("Up", {"x": 2, "y": 11}),
        ("Left", {"x": 1, "y": 11}),
    ]):
        print("Failed to reach (1, 11)")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 1, "y": 11}:
    # Face RIGHT towards (2, 11)
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    
    # Save a screenshot before pressing A
    mgba.take_screenshot()
    
    # Press A to see if dialogue opens
    print("Pressing A...")
    mgba.press_buttons(["A"])
    time.sleep(0.8)
    
    # Check if dialogue is open
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file).resize((160, 144), Image.Resampling.NEAREST)
    cropped = img.crop((0, 104, 160, 144))
    
    white_cream_pixels = 0
    for y in range(cropped.height):
        for x in range(cropped.width):
            r, g, b = cropped.getpixel((x, y))[:3]
            if r > 200 and g > 200 and b > 200:
                white_cream_pixels += 1
                
    if white_cream_pixels > 3000:
        print("SUCCESS! Switch dialogue opened at (1, 11) facing RIGHT!")
        # Toggle switch to State B
        mgba.press_buttons(["A"]) # YES
        time.sleep(1.2)
        mgba.press_buttons(["A"]) # Result
        time.sleep(1.2)
        mgba.press_buttons(["A"]) # Dismiss
        time.sleep(1.0)
        print("Switch successfully toggled!")
        exit(0)
    else:
        print("Failed to open switch dialogue at (1, 11) facing RIGHT.")
        mgba.press_buttons(["B"])
        time.sleep(0.3)
