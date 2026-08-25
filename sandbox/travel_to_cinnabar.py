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

# Current position is (9, 12) on Cinnabar Island. First press B to clear the active signpost dialogue.
print("Dismissing POKEMON LAB dialogue...")
mgba.press_buttons(["B"])
time.sleep(0.5)

# Step 1: Walk to (18, 12)
print("Walking to (18, 12)...")
success = True
for x in range(10, 19):
    if not walk_step("Right", {"x": x, "y": 12}):
        success = False
        break

if success:
    # Step 2: Walk UP to (18, 5)
    print("Walking UP to (18, 5)...")
    for y in range(11, 4, -1):
        if not walk_step("Up", {"x": 18, "y": y}):
            success = False
            break

if success:
    # Step 3: Walk LEFT to (6, 5)
    print("Walking LEFT to (6, 5)...")
    for x in range(17, 5, -1):
        if not walk_step("Left", {"x": x, "y": 5}):
            success = False
            break

if success:
    # Step 4: Walk UP to (6, 3) and enter Mansion
    print("Walking to entrance...")
    if walk_step("Up", {"x": 6, "y": 4}):
        if walk_step("Up", {"x": 6, "y": 3}):
            print("At entrance. Entering Mansion 1F West...")
            mgba.press_buttons(["Up"])
            time.sleep(1.5)
            pos = mgba.get_coordinates()
            print("Entered Mansion! Position:", pos)
            
            # Step 5: Walk UP Column 5 inside Mansion from (5, 27) to (5, 11)
            if pos == {"x": 5, "y": 27}:
                print("Walking UP Column 5 to Row 11...")
                for y in range(26, 10, -1):
                    if not walk_step("Up", {"x": 5, "y": y}):
                        success = False
                        break
                        
                if success:
                    # Step 6: Walk to (5, 10) stairs
                    steps_1f_stairs = [
                        ("Right", {"x": 6, "y": 11}),
                        ("Right", {"x": 7, "y": 11}),
                        ("Right", {"x": 8, "y": 11}),
                        ("Up", {"x": 8, "y": 10}),
                        ("Left", {"x": 7, "y": 10}),
                        ("Left", {"x": 6, "y": 10}),
                        ("Left", {"x": 5, "y": 10}),
                    ]
                    for d, c in steps_1f_stairs:
                        if not walk_step(d, c):
                            success = False
                            break
                            
                    if success:
                        print("At stairs (5, 10). Stepping LEFT to warp to 2F West...")
                        mgba.press_buttons(["Left"])
                        time.sleep(1.5)
                        print("Landed on 2F West! Position:", mgba.get_coordinates())
else:
    print("Route failed.")
