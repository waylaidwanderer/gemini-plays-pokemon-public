import mgba
import time
from PIL import Image

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def check_dialogue_or_battle():
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file)
    img_std = img.resize((160, 144), Image.Resampling.NEAREST)
    
    black_or_white = 0
    total_pixels = 0
    for y in range(112, 144):
        for x in range(8, 152):
            r, g, b = img_std.getpixel((x, y))[:3]
            total_pixels += 1
            is_bw = (r < 55 and g < 55 and b < 55) or (r > 200 and g > 200 and b > 200)
            if is_bw:
                black_or_white += 1
                
    ratio = black_or_white / total_pixels
    return ratio > 0.88

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

print("Starting solve_from_battle.py...")

# 1. RUN from the wild Ponyta
run_from_battle()
time.sleep(1.0)

pos = get_pos()
print("Position after escaping battle:", pos)

# 2. Walk to Column 3 Row 10
# Current position should be (2, 13)
if pos == (2, 13):
    steps_to_col_3 = [
        ("Right", (3, 13)),
        ("Right", (4, 13)),
        ("Up", (4, 12)),
        ("Up", (4, 11)),
        ("Left", (3, 11)),
        ("Up", (3, 10)),
    ]
    print("Walking to Column 3 Row 10...")
    if not run_safe_steps(steps_to_col_3):
        print("Failed to reach Column 3 Row 10")
        exit(1)

# 3. Walk UP Column 3 through open gate to Row 6 (gate at (3, 9) is OPEN in State B!)
print("Walking UP through Column 3 gate to Row 6...")
steps_up_gate = [
    ("Up", (3, 9)),
    ("Up", (3, 8)),
    ("Up", (3, 7)),
    ("Up", (3, 6)),
]
if not run_safe_steps(steps_up_gate):
    print("Failed walking UP Column 3")
    exit(1)

# 4. Walk RIGHT along Row 6 to Column 20
print("Walking RIGHT along Row 6 to Column 20...")
pos = get_pos()
while pos[0] < 20:
    pos = step("Right")

# 5. Walk UP Column 20 to Row 3
print("Walking UP Column 20 to Row 3...")
while get_pos()[1] > 3:
    step("Up")

# 6. Walk RIGHT along Row 3 to Column 26
print("Walking RIGHT along Row 3 to Column 26...")
while get_pos()[0] < 26:
    step("Right")

# 7. Drop through the pitfall to 1F East inside the fenced room
print("Dropping through the pitfall to 1F East...")
step("Down")
time.sleep(2.5)
pos = get_pos()
print("Landed on 1F East:", pos)

# 8. Walk to B1F East stairs and warp down
if pos[1] == 4:
    step("Down")
pos = get_pos()
while pos[0] > 22:
    pos = step("Left")
while pos[1] > 3:
    pos = step("Up")

print("Stepping UP to warp down to B1F East...")
mgba.press_buttons(["Up"])
time.sleep(2.0)
pos = get_pos()
print("Position on B1F East:", pos)

# 9. Cross B1F East to B1F West NORTH
if pos[1] == 2:
    step("Down")
# Walk to Column 21
step("Left")
# Down to Row 5
step("Down")
step("Down")
# Left to Column 1
pos = get_pos()
while pos[0] > 1:
    pos = step("Left")

# 10. Retrieve Secret Key!
print("Facing UP...")
mgba.press_buttons(["Up"])
time.sleep(1.0)

print("Retrieving Secret Key...")
mgba.press_buttons(["A"])
time.sleep(2.0)
for _ in range(5):
    mgba.press_buttons(["B"])
    time.sleep(0.4)

print("Mansion fully solved! Current Position:", get_pos())
mgba.take_screenshot()
