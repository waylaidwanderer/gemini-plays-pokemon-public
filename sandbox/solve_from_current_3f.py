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

print("Initial position:", mgba.get_coordinates())

# Dismiss "Got away safely!" if still on screen
for _ in range(3):
    mgba.press_buttons(["B"])
    time.sleep(0.3)

# Part 1: Walk to the 3F East stairs at (15, 11)
pos = mgba.get_coordinates()
if pos == {"x": 10, "y": 10}:
    print("Walking to (15, 11)...")
    steps_to_stairs = [
        ("Right", {"x": 11, "y": 10}),
        ("Right", {"x": 12, "y": 10}),
        ("Right", {"x": 13, "y": 10}),
        ("Right", {"x": 14, "y": 10}),
        ("Right", {"x": 15, "y": 10}),
        ("Down", {"x": 15, "y": 11}),
    ]
    if not run_steps(steps_to_stairs):
        print("Failed to reach stairs at (15, 11)")
        exit(1)
        
    print("Warping down to 2F East...")
    mgba.press_buttons(["Down"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after warping down to 2F East:", pos)

# Part 2: On 2F East, walk UP to Row 3, then Left to 2F West (5, 3)
pos = mgba.get_coordinates()
if pos == {"x": 15, "y": 11} or pos == {"x": 16, "y": 11}:
    print("Walking up to Row 3 on 2F East...")
    current_x = pos["x"]
    if current_x == 16:
        walk_step("Left", {"x": 15, "y": 11})
        
    steps_up_2f = [
        ("Up", {"x": 15, "y": 10}),
        ("Up", {"x": 15, "y": 9}),
        ("Up", {"x": 15, "y": 8}),
        ("Up", {"x": 15, "y": 7}),
        ("Up", {"x": 15, "y": 6}),
        ("Up", {"x": 15, "y": 5}),
        ("Up", {"x": 15, "y": 4}),
        ("Up", {"x": 15, "y": 3}),
    ]
    if not run_steps(steps_up_2f):
        print("Failed to walk UP to Row 3 on 2F")
        exit(1)
        
    print("Walking Left across 2F to (5, 3)...")
    steps_left_2f = []
    for x in range(14, 4, -1):
        steps_left_2f.append(("Left", {"x": x, "y": 3}))
    if not run_steps(steps_left_2f):
        print("Failed to walk Left across Row 3")
        exit(1)
        
    pos = mgba.get_coordinates()

# Part 3: From (5, 3) on 2F West, walk down to (5, 11)
if pos == {"x": 5, "y": 3}:
    print("Walking Down Column 5 on 2F West...")
    steps_down_2f = []
    for y in range(4, 12):
        steps_down_2f.append(("Down", {"x": 5, "y": y}))
    if not run_steps(steps_down_2f):
        print("Failed to walk Down Column 5 on 2F West")
        exit(1)
        
    pos = mgba.get_coordinates()

# Part 4: From (5, 11) on 2F West, walk to the stairs at (7, 10) and warp UP to 3F West
if pos == {"x": 5, "y": 11}:
    print("Walking to 3F West stairs...")
    if not run_steps([
        ("Right", {"x": 6, "y": 11}),
        ("Right", {"x": 7, "y": 11}),
        ("Up", {"x": 7, "y": 10}),
    ]):
        print("Failed to step UP onto stairs")
        exit(1)
        
    print("Warping UP to 3F West...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position on 3F West after warping UP:", pos)

# Part 5: On 3F West, walk to the Mewtwo switch at (2, 11)
if pos == {"x": 7, "y": 11} or pos == {"x": 7, "y": 10}:
    if pos["y"] == 10:
        walk_step("Down", {"x": 7, "y": 11})
        
    print("Walking to the Mewtwo switch...")
    steps_to_switch = [
        ("Left", {"x": 6, "y": 11}),
        ("Left", {"x": 5, "y": 11}),
        ("Left", {"x": 4, "y": 11}),
        ("Left", {"x": 3, "y": 11}),
        ("Down", {"x": 3, "y": 12}),
        ("Left", {"x": 2, "y": 12}),
    ]
    if not run_steps(steps_to_switch):
        print("Failed to reach (2, 12)")
        exit(1)
        
    pos = mgba.get_coordinates()

# Part 6: Toggle the switch to State B!
if pos == {"x": 2, "y": 12}:
    print("Toggling Mewtwo switch at (2, 11)...")
    # Face UP towards (2, 11) from (2, 12)
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # Toggle dialogue (4 A presses)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    print("Switch toggled to State B!")
    mgba.take_screenshot()

print("Script execution completed!")
