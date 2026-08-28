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

# 1. Walk from (10, 5) back to B1F East stairs (22, 2)
# Path: Right to (19, 5) -> Up to (19, 4) -> Up to (19, 3) -> Right to (22, 3) -> Up to (22, 2)
steps_to_stairs = []
for x in range(11, 20):
    steps_to_stairs.append(("Right", (x, 5)))
steps_to_stairs.extend([
    ("Up", (19, 4)),
    ("Up", (19, 3)),
    ("Right", (20, 3)),
    ("Right", (21, 3)),
    ("Right", (22, 3)),
    ("Up", (22, 2)),
])

print("Walking to B1F East stairs...")
if not run_safe_steps(steps_to_stairs):
    print("Failed to reach stairs")
    exit(1)

# 2. Warp UP to 1F East
print("Warping UP to 1F East...")
mgba.press_buttons(["Up"])
time.sleep(2.0)
pos = get_pos()
print("Position on 1F East:", pos)

# 3. Walk out of fenced room on 1F East and exit Mansion
if pos == (22, 3) or pos == (22, 2):
    print("Walking to 1F West exit...")
    # Walk Down Column 22 to Row 5, Left to Column 11
    steps_to_exit = [
        ("Down", (22, 4)),
        ("Down", (22, 5)),
    ]
    for x in range(21, 10, -1):
        steps_to_exit.append(("Left", (x, 5)))
    # Down Column 11 to exit at (5, 27)
    for y in range(6, 14):
        steps_to_exit.append(("Down", (11, y)))
    for x in range(10, 4, -1):
        steps_to_exit.append(("Left", (x, 13)))
    for y in range(14, 28):
        steps_to_exit.append(("Down", (5, y)))
        
    if not run_safe_steps(steps_to_exit):
        print("Failed to reach exit")
        exit(1)
        
    print("Stepping DOWN to exit Mansion...")
    mgba.press_buttons(["Down"])
    time.sleep(2.0)
    print("Mansion exited! Current Position:", get_pos())

mgba.take_screenshot()
