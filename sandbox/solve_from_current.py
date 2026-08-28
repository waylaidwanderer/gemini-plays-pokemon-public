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

# Ensure any active menu/battle is closed
for _ in range(5):
    handle_any_menu_or_battle()
    time.sleep(0.2)

pos = mgba.get_coordinates()
print("Starting solve from position:", pos)

# 1. Walk from (3, 10) to (1, 12)
if pos == {"x": 3, "y": 10}:
    print("Walking down and left to Column 1...")
    path_to_col1 = [
        ("Down", {"x": 3, "y": 11}),
        ("Down", {"x": 3, "y": 12}),
        ("Left", {"x": 2, "y": 12}),
        ("Left", {"x": 1, "y": 12}),
    ]
    if not run_steps(path_to_col1):
        print("Failed to reach (1, 12)")
        exit(1)
    pos = mgba.get_coordinates()

# 2. Walk up Column 1 to Row 6
if pos == {"x": 1, "y": 12} or pos == {"x": 1, "y": 11} or pos == {"x": 1, "y": 10}:
    print("Walking up Column 1 through the open Row 9 gate to Row 6...")
    path_up_col1 = []
    current_y = pos["y"]
    for y in range(current_y - 1, 5, -1):
        path_up_col1.append(("Up", {"x": 1, "y": y}))
    if not run_steps(path_up_col1):
        print("Failed to reach (1, 6)")
        exit(1)
    pos = mgba.get_coordinates()

# 3. Walk RIGHT along Row 6 to Column 20 on 3F East (crossing horizontally)
if pos == {"x": 1, "y": 6}:
    print("Walking RIGHT along Row 6 to Column 20...")
    steps_east = []
    for x in range(2, 21):
        steps_east.append(("Right", {"x": x, "y": 6}))
    if not run_steps(steps_east):
        print("Failed to reach Column 20 on Row 6")
        exit(1)
    pos = mgba.get_coordinates()

# 4. Walk UP Column 20 to Row 3
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

# 5. Walk RIGHT along Row 3 to Column 26
if pos == {"x": 20, "y": 3}:
    print("Walking RIGHT along Row 3 to Column 26...")
    steps_to_pit = []
    for x in range(21, 27):
        steps_to_pit.append(("Right", {"x": x, "y": 3}))
    if not run_steps(steps_to_pit):
        print("Failed to reach Column 26 on Row 3")
        exit(1)
    pos = mgba.get_coordinates()

# 6. Step DOWN to drop through the pitfall to 1F East inside the fenced room
if pos == {"x": 26, "y": 3}:
    print("Stepping DOWN to drop through the pitfall to 1F East...")
    mgba.press_buttons(["Down"])
    time.sleep(2.5)
    pos = mgba.get_coordinates()
    print("Position after dropping to 1F East:", pos)

# 7. Walk to B1F East stairs
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

# 8. Cross B1F East to B1F West NORTH and retrieve Secret Key!
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

# 9. Standing at (1, 5) facing UP, pick up the Secret Key!
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
    
    # Dismiss any leftover text
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        
    pos = mgba.get_coordinates()
    print("Final position after picking up Secret Key:", pos)

# 10. Walk from B1F West NORTH back to B1F East stairs
if pos == {"x": 1, "y": 5}:
    print("Walking back to B1F East stairs...")
    steps_right = []
    for x in range(2, 20):
        steps_right.append(("Right", {"x": x, "y": 5}))
    if not run_steps(steps_right):
        print("Failed to walk back on Row 5")
        exit(1)
        
    if not run_steps([
        ("Up", {"x": 19, "y": 4}),
        ("Right", {"x": 20, "y": 4}),
        ("Right", {"x": 21, "y": 4}),
        ("Right", {"x": 22, "y": 4}),
        ("Up", {"x": 22, "y": 3}),
    ]):
        print("Failed to align with B1F East stairs")
        exit(1)
        
    print("Stepping UP onto B1F East stairs to warp UP to 1F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position on 1F East after warping up:", pos)

# 11. On 1F East, walk LEFT to 1F West and exit!
if pos == {"x": 22, "y": 3} or pos == {"x": 22, "y": 2}:
    print("Walking across 1F to the main exit...")
    if pos["y"] == 2:
        walk_step("Down", {"x": 22, "y": 3})
        pos = mgba.get_coordinates()
        
    if not run_steps([
        ("Down", {"x": 22, "y": 4}),
        ("Down", {"x": 22, "y": 5}),
        ("Down", {"x": 22, "y": 6}),
    ]):
        print("Failed to reach Row 6 on 1F East")
        exit(1)
        
    steps_left_1f = []
    for x in range(21, 10, -1):
        steps_left_1f.append(("Left", {"x": x, "y": 6}))
    if not run_steps(steps_left_1f):
        print("Failed to reach Column 11 on Row 6")
        exit(1)
        
    steps_down_1f = []
    for y in range(7, 28):
        steps_down_1f.append(("Down", {"x": 11, "y": y}))
    if not run_steps(steps_down_1f):
        print("Failed to walk down Column 11 on 1F")
        exit(1)
        
    steps_exit_1f = []
    for x in range(10, 4, -1):
        steps_exit_1f.append(("Left", {"x": x, "y": 27}))
    if not run_steps(steps_exit_1f):
        print("Failed to reach exit tile (5, 27) on 1F West")
        exit(1)
        
    pos = mgba.get_coordinates()
    if pos == {"x": 5, "y": 27}:
        print("At exit tile! Stepping DOWN to exit to Cinnabar Island...")
        mgba.press_buttons(["Down"])
        time.sleep(2.5)
        print("Warped out! Current overworld position:", mgba.get_coordinates())

print("Solve completed!")
