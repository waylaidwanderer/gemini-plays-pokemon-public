import mgba
import time
from PIL import Image

def handle_any_menu_or_battle():
    time.sleep(0.15)
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
    if percentage > 0.90:
        print(f"Menu/Dialogue/Battle detected! (B/W: {percentage*100:.2f}%)")
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        
        # Check if still in battle/dialogue
        scr_file2 = mgba.take_screenshot()
        img2 = Image.open(scr_file2)
        img_std2 = img2.resize((160, 144), Image.Resampling.NEAREST)
        black_or_white2 = 0
        for y in range(115, 140):
            for x in range(10, 150):
                r, g, b = img_std2.getpixel((x, y))[:3]
                is_bw = (r < 50 and g < 50 and b < 50) or (r > 200 and g > 200 and b > 200)
                if is_bw:
                    black_or_white2 += 1
        percentage2 = black_or_white2 / total_pixels
        
        if percentage2 > 0.90:
            print("Still in battle/dialogue. Attempting to RUN...")
            mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
            time.sleep(1.5)
            for _ in range(5):
                mgba.press_buttons(["B"])
                time.sleep(0.3)
        return True
    return False

def walk_step(direction, expected_coords, retries=15):
    for i in range(retries):
        if handle_any_menu_or_battle():
            pos = mgba.get_coordinates()
            if pos == expected_coords:
                return True
        mgba.press_buttons([direction])
        time.sleep(0.45)
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            print(f"Moved {direction}, current position: {pos}")
            return True
        print(f"Blocked or battle! Retrying {direction} to {expected_coords} (attempt {i+1}/{retries}), current: {pos}")
        time.sleep(0.3)
    return False

def run_steps(steps):
    for d, c in steps:
        if not walk_step(d, c):
            return False
    return True

# Ensure menus are closed
for _ in range(3):
    handle_any_menu_or_battle()
    time.sleep(0.1)

pos = mgba.get_coordinates()
print(f"Starting toggle sequence from position: {pos}")

# 1. Walk from (3, 10) to (2, 12)
steps_to_switch = [
    ("Down", {"x": 3, "y": 11}),
    ("Down", {"x": 3, "y": 12}),
    ("Left", {"x": 2, "y": 12}),
]
if not run_steps(steps_to_switch):
    print("Failed to reach (2, 12)")
    exit(1)

# 2. Face UP towards statue at (2, 11)
print("Facing UP...")
mgba.press_buttons(["Up"])
time.sleep(0.4)

# 3. Toggle switch with exactly 4 A-presses
print("Toggling Mewtwo Switch to State B...")
mgba.press_buttons([
    "A", "sleep 400",
    "A", "sleep 400",
    "A", "sleep 400",
    "A"
])
time.sleep(1.5)

# 4. Verify gate is open by walking to (3, 9)
print("Walking to verify State B gate...")
steps_verify = [
    ("Right", {"x": 3, "y": 12}),
    ("Up", {"x": 3, "y": 11}),
    ("Up", {"x": 3, "y": 10}),
    ("Up", {"x": 3, "y": 9}),
]
if run_steps(steps_verify):
    print("SUCCESS: Gate is open! Mansion is in State B!")
else:
    print("FAILURE: Gate is still blocked! Switch did not toggle.")
