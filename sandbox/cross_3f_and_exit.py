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

print("Start position:", get_pos())

# PART 1: Toggle Mewtwo switch to State B (Exactly 4 A-presses)
print("Toggling Mewtwo switch...")
for i in range(4):
    print(f"Pressing A {i+1}/4...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
print("Switch toggle complete!")

# PART 2: Walk to (1, 12)
if not safe_step("Left", (1, 12)):
    print("Failed to step Left to (1, 12)")
    exit(1)

# PART 3: Walk UP Column 1 to Row 6 (which is now open in State B!)
steps_up_col_1 = [
    ("Up", (1, 11)),
    ("Up", (1, 10)),
    ("Up", (1, 9)),
    ("Up", (1, 8)),
    ("Up", (1, 7)),
    ("Up", (1, 6)),
]
print("Walking UP Column 1 to Row 6...")
if not run_safe_steps(steps_up_col_1):
    print("Failed walking UP Column 1")
    exit(1)

# PART 4: Walk RIGHT along Row 6 to Column 20
steps_row_6 = []
for x in range(2, 21):
    steps_row_6.append(("Right", (x, 6)))
print("Walking RIGHT along Row 6 to Column 20...")
if not run_safe_steps(steps_row_6):
    print("Failed walking RIGHT along Row 6")
    exit(1)

# PART 5: Walk UP Column 20 to Row 3
steps_col_20 = [
    ("Up", (20, 5)),
    ("Up", (20, 4)),
    ("Up", (20, 3)),
]
print("Walking UP Column 20 to Row 3...")
if not run_safe_steps(steps_col_20):
    print("Failed walking UP Column 20")
    exit(1)

# PART 6: Walk RIGHT along Row 3 to Column 26
steps_row_3 = []
for x in range(21, 27):
    steps_row_3.append(("Right", (x, 3)))
print("Walking RIGHT along Row 3 to Column 26...")
if not run_safe_steps(steps_row_3):
    print("Failed walking RIGHT along Row 3")
    exit(1)

# PART 7: Step DOWN to drop through the pitfall to 1F East inside the fenced room
print("Stepping DOWN to drop through the pitfall to 1F East...")
mgba.press_buttons(["Down"])
time.sleep(2.5)
pos = get_pos()
print("Position after dropping to 1F East:", pos)

# PART 8: On 1F East inside fenced room, walk to stairs and warp DOWN to B1F East
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

# PART 9: Cross B1F East to B1F West NORTH and retrieve Secret Key
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

# PART 10: Pick up the Secret Key!
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
