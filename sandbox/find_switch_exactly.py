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

def check_dialogue_open():
    scr = mgba.take_screenshot()
    img = Image.open(scr).resize((160, 144), Image.Resampling.NEAREST)
    cropped_dialogue = img.crop((0, 104, 160, 144))
    
    black_pixels = 0
    for y in range(cropped_dialogue.height):
        for x in range(cropped_dialogue.width):
            r, g, b = cropped_dialogue.getpixel((x, y))
            if r < 50 and g < 50 and b < 50:
                black_pixels += 1
    return black_pixels > 200

def test_interaction(dir_to_face):
    # Turn to face direction
    mgba.press_buttons([dir_to_face])
    time.sleep(0.3)
    # Check if a battle started immediately on turn
    if handle_any_menu_or_battle():
        return False
        
    # Press A
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    
    if check_dialogue_open():
        print(f"SUCCESS! Dialogue opened at {mgba.get_coordinates()} facing {dir_to_face}!")
        # Dismiss the dialogue safely
        for _ in range(4):
            mgba.press_buttons(["B"])
            time.sleep(0.4)
        return True
    return False

def walk_to_tile(direction, expected_coords):
    for i in range(10):
        if handle_any_menu_or_battle():
            pos = mgba.get_coordinates()
            if pos == expected_coords:
                return True
        mgba.press_buttons([direction])
        time.sleep(0.45)
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            return True
        time.sleep(0.2)
    return False

# Ensure active
mgba.press_buttons(["B"])
time.sleep(0.3)

# Let's map out and test positions
pos = mgba.get_coordinates()
print("Starting search script at position:", pos)

# List of positions to test: (x, y) and the direction of movement to get there
test_route = [
    # We start at (2, 11)
    {"coords": {"x": 2, "y": 11}, "dir_to_get_there": None},
    {"coords": {"x": 2, "y": 12}, "dir_to_get_there": "Down"},
    {"coords": {"x": 2, "y": 13}, "dir_to_get_there": "Down"},
    {"coords": {"x": 1, "y": 13}, "dir_to_get_there": "Left"},
    {"coords": {"x": 1, "y": 12}, "dir_to_get_there": "Up"},
    {"coords": {"x": 1, "y": 11}, "dir_to_get_there": "Up"},
    {"coords": {"x": 1, "y": 10}, "dir_to_get_there": "Up"},
    {"coords": {"x": 2, "y": 10}, "dir_to_get_there": "Right"},
]

for step in test_route:
    target = step["coords"]
    d = step["dir_to_get_there"]
    if d is not None:
        print(f"Walking to {target}...")
        if not walk_to_tile(d, target):
            print(f"Failed to reach {target}")
            continue
            
    # Now stand at 'target' and test all 4 directions
    print(f"Testing all 4 directions at {mgba.get_coordinates()}...")
    for face_dir in ["Up", "Down", "Left", "Right"]:
        if test_interaction(face_dir):
            print(f"FOUND SWITCH! Position: {mgba.get_coordinates()}, Facing: {face_dir}")
            exit(0)
            
print("Search complete. No switch found in these tiles!")
