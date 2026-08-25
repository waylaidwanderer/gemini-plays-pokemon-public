import mgba
import time
from PIL import Image

def handle_any_menu_or_battle():
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
        print(f"Menu/Battle detected! (B/W percentage: {percentage*100:.2f}%)")
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        
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
            print("Still in battle/menu. Attempting RUN...")
            mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A"])
            time.sleep(1.5)
            for _ in range(4):
                mgba.press_buttons(["B"])
                time.sleep(0.3)
        else:
            print("Successfully dismissed dialogue!")
        return True
    return False

def walk_step(direction, expected_coords, retries=15):
    for i in range(retries):
        if handle_any_menu_or_battle():
            pos = mgba.get_coordinates()
            if pos == expected_coords:
                print(f"Reached expected {expected_coords} after battle.")
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

# Starting at (15, 7) on 2F East (State B)
success = True

# 1. Walk LEFT to (12, 7)
steps_left = [
    ("Left", {"x": 14, "y": 7}),
    ("Left", {"x": 13, "y": 7}),
    ("Left", {"x": 12, "y": 7}),
]
for d, c in steps_left:
    if not walk_step(d, c):
        success = False
        break

if success:
    # 2. Walk DOWN Column 12 to (12, 11)
    steps_down_col12 = [
        ("Down", {"x": 12, "y": 8}), # Open in State B!
        ("Down", {"x": 12, "y": 9}),
        ("Down", {"x": 12, "y": 10}),
        ("Down", {"x": 12, "y": 11}),
    ]
    for d, c in steps_down_col12:
        if not walk_step(d, c):
            success = False
            break

if success:
    # 3. Walk LEFT Row 11 to Column 3 on 2F West
    print("Reached (12, 11)! Walking LEFT to Column 3...")
    steps_left_row11 = [
        ("Left", {"x": 11, "y": 11}),
        ("Left", {"x": 10, "y": 11}),
        ("Left", {"x": 9, "y": 11}),
        ("Left", {"x": 8, "y": 11}),
        ("Left", {"x": 7, "y": 11}),
        ("Left", {"x": 6, "y": 11}),
        ("Left", {"x": 5, "y": 11}),
        ("Left", {"x": 4, "y": 11}),
        ("Left", {"x": 3, "y": 11}),
    ]
    for d, c in steps_left_row11:
        if not walk_step(d, c):
            success = False
            break

if success:
    # 4. Walk DOWN Column 3 to (3, 12), then LEFT to (2, 12)
    print("Reached (3, 11)! Walking DOWN to (3, 12) then LEFT to (2, 12)...")
    success = walk_step("Down", {"x": 3, "y": 12})
    if success:
        success = walk_step("Left", {"x": 2, "y": 12})

if success:
    print("Reached (2, 12) on 2F West! Facing UP towards the switch...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # Take screenshot before A
    img_before = mgba.take_screenshot()
    print("Screenshot before A:", img_before)
    
    # Press A
    print("Pressing A (1st time)...")
    mgba.press_buttons(["A"])
    time.sleep(2.0) # Long wait to ensure dialogue is fully open
    img_1 = mgba.take_screenshot()
    print("Screenshot after 1st A:", img_1)
    
    # Press A again (YES)
    print("Pressing A (2nd time) to select YES...")
    mgba.press_buttons(["A"])
    time.sleep(2.0) # Long wait to ensure "Pressed it!" text finishes scrolling
    img_2 = mgba.take_screenshot()
    print("Screenshot after 2nd A:", img_2)
    
    # Press A again (Dismiss)
    print("Pressing A (3rd time) to dismiss dialogue...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    img_3 = mgba.take_screenshot()
    print("Screenshot after 3rd A:", img_3)
    
    # Check dialog box percentage on screenshots to see if they were active
    def check_bw(path):
        img = Image.open(path)
        img_std = img.resize((160, 144), Image.Resampling.NEAREST)
        black_or_white = 0
        for y in range(115, 140):
            for x in range(10, 150):
                r, g, b = img_std.getpixel((x, y))
                if (r < 50 and g < 50 and b < 50) or (r > 200 and g > 200 and b > 200):
                    black_or_white += 1
        return black_or_white / 3500
        
    print(f"B/W % before A: {check_bw(img_before)*100:.2f}%")
    print(f"B/W % after 1st A: {check_bw(img_1)*100:.2f}%")
    print(f"B/W % after 2nd A: {check_bw(img_2)*100:.2f}%")
    print(f"B/W % after 3rd A: {check_bw(img_3)*100:.2f}%")
    
else:
    print("Failed to reach (2, 12).")
