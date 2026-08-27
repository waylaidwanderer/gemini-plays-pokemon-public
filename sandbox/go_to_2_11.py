import mgba
import time
from PIL import Image

def is_dialogue_open():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file).resize((160, 144), Image.Resampling.NEAREST)
    cropped = img.crop((0, 104, 160, 144))
    
    # Check for GBC dialogue background (high white/cream pixel count)
    white_cream_pixels = 0
    for y in range(cropped.height):
        for x in range(cropped.width):
            r, g, b = cropped.getpixel((x, y))[:3]
            if r > 200 and g > 200 and b > 200:
                white_cream_pixels += 1
    print(f"  Check dialogue box: white_cream_pixels={white_cream_pixels}")
    return white_cream_pixels > 3000

def handle_any_menu_or_battle():
    time.sleep(0.15)
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
            # Down -> Right -> A is correct run from FIGHT cursor
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

pos = mgba.get_coordinates()
print("Starting position:", pos)

# 1. Walk LEFT along Row 11 to (2, 11)
if pos == {"x": 9, "y": 11}:
    print("Walking LEFT to (2, 11)...")
    steps = []
    for x in range(8, 1, -1):
        steps.append(("Left", {"x": x, "y": 11}))
    if not run_steps(steps):
        print("Failed to reach (2, 11)")
        exit(1)
    pos = mgba.get_coordinates()

# 2. Inspect (2, 10) by facing UP from (2, 11)
if pos == {"x": 2, "y": 11}:
    print("Facing UP towards (2, 10)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    print("Pressing A...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    if is_dialogue_open():
        print("Mewtwo switch dialogue open at (2, 11) facing UP!")
        # Toggle switch to State B/State A
        mgba.press_buttons(["A"])
        time.sleep(1.2)
        mgba.press_buttons(["A"])
        time.sleep(1.2)
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        print("Switch toggled!")
        exit(0)
    else:
        print("No dialogue box opened at (2, 11) facing UP.")
        mgba.press_buttons(["B"])
        time.sleep(0.4)

# 3. Walk DOWN to (2, 12) and inspect (2, 11) facing UP
if pos == {"x": 2, "y": 11}:
    print("Walking to (2, 12)...")
    if not walk_step("Down", {"x": 2, "y": 12}):
        print("Failed to reach (2, 12)")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 2, "y": 12}:
    print("Facing UP towards (2, 11)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    print("Pressing A...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    if is_dialogue_open():
        print("Mewtwo switch dialogue open at (2, 12) facing UP!")
        # Toggle switch
        mgba.press_buttons(["A"])
        time.sleep(1.2)
        mgba.press_buttons(["A"])
        time.sleep(1.2)
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        print("Switch toggled!")
        exit(0)
    else:
        print("No dialogue box opened at (2, 12) facing UP.")
        mgba.press_buttons(["B"])
        time.sleep(0.4)
