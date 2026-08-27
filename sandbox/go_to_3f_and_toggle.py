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
        print(f"Menu/Dialogue detected! (B/W: {percentage*100:.2f}%). Escape...")
        mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
        time.sleep(1.5)
        # Dismiss run text
        for _ in range(4):
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

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

pos = mgba.get_coordinates()
print("Starting position on 2F West:", pos)

# 1. Walk from (5, 10) to (7, 11) on 2F West
if pos == {"x": 5, "y": 10}:
    if not walk_step("Down", {"x": 5, "y": 11}):
        print("Failed to move Down to (5, 11)")
        exit(0)
    pos = mgba.get_coordinates()

if pos == {"x": 5, "y": 11}:
    steps_to_stairs = [
        ("Right", {"x": 6, "y": 11}),
        ("Right", {"x": 7, "y": 11})
    ]
    if not run_steps(steps_to_stairs):
        print("Failed to walk to (7, 11)")
        exit(0)
    pos = mgba.get_coordinates()

# 2. Warp UP to 3F West
if pos == {"x": 7, "y": 11}:
    print("Stepping UP to warp to 3F West...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position on 3F West after warp:", pos)

# In State A, the shutter gate on 3F West at Row 10/9 is CLOSED.
# This means warping UP in State A triggers a pushback, so we land on 3F West but must walk safely!
# Wait, let's verify where we are after warp.
# Often we land at (7, 11) or (7, 10) on 3F West.
# Let's take a screenshot to verify what's happening.
mgba.take_screenshot()
