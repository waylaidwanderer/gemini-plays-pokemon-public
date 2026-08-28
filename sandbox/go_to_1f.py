import mgba
import time
from PIL import Image

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def check_dialogue_or_battle():
    # To prevent B1F dark tile false positives, let's check a wider white/black threshold,
    # or let's be extremely strict about the text box background.
    # Since we are on 1F West, 2F West, and 3F West, which are brighter, we can use a standard check.
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file)
    img_std = img.resize((160, 144), Image.Resampling.NEAREST)
    
    black_or_white = 0
    total_pixels = 0
    for y in range(112, 144):
        for x in range(8, 152):
            r, g, b = img_std.getpixel((x, y))[:3]
            total_pixels += 1
            is_bw = (r < 55 and g < 55 and b < 55) or (r > 200 and g > 200 and b > 200)
            if is_bw:
                black_or_white += 1
                
    ratio = black_or_white / total_pixels
    return ratio > 0.88

def run_from_battle():
    print("Dismissing battle intro text...")
    for i in range(12):
        mgba.press_buttons(["B"])
        time.sleep(0.35)
        
    print("Attempting to select RUN...")
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
    time.sleep(2.0)
    
    print("Dismissing escape dialogue...")
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.35)

def safe_step(direction, expected_coords=None, max_attempts=15):
    for attempt in range(max_attempts):
        if check_dialogue_or_battle():
            print("Dialogue/Battle detected. Handling...")
            run_from_battle()
            time.sleep(0.5)
            continue
            
        old_pos = get_pos()
        mgba.press_buttons([direction])
        time.sleep(0.55)
        new_pos = get_pos()
        
        if new_pos != old_pos:
            if expected_coords and new_pos != expected_coords:
                print(f"Moved {direction} to {new_pos} (expected {expected_coords}). Checking...")
            else:
                print(f"Successfully stepped {direction} to {new_pos}")
            return True
            
        print(f"Collision/delay at {old_pos} trying {direction} (attempt {attempt+1}/{max_attempts})")
        time.sleep(0.25)
        
    print(f"ERROR: Could not step {direction} from {old_pos}")
    return False

def run_safe_steps(steps):
    for d, c in steps:
        if not safe_step(d, c):
            return False
    return True

print("Starting go_to_1f.py (Part 1 of Mansion Solve)...")
print("Current position:", get_pos())

# 1. Walk from (5, 15) to stairs at (5, 10) on 1F West
steps_to_stairs_1f = [
    ("Up", (5, 14)),
    ("Up", (5, 13)),
    ("Up", (5, 12)),
    ("Up", (5, 11)),
    ("Up", (5, 10)),
]
print("Walking to 1F West stairs...")
if not run_safe_steps(steps_to_stairs_1f):
    print("Failed to reach stairs on 1F West")
    exit(1)

# Step UP onto stairs to warp to 2F West (lands at (5, 11) or (5, 10))
print("Warping UP to 2F West...")
mgba.press_buttons(["Up"])
time.sleep(2.0)
pos = get_pos()
print("Position on 2F West:", pos)

# 2. Walk from 2F West landing to (7, 10) to warp UP to 3F West
if pos == (5, 11) or pos == (5, 10):
    steps_to_stairs_2f = [
        ("Right", (6, 11)),
        ("Right", (7, 11)),
        ("Up", (7, 10)),
    ]
    print("Walking to 2F West stairs...")
    if not run_safe_steps(steps_to_stairs_2f):
        print("Failed to reach stairs on 2F West")
        exit(1)
        
    print("Warping UP to 3F West...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = get_pos()
    print("Position on 3F West:", pos)

# 3. Walk from 3F West landing (7, 11) to switch (2, 12)
if pos == (7, 11) or pos == (7, 10):
    steps_to_switch_3f = [
        ("Left", (6, 11)),
        ("Left", (5, 11)),
        ("Left", (4, 11)),
        ("Left", (3, 11)),
        ("Left", (2, 11)),
        ("Left", (1, 11)),
        ("Down", (1, 12)),
        ("Down", (1, 13)),
        ("Right", (2, 13)),
        ("Up", (2, 12)),
    ]
    print("Walking to 3F West switch...")
    if not run_safe_steps(steps_to_switch_3f):
        print("Failed to reach switch on 3F West")
        exit(1)

# Face UP
print("Facing UP towards the switch...")
mgba.press_buttons(["Up"])
time.sleep(1.0)

# 4. Toggle Mewtwo Switch to State B with exactly 4 slow A-presses
print("Toggling switch to State B with exactly 4 slow A-presses...")
mgba.press_buttons([
    "A", "sleep 1500",
    "A", "sleep 1500",
    "A", "sleep 1500",
    "A", "sleep 1500"
])
time.sleep(7.0)
print("Switch toggle complete!")

# 5. Walk to Column 3 Row 10
steps_to_col_3 = [
    ("Down", (2, 13)),
    ("Right", (3, 13)),
    ("Right", (4, 13)),
    ("Up", (4, 12)),
    ("Up", (4, 11)),
    ("Left", (3, 11)),
    ("Up", (3, 10)),
]
print("Walking to Column 3 Row 10...")
if not run_safe_steps(steps_to_col_3):
    print("Failed to reach Column 3 Row 10")
    exit(1)

# 6. Walk UP Column 3 through open gate to Row 6
steps_up_gate = [
    ("Up", (3, 9)),  # open in State B!
    ("Up", (3, 8)),
    ("Up", (3, 7)),
    ("Up", (3, 6)),
]
print("Walking UP through Column 3 gate to Row 6...")
if not run_safe_steps(steps_up_gate):
    print("Failed walking UP Column 3")
    exit(1)

# 7. Walk RIGHT along Row 6 to Column 20
steps_row_6 = []
for x in range(4, 21):
    steps_row_6.append(("Right", (x, 6)))
print("Walking RIGHT along Row 6 to Column 20...")
if not run_safe_steps(steps_row_6):
    print("Failed walking RIGHT along Row 6")
    exit(1)

# 8. Walk UP Column 20 to Row 3
steps_to_row_3 = [
    ("Up", (20, 5)),
    ("Up", (20, 4)),
    ("Up", (20, 3)),
]
print("Walking UP Column 20 to Row 3...")
if not run_safe_steps(steps_to_row_3):
    print("Failed walking UP Column 20")
    exit(1)

# 9. Walk RIGHT along Row 3 to Column 26
steps_row_3 = []
for x in range(21, 27):
    steps_row_3.append(("Right", (x, 3)))
print("Walking RIGHT along Row 3 to Column 26...")
if not run_safe_steps(steps_row_3):
    print("Failed walking along Row 3")
    exit(1)

# 10. Step DOWN to drop through the pitfall to 1F East inside the fenced room
print("Dropping through the pitfall to 1F East...")
if not safe_step("Down", (26, 4)):
    print("Failed to drop through the pitfall")
    exit(1)
time.sleep(2.5)

print("Part 1 complete! Landed on 1F East. Current Position:", get_pos())
mgba.take_screenshot()
