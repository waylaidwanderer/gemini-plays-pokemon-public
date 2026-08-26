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

# Ensure active
mgba.press_buttons(["B"])
time.sleep(0.5)

pos = mgba.get_coordinates()
print("Starting real Column 12 bypass solver from position:", pos)

# 1. Walk from (10, 13) to Column 12 Row 12 (bypassing Row 13 wall)
if pos == {"x": 10, "y": 13}:
    print("Walking to Column 12 Row 12...")
    if not run_steps([
        ("Up", {"x": 10, "y": 12}),
        ("Right", {"x": 11, "y": 12}),
        ("Right", {"x": 12, "y": 12}),
    ]):
        print("Failed to reach (12, 12)")
        exit(1)
    pos = mgba.get_coordinates()

# 2. Walk UP Column 12 to Row 6
if pos == {"x": 12, "y": 12}:
    print("Walking UP Column 12 to Row 6...")
    steps = []
    for y in range(11, 5, -1):
        steps.append(("Up", {"x": 12, "y": y}))
    if not run_steps(steps):
        print("Failed to reach Row 6 on Column 12")
        exit(1)
    pos = mgba.get_coordinates()

# 3. Walk RIGHT along Row 6 to Column 20 on 3F East, UP Column 20 to Row 3, RIGHT to Column 26 (balcony drop)
if pos == {"x": 12, "y": 6}:
    print("Walking to 3F East balcony drop...")
    steps = []
    for x in range(13, 21):
        steps.append(("Right", {"x": x, "y": 6}))
    for y in range(5, 2, -1):
        steps.append(("Up", {"x": 20, "y": y}))
    for x in range(21, 27):
        steps.append(("Right", {"x": x, "y": 3}))
        
    if not run_steps(steps):
        print("Failed to reach balcony drop on 3F East")
        exit(1)
    pos = mgba.get_coordinates()

# 4. Step DOWN to drop through pitfall to 1F East
if pos == {"x": 26, "y": 3}:
    print("Stepping DOWN to drop through pitfall to 1F East...")
    mgba.press_buttons(["Down"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after dropping to 1F East:", pos)

# 5. Walk to B1F East stairs
if pos == {"x": 26, "y": 4}:
    print("Walking to B1F East stairs...")
    if not run_steps([
        ("Left", {"x": 25, "y": 4}),
        ("Left", {"x": 24, "y": 4}),
        ("Left", {"x": 23, "y": 4}),
        ("Left", {"x": 22, "y": 4}),
        ("Up", {"x": 22, "y": 3}),
    ]):
        print("Failed to reach 1F East stairs")
        exit(1)
        
    print("Stepping UP to warp down to B1F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)
    pos = mgba.get_coordinates()
    print("Position after warping down to B1F East:", pos)

# 6. Cross B1F East to B1F West NORTH and retrieve Secret Key!
if pos == {"x": 22, "y": 3}:
    print("Crossing to B1F West NORTH...")
    if not run_steps([
        ("Down", {"x": 22, "y": 4}),
        ("Left", {"x": 21, "y": 4}),
        ("Left", {"x": 20, "y": 4}),
        ("Left", {"x": 19, "y": 4}),
        ("Down", {"x": 19, "y": 5}),
    ]):
        print("Failed to reach Row 5 on B1F East")
        exit(1)
        
    steps = []
    for x in range(18, 0, -1):
        steps.append(("Left", {"x": x, "y": 5}))
    if not run_steps(steps):
        print("Failed to reach Secret Key room")
        exit(1)
    pos = mgba.get_coordinates()

# 7. Standing at (1, 5) facing UP, pick up the Secret Key!
if pos == {"x": 1, "y": 5}:
    print("Aligning UP towards the Secret Key...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    print("Retrieving the Secret Key...")
    mgba.press_buttons([
        "A", "sleep 2500",
        "A", "sleep 2500",
        "A", "sleep 2500"
    ])
    time.sleep(8.5)
    pos = mgba.get_coordinates()
    print("Final position after picking up Secret Key:", pos)
