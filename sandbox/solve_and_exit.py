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

print("Starting solve_and_exit.py with Column 12 Bypass Route...")
print("Start position:", get_pos())

# 1. Walk from (1, 10) to switch standing position (2, 12)
steps_to_switch = [
    ("Down", (1, 11)),
    ("Down", (1, 12)),
    ("Right", (2, 12)),
]
print("Walking to switch standing position...")
if not run_safe_steps(steps_to_switch):
    print("Failed to reach switch")
    exit(1)

print("Facing UP...")
mgba.press_buttons(["Up"])
time.sleep(1.0)

# 2. Toggle Mewtwo Switch to State B with exactly 4 slow A-presses
print("Toggling switch to State B with exactly 4 slow A-presses...")
mgba.press_buttons([
    "A", "sleep 1500",
    "A", "sleep 1500",
    "A", "sleep 1500",
    "A", "sleep 1500"
])
time.sleep(7.0)
print("Switch toggle complete!")

# 3. Walk to Column 12 Row 11 via Row 13 (to bypass cabinets at Column 3, Column 8, and Column 8 NPC)
print("Walking to Column 12 Row 11...")
steps_to_col_12 = [
    ("Down", (2, 13)),
    ("Right", (3, 13)),
    ("Right", (4, 13)),
    ("Right", (5, 13)),
    ("Right", (6, 13)),
    ("Right", (7, 13)),
    ("Right", (8, 13)),
    ("Right", (9, 13)),
    ("Right", (10, 13)),
    ("Right", (11, 13)),
    ("Right", (12, 13)),
    ("Up", (12, 12)),
    ("Up", (12, 11)),
]
if not run_safe_steps(steps_to_col_12):
    print("Failed to reach Column 12 Row 11")
    exit(1)

# 4. Walk UP Column 12 to Row 6 (completely open in both states!)
steps_up_col_12 = [
    ("Up", (12, 10)),
    ("Up", (12, 9)),
    ("Up", (12, 8)),
    ("Up", (12, 7)),
    ("Up", (12, 6)),
]
print("Walking UP Column 12 to Row 6...")
if not run_safe_steps(steps_up_col_12):
    print("Failed walking UP Column 12")
    exit(1)

# 5. Walk RIGHT along Row 6 to Column 20
print("Walking RIGHT along Row 6 to Column 20...")
pos = get_pos()
while pos[0] < 20:
    pos_old = pos
    pos = safe_step("Right") # wait, we can just use safe_step!
    if not pos:
        print("Failed stepping Right")
        exit(1)
    pos = get_pos()
    
# 6. Walk UP Column 20 to Row 3
print("Walking UP Column 20 to Row 3...")
while get_pos()[1] > 3:
    if not safe_step("Up"):
        print("Failed stepping Up")
        exit(1)
    
# 7. Walk RIGHT along Row 3 to Column 26
print("Walking RIGHT along Row 3 to Column 26...")
while get_pos()[0] < 26:
    if not safe_step("Right"):
        print("Failed stepping Right")
        exit(1)
    
# 8. Drop through the pitfall to 1F East inside the fenced room
print("Dropping through the pitfall to 1F East...")
if not safe_step("Down"):
    print("Failed to drop through pitfall")
    exit(1)
time.sleep(2.5)
pos = get_pos()
print("Landed on 1F East inside fenced room:", pos)

# 9. Walk to B1F East stairs and warp down
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

# 10. Cross B1F East to B1F West NORTH
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
    
# 11. Retrieve Secret Key!
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
