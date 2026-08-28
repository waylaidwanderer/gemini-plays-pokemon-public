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

print("Initial position:", get_pos())

# Step UP onto the stairs at (7, 10) on 2F West to warp UP to 3F West
print("Stepping UP to warp...")
mgba.press_buttons(["Up"])
time.sleep(2.0)

pos = get_pos()
print("Position on 3F West:", pos)

if pos == (7, 11) or pos == (7, 10):
    if pos == (7, 10):
        walk_step("Down", (7, 11))
        
    print("Attempting direct path to switch along Row 11...")
    path_row_11 = [
        ("Left", (6, 11)),
        ("Left", (5, 11)),
        ("Left", (4, 11)),
        ("Left", (3, 11)),
        ("Down", (3, 12)),
        ("Left", (2, 12)),
    ]
    if run_steps(path_row_11):
        print("Successfully reached switch at (2, 12) via Row 11!")
    else:
        print("Blocked on Row 11. Trying alternative bypass via Row 13...")
        # Since we got blocked, let's find current position
        pos = get_pos()
        print("Blocked at position:", pos)
        if pos == (5, 11):
            steps_bypass = [
                ("Down", (5, 12)),
                ("Down", (5, 13)),
                ("Left", (4, 13)),
                ("Left", (3, 13)),
                ("Left", (2, 13)),
                ("Up", (2, 12)),
            ]
            if not run_steps(steps_bypass):
                print("Bypass path failed!")
                exit(1)
        else:
            print("Unknown blocked position. Aborting.")
            exit(1)

# Now toggle switch at (2, 12)
pos = get_pos()
if pos == (2, 12):
    print("Toggling Mewtwo switch at (2, 11)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # Toggle dialogue (4 A presses)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    print("Switch toggled to State B!")
    mgba.take_screenshot()

print("Warp and toggle script finished!")
