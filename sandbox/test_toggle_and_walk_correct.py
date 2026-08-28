import mgba
import time
from PIL import Image

def handle_any_menu_or_battle():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file)
    img_std = img.resize((160, 144), Image.Resampling.NEAREST)
    
    # We first press B to exit any move sub-menu we might be in
    mgba.press_buttons(["B"])
    time.sleep(0.3)
    
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

print("Running test_toggle_and_walk_correct.py...")
pos = mgba.get_coordinates()
print("Starting from:", pos)

# 1. Walk to (1, 12)
if pos == {"x": 2, "y": 11}:
    print("Walking to (1, 12)...")
    if not run_steps([
        ("Left", {"x": 1, "y": 11}),
        ("Down", {"x": 1, "y": 12}),
    ]):
        print("Failed to reach (1, 12)")
        exit(1)
    pos = mgba.get_coordinates()

# 2. Walk UP to (1, 11) to face UP towards (1, 10)
if pos == {"x": 1, "y": 12}:
    print("Stepping UP to face UP towards the Mewtwo switch at (1, 10)...")
    if not walk_step("Up", {"x": 1, "y": 11}):
        print("Failed to step UP to (1, 11)")
        exit(1)
    pos = mgba.get_coordinates()

# 3. Standing at (1, 11) facing UP, toggle the switch to State B!
if pos == {"x": 1, "y": 11}:
    print("Toggling switch at (1, 10) facing UP...")
    mgba.press_buttons(["A"]) # Step 1: secret switch
    time.sleep(0.8)
    mgba.press_buttons(["A"]) # Step 2: press it?
    time.sleep(0.8)
    mgba.press_buttons(["A"]) # Step 3: YES
    time.sleep(0.8)
    mgba.press_buttons(["A"]) # Step 4: dismiss
    time.sleep(1.2)
    pos = mgba.get_coordinates()

# 4. Now walk to Column 2 and go up to Row 6
if pos == {"x": 1, "y": 11}:
    print("Walking up Column 2 to Row 6...")
    steps_up = [
        ("Right", {"x": 2, "y": 11}),
        ("Up", {"x": 2, "y": 10}),
    ]
    for y in range(9, 5, -1):
        steps_up.append(("Up", {"x": 2, "y": y}))
    if not run_steps(steps_up):
        print("Failed to reach Row 6")
        exit(1)
    pos = mgba.get_coordinates()

print("Reached Row 6 successfully! Current position:", pos)
