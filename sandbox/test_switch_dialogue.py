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

print("Running test_switch_dialogue.py...")

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

pos = mgba.get_coordinates()
print("Starting position:", pos)

# Walk to (1, 16) via Column 2
if pos == {"x": 2, "y": 10}:
    if not run_steps([
        ("Down", {"x": 2, "y": 11}),
        ("Down", {"x": 2, "y": 12}),
        ("Down", {"x": 2, "y": 13}),
        ("Down", {"x": 2, "y": 14}),
        ("Down", {"x": 2, "y": 15}),
        ("Down", {"x": 2, "y": 16}),
        ("Left", {"x": 1, "y": 16}),
    ]):
        print("Failed to reach (1, 16)")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 1, "y": 16}:
    # Face UP
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    # Save a screenshot of the overworld before pressing A
    mgba.take_screenshot()
    
    # Step 1: Press A to interact
    print("Pressing A (Step 1)...")
    mgba.press_buttons(["A"])
    time.sleep(0.8)
    scr_1 = mgba.take_screenshot()
    img_1 = Image.open(scr_1)
    img_1.crop((0, 104*2, 240*2, 144*2)).save("cropped_test/switch_dialogue_step1.png")
    img_1.save("cropped_test/switch_dialogue_step1_full.png")
    
    # Step 2: Press A to advance
    print("Pressing A (Step 2)...")
    mgba.press_buttons(["A"])
    time.sleep(0.8)
    scr_2 = mgba.take_screenshot()
    img_2 = Image.open(scr_2)
    img_2.crop((0, 104*2, 240*2, 144*2)).save("cropped_test/switch_dialogue_step2.png")
    img_2.save("cropped_test/switch_dialogue_step2_full.png")
    
    # Step 3: Press A to choose YES
    print("Pressing A (Step 3)...")
    mgba.press_buttons(["A"])
    time.sleep(0.8)
    scr_3 = mgba.take_screenshot()
    img_3 = Image.open(scr_3)
    img_3.crop((0, 104*2, 240*2, 144*2)).save("cropped_test/switch_dialogue_step3.png")
    img_3.save("cropped_test/switch_dialogue_step3_full.png")
    
    # Step 4: Press A to dismiss and toggle!
    print("Pressing A (Step 4)...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    scr_4 = mgba.take_screenshot()
    img_4 = Image.open(scr_4)
    img_4.crop((0, 104*2, 240*2, 144*2)).save("cropped_test/switch_dialogue_final.png")
    img_4.save("cropped_test/switch_dialogue_final_full.png")
    
    print("Dialogue steps recorded and saved to cropped_test/")
