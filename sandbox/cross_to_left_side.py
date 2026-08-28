import mgba
import time
from PIL import Image

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

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
        # Try pressing B first to dismiss text
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
            # Try pressing Down, Right, A to select RUN
            mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
            time.sleep(1.5)
            # Dismiss any "Escaped" or "Can't escape" text
            for _ in range(5):
                mgba.press_buttons(["B"])
                time.sleep(0.3)
        return True
    return False

def walk_step(direction, expected_coords, retries=15):
    for i in range(retries):
        if handle_any_menu_or_battle():
            pos = get_pos()
            if pos == expected_coords:
                return True
        mgba.press_buttons([direction])
        time.sleep(0.45)
        pos = get_pos()
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

print("Start position:", get_pos())

# 1. Walk from (1, 10) to (2, 12)
steps_to_switch = [
    ("Down", (1, 11)),
    ("Down", (1, 12)),
    ("Right", (2, 12)),
]
print("Walking to switch at (2, 12)...")
if not run_steps(steps_to_switch):
    print("Failed to reach (2, 12)")
    exit(1)

# 2. Turn UP to face switch at (2, 11)
print("Turning UP...")
mgba.press_buttons(["Up"])
time.sleep(0.5)

# 3. Toggle switch to State B (Exactly 5 A presses with delays to fully complete dialogue!)
print("Toggling Mewtwo switch...")
for i in range(5):
    mgba.press_buttons(["A"])
    time.sleep(1.0)
print("Switch toggle complete!")

# 4. Walk to (1, 12)
if not walk_step("Left", (1, 12)):
    print("Failed to step Left to (1, 12)")
    exit(1)

# 5. Walk UP Column 1 to Row 6
steps_up_col_1 = [
    ("Up", (1, 11)),
    ("Up", (1, 10)),
    ("Up", (1, 9)),
    ("Up", (1, 8)),
    ("Up", (1, 7)),
    ("Up", (1, 6)),
]
print("Walking UP Column 1...")
if not run_steps(steps_up_col_1):
    print("Failed to walk UP Column 1 (switch might not have toggled or still blocked!)")
    exit(1)

# 6. Walk RIGHT along Row 6 to Column 20
steps_row_6 = []
for x in range(2, 21):
    steps_row_6.append(("Right", (x, 6)))
print("Walking RIGHT along Row 6 to Column 20...")
if not run_steps(steps_row_6):
    print("Failed walking RIGHT along Row 6")
    exit(1)

print("SUCCESS: Fully crossed 3F West to Column 20 in State B!")
mgba.take_screenshot()
