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

def run_steps(steps):
    for d, c in steps:
        if not walk_step(d, c):
            return False
    return True

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

pos = mgba.get_coordinates()
print("Starting fast switch find from:", pos)

if pos == {"x": 5, "y": 10}:
    print("Walking down to (5, 13)...")
    if not run_steps([
        ("Down", {"x": 5, "y": 11}),
        ("Down", {"x": 5, "y": 12}),
        ("Down", {"x": 5, "y": 13}),
    ]):
        print("Failed to walk to (5, 13)")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 5, "y": 13}:
    print("Walking left to (2, 13)...")
    if not run_steps([
        ("Left", {"x": 4, "y": 13}),
        ("Left", {"x": 3, "y": 13}),
        ("Left", {"x": 2, "y": 13}),
    ]):
        print("Failed to walk to (2, 13)")
        exit(1)
    pos = mgba.get_coordinates()

# Now we are at (2, 13). Let's test Up from (2, 13).
if pos == {"x": 2, "y": 13}:
    print("Testing UP from (2, 13)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.45)
    test_pos = mgba.get_coordinates()
    
    if test_pos == {"x": 2, "y": 12}:
        print("We walked onto (2, 12). So (2, 12) is not solid.")
        # Walk back down to (2, 13)
        walk_step("Down", {"x": 2, "y": 13})
    else:
        print("Blocked! (2, 12) is SOLID! Trying to interact...")
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        if is_dialogue_open():
            print("Dialogue open! Toggling switch...")
            mgba.press_buttons(["A"]) # YES
            time.sleep(1.2)
            mgba.press_buttons(["A"]) # Result
            time.sleep(1.2)
            mgba.press_buttons(["A"]) # Dismiss
            time.sleep(1.0)
            print("SUCCESS! Switch toggled!")
            exit(0)
            
    pos = mgba.get_coordinates()

# Walk left to (1, 13)
if pos == {"x": 2, "y": 13}:
    if not walk_step("Left", {"x": 1, "y": 13}):
        print("Failed to reach (1, 13)")
        exit(1)
    pos = mgba.get_coordinates()

# Test Up from (1, 13)
if pos == {"x": 1, "y": 13}:
    print("Testing UP from (1, 13)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.45)
    test_pos = mgba.get_coordinates()
    
    if test_pos == {"x": 1, "y": 12}:
        print("We walked onto (1, 12). So (1, 12) is not solid.")
    else:
        print("Blocked! (1, 12) is SOLID! Trying to interact...")
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        if is_dialogue_open():
            print("Dialogue open! Toggling switch...")
            mgba.press_buttons(["A"]) # YES
            time.sleep(1.2)
            mgba.press_buttons(["A"]) # Result
            time.sleep(1.2)
            mgba.press_buttons(["A"]) # Dismiss
            time.sleep(1.0)
            print("SUCCESS! Switch toggled!")
            exit(0)

print("Fast search finished. Switch not found yet.")
