import mgba
import time
from PIL import Image

def is_real_dialogue_open():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file).resize((160, 144), Image.Resampling.NEAREST)
    cropped = img.crop((0, 104, 160, 144))
    
    # Check for dialogue box white/cream pixels
    white_cream_pixels = 0
    for y in range(cropped.height):
        for x in range(cropped.width):
            r, g, b = cropped.getpixel((x, y))
            if r > 200 and g > 200 and b > 200:
                white_cream_pixels += 1
    print(f"DEBUG: white_cream_pixels={white_cream_pixels}")
    return white_cream_pixels > 3000

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
print("Starting position:", pos)

# Step 1: Walk UP to (1, 11) from (1, 13)
if pos == {"x": 1, "y": 13}:
    print("Walking UP to (1, 11)...")
    if not run_steps([
        ("Up", {"x": 1, "y": 12}),
        ("Up", {"x": 1, "y": 11}),
    ]):
        print("Failed to reach (1, 11)")
        exit(1)
    pos = mgba.get_coordinates()

# Step 2: Face LEFT towards (0, 11) and toggle the switch
if pos == {"x": 1, "y": 11}:
    print("Facing LEFT...")
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    
    print("Pressing A to interact with switch...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    if is_real_dialogue_open():
        print("Mewtwo switch dialogue is open! Toggling switch...")
        # Dialogue: "A secret switch!" -> press A to advance
        mgba.press_buttons(["A"])
        time.sleep(1.2)
        
        # Dialogue: "Who'd press it?" YES/NO -> press A to select YES
        mgba.press_buttons(["A"])
        time.sleep(1.2)
        
        # Dialogue: "Pressed it!" -> press A to dismiss
        mgba.press_buttons(["A"])
        time.sleep(1.2)
        
        print("Switch successfully toggled to State B!")
    else:
        print("Failed to open switch dialogue at (1, 11) facing LEFT.")
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        exit(1)
        
    pos = mgba.get_coordinates()

# Now that the switch is toggled, gate at (1,9) is open!
# Step 3: Walk UP Column 1 to Row 6 (gate at 1,9 is open!)
if pos == {"x": 1, "y": 11}:
    print("Walking UP Column 1 to Row 6...")
    if not run_steps([
        ("Up", {"x": 1, "y": 10}),
        ("Up", {"x": 1, "y": 9}),
        ("Up", {"x": 1, "y": 8}),
        ("Up", {"x": 1, "y": 7}),
        ("Up", {"x": 1, "y": 6}),
    ]):
        print("Failed to pass through Column 1 Row 9 gate")
        exit(1)
    pos = mgba.get_coordinates()

# Step 4: Walk RIGHT along Row 6 to Column 20 (crossing horizontally to 3F East)
if pos == {"x": 1, "y": 6}:
    print("Walking RIGHT along Row 6 to Column 20...")
    steps = []
    for x in range(2, 21):
        steps.append(("Right", {"x": x, "y": 6}))
    if not run_steps(steps):
        print("Failed to reach Column 20 on Row 6")
        exit(1)
    pos = mgba.get_coordinates()

# Step 5: Walk UP Column 20 to Row 3
if pos == {"x": 20, "y": 6}:
    print("Walking UP Column 20 to Row 3...")
    steps = []
    for y in range(5, 2, -1):
        steps.append(("Up", {"x": 20, "y": y}))
    if not run_steps(steps):
        print("Failed to reach Row 3 on Column 20")
        exit(1)
    pos = mgba.get_coordinates()

# Step 6: Walk RIGHT along Row 3 to Column 26
if pos == {"x": 20, "y": 3}:
    print("Walking RIGHT along Row 3 to Column 26...")
    steps = []
    for x in range(21, 27):
        steps.append(("Right", {"x": x, "y": 3}))
    if not run_steps(steps):
        print("Failed to reach Column 26 on Row 3")
        exit(1)
    pos = mgba.get_coordinates()

# Step 7: Step DOWN onto Column 26 to drop through the pitfall
if pos == {"x": 26, "y": 3}:
    print("Stepping DOWN onto Column 26 to drop through the pitfall...")
    mgba.press_buttons(["Down"])
    time.sleep(2.5)
    pos = mgba.get_coordinates()
    print("Position after dropping to 1F East:", pos)

# Step 8: Walk to B1F East stairs
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
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after warping down to B1F East:", pos)

# Step 9: Cross B1F East to B1F West NORTH and retrieve Secret Key!
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

# Step 10: Standing at (1, 5) facing UP, pick up the Secret Key!
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
