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
        
        # Check if still in battle
        scr_file2 = mgba.take_screenshot()
        img2 = Image.open(scr_file2)
        img_std2 = img2.resize((160, 144), Image.Resampling.NEAREST)
        black_or_white2 = 0
        for y in range(115, 140):
            for x in range(10, 150):
                r, g, b = img_std2.getpixel((x, y))
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

# Ensure any previous menus are dismissed
mgba.press_buttons(["B"])
time.sleep(0.5)

pos = mgba.get_coordinates()
print("Starting toggle script at position:", pos)

# 1. Walk down to (1, 13)
if pos == {"x": 1, "y": 10}:
    if not run_steps([
        ("Down", {"x": 1, "y": 11}),
        # Note: (1, 12) is the statue itself, but wait!
        # In solve_from_current_correct_switch.py, we walked down Column 2 to (2, 13) and then Left to (1, 13).
        # Let's do that to avoid the statue at (1, 12)!
        ("Right", {"x": 2, "y": 11}),
        ("Down", {"x": 2, "y": 12}),
        ("Down", {"x": 2, "y": 13}),
        ("Left", {"x": 1, "y": 13}),
    ]):
        print("Failed to reach (1, 13)")
        exit(1)
    pos = mgba.get_coordinates()

# 2. Stand at (1, 13) facing UP and press A to open switch dialog
if pos == {"x": 1, "y": 13}:
    print("Aligning UP towards the switch at (1, 12)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    print("Interacting with the Mewtwo statue switch...")
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    
    # Take screenshot of the dialogue box
    scr = mgba.take_screenshot()
    img = Image.open(scr).resize((160, 144), Image.Resampling.NEAREST)
    cropped_dialogue = img.crop((0, 104, 160, 144))
    
    black_pixels = 0
    for y in range(cropped_dialogue.height):
        for x in range(cropped_dialogue.width):
            r, g, b = cropped_dialogue.getpixel((x, y))
            if r < 50 and g < 50 and b < 50:
                black_pixels += 1
    print(f"Black pixels in dialogue area: {black_pixels}")
    
    if black_pixels > 200:
        print("Dialogue box opened successfully! Selecting YES to toggle switch...")
        # Advance "A secret switch!"
        mgba.press_buttons(["A"])
        time.sleep(1.5)
        # Select YES
        mgba.press_buttons(["A"])
        time.sleep(1.5)
        # Dismiss "Pressed it!"
        mgba.press_buttons(["A"])
        time.sleep(1.5)
        print("Switch successfully toggled to State B!")
    else:
        print("Failed to open dialogue. Wrong position or facing direction?")
        # Let's try to take a full screenshot to debug
        img.save("mansion_switch_dialogue_open.png")
        print("Saved full screenshot to mansion_switch_dialogue_open.png")
        exit(1)

# 3. Verify that we can now walk UP Column 2 Row 9!
    pos = mgba.get_coordinates()
    print("Walking UP Column 2 to Row 6...")
    steps = [
        ("Right", {"x": 2, "y": 13}),
        ("Up", {"x": 2, "y": 12}),
        ("Up", {"x": 2, "y": 11}),
        ("Up", {"x": 2, "y": 10}),
        ("Up", {"x": 2, "y": 9}),  # This is the gate!
        ("Up", {"x": 2, "y": 8}),
        ("Up", {"x": 2, "y": 7}),
        ("Up", {"x": 2, "y": 6}),
    ]
    if not run_steps(steps):
        print("Failed to pass through the Column 2 Row 9 gate")
        exit(1)
    print("Successfully passed through the gate and reached (2, 6)!")
