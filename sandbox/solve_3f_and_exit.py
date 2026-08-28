import mgba
import time
from PIL import Image

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def check_dialogue_or_battle():
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

print("Start position:", get_pos())

# 1. Walk from (10, 6) to Column 20 Row 6 on 3F East
steps_row_6 = []
for x in range(11, 21):
    steps_row_6.append(("Right", (x, 6)))
print("Walking RIGHT to Column 20...")
if not run_safe_steps(steps_row_6):
    print("Failed walking RIGHT to Column 20")
    exit(1)

# 2. Walk UP Column 20 to Row 3
steps_to_row_3 = [
    ("Up", (20, 5)),
    ("Up", (20, 4)),
    ("Up", (20, 3)),
]
print("Walking UP Column 20 to Row 3...")
if not run_safe_steps(steps_to_row_3):
    print("Failed walking UP Column 20")
    exit(1)

# 3. Walk RIGHT along Row 3 to Column 26
steps_row_3 = []
for x in range(21, 27):
    steps_row_3.append(("Right", (x, 3)))
print("Walking RIGHT along Row 3 to Column 26...")
if not run_safe_steps(steps_row_3):
    print("Failed walking along Row 3")
    exit(1)

# 4. Step DOWN to drop through the pitfall to 1F East inside the fenced room
print("Dropping through the pitfall to 1F East...")
if not safe_step("Down", (26, 4)):
    print("Failed to drop through the pitfall")
    exit(1)
time.sleep(2.5)
pos = get_pos()
print("Landed on 1F East. Position:", pos)

# 5. Walk LEFT to stairs and warp DOWN to B1F East
if pos == (26, 4) or pos == (25, 4):
    print("Walking to B1F East stairs...")
    steps_to_stairs = []
    current_x = pos[0]
    for x in range(current_x - 1, 21, -1):
        steps_to_stairs.append(("Left", (x, 4)))
    steps_to_stairs.append(("Up", (22, 3)))
    if not run_safe_steps(steps_to_stairs):
        print("Failed to reach stairs")
        exit(1)

    print("Stepping UP to warp down to B1F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = get_pos()
    print("Position after warping down to B1F East:", pos)

# 6. Cross B1F East to B1F West NORTH and retrieve Secret Key
if pos == (22, 3) or pos == (22, 2):
    print("Crossing B1F East to B1F West NORTH...")
    if pos[1] == 2:
        safe_step("Down")
        pos = get_pos()

    # Move to Row 5 (B1F East Column 19 Row 5)
    steps_to_row_5 = [
        ("Down", (22, 4)),
        ("Left", (21, 4)),
        ("Left", (20, 4)),
        ("Left", (19, 4)),
        ("Down", (19, 5)),
    ]
    if not run_safe_steps(steps_to_row_5):
        print("Failed to reach B1F Row 5")
        exit(1)

    steps_left = []
    for x in range(18, 0, -1):
        steps_left.append(("Left", (x, 5)))
    if not run_safe_steps(steps_left):
        print("Failed to reach Secret Key room")
        exit(1)
    pos = get_pos()

# 7. Pick up the Secret Key!
if pos == (1, 5):
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

    # Dismiss any leftover text
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.4)

    pos = get_pos()
    print("Position after picking up Secret Key:", pos)

print("Mansion master route completed successfully!")
mgba.take_screenshot()
