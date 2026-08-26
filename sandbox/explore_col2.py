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

# Step 1: Walk to (2, 13)
if pos == {"x": 7, "y": 10}:
    print("Walking to (2, 13)...")
    if not run_steps([
        ("Down", {"x": 7, "y": 11}),
        ("Down", {"x": 7, "y": 12}),
        ("Down", {"x": 7, "y": 13}),
        ("Left", {"x": 6, "y": 13}),
        ("Left", {"x": 5, "y": 13}),
        ("Left", {"x": 4, "y": 13}),
        ("Left", {"x": 3, "y": 13}),
        ("Left", {"x": 2, "y": 13}),
    ]):
        print("Failed to reach (2, 13)")
        exit(1)
    pos = mgba.get_coordinates()

# Step 2: Try interacting from (2, 13) facing UP (if statue is at (2, 12))
if pos == {"x": 2, "y": 13}:
    print("Facing UP at (2, 13)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    pos_after_up = mgba.get_coordinates()
    print("Position after pressing Up at (2, 13):", pos_after_up)
    
    if pos_after_up == {"x": 2, "y": 13}:
        print("Blocked from walking UP to (2, 12)! This means (2, 12) has a solid object (statue!).")
        print("Interacting with statue at (2, 12) from (2, 13) facing UP...")
        mgba.press_buttons([
            "A", "sleep 2500",   # 1. Opens "A secret switch!"
            "A", "sleep 2500",   # 2. Opens YES/NO menu
            "A", "sleep 2500",   # 3. Selects YES -> prints "Who wouldn't!"
            "A", "sleep 2500"    # 4. Closes dialogue and returns to overworld
        ])
        time.sleep(10.5)
        
    elif pos_after_up == {"x": 2, "y": 12}:
        print("Successfully walked UP to (2, 12). This means (2, 12) is passable.")
        print("We are now standing at (2, 12) facing UP. Statue must be at (2, 11).")
        print("Interacting with statue at (2, 11) from (2, 12) facing UP...")
        mgba.press_buttons([
            "A", "sleep 2500",   # 1. Opens "A secret switch!"
            "A", "sleep 2500",   # 2. Opens YES/NO menu
            "A", "sleep 2500",   # 3. Selects YES -> prints "Who wouldn't!"
            "A", "sleep 2500"    # 4. Closes dialogue and returns to overworld
        ])
        time.sleep(10.5)

# Verify if we are currently on 3F West
pos = mgba.get_coordinates()
print("Current position after interaction:", pos)

# Now, walk to (7, 10) to verify if the gate at (7, 9) is open!
if pos in [{"x": 2, "y": 12}, {"x": 2, "y": 13}]:
    print("Walking to (7, 10) to verify gate status...")
    if pos == {"x": 2, "y": 12}:
        run_steps([("Down", {"x": 2, "y": 13})])
        
    run_steps([
        ("Right", {"x": 3, "y": 13}),
        ("Right", {"x": 4, "y": 13}),
        ("Right", {"x": 5, "y": 13}),
        ("Right", {"x": 6, "y": 13}),
        ("Right", {"x": 7, "y": 13}),
        ("Up", {"x": 7, "y": 12}),
        ("Up", {"x": 7, "y": 11}),
        ("Up", {"x": 7, "y": 10}),
    ])
    pos = mgba.get_coordinates()

if pos == {"x": 7, "y": 10}:
    print("Trying to walk UP onto (7, 9)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    pos = mgba.get_coordinates()
    print("Position after walking UP:", pos)
    
    # Take screenshot of gate area
    scr = mgba.take_screenshot()
    print("Gate verification screenshot:", scr)

