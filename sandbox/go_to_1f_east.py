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

# Step 1: Walk from (2, 12) back to (5, 11)
if pos == {"x": 2, "y": 12}:
    print("Walking back to Column 5...")
    if not run_steps([
        ("Down", {"x": 2, "y": 13}),
        ("Right", {"x": 3, "y": 13}),
        ("Right", {"x": 4, "y": 13}),
        ("Right", {"x": 5, "y": 13}),
        ("Up", {"x": 5, "y": 12}),
        ("Up", {"x": 5, "y": 11}),
    ]):
        print("Failed to walk back to (5, 11)")
        exit(1)
    pos = mgba.get_coordinates()

# Step 2: Bypass stairs at (5, 10) by going Column 6
if pos == {"x": 5, "y": 11}:
    print("Bypassing 2F West stairs via Column 6...")
    if not run_steps([
        ("Right", {"x": 6, "y": 11}),
        ("Up", {"x": 6, "y": 10}),
        ("Up", {"x": 6, "y": 9}),
        ("Up", {"x": 6, "y": 8}),
        ("Left", {"x": 5, "y": 8}),
    ]):
        print("Failed to bypass stairs")
        exit(1)
    pos = mgba.get_coordinates()

# Step 3: Walk UP Column 5 directly to Row 3
if pos == {"x": 5, "y": 8}:
    print("Walking UP Column 5 directly to Row 3...")
    if not run_steps([
        ("Up", {"x": 5, "y": 7}),
        ("Up", {"x": 5, "y": 6}),
        ("Up", {"x": 5, "y": 5}),
        ("Up", {"x": 5, "y": 4}),
        ("Up", {"x": 5, "y": 3}),
    ]):
        print("Failed to reach Row 3")
        exit(1)
    pos = mgba.get_coordinates()

# Step 4: Cross horizontally from 2F West to 2F East on Row 3
if pos == {"x": 5, "y": 3}:
    print("Crossing horizontally on Row 3 to Column 18...")
    steps = []
    for x in range(6, 19):
        steps.append(("Right", {"x": x, "y": 3}))
    if not run_steps(steps):
        print("Failed to cross to 2F East")
        exit(1)
    pos = mgba.get_coordinates()

# Step 5: Walk DOWN Column 18 to Row 10
if pos == {"x": 18, "y": 3}:
    print("Walking DOWN Column 18 to Row 10...")
    steps = []
    for y in range(4, 11):
        steps.append(("Down", {"x": 18, "y": y}))
    if not run_steps(steps):
        print("Failed to reach Row 10")
        exit(1)
    pos = mgba.get_coordinates()

# Step 6: Walk LEFT along Row 10 to (15, 10)
if pos == {"x": 18, "y": 10}:
    print("Walking LEFT along Row 10 to (15, 10)...")
    if not run_steps([
        ("Left", {"x": 17, "y": 10}),
        ("Left", {"x": 16, "y": 10}),
        ("Left", {"x": 15, "y": 10}),
    ]):
        print("Failed to reach (15, 10)")
        exit(1)
    pos = mgba.get_coordinates()

# Step 7: Step DOWN onto the stairs at (15, 11) on 2F East to warp UP to 3F East
if pos == {"x": 15, "y": 10}:
    print("Stepping DOWN to warp UP to 3F East...")
    mgba.press_buttons(["Down"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after warping UP to 3F East:", pos)

# Step 8: On 3F East, land at (16, 11). Since we are in State B, walk to Column 20, then Row 3, then drop at (26, 4)
if pos == {"x": 16, "y": 11}:
    print("Walking horizontally along Row 11 on 3F East...")
    if not run_steps([
        ("Right", {"x": 17, "y": 11}),
        ("Right", {"x": 18, "y": 11}),
        ("Right", {"x": 19, "y": 11}),
        ("Right", {"x": 20, "y": 11}),
    ]):
        print("Failed to walk Row 11 on 3F East")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 20, "y": 11}:
    print("Walking UP Column 20 to Row 3...")
    steps = []
    for y in range(10, 2, -1):
        steps.append(("Up", {"x": 20, "y": y}))
    if not run_steps(steps):
        print("Failed to walk UP Column 20 on 3F East")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 20, "y": 3}:
    print("Walking RIGHT along Row 3 to Column 26...")
    steps = []
    for x in range(21, 27):
        steps.append(("Right", {"x": x, "y": 3}))
    if not run_steps(steps):
        print("Failed to walk Row 3 on 3F East")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 26, "y": 3}:
    print("Stepping DOWN onto Column 26 to drop through the pitfall...")
    mgba.press_buttons(["Down"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after dropping to 1F East:", pos)

