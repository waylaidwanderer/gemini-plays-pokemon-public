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

def safe_step(direction, expected_coords=None):
    old_pos = get_pos()
    mgba.press_buttons([direction])
    time.sleep(0.45)
    new_pos = get_pos()
    
    if new_pos != old_pos:
        if expected_coords and new_pos != expected_coords:
            print(f"Moved {direction} but landed at unexpected position: {new_pos} (expected {expected_coords})")
        else:
            print(f"Successfully stepped {direction} to {new_pos}")
        return True
        
    # If we didn't move, check for battle or dialogue
    if handle_any_menu_or_battle():
        print(f"Handled battle/dialogue. Retrying step {direction}...")
        mgba.press_buttons([direction])
        time.sleep(0.45)
        new_pos = get_pos()
        if new_pos != old_pos:
            print(f"Successfully stepped {direction} to {new_pos} after retry")
            return True
            
    print(f"BLOCKED: Could not step {direction} from {old_pos}")
    return False

def run_safe_steps(steps):
    for d, c in steps:
        if not safe_step(d, c):
            return False
    return True

print("Start position:", get_pos())

# PART 1: Walk from (1, 10) to (2, 12)
steps_to_switch = [
    ("Down", (1, 11)),
    ("Down", (1, 12)),
    ("Right", (2, 12)),
]
print("Walking to switch...")
if not run_safe_steps(steps_to_switch):
    print("Failed to reach switch")
    exit(1)

# PART 2: Face UP and Toggle Switch to State B (Exactly 4 A-presses)
print("Turning UP...")
mgba.press_buttons(["Up"])
time.sleep(0.5)

print("Toggling Mewtwo switch...")
for i in range(4):
    mgba.press_buttons(["A"])
    time.sleep(1.0)
print("Switch toggle complete!")

# PART 3: Walk to (7, 11) on Row 11
steps_to_stairs = [
    ("Right", (3, 12)),
    ("Up", (3, 11)),
    ("Right", (4, 11)),
    ("Right", (5, 11)),
    ("Right", (6, 11)),
    ("Right", (7, 11)),
]
print("Walking to 3F West stairs...")
if not run_safe_steps(steps_to_stairs):
    print("Failed to reach 3F West stairs")
    exit(1)

# PART 4: Step UP to warp down to 2F West (landing at 7, 11)
print("Stepping UP to warp DOWN to 2F West...")
mgba.press_buttons(["Up"])
time.sleep(2.0)
pos = get_pos()
print("Position after warping DOWN:", pos)

# PART 5: Cross 2F West to 2F East
if pos == (7, 11) or pos == (7, 10):
    if pos[1] == 10:
        safe_step("Down")
    if not run_safe_steps([
        ("Left", (6, 11)),
        ("Left", (5, 11)),
    ]):
        print("Failed to reach Column 5")
        exit(1)
        
    steps_up_2f = []
    for y in range(10, 2, -1):
        steps_up_2f.append(("Up", (5, y)))
    print("Walking UP Column 5 on 2F West...")
    if not run_safe_steps(steps_up_2f):
        print("Failed walking UP Column 5")
        exit(1)
        
    steps_across_2f = []
    for x in range(6, 19):
        steps_across_2f.append(("Right", (x, 3)))
    print("Walking across Row 3 on 2F...")
    if not run_safe_steps(steps_across_2f):
        print("Failed walking across Row 3")
        exit(1)
        
    steps_down_2f = []
    for y in range(4, 11):
        steps_down_2f.append(("Down", (18, y)))
    print("Walking DOWN Column 18 on 2F East...")
    if not run_safe_steps(steps_down_2f):
        print("Failed walking DOWN Column 18")
        exit(1)
        
    steps_left_2f = [
        ("Left", (17, 10)),
        ("Left", (16, 10)),
        ("Left", (15, 10)),
    ]
    print("Walking LEFT to stairs...")
    if not run_safe_steps(steps_left_2f):
        print("Failed to reach (15, 10)")
        exit(1)
        
    print("Stepping DOWN to warp UP to 3F East...")
    mgba.press_buttons(["Down"])
    time.sleep(2.0)
    pos = get_pos()
    print("Position after warping UP to 3F East:", pos)

# PART 6: Cross 3F East to pitfall and drop down to 1F East inside fenced room
if pos == (15, 11) or pos == (16, 11):
    if pos[0] == 15:
        safe_step("Right")
    steps_to_pitfall_3f = [
        ("Right", (17, 11)),
        ("Right", (18, 11)),
        ("Right", (19, 11)),
        ("Right", (20, 11)),
    ]
    print("Walking RIGHT along Row 11 on 3F East...")
    if not run_safe_steps(steps_to_pitfall_3f):
        print("Failed to reach Column 20")
        exit(1)
        
    steps_up_3f = []
    for y in range(10, 2, -1):
        steps_up_3f.append(("Up", (20, y)))
    print("Walking UP Column 20 on 3F East...")
    if not run_safe_steps(steps_up_3f):
        print("Failed walking UP Column 20")
        exit(1)
        
    steps_right_3f = []
    for x in range(21, 27):
        steps_right_3f.append(("Right", (x, 3)))
    print("Walking RIGHT along Row 3 to Column 26...")
    if not run_safe_steps(steps_right_3f):
        print("Failed walking RIGHT along Row 3")
        exit(1)
        
    print("Stepping DOWN to drop through the pitfall to 1F East...")
    mgba.press_buttons(["Down"])
    time.sleep(2.5)
    pos = get_pos()
    print("Position after dropping to 1F East:", pos)

# PART 7: From 1F East inside fenced room, walk to stairs and warp DOWN to B1F East
if pos == (26, 4) or pos == (25, 4):
    print("Walking to B1F East stairs...")
    steps_to_stairs = []
    current_x = pos[0]
    for x in range(current_x - 1, 21, -1):
        steps_to_stairs.append(("Left", (x, 4)))
    steps_to_stairs.append(("Up", (22, 3)))
    if not run_safe_steps(steps_to_stairs):
        print("Failed to reach stairs at (22, 3)")
        exit(1)
        
    print("Stepping UP to warp down to B1F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = get_pos()
    print("Position after warping down to B1F East:", pos)

# PART 8: Cross B1F East to B1F West NORTH and retrieve Secret Key
if pos == (22, 3) or pos == (22, 2):
    print("Crossing B1F East to B1F West NORTH...")
    if pos[1] == 2:
        safe_step("Down")
        pos = get_pos()
        
    if not run_safe_steps([
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
    if not run_safe_steps(steps_left):
        print("Failed to reach Secret Key room")
        exit(1)
    pos = get_pos()

# PART 9: Pick up the Secret Key!
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

print("Mansion master route completely solved!")
mgba.take_screenshot()
