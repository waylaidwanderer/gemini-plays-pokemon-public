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

# Walk back to Column 18, Row 6, then walk Left all the way on Row 6
if pos == {"x": 16, "y": 4}:
    print("Navigating to Row 6 Column 18...")
    if not run_steps([
        ("Right", {"x": 17, "y": 4}),
        ("Right", {"x": 18, "y": 4}),
        ("Down", {"x": 18, "y": 5}),
        ("Down", {"x": 18, "y": 6}),
    ]):
        print("Failed to reach (18, 6)")
        exit(1)
    pos = mgba.get_coordinates()

# Walk LEFT along Row 6 directly to B1F West at (1, 6) (open in State B!)
if pos == {"x": 18, "y": 6}:
    print("Walking LEFT along B1F Row 6 directly to (1, 6)...")
    if not run_steps([("Left", {"x": 18 - i - 1, "y": 6}) for i in range(17)]):
        print("Failed to reach B1F West at (1, 6)")
        exit(1)
    pos = mgba.get_coordinates()

# Walk UP to (1, 5) and stand facing UP towards the Secret Key at (1, 4)
if pos == {"x": 1, "y": 6}:
    if not walk_step("Up", {"x": 1, "y": 5}):
        print("Failed to reach (1, 5)")
        exit(1)
    pos = mgba.get_coordinates()

# Stand at (1, 5) facing UP and retrieve the Secret Key at (1, 4)!
if pos == {"x": 1, "y": 5}:
    print("Aligning UP towards the Secret Key...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    print("Picking up the Secret Key...")
    mgba.press_buttons([
        "A", "sleep 1200", # 1. Opens "ACE found SECRET KEY!"
        "A", "sleep 1200", # 2. Completes text
        "A", "sleep 1200"  # 3. Dismisses final text box and returns to overworld!
    ])
    time.sleep(4.5)
    pos = mgba.get_coordinates()
    print("Final position after retrieving Secret Key:", pos)
