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

# Starting at (11, 5) in Saffron City
print("Starting walk out of Saffron City...")
success = True

# 1. Walk RIGHT to Column 37 (the eastern vertical street)
print("Walking RIGHT along Row 5 to Column 37...")
for x in range(12, 38):
    if not walk_step("Right", {"x": x, "y": 5}):
        success = False
        break

if success:
    # 2. Walk DOWN Column 37 to Row 11 (just before the first decorative post at (37, 12))
    print("Walking DOWN Column 37 to Row 11...")
    for y in range(6, 12):
        if not walk_step("Down", {"x": 37, "y": y}):
            success = False
            break

if success:
    # 3. Bypass post at (37, 12)
    # Bypass: Walk right to (38, 11), down 2 steps to (38, 13), left to (37, 13)
    print("Bypassing first decorative post...")
    bypass_1 = [
        ("Right", {"x": 38, "y": 11}),
        ("Down", {"x": 38, "y": 12}),
        ("Down", {"x": 38, "y": 13}),
        ("Left", {"x": 37, "y": 13}),
    ]
    for d, c in bypass_1:
        if not walk_step(d, c):
            success = False
            break

if success:
    # 4. Walk DOWN Column 37 to Row 18 (just before the second decorative post at (37, 19))
    print("Walking DOWN Column 37 to Row 18...")
    for y in range(14, 19):
        if not walk_step("Down", {"x": 37, "y": y}):
            success = False
            break

if success:
    # 5. Bypass post at (37, 19)
    # Bypass: Walk left to (36, 18), down 2 steps to (36, 20), right to (37, 20)
    print("Bypassing second decorative post...")
    bypass_2 = [
        ("Left", {"x": 36, "y": 18}),
        ("Down", {"x": 36, "y": 19}),
        ("Down", {"x": 36, "y": 20}),
        ("Right", {"x": 37, "y": 20}),
    ]
    for d, c in bypass_2:
        if not walk_step(d, c):
            success = False
            break

if success:
    # 6. Walk DOWN Column 37 to Row 30
    print("Walking DOWN Column 37 to Row 30...")
    for y in range(21, 31):
        if not walk_step("Down", {"x": 37, "y": y}):
            success = False
            break

if success:
    # 7. Walk LEFT along Row 30 to Column 18
    print("Walking LEFT along Row 30 to Column 18...")
    for x in range(36, 17, -1):
        if not walk_step("Left", {"x": x, "y": 30}):
            success = False
            break

if success:
    print("Successfully navigated to (18, 30) near Saffron South Gatehouse!")
    # Saffron South Gatehouse is located at (18, 31). Let's step DOWN to enter!
    mgba.press_buttons(["Down"])
    time.sleep(1.5)
    print("New position inside Gatehouse:", mgba.get_coordinates())
