import mgba
import time
from PIL import Image

def is_dialogue_or_battle_open():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file).resize((160, 144), Image.Resampling.NEAREST)
    cropped = img.crop((0, 104, 160, 144))
    
    # Check for white/cream pixels in dialogue area
    white_cream_pixels = 0
    for y in range(cropped.height):
        for x in range(cropped.width):
            r, g, b = cropped.getpixel((x, y))
            if r > 200 and g > 200 and b > 200:
                white_cream_pixels += 1
    return white_cream_pixels > 2500

def walk_step(direction, expected_coords, retries=10):
    for i in range(retries):
        if is_dialogue_or_battle_open():
            mgba.press_buttons(["B"])
            time.sleep(0.4)
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

# Dismiss active menus
mgba.press_buttons(["B"])
time.sleep(0.4)

pos = mgba.get_coordinates()
print("Starting position:", pos)

# From (2, 13): Left to (1, 13) -> Up to (1, 12) -> Up to (1, 11) -> Right to (2, 11)
steps = [
    ("Left", {"x": 1, "y": 13}),
    ("Up", {"x": 1, "y": 12}),
    ("Up", {"x": 1, "y": 11}),
    ("Right", {"x": 2, "y": 11}),
]

if run_steps(steps):
    print("At (2, 11) successfully! Facing UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    print("Interacting with the switch...")
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    
    if is_dialogue_or_battle_open():
        print("Switch dialogue open! Toggling to State B...")
        mgba.press_buttons(["A"]) # Advance "A secret switch!"
        time.sleep(1.2)
        mgba.press_buttons(["A"]) # Select YES
        time.sleep(1.2)
        mgba.press_buttons(["A"]) # Dismiss "Pressed it!"
        time.sleep(1.5)
        print("Mansion state successfully toggled to State B!")
    else:
        print("Failed to open switch dialogue.")
else:
    print("Failed to reach (2, 11)")

print("Final position:", mgba.get_coordinates())
