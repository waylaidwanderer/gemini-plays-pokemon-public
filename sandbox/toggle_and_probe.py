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

# Transit helper using Row 12
def go_to_row_10_col(target_col):
    pos = get_pos()
    while pos[1] < 12:
        pos_new = step("Down")
        if pos_new == pos: break
        pos = pos_new
    while pos[1] > 12:
        pos_new = step("Up")
        if pos_new == pos: break
        pos = pos_new
        
    pos = get_pos()
    while pos[0] < target_col:
        pos_new = step("Right")
        if pos_new == pos: break
        pos = pos_new
    while pos[0] > target_col:
        pos_new = step("Left")
        if pos_new == pos: break
        pos = pos_new
        
    pos = get_pos()
    while pos[1] > 10:
        pos_new = step("Up")
        if pos_new == pos: break
        pos = pos_new
        
    return get_pos() == (target_col, 10)

def step(direction):
    old_pos = get_pos()
    mgba.press_buttons([direction])
    time.sleep(0.55)
    return get_pos()

# --- Execution ---
print("Starting toggle_and_probe.py...")
pos = get_pos()

# 1. Walk to switch (2, 12) from (7, 12)
steps_to_switch = []
if pos == (7, 12):
    for x in range(6, 1, -1):
        steps_to_switch.append(("Left", (x, 12)))
else:
    print("Warning: unexpected starting pos:", pos)
    
if steps_to_switch:
    if not run_safe_steps(steps_to_switch):
        print("Failed to reach switch")
        exit(1)

# Face UP
print("Facing UP...")
mgba.press_buttons(["Up"])
time.sleep(1.0)

# 2. Toggle switch with 4 A-presses
print("Toggling switch to State B...")
mgba.press_buttons([
    "A", "sleep 1500",
    "A", "sleep 1500",
    "A", "sleep 1500",
    "A", "sleep 1500"
])
time.sleep(7.0)
print("Switch toggled!")

# 3. Probe columns on Row 9
open_columns = []
columns_to_test = [1, 3, 4, 5, 6, 7]

for col in columns_to_test:
    print(f"Moving to Column {col}...")
    if not go_to_row_10_col(col):
        print(f"Failed to reach Column {col} Row 10")
        continue
        
    print(f"Testing Column {col} Row 9...")
    old_pos = get_pos()
    mgba.press_buttons(["Up"])
    time.sleep(0.55)
    new_pos = get_pos()
    
    if new_pos[1] == 9:
        print(f"SUCCESS: Column {col} Row 9 is OPEN!")
        open_columns.append(col)
        # Step back down to Row 10
        step("Down")
    else:
        print(f"Column {col} Row 9 is CLOSED.")

print("Probe complete! Open columns on Row 9 in State B:", open_columns)
mgba.take_screenshot()
