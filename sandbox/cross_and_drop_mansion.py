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
    print("Walking the bypass path to 2F East Row 3...")
    if not run_steps([
        ("Down", {"x": 2, "y": 13}),
        ("Right", {"x": 3, "y": 13}),
        ("Right", {"x": 4, "y": 13}),
        ("Right", {"x": 5, "y": 13}),
        ("Right", {"x": 6, "y": 13}),
        ("Up", {"x": 6, "y": 12}),
        ("Up", {"x": 6, "y": 11}),
        ("Up", {"x": 6, "y": 10}),
        ("Up", {"x": 6, "y": 9}),      # Row 9 gate is open in State B!
        ("Left", {"x": 5, "y": 9}),    # Bypass down staircase by going Left
        ("Up", {"x": 5, "y": 8}),
        ("Up", {"x": 5, "y": 7}),
        ("Up", {"x": 5, "y": 6}),
        ("Up", {"x": 5, "y": 5}),
        ("Up", {"x": 5, "y": 4}),
        ("Up", {"x": 5, "y": 3}),      # Row 3 (above the barriers)
    ]):
        print("Failed to reach Row 3 on Column 5")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 5, "y": 3}:
    print("Walking RIGHT along Row 3 to (18, 3)...")
    if not run_steps([("Right", {"x": 5 + i + 1, "y": 3}) for i in range(13)]):
        print("Failed to reach (18, 3)")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 18, "y": 3}:
    print("Walking DOWN to (18, 10)...")
    if not run_steps([("Down", {"x": 18, "y": 3 + i + 1}) for i in range(7)]):
        print("Failed to reach (18, 10)")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 18, "y": 10}:
    print("Walking LEFT to (15, 10)...")
    if not run_steps([
        ("Left", {"x": 17, "y": 10}),
        ("Left", {"x": 16, "y": 10}),
        ("Left", {"x": 15, "y": 10}),
    ]):
        print("Failed to reach (15, 10)")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 15, "y": 10}:
    print("Stepping DOWN onto stairs to warp UP to 3F East (landing at 16, 11)...")
    # Walking Down onto (15, 11) warps us up to 3F East, which lands us at (16, 11)
    if not walk_step("Down", {"x": 16, "y": 11}):
        print("Failed to warp to 3F East")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 16, "y": 11}:
    print("Successfully on 3F East! Walking to (20, 11)...")
    if not run_steps([
        ("Right", {"x": 17, "y": 11}),
        ("Right", {"x": 18, "y": 11}),
        ("Right", {"x": 19, "y": 11}),
        ("Right", {"x": 20, "y": 11}),
    ]):
        print("Failed to reach (20, 11)")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 20, "y": 11}:
    print("Walking UP Column 20 to Row 3...")
    if not run_steps([("Up", {"x": 20, "y": 11 - i - 1}) for i in range(8)]):
        print("Failed to reach Row 3 on Column 20")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 20, "y": 3}:
    print("Walking RIGHT along Row 3 to (26, 3)...")
    if not run_steps([("Right", {"x": 20 + i + 1, "y": 3}) for i in range(6)]):
        print("Failed to reach (26, 3)")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 26, "y": 3}:
    print("Dropping through the pitfall to 1F East!")
    # Stepping DOWN on (26, 3) falls through the pitfall (26, 4), landing on 1F East inside the fenced room
    mgba.press_buttons(["Down"])
    time.sleep(1.5)
    pos = mgba.get_coordinates()
    print("Final position after dropping:", pos)
