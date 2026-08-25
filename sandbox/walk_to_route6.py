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

# Starting at (8, 11) in Saffron City
print("Starting Saffron South-Gate Bypass Walk...")
success = True

# 1. Walk DOWN Column 8 to Row 30
print("Walking DOWN Column 8 to Row 30...")
for y in range(12, 31):
    if not walk_step("Down", {"x": 8, "y": y}):
        success = False
        break

if success:
    # 2. Walk RIGHT along Row 30 to Column 18
    print("Reached (8, 30)! Walking RIGHT to Column 18...")
    for x in range(9, 19):
        if not walk_step("Right", {"x": x, "y": 30}):
            success = False
            break

if success:
    print("Reached (18, 30) Saffron South Gatehouse! Stepping DOWN to enter...")
    mgba.press_buttons(["Down"])
    time.sleep(1.5)
    print("Warped into Gatehouse! Current position:", mgba.get_coordinates())
    
    # 3. Step DOWN through Gatehouse to exit Saffron City to Route 6
    print("Stepping DOWN to exit Saffron City to Route 6...")
    mgba.press_buttons(["Down"])
    time.sleep(1.5)
    print("Warped out onto Route 6! Position:", mgba.get_coordinates())
else:
    print("Failed during Saffron South Gate bypass.")
