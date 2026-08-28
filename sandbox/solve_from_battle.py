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

print("Starting solve_from_battle.py with robust white-only battle detection...")

# 1. RUN from the wild Vulpix
run_from_battle()
time.sleep(1.0)

pos = get_pos()
print("Position after escaping battle:", pos)

# 2. Walk to Column 3 Row 10
# Current position should be (3, 11)
if pos == (3, 11):
    if not safe_step("Up", (3, 10)):
        print("Failed to reach (3, 10)")
        exit(1)

# 3. Test Column 3 Row 9 gate (now open in State B!)
print("Testing if Column 3 Row 9 is open...")
old_pos = get_pos()
mgba.press_buttons(["Up"])
time.sleep(0.55)
new_pos = get_pos()

if new_pos[1] == 9:
    print("SUCCESS: Column 3 Row 9 gate is OPEN in State B!!!")
    # Walk UP through gate to Row 6
    steps_up = [
        ("Up", (3, 8)),
        ("Up", (3, 7)),
        ("Up", (3, 6)),
    ]
    if not run_safe_steps(steps_up):
        print("Failed to walk up to Row 6")
        exit(1)
        
    # Walk RIGHT along Row 6 to Column 20
    print("Walking RIGHT along Row 6 to Column 20...")
    pos = get_pos()
    while pos[0] < 20:
        pos = step("Right")
        
    # Walk UP Column 20 to Row 3
    print("Walking UP Column 20 to Row 3...")
    while get_pos()[1] > 3:
        step("Up")
        
    # Walk RIGHT along Row 3 to Column 26
    print("Walking RIGHT along Row 3 to Column 26...")
    while get_pos()[0] < 26:
        step("Right")
        
    # Drop through pitfall to 1F East
    print("Dropping through the pitfall to 1F East...")
    step("Down")
    time.sleep(2.5)
    pos = get_pos()
    print("Landed on 1F East inside fenced room:", pos)
    
    # Walk to B1F East stairs and warp down
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
    
    # Cross B1F East to B1F West NORTH
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
        
    # Retrieve Secret Key!
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
else:
    print("Gate at Column 3 Row 9 is CLOSED.")
