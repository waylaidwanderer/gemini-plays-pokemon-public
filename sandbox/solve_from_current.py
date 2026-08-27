import mgba
import time
from PIL import Image

def is_in_battle_or_menu():
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file)
    img_std = img.resize((160, 144), Image.Resampling.NEAREST)
    
    black_or_white = 0
    total_pixels = 0
    for y in range(115, 140):
        for x in range(10, 150):
            r, g, b = img_std.getpixel((x, y))[:3]
            total_pixels += 1
            is_bw = (r < 50 and g < 50 and b < 50) or (r > 200 and g > 200 and b > 200)
            if is_bw:
                black_or_white += 1
                
    percentage = black_or_white / total_pixels
    return percentage > 0.85

def escape_battle_safely():
    if not is_in_battle_or_menu():
        print("No battle or menu detected.")
        return False
        
    print("Battle or menu detected! Attempting escape...")
    mgba.press_buttons(["B"])
    time.sleep(0.4)
    
    if is_in_battle_or_menu():
        print("Still in battle menu. Pressing RUN...")
        mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
        time.sleep(1.5)
        for _ in range(5):
            mgba.press_buttons(["B"])
            time.sleep(0.2)
    return True

def walk_step(direction, expected_coords, retries=15):
    for i in range(retries):
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            return True
            
        # Check if we are stuck in a battle first
        if escape_battle_safely():
            time.sleep(0.5)
            pos = mgba.get_coordinates()
            if pos == expected_coords:
                return True
                
        mgba.press_buttons([direction])
        time.sleep(0.5)
        
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            print(f"Moved {direction} to {pos}")
            return True
            
        print(f"Move {direction} failed. Current: {pos}, Expected: {expected_coords}. Retrying...")
        time.sleep(0.3)
    return False

def run_steps(steps):
    for d, c in steps:
        if not walk_step(d, c):
            return False
    return True

pos = mgba.get_coordinates()
print("Starting from:", pos)

if pos == {"x": 28, "y": 6}:
    print("Walking to B1F East stairs from (28, 6)...")
    steps = [
        ("Left", {"x": 27, "y": 6}),
        ("Left", {"x": 26, "y": 6}),
        ("Left", {"x": 25, "y": 6}),
        ("Left", {"x": 24, "y": 6}),
        ("Left", {"x": 23, "y": 6}),
        ("Up", {"x": 23, "y": 5}),
        ("Up", {"x": 23, "y": 4}),
        ("Up", {"x": 23, "y": 3}),
        ("Left", {"x": 22, "y": 3}),
    ]
    if run_steps(steps):
        print("Reached B1F East stairs pre-warp!")
    else:
        print("Failed to reach stairs")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 22, "y": 3}:
    print("Stepping UP to warp down to B1F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after warping down to B1F East:", pos)

print("Finished stairs warp! Current position:", pos)
