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

# Step 1: Walk UP to (5, 10) on 1F West (avoiding closed gate at (3, 15) by going through Column 4)
if pos == {"x": 3, "y": 16}:
    print("Bypassing Row 15 gate via Column 4...")
    if not run_steps([
        ("Right", {"x": 4, "y": 16}),
        ("Up", {"x": 4, "y": 15}),
        ("Up", {"x": 4, "y": 14}),
        ("Up", {"x": 4, "y": 13}),
        ("Up", {"x": 4, "y": 12}),
        ("Up", {"x": 4, "y": 11}),
        ("Up", {"x": 4, "y": 10}),
        ("Right", {"x": 5, "y": 10}),
    ]):
        print("Failed to reach stairs at (5, 10)")
        exit(1)
    
    print("Stepping UP to warp up to 2F West...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after warping UP to 2F West:", pos)

# Step 2: Walk to switch standing tile (2, 12) on 2F West
if pos == {"x": 5, "y": 11}:
    print("Walking to switch standing tile (2, 12)...")
    if not run_steps([
        ("Down", {"x": 5, "y": 12}),
        ("Down", {"x": 5, "y": 13}),
        ("Left", {"x": 4, "y": 13}),
        ("Left", {"x": 3, "y": 13}),
        ("Left", {"x": 2, "y": 13}),
        ("Up", {"x": 2, "y": 12}),
    ]):
        print("Failed to reach (2, 12)")
        exit(1)
    pos = mgba.get_coordinates()

# Step 3: Toggle the Mewtwo statue switch ONCE to activate State A (using exactly 4 A-presses)
if pos == {"x": 2, "y": 12}:
    print("Aligning UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    print("Toggling Mewtwo statue switch to State A...")
    mgba.press_buttons([
        "A", "sleep 2500",   # 1. Opens "A secret switch!"
        "A", "sleep 2500",   # 2. Opens YES/NO menu
        "A", "sleep 2500",   # 3. Selects YES (selected by default) -> prints "Who wouldn't!"
        "A", "sleep 2500"    # 4. Closes the dialogue box and returns to overworld!
    ])
    time.sleep(10.5)
    pos = mgba.get_coordinates()

# Step 4: Walk back to the stairs at (5, 10) on 2F West
if pos == {"x": 2, "y": 12}:
    print("Walking to 2F West stairs...")
    if not run_steps([
        ("Down", {"x": 2, "y": 13}),
        ("Right", {"x": 3, "y": 13}),
        ("Right", {"x": 4, "y": 13}),
        ("Right", {"x": 5, "y": 13}),
        ("Up", {"x": 5, "y": 12}),
        ("Up", {"x": 5, "y": 11}),
    ]):
        print("Failed to reach 2F West stairs")
        exit(1)
    
    print("Stepping UP to warp down to 1F West...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after warping DOWN to 1F West:", pos)

# Step 5: Walk DOWN Column 5 directly to Row 27 to exit the mansion (open in State A!)
if pos == {"x": 5, "y": 11}:
    print("Walking DOWN Column 5 directly to exit...")
    if not run_steps([("Down", {"x": 5, "y": 11 + i + 1}) for i in range(16)]):
        print("Failed to reach exit mat")
        exit(1)
    pos = mgba.get_coordinates()
    print("Final position after exiting mansion:", pos)
