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

# 1. Walk from (4, 11) to (7, 11) on 2F West
steps_to_stairs_2f = [
    ("Right", (5, 11)),
    ("Right", (6, 11)),
    ("Right", (7, 11)),
]
print("Walking to 2F West stairs...")
if not run_safe_steps(steps_to_stairs_2f):
    print("Failed to reach 2F West stairs")
    exit(1)

# 2. Step UP to warp UP to 3F West (landing at 7, 11)
print("Stepping UP to warp UP to 3F West...")
mgba.press_buttons(["Up"])
time.sleep(2.0)
pos = get_pos()
print("Position on 3F West after warping UP:", pos)

# 3. On 3F West, walk to (2, 12)
if pos == (7, 11) or pos == (7, 10):
    if pos[1] == 10:
        safe_step("Down")
    steps_to_switch_3f = [
        ("Left", (6, 11)),
        ("Left", (5, 11)),
        ("Left", (4, 11)),
        ("Left", (3, 11)),
        ("Down", (3, 12)),
        ("Left", (2, 12)),
    ]
    print("Walking to switch on 3F West...")
    if not run_safe_steps(steps_to_switch_3f):
        print("Failed to reach 3F West switch")
        exit(1)

# 4. Turn UP and press A exactly 5 times (testing 5 A-presses!)
print("Turning UP...")
mgba.press_buttons(["Up"])
time.sleep(0.5)

print("Toggling Mewtwo switch with 5 A-presses...")
for i in range(5):
    print(f"Pressing A {i+1}/5...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
print("Switch toggle complete!")

# 5. Walk to (7, 11) on 3F West Row 11
steps_to_stairs_3f = [
    ("Right", (3, 12)),
    ("Up", (3, 11)),
    ("Right", (4, 11)),
    ("Right", (5, 11)),
    ("Right", (6, 11)),
    ("Right", (7, 11)),
]
print("Walking to 3F West stairs to warp DOWN...")
if not run_safe_steps(steps_to_stairs_3f):
    print("Failed to reach 3F West stairs")
    exit(1)

# 6. Step UP to warp DOWN to 2F West (landing at 7, 11)
print("Stepping UP to warp DOWN to 2F West...")
mgba.press_buttons(["Up"])
time.sleep(2.0)
pos = get_pos()
print("Position after warping DOWN to 2F West:", pos)

# 7. On 2F West, walk to Column 5 Row 11
if pos == (7, 11) or pos == (7, 10):
    if pos[1] == 10:
        safe_step("Down")
    if not run_safe_steps([
        ("Left", (6, 11)),
        ("Left", (5, 11)),
    ]):
        print("Failed to reach Column 5")
        exit(1)

# 8. Try to walk UP Column 5
print("Testing walking UP Column 5 on 2F West after 5 A-presses...")
p1 = safe_step("Up", (5, 10))
p2 = safe_step("Up", (5, 9))
p3 = safe_step("Up", (5, 8))
p4 = safe_step("Up", (5, 7))

if p4:
    print("SUCCESS: Crossed Row 7 gate! 5 A-presses is indeed the correct switch toggle sequence!")
else:
    print("FAILED: Blocked at Row 7 gate! 5 A-presses did not open it.")

mgba.take_screenshot()
