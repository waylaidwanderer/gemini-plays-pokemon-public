import mgba
import time
from PIL import Image

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def handle_any_menu_or_battle():
    time.sleep(0.15)
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
        print(f"Menu/Dialogue/Battle detected! (B/W: {percentage*100:.2f}%)")
        # Try pressing B first to dismiss text
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        
        # Check if still in battle/dialogue
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
            print("Still in battle/dialogue. Attempting to RUN...")
            # Try pressing Down, Right, A to select RUN
            mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
            time.sleep(1.5)
            # Dismiss any "Escaped" or "Can't escape" text
            for _ in range(5):
                mgba.press_buttons(["B"])
                time.sleep(0.3)
        return True
    return False

def walk_step(direction, expected_coords, retries=15):
    for i in range(retries):
        if handle_any_menu_or_battle():
            pos = get_pos()
            if pos == expected_coords:
                return True
        mgba.press_buttons([direction])
        time.sleep(0.45)
        pos = get_pos()
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

print("Initial position:", get_pos())

# Part 1: Walk UP Column 3 to Row 6 from (3, 10)
steps_up_col_3 = [
    ("Up", (3, 9)),
    ("Up", (3, 8)),
    ("Up", (3, 7)),
    ("Up", (3, 6)),
]
print("Walking UP Column 3 to Row 6...")
if not run_steps(steps_up_col_3):
    print("Failed walking UP Column 3")
    exit(1)

# Part 2: Walk RIGHT along Row 6 to Column 20
steps_row_6 = []
for x in range(4, 21):
    steps_row_6.append(("Right", (x, 6)))
print("Walking RIGHT along Row 6 to Column 20...")
if not run_steps(steps_row_6):
    print("Failed walking RIGHT along Row 6")
    exit(1)

# Part 3: Walk UP Column 20 to Row 3
steps_col_20 = [
    ("Up", (20, 5)),
    ("Up", (20, 4)),
    ("Up", (20, 3)),
]
print("Walking UP Column 20 to Row 3...")
if not run_steps(steps_col_20):
    print("Failed walking UP Column 20")
    exit(1)

# Part 4: Walk RIGHT along Row 3 to Column 26
steps_row_3 = []
for x in range(21, 27):
    steps_row_3.append(("Right", (x, 3)))
print("Walking RIGHT along Row 3 to Column 26...")
if not run_steps(steps_row_3):
    print("Failed walking RIGHT along Row 3")
    exit(1)

# Part 5: Step DOWN to drop through the pitfall to 1F East inside the fenced room
print("Stepping DOWN to drop through the pitfall to 1F East...")
mgba.press_buttons(["Down"])
time.sleep(2.5)
pos = get_pos()
print("Position after dropping to 1F East:", pos)

# Part 6: On 1F East inside fenced room, walk to stairs and warp DOWN to B1F East
if pos == (26, 4) or pos == (25, 4):
    print("Walking to B1F East stairs...")
    steps_to_stairs = []
    current_x = pos[0]
    for x in range(current_x - 1, 21, -1):
        steps_to_stairs.append(("Left", (x, 4)))
    steps_to_stairs.append(("Up", (22, 3)))
    if not run_steps(steps_to_stairs):
        print("Failed to reach stairs at (22, 3)")
        exit(1)
        
    print("Stepping UP to warp down to B1F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = get_pos()
    print("Position after warping down to B1F East:", pos)

# Part 7: Cross B1F East to B1F West NORTH
if pos == (22, 3) or pos == (22, 2):
    print("Crossing B1F East to B1F West NORTH...")
    if pos[1] == 2:
        walk_step("Down", (22, 3))
        pos = get_pos()
        
    if not run_steps([
        ("Down", (22, 4)),
        ("Left", (21, 4)),
        ("Left", (20, 4)),
        ("Left", (19, 4)),
        ("Down", (19, 5)),
    ]):
        print("Failed to reach B1F Row 5")
        exit(1)
        
    steps_left = []
    for x in range(18, 0, -1):
        steps_left.append(("Left", (x, 5)))
    if not run_steps(steps_left):
        print("Failed to reach Secret Key room")
        exit(1)
    pos = get_pos()

# Part 8: Stand at (1, 5) facing UP, pick up the Secret Key!
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

print("Balcony drop and key retrieval completed successfully!")
mgba.take_screenshot()
