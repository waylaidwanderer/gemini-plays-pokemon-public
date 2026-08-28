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

# Escape route from B1F East to B1F West SOUTH and then warp UP to 1F West
steps = [
    ("Down", (10, 6)),
    ("Down", (10, 7)),
    ("Right", (11, 7)),
    ("Right", (12, 7)),
    ("Down", (12, 8)),
    ("Down", (12, 9)),
    ("Down", (12, 10)),
    ("Down", (12, 11)),
    ("Left", (11, 11)),
    ("Left", (10, 11)), # Crosses through open Row 11 gate
    ("Left", (9, 11)),
    ("Left", (8, 11)),
    ("Left", (7, 11)),
    ("Left", (6, 11)),
    ("Left", (5, 11)),
    ("Up", (5, 10)),
]

print("Walking State A escape route to B1F West stairs...")
if not run_safe_steps(steps):
    print("Failed to reach stairs")
    exit(1)

print("Stepping UP onto stairs to warp UP to 1F West...")
mgba.press_buttons(["Up"])
time.sleep(2.0)
pos = get_pos()
print("Position on 1F West:", pos)

# Walk from 1F West stairs landing to exit Mansion
if pos == (5, 11) or pos == (5, 10):
    steps_to_exit = [
        ("Down", (5, 11)),
        ("Down", (5, 12)),
        ("Down", (5, 13)),
        ("Down", (5, 14)),
        ("Down", (5, 15)),
        ("Down", (5, 16)),
        ("Down", (5, 17)),
        ("Down", (5, 18)),
        ("Down", (5, 19)),
        ("Down", (5, 20)),
        ("Down", (5, 21)),
        ("Down", (5, 22)),
        ("Down", (5, 23)),
        ("Down", (5, 24)),
        ("Down", (5, 25)),
        ("Down", (5, 26)),
        ("Down", (5, 27)),
    ]
    print("Walking down Column 5 to exit...")
    if not run_safe_steps(steps_to_exit):
        print("Failed to reach exit")
        exit(1)
        
    print("Stepping DOWN to exit Mansion...")
    mgba.press_buttons(["Down"])
    time.sleep(2.0)
    print("Mansion exited! Current Position:", get_pos())

mgba.take_screenshot()
