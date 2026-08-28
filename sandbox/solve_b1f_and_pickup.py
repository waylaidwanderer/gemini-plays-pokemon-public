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

print("Start position:", get_pos())
pos = get_pos()

# Step 1: Walk to Row 5 Column 19
# Current pos on B1F is (22, 2)
steps_to_row_5 = [
    ("Down", (22, 3)),
    ("Down", (22, 4)),
    ("Left", (21, 4)),
    ("Left", (20, 4)),
    ("Left", (19, 4)),
    ("Down", (19, 5)),
]
print("Walking to B1F Row 5...")
if not run_safe_steps(steps_to_row_5):
    print("Failed to reach Row 5")
    exit(1)

# Step 2: Walk straight LEFT along Row 5 across Column 9 gate (now open in State B) directly to B1F West
steps_left = []
for x in range(18, 0, -1):
    steps_left.append(("Left", (x, 5)))
print("Walking LEFT to Secret Key room...")
if not run_safe_steps(steps_left):
    print("Failed to reach Secret Key room")
    exit(1)

# Step 3: Align UP towards the Secret Key at (1, 4)
print("Facing UP towards Secret Key...")
mgba.press_buttons(["Up"])
time.sleep(0.5)

# Step 4: Pick up the Secret Key!
print("Retrieving Secret Key...")
mgba.press_buttons(["A"])
time.sleep(2.0)
# Dismiss dialogue
for _ in range(5):
    mgba.press_buttons(["B"])
    time.sleep(0.4)

print("Mansion Secret Key retrieved successfully! Final Position:", get_pos())
mgba.take_screenshot()
