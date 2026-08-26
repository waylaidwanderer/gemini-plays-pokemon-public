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

if pos == {"x": 2, "y": 12}:
    # Walk to Column 1 Row 13 via the Row 12/13 bypass to be completely safe
    print("Walking to (1, 13)...")
    if run_steps([
        ("Down", {"x": 2, "y": 13}),
        ("Left", {"x": 1, "y": 13}),
    ]):
        pos = mgba.get_coordinates()

if pos == {"x": 1, "y": 13}:
    # Walk up Column 1 to Row 6 (open in State B!)
    print("Walking up Column 1 to Row 6...")
    if run_steps([
        ("Up", {"x": 1, "y": 12}),
        ("Up", {"x": 1, "y": 11}),
        ("Up", {"x": 1, "y": 10}),
        ("Up", {"x": 1, "y": 9}), # OPEN gate!
        ("Up", {"x": 1, "y": 8}),
        ("Up", {"x": 1, "y": 7}),
        ("Up", {"x": 1, "y": 6}),
    ]):
        pos = mgba.get_coordinates()

if pos == {"x": 1, "y": 6}:
    # Walk RIGHT along Row 6 across Column 10 to 3F East (12, 6)
    print("Crossing horizontally on Row 6 to 3F East...")
    if run_steps([
        ("Right", {"x": 2, "y": 6}),
        ("Right", {"x": 3, "y": 6}),
        ("Right", {"x": 4, "y": 6}),
        ("Right", {"x": 5, "y": 6}),
        ("Right", {"x": 6, "y": 6}),
        ("Right", {"x": 7, "y": 6}),
        ("Right", {"x": 8, "y": 6}),
        ("Right", {"x": 9, "y": 6}),
        ("Right", {"x": 10, "y": 6}),
        ("Right", {"x": 11, "y": 6}),
        ("Right", {"x": 12, "y": 6}),
    ]):
        pos = mgba.get_coordinates()

if pos == {"x": 12, "y": 6}:
    # Walk horizontally along Row 6 to Column 19
    print("Walking on 3F East to Column 19...")
    if run_steps([
        ("Right", {"x": 13, "y": 6}),
        ("Right", {"x": 14, "y": 6}),
        ("Right", {"x": 15, "y": 6}),
        ("Right", {"x": 16, "y": 6}),
        ("Right", {"x": 17, "y": 6}),
        ("Right", {"x": 18, "y": 6}),
        ("Right", {"x": 19, "y": 6}),
    ]):
        pos = mgba.get_coordinates()

if pos == {"x": 19, "y": 6}:
    # Walk UP Column 19 to Row 3
    print("Walking UP Column 19 to Row 3...")
    if run_steps([
        ("Up", {"x": 19, "y": 5}),
        ("Up", {"x": 19, "y": 4}),
        ("Up", {"x": 19, "y": 3}),
    ]):
        pos = mgba.get_coordinates()

if pos == {"x": 19, "y": 3}:
    # Walk RIGHT along Row 3 to Column 26
    print("Walking RIGHT along Row 3 to Column 26...")
    if run_steps([
        ("Right", {"x": 20, "y": 3}),
        ("Right", {"x": 21, "y": 3}),
        ("Right", {"x": 22, "y": 3}),
        ("Right", {"x": 23, "y": 3}),
        ("Right", {"x": 24, "y": 3}),
        ("Right", {"x": 25, "y": 3}),
        ("Right", {"x": 26, "y": 3}),
    ]):
        pos = mgba.get_coordinates()

if pos == {"x": 26, "y": 3}:
    # Step DOWN into the pitfall to fall to 1F East
    print("Stepping DOWN into the pitfall...")
    mgba.press_buttons(["Down"])
    time.sleep(1.5)
    pos = mgba.get_coordinates()
    print("Final position after drop:", pos)
