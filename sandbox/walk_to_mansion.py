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
            r, g, b = img_std.getpixel((x, y))
            total_pixels += 1
            is_bw = (r < 50 and g < 50 and b < 50) or (r > 200 and g > 200 and b > 200)
            if is_bw:
                black_or_white += 1
                
    percentage = black_or_white / total_pixels
    if percentage > 0.90:
        print(f"Menu/Dialogue detected! (B/W: {percentage*100:.2f}%)")
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        return True
    return False

def walk_step(direction, expected_coords, retries=15):
    for i in range(retries):
        if handle_any_menu_or_battle():
            pos = mgba.get_coordinates()
            if pos == expected_coords:
                return True
        mgba.press_buttons([direction])
        time.sleep(0.4)
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

# Ensure any active menus are dismissed
mgba.press_buttons(["B"])
time.sleep(0.4)

pos = mgba.get_coordinates()
print("Starting walk to Pokémon Mansion from position:", pos)

# Walk Left on Row 5 to Column 6
if pos["y"] == 5 and pos["x"] > 6:
    print("Walking Left to Column 6...")
    steps_left = []
    for x in range(pos["x"] - 1, 5, -1):
        steps_left.append(("Left", {"x": x, "y": 5}))
    if not run_steps(steps_left):
        print("Failed to reach Column 6")
        exit(1)
    pos = mgba.get_coordinates()

# Walk Up Column 6 to Row 3
if pos == {"x": 6, "y": 5}:
    print("Walking Up to Row 3...")
    if not run_steps([
        ("Up", {"x": 6, "y": 4}),
        ("Up", {"x": 6, "y": 3}),
    ]):
        print("Failed to reach (6, 3)")
        exit(1)
    pos = mgba.get_coordinates()

# Enter the Mansion door at (6, 3)
if pos == {"x": 6, "y": 3}:
    print("Entering the Pokémon Mansion...")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)
    pos = mgba.get_coordinates()
    print("Position inside Mansion:", pos)
