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
print("Starting exhaustive switch search from:", pos)

# We want to test the following positions:
# 1. (1, 13) facing UP (facing 1, 12)
# 2. (2, 13) facing UP (facing 2, 12)
# 3. (2, 12) facing UP (facing 2, 11)
# 4. (1, 12) facing UP (facing 1, 11)
# 5. (1, 11) facing UP (facing 1, 10)
# 6. (2, 11) facing UP (facing 2, 10)
# Let's also test facing RIGHT from (1, 11) towards (2, 11) and (1, 12) towards (2, 12)

# Make sure we are at (1, 13)
if pos != {"x": 1, "y": 13}:
    # Walk to (1, 13) via Column 2 to avoid blocking
    # Current pos can be (2, 12)
    if pos["y"] == 11:
        walk_step("Down", {"x": pos["x"], "y": 12})
        pos = mgba.get_coordinates()
    if pos["y"] == 12:
        walk_step("Down", {"x": pos["x"], "y": 13})
        pos = mgba.get_coordinates()
    if pos["x"] == 2 and pos["y"] == 13:
        walk_step("Left", {"x": 1, "y": 13})
        pos = mgba.get_coordinates()

# Now we are at (1, 13)
tests = [
    # (x, y, facing_dir, target_desc)
    (1, 13, "Up", "UP towards (1, 12)"),
    (2, 13, "Up", "UP towards (2, 12)"),
    (2, 12, "Up", "UP towards (2, 11)"),
    (1, 12, "Up", "UP towards (1, 11)"),
    (1, 11, "Up", "UP towards (1, 10)"),
    (2, 11, "Up", "UP towards (2, 10)"),
    (1, 11, "Right", "RIGHT towards (2, 11)"),
    (1, 12, "Right", "RIGHT towards (2, 12)"),
    (1, 13, "Right", "RIGHT towards (2, 13)"),
    (2, 11, "Left", "LEFT towards (1, 11)"),
    (2, 12, "Left", "LEFT towards (1, 12)"),
    (2, 13, "Left", "LEFT towards (1, 13)"),
]

# Simple path to visit:
# Start at (1, 13) -> (2, 13) -> (2, 12) -> (1, 12) -> (1, 11) -> (2, 11)
visit_coords = [
    {"x": 1, "y": 13},
    {"x": 2, "y": 13},
    {"x": 2, "y": 12},
    {"x": 1, "y": 12},
    {"x": 1, "y": 11},
    {"x": 2, "y": 11},
]

for target_coord in visit_coords:
    # Walk to target_coord
    cur_pos = mgba.get_coordinates()
    if cur_pos != target_coord:
        # We can do simple orthogonal movements
        dx = target_coord["x"] - cur_pos["x"]
        dy = target_coord["y"] - cur_pos["y"]
        if dx > 0:
            walk_step("Right", {"x": cur_pos["x"] + 1, "y": cur_pos["y"]})
        elif dx < 0:
            walk_step("Left", {"x": cur_pos["x"] - 1, "y": cur_pos["y"]})
        elif dy > 0:
            walk_step("Down", {"x": cur_pos["x"], "y": cur_pos["y"] + 1})
        elif dy < 0:
            walk_step("Up", {"x": cur_pos["x"], "y": cur_pos["y"] - 1})
            
    cur_pos = mgba.get_coordinates()
    if cur_pos == target_coord:
        # Run all tests for this coordinate
        for tx, ty, tdir, desc in tests:
            if tx == cur_pos["x"] and ty == cur_pos["y"]:
                print(f"Testing {desc} from {cur_pos}...")
                mgba.press_buttons([tdir])
                time.sleep(0.4)
                mgba.press_buttons(["A"])
                time.sleep(1.0)
                if is_dialogue_open():
                    print(f"SUCCESS! Dialogue opened from {cur_pos} facing {tdir}!")
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
