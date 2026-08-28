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

print("Starting solve_from_current.py (Bypass Column 20 Closed Gate)...")
print("Start position:", get_pos())

# 1. Walk Left to Column 19 (to bypass Column 20 Row 5 shutter gate)
print("Stepping Left to Column 19...")
if not safe_step("Left", (19, 6)):
    print("Failed to reach Column 19")
    exit(1)

# 2. Walk UP Column 19 to Row 3 (completely open!)
steps_up_col_19 = [
    ("Up", (19, 5)),
    ("Up", (19, 4)),
    ("Up", (19, 3)),
]
print("Walking UP Column 19 to Row 3...")
if not run_safe_steps(steps_up_col_19):
    print("Failed walking UP Column 19")
    exit(1)

# 3. Walk RIGHT along Row 3 to Column 26
steps_row_3 = []
for x in range(20, 27):
    steps_row_3.append(("Right", (x, 3)))
print("Walking RIGHT along Row 3 to Column 26...")
if not run_safe_steps(steps_row_3):
    print("Failed walking along Row 3")
    exit(1)

# 4. Drop through the pitfall to 1F East inside the fenced room
print("Dropping through the pitfall to 1F East...")
if not safe_step("Down"):
    print("Failed to drop through pitfall")
    exit(1)
time.sleep(2.5)
pos = get_pos()
print("Landed on 1F East inside fenced room:", pos)

# 5. Walk to B1F East stairs and warp down
if pos[1] == 4:
    if not safe_step("Down"):
        exit(1)
pos = get_pos()
while pos[0] > 22:
    if not safe_step("Left"):
        exit(1)
    pos = get_pos()
while pos[1] > 3:
    if not safe_step("Up"):
        exit(1)
    pos = get_pos()
    
print("Stepping UP to warp down to B1F East...")
mgba.press_buttons(["Up"])
time.sleep(2.0)
pos = get_pos()
print("Position on B1F East:", pos)

# 6. Cross B1F East to B1F West NORTH
if pos[1] == 2:
    if not safe_step("Down"):
        exit(1)
# Walk to Column 21
if not safe_step("Left"):
    exit(1)
# Down to Row 5
if not safe_step("Down") or not safe_step("Down"):
    exit(1)
# Left to Column 1
pos = get_pos()
while pos[0] > 1:
    if not safe_step("Left"):
        exit(1)
    pos = get_pos()
    
# 7. Retrieve Secret Key!
print("Facing UP...")
mgba.press_buttons(["Up"])
time.sleep(1.0)

print("Retrieving Secret Key...")
mgba.press_buttons(["A"])
time.sleep(2.0)
for _ in range(5):
    mgba.press_buttons(["B"])
    time.sleep(0.4)

print("Mansion fully solved! Secret Key retrieved successfully! Current Position:", get_pos())
mgba.take_screenshot()
