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

# Starting at (6, 8) on 2F West (State B)
success = True

# 1. Walk back to (5, 11) on 2F West
print("Walking to (5, 11) on 2F West...")
steps_to_5_11 = [
    ("Down", {"x": 6, "y": 9}),
    ("Down", {"x": 6, "y": 10}),
    ("Down", {"x": 6, "y": 11}),
    ("Left", {"x": 5, "y": 11}),
]
for d, c in steps_to_5_11:
    if not walk_step(d, c):
        success = False
        break

if success:
    # 2. Walk to Column 0 Row 13 on 2F West
    print("Walking to (0, 13)...")
    steps_to_0_13 = [
        ("Down", {"x": 5, "y": 12}),
        ("Down", {"x": 5, "y": 13}),
        ("Left", {"x": 4, "y": 13}),
        ("Left", {"x": 3, "y": 13}),
        ("Left", {"x": 2, "y": 13}),
        ("Left", {"x": 1, "y": 13}),
        ("Left", {"x": 0, "y": 13}),
    ]
    for d, c in steps_to_0_13:
        if not walk_step(d, c):
            success = False
            break
            
    if success:
        # 3. Walk UP Column 0 to Row 4
        print("Walking UP Column 0 to Row 4...")
        steps_up_col0 = []
        for y in range(12, 3, -1):
            steps_up_col0.append(("Up", {"x": 0, "y": y}))
        for d, c in steps_up_col0:
            if not walk_step(d, c):
                success = False
                break
                
        if success:
            # 4. Step UP onto stairs at (0, 3) to warp DOWN to 1F West
            print("Stepping UP onto stairs to warp DOWN to 1F West...")
            mgba.press_buttons(["Up"])
            time.sleep(1.5)
            pos = mgba.get_coordinates()
            print(f"Warped DOWN to 1F West! Landing position: {pos}")
            
            # 5. On 1F West (landing at 0, 4), walk to (3, 3)
            print("Walking to (3, 3) on 1F West...")
            steps_to_3_3 = [
                ("Right", {"x": 1, "y": 4}),
                ("Right", {"x": 2, "y": 4}),
                ("Right", {"x": 3, "y": 4}),
                ("Up", {"x": 3, "y": 3}),
            ]
            for d, c in steps_to_3_3:
                if not walk_step(d, c):
                    success = False
                    break
                    
            if success:
                # 6. Face UP towards (3, 2) and check for switch!
                print("Reached (3, 3)! Facing UP to test if (3, 2) has a switch...")
                mgba.press_buttons(["Up"])
                time.sleep(0.5)
                
                mgba.press_buttons(["A"])
                time.sleep(1.0)
                # Take screenshot of dialogue
                scr = mgba.take_screenshot()
                print(f"Screenshot after A: {scr}")
                
                # Try to dismiss text if any
                for _ in range(3):
                    mgba.press_buttons(["B"])
                    time.sleep(0.3)
                
                # Check position
                print("Final Position:", mgba.get_coordinates())
