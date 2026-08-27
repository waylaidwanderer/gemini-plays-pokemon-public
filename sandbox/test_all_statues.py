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
    mgba.press_buttons(["B"])
    time.sleep(0.3)
    return False

def walk_step(direction, expected_coords, retries=15):
    for i in range(retries):
        handle_any_menu_or_battle()
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

print("Running test_all_statues.py...")
pos = mgba.get_coordinates()
print("Starting from:", pos)

# We are at (1, 15).
# Walk to (2, 16)
if pos == {"x": 1, "y": 15}:
    if not run_steps([
        ("Down", {"x": 1, "y": 16}),
        ("Right", {"x": 2, "y": 16}),
    ]):
        print("Failed to reach (2, 16)")
        exit(1)
    pos = mgba.get_coordinates()

# Test (2, 16) facing RIGHT towards (3, 16)
if pos == {"x": 2, "y": 16}:
    print("Testing (2, 16) facing RIGHT...")
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    # Check if we moved
    pos_test = mgba.get_coordinates()
    if pos_test != {"x": 2, "y": 16}:
        print("We walked onto (3, 16)! Walking back...")
        walk_step("Left", {"x": 2, "y": 16})
    else:
        # We are facing RIGHT
        mgba.press_buttons(["A"])
        time.sleep(0.8)
        if is_dialogue_open():
            print("SUCCESS! Switch dialogue opened at (2, 16) facing RIGHT!")
            # Toggle it to State B
            mgba.press_buttons(["A"]) # YES
            time.sleep(1.0)
            mgba.press_buttons(["A"]) # Result
            time.sleep(1.0)
            mgba.press_buttons(["A"]) # Dismiss
            time.sleep(1.0)
            exit(0)
        else:
            mgba.press_buttons(["B"])
            time.sleep(0.3)

# Walk to (2, 14)
if pos == {"x": 2, "y": 16}:
    if not run_steps([
        ("Up", {"x": 2, "y": 15}),
        ("Up", {"x": 2, "y": 14}),
    ]):
        print("Failed to reach (2, 14)")
        exit(1)
    pos = mgba.get_coordinates()

# Test (2, 14) facing RIGHT towards (3, 14)
if pos == {"x": 2, "y": 14}:
    print("Testing (2, 14) facing RIGHT...")
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    pos_test = mgba.get_coordinates()
    if pos_test != {"x": 2, "y": 14}:
        print("We walked onto (3, 14)! Walking back...")
        walk_step("Left", {"x": 2, "y": 14})
    else:
        mgba.press_buttons(["A"])
        time.sleep(0.8)
        if is_dialogue_open():
            print("SUCCESS! Switch dialogue opened at (2, 14) facing RIGHT!")
            # Toggle it to State B
            mgba.press_buttons(["A"]) # YES
            time.sleep(1.0)
            mgba.press_buttons(["A"]) # Result
            time.sleep(1.0)
            mgba.press_buttons(["A"]) # Dismiss
            time.sleep(1.0)
            exit(0)
        else:
            mgba.press_buttons(["B"])
            time.sleep(0.3)

# Walk to (2, 12)
if pos == {"x": 2, "y": 14}:
    if not run_steps([
        ("Up", {"x": 2, "y": 13}),
        ("Up", {"x": 2, "y": 12}),
    ]):
        print("Failed to reach (2, 12)")
        exit(1)
    pos = mgba.get_coordinates()

# Test (2, 12) facing RIGHT towards (3, 12)
if pos == {"x": 2, "y": 12}:
    print("Testing (2, 12) facing RIGHT...")
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    pos_test = mgba.get_coordinates()
    if pos_test != {"x": 2, "y": 12}:
        print("We walked onto (3, 12)! Walking back...")
        walk_step("Left", {"x": 2, "y": 12})
    else:
        mgba.press_buttons(["A"])
        time.sleep(0.8)
        if is_dialogue_open():
            print("SUCCESS! Switch dialogue opened at (2, 12) facing RIGHT!")
            # Toggle it to State B
            mgba.press_buttons(["A"]) # YES
            time.sleep(1.0)
            mgba.press_buttons(["A"]) # Result
            time.sleep(1.0)
            mgba.press_buttons(["A"]) # Dismiss
            time.sleep(1.0)
            exit(0)
        else:
            mgba.press_buttons(["B"])
            time.sleep(0.3)

print("All tested statues failed.")
exit(1)
