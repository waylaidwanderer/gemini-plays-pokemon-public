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

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

pos = mgba.get_coordinates()
print("Starting position inside fenced room 1F East:", pos)

# 1. Walk DOWN to (26, 5) to bypass the Row 4 Column 25 wall
if pos == {"x": 26, "y": 4}:
    print("Walking DOWN to (26, 5)...")
    if not walk_step("Down", {"x": 26, "y": 5}):
        print("Failed to reach (26, 5)")
        exit(1)
    pos = mgba.get_coordinates()

# 2. Walk LEFT along Row 5 to Column 22 (22, 5)
if pos == {"x": 26, "y": 5}:
    print("Walking LEFT to (22, 5)...")
    steps = [
        ("Left", {"x": 25, "y": 5}),
        ("Left", {"x": 24, "y": 5}),
        ("Left", {"x": 23, "y": 5}),
        ("Left", {"x": 22, "y": 5}),
    ]
    if not run_steps(steps):
        print("Failed to reach (22, 5)")
        exit(1)
    pos = mgba.get_coordinates()

# 3. Walk UP Column 22 to Row 2 (22, 2)
if pos == {"x": 22, "y": 5}:
    print("Walking UP Column 22 to Row 2...")
    steps = [
        ("Up", {"x": 22, "y": 4}),
        ("Up", {"x": 22, "y": 3}),
    ]
    if not run_steps(steps):
        print("Failed to reach Row 3 on Column 22")
        exit(1)
    pos = mgba.get_coordinates()

# 4. Step UP onto (22, 2) to warp DOWN to B1F East
if pos == {"x": 22, "y": 3}:
    print("Stepping UP to warp down to B1F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after warping down to B1F East:", pos)

# 5. Cross B1F East to B1F West NORTH and retrieve Secret Key!
if pos == {"x": 22, "y": 2} or pos == {"x": 22, "y": 3}:
    print("Crossing to B1F West NORTH...")
    if pos["y"] == 2:
        if not walk_step("Down", {"x": 22, "y": 3}):
            print("Failed to move to (22, 3)")
            exit(1)
            
    if not run_steps([
        ("Down", {"x": 22, "y": 4}),
        ("Left", {"x": 21, "y": 4}),
        ("Left", {"x": 20, "y": 4}),
        ("Left", {"x": 19, "y": 4}),
        ("Down", {"x": 19, "y": 5}),
    ]):
        print("Failed to reach Row 5 on B1F East")
        exit(1)
        
    steps_left = []
    for x in range(18, 0, -1):
        steps_left.append(("Left", {"x": x, "y": 5}))
    if not run_steps(steps_left):
        print("Failed to reach Secret Key room")
        exit(1)
    pos = mgba.get_coordinates()

# 6. Standing at (1, 5) facing UP, pick up the Secret Key!
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

print("Mansion master route completed successfully!")
