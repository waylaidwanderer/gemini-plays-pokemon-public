import mgba
import time
from PIL import Image

def handle_any_menu_or_battle():
    time.sleep(0.1)
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

def run_steps(steps):
    for d, c in steps:
        if not walk_step(d, c):
            return False
    return True

pos = mgba.get_coordinates()
print("Starting position:", pos)

if pos == {"x": 6, "y": 10}:
    # Walk to (2, 12)
    print("Walking to switch standing tile (2, 12)...")
    if run_steps([
        ("Down", {"x": 6, "y": 11}),
        ("Left", {"x": 5, "y": 11}),
        ("Left", {"x": 4, "y": 11}),
        ("Left", {"x": 3, "y": 11}),
        ("Down", {"x": 3, "y": 12}),
        ("Left", {"x": 2, "y": 12}),
    ]):
        pos = mgba.get_coordinates()

if pos == {"x": 2, "y": 12}:
    # Step-by-step switch dialogue inspection
    print("Facing UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    print("Step 1: Pressing A to interact with statue...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    s1 = mgba.take_screenshot()
    img1 = Image.open(s1)
    img1.save("switch_dialogue_pil_1.png")
    # Also save to cropped folder for visibility
    img1.resize((320, 288), Image.Resampling.NEAREST).save("notepads/../screenshots/cropped/switch_dialogue_pil_1.png")
    
    print("Step 2: Pressing A to show YES/NO...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    s2 = mgba.take_screenshot()
    img2 = Image.open(s2)
    img2.save("switch_dialogue_pil_2.png")
    img2.resize((320, 288), Image.Resampling.NEAREST).save("notepads/../screenshots/cropped/switch_dialogue_pil_2.png")
    
    print("Step 3: Pressing A to select YES...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    s3 = mgba.take_screenshot()
    img3 = Image.open(s3)
    img3.save("switch_dialogue_pil_3.png")
    img3.resize((320, 288), Image.Resampling.NEAREST).save("notepads/../screenshots/cropped/switch_dialogue_pil_3.png")
    
    print("Step 4: Pressing A to show opened/closed status...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    s4 = mgba.take_screenshot()
    img4 = Image.open(s4)
    img4.save("switch_dialogue_pil_4.png")
    img4.resize((320, 288), Image.Resampling.NEAREST).save("notepads/../screenshots/cropped/switch_dialogue_pil_4.png")
    
    print("Step 5: Pressing A to dismiss dialogue...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    s5 = mgba.take_screenshot()
    img5 = Image.open(s5)
    img5.save("switch_dialogue_pil_5.png")
    img5.resize((320, 288), Image.Resampling.NEAREST).save("notepads/../screenshots/cropped/switch_dialogue_pil_5.png")
    
    # Dismiss fully
    mgba.press_buttons(["B"])
    time.sleep(0.4)
    print("Dialogue test complete! Screenshots saved.")
