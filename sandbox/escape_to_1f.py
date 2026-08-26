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
print("Starting position on B1F West:", pos)

# Step 1: Walk to the stairs at (7, 10) on B1F West and warp up to 1F West (landing at (7, 11) or (7, 10))
if pos == {"x": 3, "y": 11}:
    print("Walking to B1F West stairs...")
    if not run_steps([
        ("Right", {"x": 4, "y": 11}),
        ("Right", {"x": 5, "y": 11}),
        ("Right", {"x": 6, "y": 11}),
        ("Right", {"x": 7, "y": 11}),
    ]):
        print("Failed to reach (7, 11)")
        exit(1)
    
    print("Stepping UP onto stairs to warp UP to 1F West...")
    # Stepping UP on (7, 11) onto (7, 10) warps us up to 1F West, which lands us at (7, 11) on 1F West
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after warping UP to 1F West:", pos)

# Step 2: From 1F West landing (7, 11), walk to exit at (5, 27) (or step down to leave)
# The exit mat is at Column 5, Row 27. Walking Down from (5, 26) onto (5, 27) exits the mansion.
# First, let's walk from (7, 11) to Column 5:
# - Walk Left to Column 5: (7, 11) -> (6, 11) -> (5, 11)
# - Walk Down Column 5 to Row 27: (5, 11) -> ... -> (5, 27)
# Let's do this in the script!
if pos == {"x": 7, "y": 11}:
    print("Walking to 1F West exit Column 5...")
    if not run_steps([
        ("Left", {"x": 6, "y": 11}),
        ("Left", {"x": 5, "y": 11}),
    ]):
        print("Failed to reach 1F West Column 5")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 5, "y": 11}:
    print("Walking Down Column 5 to Row 27 to exit...")
    if not run_steps([("Down", {"x": 5, "y": 11 + i + 1}) for i in range(16)]):
        print("Failed to exit the mansion")
        exit(1)
    pos = mgba.get_coordinates()
    print("Final position after exit:", pos)
