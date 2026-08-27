import mgba
import time
from PIL import Image

def is_dialogue_open():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file).resize((160, 144), Image.Resampling.NEAREST)
    cropped = img.crop((0, 104, 160, 144))
    
    white_cream_pixels = 0
    for y in range(cropped.height):
        for x in range(cropped.width):
            r, g, b = cropped.getpixel((x, y))[:3]
            if r > 200 and g > 200 and b > 200:
                white_cream_pixels += 1
    return white_cream_pixels > 3000

def handle_any_menu_or_battle():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file)
    img_std = img.resize((160, 144), Image.Resampling.NEAREST)
    
    # We first press B to exit any move sub-menu we might be in
    mgba.press_buttons(["B"])
    time.sleep(0.3)
    
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
        print(f"Menu/Dialogue detected! (B/W: {percentage*100:.2f}%)")
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        
        # Check if still in battle
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
            print("Still in battle. Running...")
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

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

pos = mgba.get_coordinates()
print("Starting exhaustive switch search from:", pos)

# Let's align to (1, 13) which is a very central and safe coordinate
if pos != {"x": 1, "y": 13}:
    if pos["y"] == 11:
        walk_step("Down", {"x": pos["x"], "y": 12})
    elif pos["y"] == 12:
        walk_step("Down", {"x": pos["x"], "y": 13})
    elif pos["y"] == 10:
        walk_step("Down", {"x": pos["x"], "y": 11})
        walk_step("Down", {"x": pos["x"], "y": 12})
        walk_step("Down", {"x": pos["x"], "y": 13})
    pos = mgba.get_coordinates()
    if pos["x"] == 2 and pos["y"] == 13:
        walk_step("Left", {"x": 1, "y": 13})
    pos = mgba.get_coordinates()

# We are at (1, 13).
# We want to test every tile in this room: Column 1 and Column 2, Rows 11 to 15.
# Let's do a sequence of coordinate nodes we want to visit:
# (x, y, facing_dir, target_desc)
tests = [
    (1, 13, "Left", "Statue at (0, 13)"),
    (1, 13, "Up", "Statue at (1, 12)"),
    (1, 13, "Right", "Statue at (2, 13)"),
    (2, 13, "Right", "Statue at (3, 13)"),
    (2, 13, "Up", "Statue at (2, 12)"),
    (2, 12, "Up", "Statue at (2, 11)"),
    (2, 12, "Right", "Statue at (3, 12)"),
    (1, 12, "Left", "Statue at (0, 12)"),
    (1, 12, "Up", "Statue at (1, 11)"),
    (1, 11, "Left", "Statue at (0, 11)"),
    (1, 11, "Up", "Statue at (1, 10)"),
    (1, 11, "Right", "Statue at (2, 11)"),
    (2, 11, "Right", "Statue at (3, 11)"),
    (2, 11, "Up", "Statue at (2, 10)"),
]

# We will navigate between the test coordinate nodes dynamically!
for tx, ty, tdir, desc in tests:
    # Walk to (tx, ty)
    cur_pos = mgba.get_coordinates()
    while cur_pos != {"x": tx, "y": ty}:
        dx = tx - cur_pos["x"]
        dy = ty - cur_pos["y"]
        if dx > 0:
            walk_step("Right", {"x": cur_pos["x"] + 1, "y": cur_pos["y"]})
        elif dx < 0:
            walk_step("Left", {"x": cur_pos["x"] - 1, "y": cur_pos["y"]})
        elif dy > 0:
            walk_step("Down", {"x": cur_pos["x"], "y": cur_pos["y"] + 1})
        elif dy < 0:
            walk_step("Up", {"x": cur_pos["x"], "y": cur_pos["y"] - 1})
        cur_pos = mgba.get_coordinates()
        
    print(f"Testing interaction from {cur_pos} facing {tdir} towards {desc}...")
    
    # Face the tdir direction
    mgba.press_buttons([tdir])
    time.sleep(0.4)
    
    # Press A
    mgba.press_buttons(["A"])
    time.sleep(0.8)
    
    if is_dialogue_open():
        print(f"SUCCESS! Dialogue opened from {cur_pos} facing {tdir}!")
        # Let's toggle it!
        mgba.press_buttons(["A"]) # YES
        time.sleep(1.2)
        mgba.press_buttons(["A"]) # Result
        time.sleep(1.2)
        mgba.press_buttons(["A"]) # Dismiss
        time.sleep(1.0)
        print("Switch successfully toggled!")
        exit(0)
    else:
        # Cancel any potential menu desync
        mgba.press_buttons(["B"])
        time.sleep(0.3)

print("Exhaustive search finished. No switch was found.")
