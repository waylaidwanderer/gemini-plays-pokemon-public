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

# Ensure any active menus are dismissed
mgba.press_buttons(["B"])
time.sleep(0.4)

pos = mgba.get_coordinates()
print("Starting exploration from position:", pos)

# Walk back to (1, 13)
if pos == {"x": 5, "y": 8}:
    print("Walking back to (1, 13)...")
    run_steps([
        ("Down", {"x": 5, "y": 9}),
        ("Down", {"x": 5, "y": 10}),
        ("Down", {"x": 5, "y": 11}),
        ("Down", {"x": 5, "y": 12}),
        ("Down", {"x": 5, "y": 13}),
        ("Left", {"x": 4, "y": 13}),
        ("Left", {"x": 3, "y": 13}),
        ("Left", {"x": 2, "y": 13}),
        ("Left", {"x": 1, "y": 13}),
    ])
    pos = mgba.get_coordinates()

# Let's try to walk UP Column 1 in State B first (checking if Row 9 gate was indeed open or closed)
if pos == {"x": 1, "y": 13}:
    print("Trying to walk UP Column 1 in State B...")
    run_steps([
        ("Up", {"x": 1, "y": 12}),
        ("Up", {"x": 1, "y": 11}),
    ])
    success = walk_step("Up", {"x": 1, "y": 10}, retries=2)
    if success:
        success = walk_step("Up", {"x": 1, "y": 9}, retries=2)
        if success:
            print("!!! Column 1 is OPEN in State B! We made it to (1, 9)")
            exit(0)
        else:
            print("Blocked at (1, 10) in State B")
            walk_step("Down", {"x": 1, "y": 11})
            walk_step("Down", {"x": 1, "y": 12})
            walk_step("Down", {"x": 1, "y": 13})
    pos = mgba.get_coordinates()

# Toggle back to State A
if pos == {"x": 1, "y": 13}:
    print("Toggling switch back to State A...")
    walk_step("Up", {"x": 1, "y": 12})
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    print("Toggled back to State A.")
    
    # Try to walk UP Column 1 in State A
    print("Trying to walk UP Column 1 in State A...")
    walk_step("Up", {"x": 1, "y": 11})
    success = walk_step("Up", {"x": 1, "y": 10}, retries=2)
    if success:
        success = walk_step("Up", {"x": 1, "y": 9}, retries=2)
        if success:
            print("!!! Column 1 is OPEN in State A!")
            exit(0)
        else:
            print("Blocked at (1, 10) in State A")

