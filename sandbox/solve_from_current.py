import mgba
import time
from PIL import Image

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def check_bw_percentage():
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
                
    return black_or_white / total_pixels

def handle_any_menu_or_battle():
    # Loop and check up to 5 times with delays to handle slow battle transitions!
    for attempt in range(5):
        percentage = check_bw_percentage()
        if percentage > 0.90:
            print(f"Menu/Dialogue/Battle detected! (B/W: {percentage*100:.2f}%, attempt {attempt+1})")
            # Try pressing B first to dismiss text
            mgba.press_buttons(["B"])
            time.sleep(0.4)
            
            # Check if still in battle/dialogue
            percentage2 = check_bw_percentage()
            if percentage2 > 0.90:
                print("Still in battle/dialogue. Attempting to RUN...")
                # Select RUN
                mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
                time.sleep(1.5)
                # Dismiss "Escaped" or "Can't escape" text
                for _ in range(5):
                    mgba.press_buttons(["B"])
                    time.sleep(0.3)
            return True
        time.sleep(0.2)
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

pos = get_pos()
print("Starting solve from current position:", pos)

# PART 1: Cross 2F West to 2F East starting from Column 5 Row 11
if pos == (5, 11) or pos == (5, 10):
    steps_up_2f = []
    for y in range(pos[1] - 1, 2, -1):
        steps_up_2f.append(("Up", (5, y)))
    print("Walking UP Column 5 on 2F West...")
    if not run_safe_steps(steps_up_2f):
        print("Failed walking UP Column 5")
        exit(1)
        
    pos = get_pos()

if pos == (5, 3):
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

# PART 2: Cross 3F East to pitfall and drop down to 1F East inside fenced room
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

# PART 3: From 1F East inside fenced room, walk to stairs and warp DOWN to B1F East
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

# PART 4: Cross B1F East to B1F West NORTH and retrieve Secret Key
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

# PART 5: Pick up the Secret Key!
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
