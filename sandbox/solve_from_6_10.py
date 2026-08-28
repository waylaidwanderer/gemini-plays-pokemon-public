import mgba
import time
from PIL import Image

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
            print("Still in battle/dialogue. Attempting to RUN...")
            mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
            time.sleep(1.5)
            for _ in range(5):
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

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

pos = mgba.get_coordinates()
print("Starting position:", pos)

# Try Column 6 UP first
print("Testing Column 6 UP...")
column_6_success = True
steps_col6 = [
    ("Up", {"x": 6, "y": 9}),
    ("Up", {"x": 6, "y": 8}),
    ("Up", {"x": 6, "y": 7}),
    ("Up", {"x": 6, "y": 6}),
]

for d, c in steps_col6:
    if not walk_step(d, c, retries=4):
        column_6_success = False
        break

if not column_6_success:
    print("Column 6 UP is BLOCKED! Re-routing via Column 2...")
    # Walk back to safe ground if we got partially moved
    pos = mgba.get_coordinates()
    if pos["y"] < 10:
        # Walk back down to Row 11
        for y in range(pos["y"] + 1, 12):
            walk_step("Down", {"x": pos["x"], "y": y})
    else:
        walk_step("Down", {"x": pos["x"], "y": 11})
        
    # We should be at (6, 11) now (or we can walk to it)
    pos = mgba.get_coordinates()
    if pos["y"] != 11:
        walk_step("Down", {"x": pos["x"], "y": 11})
    if pos["x"] != 6:
        walk_step("Right" if pos["x"] < 6 else "Left", {"x": 6, "y": 11})
        
    # Walk to Column 2
    steps_to_col2 = [
        ("Left", {"x": 5, "y": 11}),
        ("Left", {"x": 4, "y": 11}),
        ("Left", {"x": 3, "y": 11}),
        ("Down", {"x": 3, "y": 12}),
        ("Left", {"x": 2, "y": 12}),
    ]
    if not run_steps(steps_to_col2):
        print("Failed to reach Column 2")
        exit(1)
        
    # Walk UP Column 2 to Row 6
    steps_up_col2 = []
    for y in range(11, 5, -1):
        steps_up_col2.append(("Up", {"x": 2, "y": y}))
    if not run_steps(steps_up_col2):
        print("Failed to walk UP Column 2")
        exit(1)
        
    # Walk RIGHT Row 6 to Column 20
    steps_to_col20 = []
    for x in range(3, 21):
        steps_to_col20.append(("Right", {"x": x, "y": 6}))
    if not run_steps(steps_to_col20):
        print("Failed to cross to Column 20")
        exit(1)
else:
    # Column 6 succeeded! We are at (6, 6). Go to Column 20.
    pos = mgba.get_coordinates()
    print("Column 6 UP succeeded! Crossing horizontally to Column 20...")
    steps_to_col20 = []
    for x in range(7, 21):
        steps_to_col20.append(("Right", {"x": x, "y": 6}))
    if not run_steps(steps_to_col20):
        print("Failed to cross to Column 20")
        exit(1)

pos = mgba.get_coordinates()
# Step 3: Walk UP Column 20 to Row 3
if pos == {"x": 20, "y": 6}:
    print("Walking UP Column 20 to Row 3...")
    steps_up_col20 = [
        ("Up", {"x": 20, "y": 5}),
        ("Up", {"x": 20, "y": 4}),
        ("Up", {"x": 20, "y": 3}),
    ]
    if not run_steps(steps_up_col20):
        print("Failed to reach Row 3 on Column 20")
        exit(1)
    pos = mgba.get_coordinates()

# Step 4: Walk RIGHT along Row 3 to Column 26
if pos == {"x": 20, "y": 3}:
    print("Walking RIGHT along Row 3 to Column 26...")
    steps_to_pit = []
    for x in range(21, 27):
        steps_to_pit.append(("Right", {"x": x, "y": 3}))
    if not run_steps(steps_to_pit):
        print("Failed to reach Column 26 on Row 3")
        exit(1)
    pos = mgba.get_coordinates()

# Step 5: Step DOWN to drop through the pitfall to 1F East inside the fenced room
if pos == {"x": 26, "y": 3}:
    print("Stepping DOWN to drop through the pitfall to 1F East...")
    mgba.press_buttons(["Down"])
    time.sleep(2.5)
    pos = mgba.get_coordinates()
    print("Position after dropping to 1F East:", pos)

# Step 6: Walk to B1F East stairs
if pos == {"x": 26, "y": 4} or pos == {"x": 25, "y": 4}:
    print("Walking to B1F East stairs...")
    steps_to_stairs = []
    current_x = pos["x"]
    for x in range(current_x - 1, 21, -1):
        steps_to_stairs.append(("Left", {"x": x, "y": 4}))
    steps_to_stairs.append(("Up", {"x": 22, "y": 3}))
    if not run_steps(steps_to_stairs):
        print("Failed to reach 1F East stairs")
        exit(1)
        
    print("Stepping UP to warp down to B1F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after warping down to B1F East:", pos)

# Step 7: Cross B1F East to B1F West NORTH and retrieve Secret Key!
if pos == {"x": 22, "y": 3} or pos == {"x": 22, "y": 2}:
    print("Crossing to B1F West NORTH...")
    if pos["y"] == 2:
        walk_step("Down", {"x": 22, "y": 3})
        pos = mgba.get_coordinates()
        
    if not run_steps([
        ("Down", {"x": 22, "y": 4}),
        ("Left", {"x": 21, "y": 4}),
        ("Left", {"x": 20, "y": 4}),
        ("Left", {"x": 19, "y": 4}),
        ("Down", {"x": 19, "y": 5}),
    ]):
        print("Failed to reach Row 5 on B1F East")
        exit(1)
        
    steps_left = []
    for x in range(18, 0, -1):
        steps_left.append(("Left", {"x": x, "y": 5}))
    if not run_steps(steps_left):
        print("Failed to reach Secret Key room")
        exit(1)
    pos = mgba.get_coordinates()

# Step 8: Standing at (1, 5) facing UP, pick up the Secret Key!
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
    print("Position after picking up Secret Key:", pos)

# Walk back to 1F East and exit on foot
if pos == {"x": 1, "y": 5}:
    print("Walking back to B1F East stairs...")
    steps_back = []
    for x in range(2, 20):
        steps_back.append(("Right", {"x": x, "y": 5}))
    steps_back.extend([
        ("Up", {"x": 19, "y": 4}),
        ("Right", {"x": 20, "y": 4}),
        ("Right", {"x": 21, "y": 4}),
        ("Right", {"x": 22, "y": 4}),
        ("Up", {"x": 22, "y": 3}),
    ])
    if not run_steps(steps_back):
        print("Failed to walk back to B1F East stairs")
        exit(1)
        
    print("Stepping UP to warp UP to 1F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after warping UP to 1F East:", pos)

# On 1F East at (22, 2) or (22, 3), walk to 1F West and exit!
if pos == {"x": 22, "y": 3} or pos == {"x": 22, "y": 2}:
    print("Walking to 1F West...")
    if pos["y"] == 2:
        walk_step("Down", {"x": 22, "y": 3})
        pos = mgba.get_coordinates()
        
    if not run_steps([
        ("Down", {"x": 22, "y": 4}),
        ("Down", {"x": 22, "y": 5}),
    ]):
        print("Failed to reach Row 5 on 1F East")
        exit(1)
        
    steps_to_exit = []
    for x in range(21, 4, -1):
        steps_to_exit.append(("Left", {"x": x, "y": 5}))
    for y in range(6, 28):
        steps_to_exit.append(("Down", {"x": 5, "y": y}))
        
    if not run_steps(steps_to_exit):
        print("Failed to reach exit tile")
        exit(1)
        
    print("Exiting Mansion...")
    mgba.press_buttons(["Down"])
    time.sleep(2.5)
    print("Final position after exiting:", mgba.get_coordinates())

print("Mansion master run completed successfully!")
