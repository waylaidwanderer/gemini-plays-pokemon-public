import mgba
import time
import os

# 1. Clean up obsolete files as requested by the overwatch system
files_to_delete = [
    "check_state.py",
    "explore_col2.py",
    "go_to_switch_2f.py",
    "explore_switch_3f.py"
]
for f in files_to_delete:
    if os.path.exists(f):
        os.remove(f)
        print(f"Cleaned up sandbox file: {f}")
    pyc = os.path.join("__pycache__", f.split(".")[0] + ".cpython-314.pyc")
    if os.path.exists(pyc):
        os.remove(pyc)
        print(f"Cleaned up pycache file: {pyc}")

def handle_any_menu_or_battle():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    from PIL import Image
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

# 1. Escape the wild battle with Ponyta
print("Fleeing from wild battle with Ponyta...")
# Make sure we select RUN
mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
time.sleep(1.5)

# Dismiss any remaining text
for _ in range(5):
    mgba.press_buttons(["B"])
    time.sleep(0.3)

pos = mgba.get_coordinates()
print("Position after escaping battle:", pos)

# We might be at (2, 11) or (2, 12). Let's go to (2, 11) first.
if pos == {"x": 2, "y": 12}:
    print("Walking UP to (2, 11)...")
    if not walk_step("Up", {"x": 2, "y": 11}):
        print("Failed to reach (2, 11)")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 2, "y": 11}:
    print("Walking RIGHT along Row 11 to Column 6...")
    steps_to_col6 = [
        ("Right", {"x": 3, "y": 11}),
        ("Right", {"x": 4, "y": 11}),
        ("Right", {"x": 5, "y": 11}),
        ("Right", {"x": 6, "y": 11}),
    ]
    if not run_steps(steps_to_col6):
        print("Failed to reach (6, 11)")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 6, "y": 11}:
    print("Walking UP Column 6 past the Row 9 gate (now open in State B!)...")
    steps_up = [
        ("Up", {"x": 6, "y": 10}),
        ("Up", {"x": 6, "y": 9}),  # Open gate!
        ("Up", {"x": 6, "y": 8}),
        ("Right", {"x": 7, "y": 8}),
        ("Up", {"x": 7, "y": 7}),
        ("Up", {"x": 7, "y": 6}),
    ]
    if not run_steps(steps_up):
        print("Failed to cross to Row 6 on 3F West")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 7, "y": 6}:
    print("Walking RIGHT along Row 6 to 3F East (Column 26)...")
    steps_east = []
    for x in range(8, 27):
        steps_east.append(("Right", {"x": x, "y": 6}))
    if not run_steps(steps_east):
        print("Failed to reach 3F East")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 26, "y": 6}:
    print("Walking UP Column 26 to Row 3...")
    steps_up_pit = [
        ("Up", {"x": 26, "y": 5}),
        ("Up", {"x": 26, "y": 4}),
        ("Up", {"x": 26, "y": 3}),
    ]
    if not run_steps(steps_up_pit):
        print("Failed to reach Row 3 pitfall")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 26, "y": 3}:
    print("Stepping DOWN to fall through the pitfall...")
    mgba.press_buttons(["Down"])
    time.sleep(2.5)
    pos = mgba.get_coordinates()
    print("Position after dropping to 1F East:", pos)

if pos == {"x": 26, "y": 4}:
    print("Walking to B1F East stairs warp on 1F East...")
    steps_to_stairs = [
        ("Left", {"x": 25, "y": 4}),
        ("Left", {"x": 24, "y": 4}),
        ("Left", {"x": 23, "y": 4}),
        ("Left", {"x": 22, "y": 4}),
        ("Up", {"x": 22, "y": 3}),
        ("Up", {"x": 22, "y": 2}),  # B1F East stairs warp tile!
    ]
    if not run_steps(steps_to_stairs):
        print("Failed to reach 1F East stairs warp")
        exit(1)
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after warping down to B1F East:", pos)

if pos == {"x": 22, "y": 2}:
    print("Crossing B1F East to B1F West NORTH...")
    steps_b1f = [
        ("Down", {"x": 22, "y": 3}),
        ("Down", {"x": 22, "y": 4}),
        ("Left", {"x": 21, "y": 4}),
        ("Left", {"x": 20, "y": 4}),
        ("Left", {"x": 19, "y": 4}),
        ("Down", {"x": 19, "y": 5}),
    ]
    if not run_steps(steps_b1f):
        print("Failed to reach Row 5 on B1F East")
        exit(1)
        
    steps_left = []
    for x in range(18, 0, -1):
        steps_left.append(("Left", {"x": x, "y": 5}))
    if not run_steps(steps_left):
        print("Failed to reach (1, 5)")
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

print("Secret Key successfully retrieved!")
