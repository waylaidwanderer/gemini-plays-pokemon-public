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

# Ensure menu/battle is cleared
for _ in range(3):
    handle_any_menu_or_battle()

pos = mgba.get_coordinates()
print("Starting position:", pos)

if pos == {"x": 10, "y": 7}:
    print("Walking to Column 12 and DOWN to Row 11...")
    steps = [
        ("Right", {"x": 11, "y": 7}),
        ("Right", {"x": 12, "y": 7}),
        ("Down", {"x": 12, "y": 8}),
        ("Down", {"x": 12, "y": 9}),
        ("Down", {"x": 12, "y": 10}),
        ("Down", {"x": 12, "y": 11}),
    ]
    if not run_steps(steps):
        print("Failed to reach (12, 11)")
        exit(1)
    pos = mgba.get_coordinates()

# Now at (12, 11). Walk LEFT along Row 11 to the stairs at (7, 11) to warp to 2F West
if pos == {"x": 12, "y": 11}:
    print("Walking LEFT along Row 11 to the stairs at (7, 11)...")
    steps = [
        ("Left", {"x": 11, "y": 11}),
        ("Left", {"x": 10, "y": 11}),
        ("Left", {"x": 9, "y": 11}),
        ("Left", {"x": 8, "y": 11}),
    ]
    if not run_steps(steps):
        print("Failed to reach (8, 11)")
        exit(1)
        
    print("Stepping LEFT onto (7, 11) to warp to 2F West...")
    mgba.press_buttons(["Left"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after warping UP to 2F West:", pos)

# Now on 2F West (landing at 5, 11 or 5, 10? Wait, the stairs warp lands at 5, 11). Walk UP Column 5 to Row 3 (5, 3)
if pos == {"x": 5, "y": 11} or pos == {"x": 5, "y": 10}:
    pos_y = pos["y"]
    print("Walking UP Column 5 directly to Row 3...")
    steps = []
    for y in range(pos_y - 1, 2, -1):
        steps.append(("Up", {"x": 5, "y": y}))
    if not run_steps(steps):
        print("Failed to reach (5, 3) on 2F West. We might be in State A!")
        exit(1)
    pos = mgba.get_coordinates()

print("Reached (5, 3) successfully!")
