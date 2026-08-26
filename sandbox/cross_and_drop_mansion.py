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

# Step 1: From (5, 10), walk down and left to the 2F West switch standing tile (2, 12)
if pos == {"x": 5, "y": 10}:
    print("Walking to switch standing tile (2, 12)...")
    if not run_steps([
        ("Down", {"x": 5, "y": 11}),
        ("Down", {"x": 5, "y": 12}),
        ("Left", {"x": 4, "y": 12}),
        ("Left", {"x": 3, "y": 12}),
        ("Left", {"x": 2, "y": 12}),
    ]):
        exit(1)
    pos = mgba.get_coordinates()

# Step 2: Toggle the Mewtwo statue switch ONCE to activate State B
if pos == {"x": 2, "y": 12}:
    print("Aligning UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    print("Toggling Mewtwo statue switch to State B...")
    mgba.press_buttons([
        "A", "sleep 1500",   # 1. Opens "A secret switch!" / YES-NO menu (scrolling finishes)
        "Up", "sleep 600",   # 2. Highlights YES
        "A", "sleep 1500",   # 3. Selects YES -> prints "Who wouldn't!"
        "A", "sleep 1500"    # 4. Closes the dialogue box and returns to overworld!
    ])
    time.sleep(6.5)
    pos = mgba.get_coordinates()

# Step 3: Walk back to Column 5. Since Column 3 Row 12 is now CLOSED in State B, we must bypass via Row 13!
if pos == {"x": 2, "y": 12}:
    print("Walking back to Column 5 via Row 13 bypass...")
    if not run_steps([
        ("Down", {"x": 2, "y": 13}),
        ("Right", {"x": 3, "y": 13}),
        ("Right", {"x": 4, "y": 13}),
        ("Right", {"x": 5, "y": 13}),
        ("Up", {"x": 5, "y": 12}),
        ("Up", {"x": 5, "y": 11}),
    ]):
        exit(1)
    pos = mgba.get_coordinates()

# Step 4: Walk UP Column 5 directly to Row 3 (5, 3) (which is now OPEN in State B!)
if pos == {"x": 5, "y": 11}:
    print("Walking UP Column 5 to Row 3...")
    if not run_steps([
        ("Up", {"x": 5, "y": 10}),
        ("Up", {"x": 5, "y": 9}),
        ("Up", {"x": 5, "y": 8}),
        ("Up", {"x": 5, "y": 7}),
        ("Up", {"x": 5, "y": 6}),
        ("Up", {"x": 5, "y": 5}),
        ("Up", {"x": 5, "y": 4}),
        ("Up", {"x": 5, "y": 3}),
    ]):
        exit(1)
    pos = mgba.get_coordinates()

# Step 5: Cross horizontally on Row 3 from (5, 3) to (18, 3) on 2F East
if pos == {"x": 5, "y": 3}:
    print("Crossing horizontally on Row 3 to (18, 3)...")
    if not run_steps([("Right", {"x": 5 + i + 1, "y": 3}) for i in range(13)]):
        exit(1)
    pos = mgba.get_coordinates()

# Step 6: On 2F East, walk DOWN Column 18 to Row 10 (18, 10)
if pos == {"x": 18, "y": 3}:
    print("Walking DOWN Column 18 to Row 10...")
    if not run_steps([("Down", {"x": 18, "y": 3 + i + 1}) for i in range(7)]):
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 18, "y": 10}:
    print("Walking LEFT to (15, 10)...")
    if not run_steps([
        ("Left", {"x": 17, "y": 10}),
        ("Left", {"x": 16, "y": 10}),
        ("Left", {"x": 15, "y": 10}),
    ]):
        exit(1)
    pos = mgba.get_coordinates()

# Step 7: Step DOWN onto the stairs at (15, 11) on 2F East to warp UP to 3F East, landing at (16, 11)
if pos == {"x": 15, "y": 10}:
    print("Taking stairs up to 3F East...")
    if not run_steps([
        ("Down", {"x": 16, "y": 11}) # The warp takes us to (16, 11) on 3F East
    ]):
        exit(1)
    pos = mgba.get_coordinates()

# Step 8: On 3F East (landing at 16, 11), walk to Column 20, UP Column 20 to Row 3, RIGHT Row 3 to Column 26, drop!
if pos == {"x": 16, "y": 11}:
    print("Walking to (20, 11) on 3F East...")
    if not run_steps([
        ("Right", {"x": 17, "y": 11}),
        ("Right", {"x": 18, "y": 11}),
        ("Right", {"x": 19, "y": 11}),
        ("Right", {"x": 20, "y": 11}),
    ]):
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 20, "y": 11}:
    print("Walking UP Column 20 to Row 3...")
    if not run_steps([("Up", {"x": 20, "y": 11 - i - 1}) for i in range(8)]):
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 20, "y": 3}:
    print("Walking RIGHT along Row 3 to Column 26...")
    if not run_steps([("Right", {"x": 20 + i + 1, "y": 3}) for i in range(6)]):
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 26, "y": 3}:
    print("SUCCESS! Stepping DOWN into the pitfall to fall to 1F East!")
    mgba.press_buttons(["Down"])
    time.sleep(1.5)
    pos = mgba.get_coordinates()
    print("Final position after drop:", pos)
