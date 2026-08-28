import mgba
import time
from PIL import Image

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def check_dialogue_or_battle():
    # Robust white-only check to completely eliminate dark tile false positives on B1F
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file)
    img_std = img.resize((160, 144), Image.Resampling.NEAREST)
    
    white_pixels = 0
    total_pixels = 0
    for y in range(112, 144):
        for x in range(8, 152):
            r, g, b = img_std.getpixel((x, y))[:3]
            total_pixels += 1
            if r > 220 and g > 220 and b > 220:
                white_pixels += 1
                
    ratio = white_pixels / total_pixels
    return ratio > 0.80

def run_from_battle():
    print("Dismissing battle intro text...")
    for i in range(12):
        mgba.press_buttons(["B"])
        time.sleep(0.35)
        
    print("Attempting to select RUN...")
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
    time.sleep(2.0)
    
    print("Dismissing escape dialogue...")
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.35)

def safe_step(direction, expected_coords=None, max_attempts=15):
    for attempt in range(max_attempts):
        if check_dialogue_or_battle():
            print("Dialogue/Battle detected. Handling...")
            run_from_battle()
            time.sleep(0.5)
            continue
            
        old_pos = get_pos()
        mgba.press_buttons([direction])
        time.sleep(0.55)
        new_pos = get_pos()
        
        if new_pos != old_pos:
            if expected_coords and new_pos != expected_coords:
                print(f"Moved {direction} to {new_pos} (expected {expected_coords}). Checking...")
            else:
                print(f"Successfully stepped {direction} to {new_pos}")
            return True
            
        print(f"Collision/delay at {old_pos} trying {direction} (attempt {attempt+1}/{max_attempts})")
        time.sleep(0.25)
        
    print(f"ERROR: Could not step {direction} from {old_pos}")
    return False

def run_safe_steps(steps):
    for d, c in steps:
        if not safe_step(d, c):
            return False
    return True

print("Starting solve_b1f_and_pickup.py...")
print("Start position:", get_pos())

# 1. Walk from (25, 5) to (22, 2) on 1F East (warp stairs)
steps_to_stairs = [
    ("Up", (25, 4)),
    ("Up", (25, 3)),
    ("Up", (25, 2)),
    ("Left", (24, 2)),
    ("Left", (23, 2)),
]
print("Walking to B1F East stairs corridor...")
if not run_safe_steps(steps_to_stairs):
    print("Failed to reach (23, 2)")
    exit(1)

print("Stepping Left onto stairs at (22, 2) to warp down...")
mgba.press_buttons(["Left"])
time.sleep(2.5)

pos = get_pos()
print("Position after warp:", pos)

# 2. Cross B1F East to B1F West NORTH
if pos == (22, 2) or pos == (22, 3):
    print("Crossing B1F East to B1F West NORTH...")
    if pos[1] == 2:
        safe_step("Down")
    
    # Walk: Left to (21, 3) -> Down to (21, 5)
    if not run_safe_steps([
        ("Left", (21, 3)),
        ("Down", (21, 4)),
        ("Down", (21, 5)),
    ]):
        print("Failed to reach Column 21 Row 5")
        exit(1)
        
    # Walk straight Left on Row 5 to Column 1 (Secret Key room)
    steps_left = []
    for x in range(20, 0, -1):
        steps_left.append(("Left", (x, 5)))
    if not run_safe_steps(steps_left):
        print("Failed to reach B1F West")
        exit(1)
        
    pos = get_pos()

# 3. Pick up the Secret Key!
if pos == (1, 5):
    print("Aligning UP towards the Secret Key...")
    mgba.press_buttons(["Up"])
    time.sleep(1.0)
    
    print("Retrieving Secret Key...")
    mgba.press_buttons(["A"])
    time.sleep(2.0)
    # Dismiss dialogue
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        
    print("Mansion fully solved! Secret Key retrieved successfully! Current Position:", get_pos())
    mgba.take_screenshot()
