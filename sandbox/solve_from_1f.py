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
print("Starting 1F West to B1F West NORTH route:", pos)

if pos == {"x": 4, "y": 10}:
    steps = [
        ("Right", {"x": 5, "y": 10}),
        ("Down", {"x": 5, "y": 11}),
    ]
    if not run_steps(steps):
        print("Failed to reach (5, 11)")
        exit(1)
    pos = mgba.get_coordinates()

# On 1F West (landing at 5, 11 or 5, 10). Walk to Row 5 Column 13 (13, 5)
if pos == {"x": 5, "y": 11}:
    print("Walking to Row 5 Column 13 on 1F West...")
    steps = []
    # From (5, 11), walk RIGHT along Row 11 to Column 13 (13, 11)
    for x in range(6, 14):
        steps.append(("Right", {"x": x, "y": 11}))
    # Walk UP Column 13 to Row 5 (13, 5)
    for y in range(10, 4, -1):
        steps.append(("Up", {"x": 13, "y": y}))
        
    if not run_steps(steps):
        print("Failed to reach (13, 5)")
        exit(1)
    pos = mgba.get_coordinates()

# Now on (13, 5). Walk RIGHT along Row 5 across Column 13 to 1F East (22, 5)
if pos == {"x": 13, "y": 5}:
    print("Crossing horizontally to 1F East along Row 5 to Column 22...")
    steps = []
    for x in range(14, 23):
        steps.append(("Right", {"x": x, "y": 5}))
    if not run_steps(steps):
        print("Failed to reach (22, 5) on 1F East")
        exit(1)
    pos = mgba.get_coordinates()

# Walk UP Column 22 to Row 2 (22, 2)
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

# Step UP onto (22, 2) to warp DOWN to B1F East
if pos == {"x": 22, "y": 3}:
    print("Stepping UP to warp down to B1F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after warping down to B1F East:", pos)

# Now on B1F East (landing at 22, 3 or 22, 2). Walk to Row 4 (y=4)
if pos["x"] == 22 and (pos["y"] == 2 or pos["y"] == 3):
    print("Walking DOWN to Row 4...")
    steps = []
    for y in range(pos["y"] + 1, 5):
        steps.append(("Down", {"x": 22, "y": y}))
    if not run_steps(steps):
        print("Failed to reach (22, 4) on B1F East")
        exit(1)
    pos = mgba.get_coordinates()

# Walk LEFT along Row 4 to Column 19 (19, 4)
if pos == {"x": 22, "y": 4}:
    print("Walking LEFT along Row 4 to Column 19...")
    steps = []
    for x in range(21, 18, -1):
        steps.append(("Left", {"x": x, "y": 4}))
    if not run_steps(steps):
        print("Failed to reach (19, 4) on B1F East")
        exit(1)
    pos = mgba.get_coordinates()

# Walk DOWN to Row 5 (19, 5)
if pos == {"x": 19, "y": 4}:
    print("Walking DOWN to Row 5...")
    if not walk_step("Down", {"x": 19, "y": 5}):
        print("Failed to reach (19, 5)")
        exit(1)
    pos = mgba.get_coordinates()

# Cross B1F East to B1F West NORTH along Row 5 across Column 9 gate
if pos == {"x": 19, "y": 5}:
    print("Walking LEFT along Row 5 to B1F West NORTH (Secret Key Room)...")
    steps = []
    for x in range(18, 0, -1):
        steps.append(("Left", {"x": x, "y": 5}))
    if not run_steps(steps):
        print("Failed to reach (1, 5) on B1F West NORTH")
        exit(1)
    pos = mgba.get_coordinates()

# Standing at (1, 5) facing UP, pick up the Secret Key!
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
