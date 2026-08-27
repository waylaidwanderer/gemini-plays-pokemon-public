import mgba
import time
from PIL import Image

def is_dialogue_open():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file).resize((160, 144), Image.Resampling.NEAREST)
    cropped = img.crop((0, 104, 160, 144))
    
    # Check for GBC dialogue background (high white/cream pixel count)
    white_cream_pixels = 0
    for y in range(cropped.height):
        for x in range(cropped.width):
            r, g, b = cropped.getpixel((x, y))[:3]
            if r > 200 and g > 200 and b > 200:
                white_cream_pixels += 1
    print(f"  Check dialogue box: white_cream_pixels={white_cream_pixels}")
    return white_cream_pixels > 3000

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
        print(f"Menu/Dialogue detected! (B/W: {percentage*100:.2f}%). Escape...")
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

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

pos = mgba.get_coordinates()
print("Starting position:", pos)

# 1. Walk from (2, 10) to (1, 13)
if pos == {"x": 2, "y": 10}:
    print("Walking to (1, 13)...")
    steps_to_statue = [
        ("Down", {"x": 2, "y": 11}),
        ("Down", {"x": 2, "y": 12}),
        ("Down", {"x": 2, "y": 13}),
        ("Left", {"x": 1, "y": 13})
    ]
    if not run_steps(steps_to_statue):
        print("Failed to reach (1, 13)")
        exit(0)
    pos = mgba.get_coordinates()

# 2. Toggle Mewtwo Switch at (1, 12) facing UP
if pos == {"x": 1, "y": 13}:
    print("Facing UP towards Mewtwo Switch at (1, 12)...")
    mgba.press_buttons(["Up", "sleep 400", "A", "sleep 1000", "A", "sleep 1000", "A", "sleep 1000", "B", "sleep 300", "B"])
    time.sleep(4.5)
    
# 3. Walk to (7, 11) on 3F West
pos = mgba.get_coordinates()
if pos == {"x": 1, "y": 13}:
    print("Walking to (7, 11)...")
    steps_to_stairs = [
        ("Right", {"x": 2, "y": 13}),
        ("Right", {"x": 3, "y": 13}),
        ("Right", {"x": 4, "y": 13}),
        ("Right", {"x": 5, "y": 13}),
        ("Right", {"x": 6, "y": 13}),
        ("Right", {"x": 7, "y": 13}),
        ("Up", {"x": 7, "y": 12}),
        ("Up", {"x": 7, "y": 11})
    ]
    if not run_steps(steps_to_stairs):
        print("Failed to reach (7, 11)")
        exit(0)
    pos = mgba.get_coordinates()

# 4. Step UP onto stairs at (7, 10) to warp DOWN to 2F West!
if pos == {"x": 7, "y": 11}:
    print("Stepping UP onto stairs at (7, 10)...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("New position on 2F West after warp DOWN:", pos)

# 5. Walk to (5, 11) on 2F West
# We land at (7, 11) on 2F West.
if pos == {"x": 7, "y": 11}:
    print("Walking LEFT to (5, 11) on 2F West...")
    steps_to_col5 = [
        ("Left", {"x": 6, "y": 11}),
        ("Left", {"x": 5, "y": 11})
    ]
    if not run_steps(steps_to_col5):
        print("Failed to walk to (5, 11)")
        exit(0)
    pos = mgba.get_coordinates()

# 6. Walk UP Column 5 directly to Row 3 (5, 3) (OPEN in State B!)
if pos == {"x": 5, "y": 11}:
    print("Walking UP Column 5 to Row 3...")
    steps_up_col5 = []
    for y in range(10, 2, -1):
        steps_up_col5.append(("Up", {"x": 5, "y": y}))
    if not run_steps(steps_up_col5):
        print("Failed to climb Column 5")
        exit(0)
    pos = mgba.get_coordinates()

# 7. Walk RIGHT along Row 3 to Column 18 (18, 3) on 2F East
if pos == {"x": 5, "y": 3}:
    print("Walking RIGHT along Row 3 to Column 18...")
    steps_right_row3 = []
    for x in range(6, 19):
        steps_right_row3.append(("Right", {"x": x, "y": 3}))
    if not run_steps(steps_right_row3):
        print("Failed to walk RIGHT along Row 3")
        exit(0)
    pos = mgba.get_coordinates()

# 8. Walk DOWN Column 18 to Row 10 (18, 10)
if pos == {"x": 18, "y": 3}:
    print("Walking DOWN Column 18 to Row 10...")
    steps_down_col18 = []
    for y in range(4, 11):
        steps_down_col18.append(("Down", {"x": 18, "y": y}))
    if not run_steps(steps_down_col18):
        print("Failed to walk DOWN Column 18")
        exit(0)
    pos = mgba.get_coordinates()

# 9. Walk LEFT along Row 10 to (15, 10)
if pos == {"x": 18, "y": 10}:
    print("Walking LEFT along Row 10 to (15, 10)...")
    steps_left_row10 = []
    for x in range(17, 14, -1):
        steps_left_row10.append(("Left", {"x": x, "y": 10}))
    if not run_steps(steps_left_row10):
        print("Failed to walk LEFT along Row 10")
        exit(0)
    pos = mgba.get_coordinates()

# 10. Step DOWN onto the stairs at (15, 11) to warp UP to 3F East!
if pos == {"x": 15, "y": 10}:
    print("Stepping DOWN onto stairs at (15, 11)...")
    mgba.press_buttons(["Down"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("New position after warp UP to 3F East:", pos)

mgba.take_screenshot()
