import mgba
import time
from PIL import Image

def is_dialogue_open():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file).resize((160, 144), Image.Resampling.NEAREST)
    cropped = img.crop((0, 104, 160, 144))
    
    target_color = (57, 57, 57)
    found_target = 0
    for y in range(cropped.height):
        for x in range(cropped.width):
            r, g, b = cropped.getpixel((x, y))
            if abs(r - 57) < 10 and abs(g - 57) < 10 and abs(b - 57) < 10:
                found_target += 1
                
    bg_color = (247, 231, 214)
    found_bg = 0
    for y in range(cropped.height):
        for x in range(cropped.width):
            r, g, b = cropped.getpixel((x, y))
            if abs(r - 247) < 15 and abs(g - 231) < 15 and abs(b - 214) < 15:
                found_bg += 1
                
    print(f"Check: found_border={found_target}, found_bg={found_bg}")
    return found_target > 80 and found_bg > 500

def walk_step(direction, expected_coords):
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos = mgba.get_coordinates()
    if pos == expected_coords:
        return True
    return False

# Currently we are at (1, 10)
pos = mgba.get_coordinates()
print("Starting position:", pos)

if pos == {"x": 1, "y": 10}:
    walk_step("Down", {"x": 1, "y": 11})
    walk_step("Down", {"x": 1, "y": 12})
    walk_step("Down", {"x": 1, "y": 13})
    pos = mgba.get_coordinates()

if pos == {"x": 1, "y": 13}:
    # Test (1, 13) directions
    for d in ["Up", "Left", "Down", "Right"]:
        print(f"Testing at (1, 13) facing {d}...")
        mgba.press_buttons([d])
        time.sleep(0.3)
        mgba.press_buttons(["A"])
        time.sleep(0.8)
        if is_dialogue_open():
            print(f"!!! SUCCESS !!! Switch found at (1, 13) facing {d}!")
            mgba.press_buttons(["B"])
            time.sleep(0.4)
        else:
            mgba.press_buttons(["B"])
            time.sleep(0.2)
            
    # Walk to (1, 12)
    walk_step("Up", {"x": 1, "y": 12})
    pos = mgba.get_coordinates()

if pos == {"x": 1, "y": 12}:
    # Test (1, 12) directions
    for d in ["Up", "Left", "Down", "Right"]:
        print(f"Testing at (1, 12) facing {d}...")
        mgba.press_buttons([d])
        time.sleep(0.3)
        mgba.press_buttons(["A"])
        time.sleep(0.8)
        if is_dialogue_open():
            print(f"!!! SUCCESS !!! Switch found at (1, 12) facing {d}!")
            mgba.press_buttons(["B"])
            time.sleep(0.4)
        else:
            mgba.press_buttons(["B"])
            time.sleep(0.2)

