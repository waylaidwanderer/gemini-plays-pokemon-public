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

def walk_step(direction, expected_coords, retries=25):
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

pos = mgba.get_coordinates()
print("Starting Mansion State B solve from (6, 12) on 2F West. Current position:", pos)

if pos != {"x": 6, "y": 12}:
    print("Warning: Player is not at (6, 12). Current position:", pos)
    exit(1)

# 1. Walk UP to (6, 11) to get onto the completely open Row 11
print("Walking UP to Row 11...")
if not walk_step("Up", {"x": 6, "y": 11}):
    print("Failed to walk UP to Row 11")
    exit(1)
pos = mgba.get_coordinates()

# 2. Walk RIGHT along Row 11 to Column 11 (11, 11)
if pos == {"x": 6, "y": 11}:
    print("Walking RIGHT to Column 11...")
    steps_right = []
    for x in range(7, 12):
        steps_right.append(("Right", {"x": x, "y": 11}))
    if not run_steps(steps_right):
        print("Failed to reach (11, 11)")
        exit(1)
    pos = mgba.get_coordinates()

# 3. Walk UP Column 11 to Row 3
if pos == {"x": 11, "y": 11}:
    print("Walking UP Column 11 to Row 3...")
    steps_up = []
    for y in range(10, 2, -1):
        steps_up.append(("Up", {"x": 11, "y": y}))
    if not run_steps(steps_up):
        print("Failed to reach Row 3 on Column 11")
        exit(1)
    pos = mgba.get_coordinates()

# 4. Walk RIGHT along Row 3 to Column 18 (crosses horizontally to 2F East)
if pos == {"x": 11, "y": 3}:
    print("Crossing horizontally to 2F East along Row 3...")
    steps_cross = []
    for x in range(12, 19):
        steps_cross.append(("Right", {"x": x, "y": 3}))
    if not run_steps(steps_cross):
        print("Failed to reach Column 18 on Row 3")
        exit(1)
    pos = mgba.get_coordinates()

# 5. Walk DOWN Column 18 to Row 10
if pos == {"x": 18, "y": 3}:
    print("Walking DOWN Column 18 to Row 10...")
    steps_down = []
    for y in range(4, 11):
        steps_down.append(("Down", {"x": 18, "y": y}))
    if not run_steps(steps_down):
        print("Failed to reach Row 10 on Column 18")
        exit(1)
    pos = mgba.get_coordinates()

# 6. Walk LEFT along Row 10 to Column 15 (15, 10)
if pos == {"x": 18, "y": 10}:
    print("Walking LEFT along Row 10 to (15, 10)...")
    steps_left = [
        ("Left", {"x": 17, "y": 10}),
        ("Left", {"x": 16, "y": 10}),
        ("Left", {"x": 15, "y": 10}),
    ]
    if not run_steps(steps_left):
        print("Failed to reach (15, 10)")
        exit(1)
    pos = mgba.get_coordinates()

# 7. Step DOWN onto stairs at (15, 11) to warp to 3F East (landing at 16, 11)
if pos == {"x": 15, "y": 10}:
    print("Stepping DOWN onto stairs to warp UP to 3F East...")
    mgba.press_buttons(["Down"])
    time.sleep(2.5)
    pos = mgba.get_coordinates()
    print("Position after warping UP:", pos)

# 8. On 3F East, land at (16, 11) or (15, 11). Walk RIGHT to Column 20
if pos == {"x": 16, "y": 11} or pos == {"x": 15, "y": 11}:
    start_x = pos["x"]
    print("Walking RIGHT along Row 11 to Column 20...")
    steps_right_3f = []
    for x in range(start_x + 1, 21):
        steps_right_3f.append(("Right", {"x": x, "y": 11}))
    if not run_steps(steps_right_3f):
        print("Failed to reach Column 20 on Row 11")
        exit(1)
    pos = mgba.get_coordinates()

# 9. Walk UP Column 20 to Row 3
if pos == {"x": 20, "y": 11}:
    print("Walking UP Column 20 to Row 3...")
    steps_up_3f = []
    for y in range(10, 2, -1):
        steps_up_3f.append(("Up", {"x": 20, "y": y}))
    if not run_steps(steps_up_3f):
        print("Failed to reach Row 3 on Column 20")
        exit(1)
    pos = mgba.get_coordinates()

# 10. Walk RIGHT along Row 3 to Column 26
if pos == {"x": 20, "y": 3}:
    print("Walking RIGHT along Row 3 to Column 26...")
    steps_to_pit = []
    for x in range(21, 27):
        steps_to_pit.append(("Right", {"x": x, "y": 3}))
    if not run_steps(steps_to_pit):
        print("Failed to reach Column 26 on Row 3")
        exit(1)
    pos = mgba.get_coordinates()

# 11. Step DOWN to drop through the pitfall to 1F East inside the fenced room (landing at 26, 4 or 25, 4)
if pos == {"x": 26, "y": 3}:
    print("Stepping DOWN to drop through the pitfall to 1F East...")
    mgba.press_buttons(["Down"])
    time.sleep(2.5)
    pos = mgba.get_coordinates()
    print("Position after dropping to 1F East:", pos)

# 12. Now inside the fenced room at (26, 4) or (25, 4). Walk LEFT to Column 22 (22, 4)
if pos == {"x": 26, "y": 4} or pos == {"x": 25, "y": 4}:
    start_x = pos["x"]
    print("Walking LEFT along Row 4 to Column 22...")
    steps_to_stairs = []
    for x in range(start_x - 1, 21, -1):
        steps_to_stairs.append(("Left", {"x": x, "y": 4}))
    if not run_steps(steps_to_stairs):
        print("Failed to reach (22, 4) on 1F East")
        exit(1)
    pos = mgba.get_coordinates()

# 13. Walk UP to (22, 3)
if pos == {"x": 22, "y": 4}:
    print("Walking UP to (22, 3)...")
    if not walk_step("Up", {"x": 22, "y": 3}):
        print("Failed to reach (22, 3)")
        exit(1)
    pos = mgba.get_coordinates()

# 14. Step UP to warp down to B1F East (landing at 22, 2 or 22, 3)
if pos == {"x": 22, "y": 3}:
    print("Stepping UP to warp down to B1F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after warping down to B1F East:", pos)

# 15. Now on B1F East (landing at 22, 3 or 22, 2). Walk to Row 5
if pos["x"] == 22 and (pos["y"] == 2 or pos["y"] == 3):
    print("Walking to Row 5...")
    steps_to_row5 = []
    for y in range(pos["y"] + 1, 6):
        steps_to_row5.append(("Down", {"x": 22, "y": y}))
    if not run_steps(steps_to_row5):
        print("Failed to reach (22, 5) on B1F East")
        exit(1)
    pos = mgba.get_coordinates()

# 16. Cross B1F East to B1F West NORTH along Row 5 across Column 9 gate
if pos == {"x": 22, "y": 5}:
    print("Walking LEFT along Row 5 to Column 19...")
    steps_left_to_19 = [
        ("Left", {"x": 21, "y": 5}),
        ("Left", {"x": 20, "y": 5}),
        ("Left", {"x": 19, "y": 5}),
    ]
    if not run_steps(steps_left_to_19):
        print("Failed to reach (19, 5) on B1F East")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 19, "y": 5}:
    print("Walking LEFT along Row 5 to B1F West NORTH (Secret Key Room)...")
    steps_left_to_key = []
    for x in range(18, 0, -1):
        steps_left_to_key.append(("Left", {"x": x, "y": 5}))
    if not run_steps(steps_left_to_key):
        print("Failed to reach (1, 5) on B1F West NORTH")
        exit(1)
    pos = mgba.get_coordinates()

# 17. Standing at (1, 5) facing UP, pick up the Secret Key!
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

print("Mansion master route completed successfully!")
