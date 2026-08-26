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
print("Starting position on 2F West:", pos)

# We should be at (6, 10). If we are at (7, 10) or elsewhere, let's normalize.
if pos == {"x": 7, "y": 10}:
    walk_step("Left", {"x": 6, "y": 10})
    pos = mgba.get_coordinates()

if pos == {"x": 6, "y": 10}:
    print("Walking LEFT to (5, 10)...")
    if not walk_step("Left", {"x": 5, "y": 10}):
        print("Failed to reach (5, 10)")
        exit(1)
    pos = mgba.get_coordinates()

# Now walk UP Column 5 to Row 3 (State B means Row 9 gate is open!)
if pos == {"x": 5, "y": 10}:
    print("Walking UP Column 5 to Row 3...")
    steps = []
    for y in range(9, 2, -1):
        steps.append(("Up", {"x": 5, "y": y}))
    if not run_steps(steps):
        print("Failed to walk UP Column 5")
        exit(1)
    pos = mgba.get_coordinates()

# Now we should be at (5, 3) on 2F West in State B!
# Execute complete State B 2F bypass route to B1F West!
if pos == {"x": 5, "y": 3}:
    print("Successfully reached (5, 3) in State B! Executing 2F -> 3F East bypass route...")
    
    # 1. Walk RIGHT along Row 3 to Column 18
    # 2. Walk DOWN Column 18 to Row 10
    # 3. Walk LEFT along Row 10 to (15, 10)
    steps = []
    for x in range(6, 19):
        steps.append(("Right", {"x": x, "y": 3}))
    for y in range(4, 11):
        steps.append(("Down", {"x": 18, "y": y}))
    for x in range(17, 14, -1):
        steps.append(("Left", {"x": x, "y": 10}))
    
    if not run_steps(steps):
        print("Failed to reach (15, 10) on 2F East")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 15, "y": 10}:
    # Step DOWN onto stairs at (15, 11) to warp UP to 3F East (landing at (16, 11))
    print("Stepping DOWN to warp UP to 3F East...")
    mgba.press_buttons(["Down"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after warping to 3F East:", pos)

if pos == {"x": 16, "y": 11}:
    print("Successfully landed on 3F East! Walking to balcony drop...")
    # 1. Walk RIGHT along Row 11 to Column 20
    # 2. Walk UP Column 20 to Row 3
    # 3. Walk RIGHT along Row 3 to Column 26
    steps = [
        ("Right", {"x": 17, "y": 11}),
        ("Right", {"x": 18, "y": 11}),
        ("Right", {"x": 19, "y": 11}),
        ("Right", {"x": 20, "y": 11}),
    ]
    for y in range(10, 2, -1):
        steps.append(("Up", {"x": 20, "y": y}))
    for x in range(21, 27):
        steps.append(("Right", {"x": x, "y": 3}))
        
    if not run_steps(steps):
        print("Failed to reach balcony drop on 3F East")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 26, "y": 3}:
    print("Stepping DOWN to drop through pitfall to 1F East...")
    mgba.press_buttons(["Down"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after dropping to 1F East:", pos)

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

