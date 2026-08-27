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

# Ensure menu/battle is cleared
for _ in range(3):
    handle_any_menu_or_battle()

pos = mgba.get_coordinates()
print("Starting position:", pos)

# We are at (8, 11) on 2F West. Walk LEFT to Column 5 (5, 11)
if pos == {"x": 8, "y": 11}:
    print("Walking LEFT to Column 5...")
    steps = [
        ("Left", {"x": 7, "y": 11}),
        ("Left", {"x": 6, "y": 11}),
        ("Left", {"x": 5, "y": 11}),
    ]
    if not run_steps(steps):
        print("Failed to reach (5, 11)")
        exit(1)
    pos = mgba.get_coordinates()

# Now at (5, 11). Walk UP Column 5 directly to Row 3 (5, 3)
if pos == {"x": 5, "y": 11}:
    print("Walking UP Column 5 directly to Row 3...")
    steps = []
    for y in range(10, 2, -1):
        steps.append(("Up", {"x": 5, "y": y}))
    if not run_steps(steps):
        print("Failed to reach (5, 3) on 2F West. We might be in State A!")
        exit(1)
    pos = mgba.get_coordinates()

# Walk RIGHT along Row 3 to Column 18 (crosses horizontally to 2F East)
if pos == {"x": 5, "y": 3}:
    print("Crossing horizontally to 2F East along Row 3...")
    steps = []
    for x in range(6, 19):
        steps.append(("Right", {"x": x, "y": 3}))
    if not run_steps(steps):
        print("Failed to reach (18, 3) on 2F East")
        exit(1)
    pos = mgba.get_coordinates()

# Walk DOWN Column 18 to Row 10 (18, 10)
if pos == {"x": 18, "y": 3}:
    print("Walking DOWN Column 18 to Row 10...")
    steps = []
    for y in range(4, 11):
        steps.append(("Down", {"x": 18, "y": y}))
    if not run_steps(steps):
        print("Failed to reach (18, 10) on 2F East")
        exit(1)
    pos = mgba.get_coordinates()

# Walk LEFT along Row 10 to Column 15 (15, 10)
if pos == {"x": 18, "y": 10}:
    print("Walking LEFT along Row 10 to (15, 10)...")
    steps = [
        ("Left", {"x": 17, "y": 10}),
        ("Left", {"x": 16, "y": 10}),
        ("Left", {"x": 15, "y": 10}),
    ]
    if not run_steps(steps):
        print("Failed to reach (15, 10) on 2F East")
        exit(1)
    pos = mgba.get_coordinates()

# Step DOWN onto stairs at (15, 11) to warp UP to 3F East (landing at 16, 11 or 15, 11)
if pos == {"x": 15, "y": 10}:
    print("Stepping DOWN to warp UP to 3F East...")
    mgba.press_buttons(["Down"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after warping UP to 3F East:", pos)

# Now on 3F East (landing at 16, 11 or 15, 11). Walk RIGHT along Row 11 to Column 20
if pos == {"x": 16, "y": 11} or pos == {"x": 15, "y": 11}:
    pos_x = pos["x"]
    print("Walking RIGHT along Row 11 to Column 20...")
    steps = []
    for x in range(pos_x + 1, 21):
        steps.append(("Right", {"x": x, "y": 11}))
    if not run_steps(steps):
        print("Failed to reach (20, 11) on 3F East")
        exit(1)
    pos = mgba.get_coordinates()

# Walk UP Column 20 to Row 3 (20, 3)
if pos == {"x": 20, "y": 11}:
    print("Walking UP Column 20 to Row 3...")
    steps = []
    for y in range(10, 2, -1):
        steps.append(("Up", {"x": 20, "y": y}))
    if not run_steps(steps):
        print("Failed to reach (20, 3) on 3F East")
        exit(1)
    pos = mgba.get_coordinates()

# Walk RIGHT along Row 3 to Column 26 (26, 3)
if pos == {"x": 20, "y": 3}:
    print("Walking RIGHT along Row 3 to Column 26...")
    steps = []
    for x in range(21, 27):
        steps.append(("Right", {"x": x, "y": 3}))
    if not run_steps(steps):
        print("Failed to reach (26, 3) on 3F East")
        exit(1)
    pos = mgba.get_coordinates()

# Step DOWN to drop through the pitfall to 1F East inside the fenced room (landing at 26, 4)
if pos == {"x": 26, "y": 3}:
    print("Stepping DOWN to drop through the pitfall to 1F East fenced room...")
    mgba.press_buttons(["Down"])
    time.sleep(2.5)
    pos = mgba.get_coordinates()
    print("Position after dropping to 1F East:", pos)

# Now inside the fenced room at (26, 4). Walk LEFT along Row 4 to Column 22 (22, 4)
if pos == {"x": 26, "y": 4} or pos == {"x": 25, "y": 4}:
    pos_x = pos["x"]
    print("Walking LEFT along Row 4 to Column 22...")
    steps = []
    for x in range(pos_x - 1, 21, -1):
        steps.append(("Left", {"x": x, "y": 4}))
    if not run_steps(steps):
        print("Failed to reach (22, 4) on 1F East")
        exit(1)
    pos = mgba.get_coordinates()

# Walk UP to (22, 3)
if pos == {"x": 22, "y": 4}:
    print("Walking UP to (22, 3)...")
    if not walk_step("Up", {"x": 22, "y": 3}):
        print("Failed to reach (22, 3)")
        exit(1)
    pos = mgba.get_coordinates()

# Step UP to warp down to B1F East (landing at 22, 3 or 22, 2)
if pos == {"x": 22, "y": 3}:
    print("Stepping UP to warp down to B1F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after warping down to B1F East:", pos)

# Now on B1F East (landing at 22, 3 or 22, 2). Walk to Row 5
if pos["x"] == 22 and (pos["y"] == 2 or pos["y"] == 3):
    print("Walking to Row 5...")
    steps = []
    for y in range(pos["y"] + 1, 6):
        steps.append(("Down", {"x": 22, "y": y}))
    if not run_steps(steps):
        print("Failed to reach (22, 5) on B1F East")
        exit(1)
    pos = mgba.get_coordinates()

# Cross B1F East to B1F West NORTH along Row 5 across Column 9 gate
if pos == {"x": 22, "y": 5}:
    print("Walking LEFT along Row 5 to Column 19...")
    steps = [
        ("Left", {"x": 21, "y": 5}),
        ("Left", {"x": 20, "y": 5}),
        ("Left", {"x": 19, "y": 5}),
    ]
    if not run_steps(steps):
        print("Failed to reach (19, 5) on B1F East")
        exit(1)
    pos = mgba.get_coordinates()

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
