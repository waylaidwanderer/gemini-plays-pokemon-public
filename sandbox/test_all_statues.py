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
            r, g, b = img_std.getpixel((x, y))[:3]
            total_pixels += 1
            is_bw = (r < 50 and g < 50 and b < 50) or (r > 200 and g > 200 and b > 200)
            if is_bw:
                black_or_white += 1
                
    percentage = black_or_white / total_pixels
    if percentage > 0.90:
        print(f"Dialogue/Menu detected! (B/W: {percentage*100:.2f}%)")
        return True
    return False

def check_dialogue():
    time.sleep(0.5)
    scr = mgba.take_screenshot()
    # Check if there is dialogue on screen
    img = Image.open(scr)
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
    return percentage > 0.90

def interact_statue(statue_coords, stand_coords, face_dir):
    print(f"Navigating to {stand_coords} facing {face_dir} to test statue at {statue_coords}...")
    # Walk to stand_coords
    # Since we are at B1F West SOUTH, we can use simple walk step
    # Current pos:
    curr = mgba.get_coordinates()
    dx = stand_coords["x"] - curr["x"]
    dy = stand_coords["y"] - curr["y"]
    
    # Move x
    if dx > 0:
        for _ in range(dx):
            mgba.press_buttons(["Right"])
            time.sleep(0.4)
    elif dx < 0:
        for _ in range(-dx):
            mgba.press_buttons(["Left"])
            time.sleep(0.4)
            
    # Move y
    if dy > 0:
        for _ in range(dy):
            mgba.press_buttons(["Down"])
            time.sleep(0.4)
    elif dy < 0:
        for _ in range(-dy):
            mgba.press_buttons(["Up"])
            time.sleep(0.4)
            
    # Turn to face_dir
    mgba.press_buttons([face_dir])
    time.sleep(0.4)
    
    # Press A
    print("Pressing A...")
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    
    # Check for dialogue
    if check_dialogue():
        print(f"SUCCESS!!! Statue at {statue_coords} has a switch! Dialogue opened!")
        # Let's see dialogue screenshot
        mgba.take_screenshot()
        # Close dialogue
        mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
        return True
    else:
        print(f"Statue at {statue_coords} is decorative (no dialogue).")
        return False

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

# We are at (5, 10). Let's go down to (5, 11) first
mgba.press_buttons(["Down"])
time.sleep(0.5)

# Test statue at (3, 10) from (3, 11) facing UP
if interact_statue({"x": 3, "y": 10}, {"x": 3, "y": 11}, "Up"):
    exit(0)

# Test statue at (3, 12) from (3, 11) facing DOWN
if interact_statue({"x": 3, "y": 12}, {"x": 3, "y": 11}, "Down"):
    exit(0)

# Test statue at (3, 12) from (3, 13) facing UP
if interact_statue({"x": 3, "y": 12}, {"x": 3, "y": 13}, "Up"):
    exit(0)

# Test statue at (3, 14) from (3, 13) facing DOWN
if interact_statue({"x": 3, "y": 14}, {"x": 3, "y": 13}, "Down"):
    exit(0)

# Test statue at (8, 10) from (8, 11) facing UP
if interact_statue({"x": 8, "y": 10}, {"x": 8, "y": 11}, "Up"):
    exit(0)

# Test statue at (8, 12) from (8, 11) facing DOWN
if interact_statue({"x": 8, "y": 12}, {"x": 8, "y": 11}, "Down"):
    exit(0)

# Test statue at (8, 12) from (8, 13) facing UP
if interact_statue({"x": 8, "y": 12}, {"x": 8, "y": 13}, "Up"):
    exit(0)

# Test statue at (8, 14) from (8, 13) facing DOWN
if interact_statue({"x": 8, "y": 14}, {"x": 8, "y": 13}, "Down"):
    exit(0)

print("All statues in B1F West SOUTH tested! None have a switch.")
