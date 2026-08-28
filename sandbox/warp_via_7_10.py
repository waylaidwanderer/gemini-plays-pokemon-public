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

# Starting at (8, 10) on B1F West SOUTH (State B)
print("Testing staircase warp from (8, 10)...")

# Try to step Left onto (7, 10)
old_pos = get_pos()
if safe_step("Left", (7, 10)):
    # Check if we warped (warping changes coordinates to 1F West)
    # On 1F West, the coordinates after warping should be (7, 10) or similar.
    # We can detect warp by taking a screenshot or checking position.
    time.sleep(1.0)
    current_pos = get_pos()
    print("Position on (7, 10):", current_pos)
    
    # Wait, did we warp to 1F West?
    # Let's take a screenshot
    mgba.take_screenshot()
    
    # If we are still on B1F (e.g. current_pos is (7, 10)), try to continue Left
    if current_pos == (7, 10):
        print("Still on B1F. Moving Left to (6, 10)...")
        if safe_step("Left", (6, 10)):
            print("Moving Left to (5, 10)...")
            if safe_step("Left", (5, 10)):
                time.sleep(1.0)
                print("Position after stepping onto (5, 10):", get_pos())
                mgba.take_screenshot()
