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

def run_steps(steps):
    for d, c in steps:
        if not walk_step(d, c):
            return False
    return True

# Ensure any active menus are dismissed
mgba.press_buttons(["B"])
time.sleep(0.4)

pos = mgba.get_coordinates()
print("Starting walk to Fuchsia Gym from position:", pos)

# Step 1: Walk Down Column 19 to Row 13
if pos["x"] == 19 and pos["y"] < 13:
    print("Walking Down Column 19 to Row 13...")
    steps_down = []
    for y in range(pos["y"] + 1, 14):
        steps_down.append(("Down", {"x": 19, "y": y}))
    if not run_steps(steps_down):
        print("Failed to reach (19, 13)")
        exit(1)
    pos = mgba.get_coordinates()

# Step 2: Walk Right on Row 13 to Column 24
if pos == {"x": 19, "y": 13}:
    print("Walking Right Row 13 to Column 24...")
    steps_right = []
    for x in range(20, 25):
        steps_right.append(("Right", {"x": x, "y": 13}))
    if not run_steps(steps_right):
        print("Failed to reach (24, 13)")
        exit(1)
    pos = mgba.get_coordinates()

# Step 3: Walk Down Column 24 to Row 27
if pos == {"x": 24, "y": 13}:
    print("Walking Down Column 24 to Row 27...")
    steps_down = []
    for y in range(14, 28):
        steps_down.append(("Down", {"x": 24, "y": y}))
    if not run_steps(steps_down):
        print("Failed to reach (24, 27)")
        exit(1)
    pos = mgba.get_coordinates()

# Step 4: Walk Left Row 27 to Column 5
if pos == {"x": 24, "y": 27}:
    print("Walking Left Row 27 to Column 5...")
    steps_left = []
    for x in range(23, 4, -1):
        steps_left.append(("Left", {"x": x, "y": 27}))
    if not run_steps(steps_left):
        print("Failed to reach (5, 27)")
        exit(1)
    pos = mgba.get_coordinates()

# Step 5: Step UP to enter the Gym!
if pos == {"x": 5, "y": 27}:
    print("Entering the Fuchsia Gym...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position inside Gym:", pos)
