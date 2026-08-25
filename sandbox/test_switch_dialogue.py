import mgba
import time
from PIL import Image

def handle_any_menu_or_battle():
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
        print(f"Menu/Battle detected! (B/W percentage: {percentage*100:.2f}%)")
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
            return True
        time.sleep(0.3)
    return False

# Currently at (5, 4) on 2F West
# Walk to (2, 12) on 2F West
print("Walking to (2, 12)...")
steps = [
    ("Left", {"x": 4, "y": 4}),
    ("Left", {"x": 3, "y": 4}),
    ("Left", {"x": 2, "y": 4}),
    ("Down", {"x": 2, "y": 5}),
    ("Down", {"x": 2, "y": 6}),
    ("Down", {"x": 2, "y": 7}),
    ("Down", {"x": 2, "y": 8}),
    ("Down", {"x": 2, "y": 9}),
    ("Down", {"x": 2, "y": 10}),
    ("Down", {"x": 2, "y": 11}),
    ("Down", {"x": 2, "y": 12}),
]
for d, c in steps:
    walk_step(d, c)

# Stand at (2, 12) facing UP and press A
mgba.press_buttons(["Up"])
time.sleep(0.5)
mgba.press_buttons(["A"])
time.sleep(1.0)
scr = mgba.take_screenshot()
print(f"Switch dialogue opened! Screenshot: {scr}")
