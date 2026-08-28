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

print("Current position:", get_pos())

# 1. Walk from (3, 10) to switch standing position (2, 12)
steps_to_switch = [
    ("Down", (3, 11)),
    ("Down", (3, 12)),
    ("Left", (2, 12)),
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

# 3. Walk to Column 3 Row 10
steps_to_col_3 = [
    ("Down", (2, 13)),
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

# 4. Walk UP Column 3 through open gate to Row 6 (gate at (3, 9) is OPEN in State B!)
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

# 5. Walk RIGHT along Row 6 to Column 20
print("Walking RIGHT along Row 6 to Column 20...")
pos = get_pos()
while pos[0] < 20:
    pos = step("Right")

# 6. Walk UP Column 20 to Row 3
print("Walking UP Column 20 to Row 3...")
while get_pos()[1] > 3:
    step("Up")

# 7. Walk RIGHT along Row 3 to Column 26
print("Walking RIGHT along Row 3 to Column 26...")
while get_pos()[0] < 26:
    step("Right")

# 8. Step DOWN to drop through the pitfall to 1F East inside the fenced room
print("Dropping through the pitfall to 1F East...")
step("Down")
time.sleep(2.5)
pos = get_pos()
print("Part 1 complete! Landed on 1F East:", pos)
mgba.take_screenshot()
