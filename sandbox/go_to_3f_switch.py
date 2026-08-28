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
        time.sleep(0.3)
        
    print("Attempting to select RUN...")
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
    time.sleep(2.0)
    
    print("Dismissing escape dialogue...")
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.3)

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

# Starting at (4, 10) on 3F West
print("Navigating to switch around Burglar NPC. Current position:", get_pos())

# Route that goes around Column 5:
# 1. Right to (5, 10)
# 2. Down to (5, 11)
# 3. Down to (5, 12)
# 4. Left to (4, 12)
# 5. Left to (3, 12)
# 6. Left to (2, 12)
steps = [
    ("Right", (5, 10)),
    ("Down", (5, 11)),
    ("Down", (5, 12)),
    ("Left", (4, 12)),
    ("Left", (3, 12)),
    ("Left", (2, 12)),
]

success = True
for d, c in steps:
    if not safe_step(d, c):
        success = False
        break
        
if success:
    print("Successfully reached (2, 12) on 3F West!")
    print("Facing UP...")
    mgba.press_buttons(["Up"])
    time.sleep(1.0)
    mgba.take_screenshot()
else:
    print("Failed to reach switch")
