import mgba
import time
from PIL import Image

def handle_any_menu_or_battle():
    time.sleep(0.1)
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
        time.sleep(0.4)
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

def walk_to_col_10(target_col):
    current_pos = mgba.get_coordinates()
    print(f"Pathing from {current_pos} to ({target_col}, 10)...")
    
    # 1. Walk down to Row 13
    dy = 13 - current_pos["y"]
    if dy > 0:
        if not run_steps([("Down", {"x": current_pos["x"], "y": current_pos["y"] + i + 1}) for i in range(dy)]):
            return False
            
    # 2. Walk horizontally on Row 13 to target_col
    current_pos = mgba.get_coordinates()
    dx = target_col - current_pos["x"]
    if dx > 0:
        if not run_steps([("Right", {"x": current_pos["x"] + i + 1, "y": 13}) for i in range(dx)]):
            return False
    elif dx < 0:
        if not run_steps([("Left", {"x": current_pos["x"] - i - 1, "y": 13}) for i in range(-dx)]):
            return False
            
    # 3. Walk UP Column target_col to Row 10
    current_pos = mgba.get_coordinates()
    dy = current_pos["y"] - 10
    if dy > 0:
        if not run_steps([("Up", {"x": target_col, "y": current_pos["y"] - i - 1}) for i in range(dy)]):
            return False
            
    pos = mgba.get_coordinates()
    if pos["x"] == target_col and pos["y"] == 10:
        return True
    return False

# First, dismiss the "Got away safely!" dialogue box
print("Dismissing 'Got away safely!' dialogue box...")
handle_any_menu_or_battle()

pos = mgba.get_coordinates()
print("Starting position:", pos)

walkable_paths = {}

# Test Columns 1, 3, 4, 5, 6
test_cols = [1, 3, 4, 5, 6]

for col in test_cols:
    print(f"\n--- Testing Column {col} Row 9 ---")
    if walk_to_col_10(col):
        # Try to step UP to (col, 9)
        success = walk_step("Up", {"x": col, "y": 9}, retries=2)
        walkable_paths[col] = success
        if success:
            print(f"RESULT: Column {col} Row 9 is WALKABLE!")
            # Walk back down to (col, 10)
            walk_step("Down", {"x": col, "y": 10}, retries=2)
        else:
            print(f"RESULT: Column {col} Row 9 is BLOCKED.")
    else:
        print(f"Failed to reach ({col}, 10)")

print("\n===============================")
print("FINAL WALKABILITY RESULTS ON ROW 9:")
for col in test_cols:
    walkable = walkable_paths.get(col, False)
    print(f"Column {col}: {'WALKABLE' if walkable else 'BLOCKED'}")
