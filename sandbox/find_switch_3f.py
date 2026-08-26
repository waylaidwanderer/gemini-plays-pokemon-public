import mgba
import time
from PIL import Image

def is_dialogue_open():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file).resize((160, 144), Image.Resampling.NEAREST)
    cropped = img.crop((0, 104, 160, 144))
    
    # Check for GBC dialog background (high white/cream pixel count)
    white_cream_pixels = 0
    for y in range(cropped.height):
        for x in range(cropped.width):
            r, g, b = cropped.getpixel((x, y))[:3]
            if r > 200 and g > 200 and b > 200:
                white_cream_pixels += 1
    print(f"  Check dialogue box: white_cream_pixels={white_cream_pixels}")
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

def walk_step(direction, expected_coords, retries=5):
    for i in range(retries):
        if handle_any_menu_or_battle():
            pos = mgba.get_coordinates()
            if pos == expected_coords:
                return True
        mgba.press_buttons([direction])
        time.sleep(0.45)
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            return True
        print(f"Blocked or battle! Retrying {direction} to {expected_coords} (attempt {i+1}/{retries}), current: {pos}")
        time.sleep(0.3)
    return pos == expected_coords

def run_steps(steps):
    for d, c in steps:
        if not walk_step(d, c):
            return False
    return True

# Dismiss any menus
mgba.press_buttons(["B"])
time.sleep(0.3)

pos = mgba.get_coordinates()
print("Starting position:", pos)

# List of positions to try interacting with the column 3 statues
# Format: (walk_to_coords, path_to_get_there, face_direction)
tests = [
    # 1. Stand at (2, 11) face Right (statue at 3,11? No, statue is at 3,10 or 3,12)
    # Wait, let's try (2, 12) facing Right (statue is at 3,12)
    ({"x": 2, "y": 12}, [("Left", {"x": 5, "y": 10}), ("Left", {"x": 4, "y": 10}), ("Left", {"x": 3, "y": 10}), ("Left", {"x": 2, "y": 10}), ("Down", {"x": 2, "y": 11}), ("Down", {"x": 2, "y": 12})], "Right"),
    
    # 2. Stand at (3, 11) face Down (towards 3,12)
    ({"x": 3, "y": 11}, [("Right", {"x": 3, "y": 11})], "Down"),
    
    # 3. Stand at (3, 11) face Up (towards 3,10)
    ({"x": 3, "y": 11}, [], "Up"),
    
    # 4. Stand at (2, 10) face Right (towards 3,10)
    ({"x": 2, "y": 10}, [("Left", {"x": 2, "y": 11}), ("Up", {"x": 2, "y": 10})], "Right"),
    
    # 5. Stand at (3, 13) face Up (towards 3,12)
    ({"x": 3, "y": 13}, [("Down", {"x": 2, "y": 11}), ("Down", {"x": 2, "y": 12}), ("Down", {"x": 2, "y": 13}), ("Right", {"x": 3, "y": 13})], "Up"),
    
    # 6. Stand at (3, 13) face Down (towards 3,14)
    ({"x": 3, "y": 13}, [], "Down"),
    
    # 7. Stand at (2, 14) face Right (towards 3,14)
    ({"x": 2, "y": 14}, [("Left", {"x": 2, "y": 13}), ("Down", {"x": 2, "y": 14})], "Right"),
]

for t_coord, path, face_dir in tests:
    print(f"\n--- Testing position {t_coord} facing {face_dir} ---")
    pos = mgba.get_coordinates()
    # Let's run path to get there if any
    if path:
        print(f"Running path to reach {t_coord}...")
        if not run_steps(path):
            print(f"Failed to reach {t_coord}, continuing to next test")
            continue
    else:
        # If we are already there, just continue
        pass
        
    # Face direction
    mgba.press_buttons([face_dir])
    time.sleep(0.4)
    
    # Press A
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    if is_dialogue_open():
        print(f"SUCCESS! Found working switch at {mgba.get_coordinates()} facing {face_dir}!")
        # Toggle it!
        mgba.press_buttons(["A"]) # YES
        time.sleep(1.2)
        mgba.press_buttons(["A"]) # pressed it!
        time.sleep(1.2)
        mgba.press_buttons(["A"]) # dismiss
        time.sleep(1.0)
        print("Switch successfully toggled to State B!")
        exit(0)
    else:
        print(f"Not a switch at {t_coord} facing {face_dir}")
        # Dismiss any accidentally opened menu
        mgba.press_buttons(["B"])
        time.sleep(0.3)

print("\nExhaustive search complete, no switch found.")
