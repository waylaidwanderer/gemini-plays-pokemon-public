import mgba
import time
from PIL import Image

def is_dialogue_open():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file).resize((160, 144), Image.Resampling.NEAREST)
    
    # Dialogue box border at y=112 (Check if solid black)
    r_border, g_border, b_border = img.getpixel((80, 112))
    is_border_black = r_border < 80 and g_border < 80 and b_border < 80
    
    # Dialogue box background at y=122 (Check if solid cream)
    r_bg, g_bg, b_bg = img.getpixel((80, 122))
    is_bg_cream = abs(r_bg - 247) < 10 and abs(g_bg - 231) < 10 and abs(b_bg - 214) < 10
    
    return is_border_black and is_bg_cream

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

# Ensure any active menus are dismissed
mgba.press_buttons(["B"])
time.sleep(0.4)

pos = mgba.get_coordinates()
print("Starting state B Master Route from position:", pos)

# Step 1: Walk UP Column 5 to Row 6
if pos == {"x": 5, "y": 10}:
    print("Walking UP Column 5 to Row 6...")
    steps = [
        ("Up", {"x": 5, "y": 9}),
        ("Up", {"x": 5, "y": 8}),
        ("Up", {"x": 5, "y": 7}),
        ("Up", {"x": 5, "y": 6}),
    ]
    if not run_steps(steps):
        print("Failed to reach (5, 6)")
        exit(1)
    pos = mgba.get_coordinates()

# Step 2: Walk RIGHT along Row 6 to Column 21
if pos == {"x": 5, "y": 6}:
    print("Walking RIGHT along Row 6 to Column 21...")
    steps = []
    for x in range(6, 22):
        steps.append(("Right", {"x": x, "y": 6}))
    if not run_steps(steps):
        print("Failed to reach Column 21 on Row 6")
        exit(1)
    pos = mgba.get_coordinates()

# Step 3: Walk LEFT 2 steps to Column 19
if pos == {"x": 21, "y": 6}:
    print("Walking LEFT to Column 19...")
    steps = [
        ("Left", {"x": 20, "y": 6}),
        ("Left", {"x": 19, "y": 6}),
    ]
    if not run_steps(steps):
        print("Failed to reach (19, 6)")
        exit(1)
    pos = mgba.get_coordinates()

# Step 4: Walk UP Column 19 to Row 3
if pos == {"x": 19, "y": 6}:
    print("Walking UP Column 19 to Row 3...")
    steps = [
        ("Up", {"x": 19, "y": 5}),
        ("Up", {"x": 19, "y": 4}),
        ("Up", {"x": 19, "y": 3}),
    ]
    if not run_steps(steps):
        print("Failed to reach (19, 3)")
        exit(1)
    pos = mgba.get_coordinates()

# Step 5: Walk RIGHT along Row 3 to Column 26
if pos == {"x": 19, "y": 3}:
    print("Walking RIGHT along Row 3 to Column 26...")
    steps = []
    for x in range(20, 27):
        steps.append(("Right", {"x": x, "y": 3}))
    if not run_steps(steps):
        print("Failed to reach (26, 3)")
        exit(1)
    pos = mgba.get_coordinates()

# Step 6: Step DOWN onto Column 26 to fall through the pitfall
if pos == {"x": 26, "y": 3}:
    print("Stepping DOWN to fall through the pit...")
    mgba.press_buttons(["Down"])
    time.sleep(2.5)
    pos = mgba.get_coordinates()
    print("Position after dropping to 1F East:", pos)

# Step 7: Walk to B1F East stairs on 1F East
if pos == {"x": 26, "y": 4}:
    print("Walking to B1F East stairs...")
    steps = [
        ("Left", {"x": 25, "y": 4}),
        ("Left", {"x": 24, "y": 4}),
        ("Left", {"x": 23, "y": 4}),
        ("Left", {"x": 22, "y": 4}),
        ("Up", {"x": 22, "y": 3}),
    ]
    if not run_steps(steps):
        print("Failed to reach 1F East stairs")
        exit(1)
        
    print("Stepping UP to warp down to B1F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position inside B1F East:", pos)

# Step 8: Cross B1F East to B1F West NORTH and retrieve Secret Key!
if pos == {"x": 22, "y": 3}:
    print("Crossing B1F East to B1F West NORTH...")
    steps = [
        ("Down", {"x": 22, "y": 4}),
        ("Left", {"x": 21, "y": 4}),
        ("Left", {"x": 20, "y": 4}),
        ("Left", {"x": 19, "y": 4}),
        ("Down", {"x": 19, "y": 5}),
    ]
    if not run_steps(steps):
        print("Failed to reach Row 5 on B1F East")
        exit(1)
        
    steps_left = []
    for x in range(18, 0, -1):
        steps_left.append(("Left", {"x": x, "y": 5}))
    if not run_steps(steps_left):
        print("Failed to reach (1, 5)")
        exit(1)
    pos = mgba.get_coordinates()

# Step 9: Stand at (1, 5) facing UP, pick up the Secret Key!
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
