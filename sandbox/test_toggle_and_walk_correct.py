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

print("Running test_toggle_and_walk_correct.py...")
pos = mgba.get_coordinates()
print("Starting from:", pos)

if pos == {"x": 1, "y": 11}:
    # Face UP
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    # Toggle switch
    print("Toggling switch at (1, 10) facing UP...")
    mgba.press_buttons(["A"]) # Step 1: secret switch
    time.sleep(0.8)
    mgba.press_buttons(["A"]) # Step 2: press it?
    time.sleep(0.8)
    mgba.press_buttons(["A"]) # Step 3: YES
    time.sleep(0.8)
    mgba.press_buttons(["A"]) # Step 4: dismiss
    time.sleep(1.0)

    pos = mgba.get_coordinates()

# Now walk to Column 2 and try walking UP to Row 6
if pos == {"x": 1, "y": 11}:
    print("Walking to Column 2 Row 6...")
    steps_up = [
        ("Right", {"x": 2, "y": 11}),
        ("Up", {"x": 2, "y": 10}),
    ]
    for y in range(9, 5, -1):
        steps_up.append(("Up", {"x": 2, "y": y}))
        
    if run_steps(steps_up):
        print("SUCCESS! Gate is open and we reached Row 6!")
        exit(0)
    else:
        print("Failed to reach Row 6. Gate might still be closed.")
        exit(1)
