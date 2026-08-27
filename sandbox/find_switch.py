import mgba
import time
from PIL import Image

def is_dialogue_open():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file).resize((160, 144), Image.Resampling.NEAREST)
    cropped = img.crop((0, 104, 160, 144))
    
    # Check for GBC dialogue background (high white/cream pixel count)
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

# We will test interactions from various positions around (2, 12).
# Let's list the candidate positions and the directions to face.
candidates = [
    # (x, y), direction_to_face, step_to_reach_from_current
    # Current is (2, 11).
    ({"x": 2, "y": 12}, "Up", [("Down", {"x": 2, "y": 12})]),
    ({"x": 2, "y": 12}, "Left", [("Down", {"x": 2, "y": 12})]),
    ({"x": 1, "y": 12}, "Up", [("Down", {"x": 2, "y": 12}), ("Left", {"x": 1, "y": 12})]),
    ({"x": 1, "y": 12}, "Right", [("Down", {"x": 2, "y": 12}), ("Left", {"x": 1, "y": 12})]),
    ({"x": 1, "y": 11}, "Right", [("Left", {"x": 1, "y": 11})]),
    ({"x": 1, "y": 11}, "Down", [("Left", {"x": 1, "y": 11})]),
    ({"x": 1, "y": 13}, "Up", [("Down", {"x": 2, "y": 12}), ("Left", {"x": 1, "y": 12}), ("Down", {"x": 1, "y": 13})]),
    ({"x": 1, "y": 13}, "Right", [("Down", {"x": 2, "y": 12}), ("Left", {"x": 1, "y": 12}), ("Down", {"x": 1, "y": 13})]),
    ({"x": 2, "y": 13}, "Up", [("Down", {"x": 2, "y": 12}), ("Down", {"x": 2, "y": 13})]),
    ({"x": 2, "y": 13}, "Left", [("Down", {"x": 2, "y": 12}), ("Down", {"x": 2, "y": 13})]),
]

found = False
for coord, direction, path in candidates:
    # Walk back to current starting position (2, 11) to reset pathing
    current_pos = mgba.get_coordinates()
    if current_pos != {"x": 2, "y": 11}:
        print(f"Returning to (2, 11) from {current_pos}...")
        # Since we are nearby, we can find a simple path back to (2, 11)
        if current_pos == {"x": 2, "y": 12}:
            walk_step("Up", {"x": 2, "y": 11})
        elif current_pos == {"x": 1, "y": 12}:
            run_steps([("Right", {"x": 2, "y": 12}), ("Up", {"x": 2, "y": 11})])
        elif current_pos == {"x": 1, "y": 11}:
            walk_step("Right", {"x": 2, "y": 11})
        elif current_pos == {"x": 1, "y": 13}:
            run_steps([("Up", {"x": 1, "y": 12}), ("Right", {"x": 2, "y": 12}), ("Up", {"x": 2, "y": 11})])
        elif current_pos == {"x": 2, "y": 13}:
            run_steps([("Up", {"x": 2, "y": 12}), ("Up", {"x": 2, "y": 11})])
        else:
            print("Unknown position, using general return path")
            # Walk up/right to find (2, 11)
            mgba.press_buttons(["Up", "sleep 100", "Right"])
            time.sleep(0.5)
            
    # Now path to the target coordinate
    print(f"\n--- Testing position {coord} facing {direction} ---")
    if not run_steps(path):
        print(f"Failed to path to {coord}")
        continue
        
    # Face the specified direction
    # We turn by pressing the direction button. BUT wait, if we press the direction, we might walk!
    # To prevent walking, we can check if the destination in that direction is solid.
    # If the destination is solid, pressing that direction will just turn us without walking.
    # Let's try pressing the direction.
    mgba.press_buttons([direction])
    time.sleep(0.45)
    
    # Check if we moved. If we moved, then it wasn't solid!
    test_pos = mgba.get_coordinates()
    if test_pos != coord:
        print(f"  We moved to {test_pos}! That means {direction} was not solid. Skipping...")
        continue
        
    # Press A to check dialogue
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    if is_dialogue_open():
        print(f"  SUCCESS!!! Switch dialogue is OPEN from {coord} facing {direction}!")
        # Let's toggle it!
        mgba.press_buttons(["A"]) # Press YES
        time.sleep(1.2)
        mgba.press_buttons(["A"]) # Result text
        time.sleep(1.2)
        mgba.press_buttons(["A"]) # Dismiss
        time.sleep(1.0)
        found = True
        break
    else:
        print(f"  No dialogue from {coord} facing {direction}.")
        mgba.press_buttons(["B"])
        time.sleep(0.3)

if found:
    print("Switch successfully found and toggled!")
else:
    print("Could not find any switch statue in the tested positions.")
