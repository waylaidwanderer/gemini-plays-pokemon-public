import mgba
import time
import sys
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

def main():
    pos = mgba.get_coordinates()
    print("Starting solve_mansion_final_step2.py, current coords:", pos)
    
    if pos != {"x": 2, "y": 12}:
        print("Error: Player is not at (2, 12) on 3F West!")
        return

    # --- STAGE 1: Walk from switch (2, 12) to Column 10 Row 9 ---
    print("Navigating to 3F West-to-East crossing...")
    if not run_steps([
        ("Down", {"x": 2, "y": 13}),
        ("Right", {"x": 3, "y": 13}),
        ("Right", {"x": 4, "y": 13}),
        ("Right", {"x": 5, "y": 13}),
        ("Right", {"x": 6, "y": 13}),
        ("Up", {"x": 6, "y": 12}),
        ("Up", {"x": 6, "y": 11}),
        ("Right", {"x": 7, "y": 11}),
        ("Right", {"x": 8, "y": 11}),
        ("Right", {"x": 9, "y": 11}),
        ("Right", {"x": 10, "y": 11}),
        ("Up", {"x": 10, "y": 10}),
        ("Up", {"x": 10, "y": 9}),
    ]):
        return
    pos = mgba.get_coordinates()

    # --- STAGE 2: Cross 3F West to 3F East ---
    if pos == {"x": 10, "y": 9}:
        print("Crossing horizontally to 3F East...")
        mgba.press_buttons(["Right"])
        time.sleep(1.5)
        pos = mgba.get_coordinates()
        print("Landed on 3F East at:", pos)
        
    # --- STAGE 3: Walk to (12, 6) ---
    if pos["x"] in [11, 12] and pos["y"] == 9:
        print("Navigating on 3F East to Row 6...")
        if pos["x"] == 11:
            if not walk_step("Right", {"x": 12, "y": 9}):
                return
        if not run_steps([
            ("Up", {"x": 12, "y": 8}),
            ("Up", {"x": 12, "y": 7}),
            ("Up", {"x": 12, "y": 6}),
        ]):
            return
        pos = mgba.get_coordinates()

    # --- STAGE 4: Walk RIGHT along Row 6 to Column 20 ---
    if pos == {"x": 12, "y": 6}:
        print("Walking RIGHT along Row 6 to Column 20...")
        if not run_steps([
            ("Right", {"x": 13, "y": 6}),
            ("Right", {"x": 14, "y": 6}),
            ("Right", {"x": 15, "y": 6}),
            ("Right", {"x": 16, "y": 6}),
            ("Right", {"x": 17, "y": 6}),
            ("Right", {"x": 18, "y": 6}),
            ("Right", {"x": 19, "y": 6}),
            ("Right", {"x": 20, "y": 6}),
        ]):
            return
        pos = mgba.get_coordinates()

    # --- STAGE 5: Walk UP Column 20 and RIGHT to Pitfall ---
    if pos == {"x": 20, "y": 6}:
        print("Walking UP Column 20 and RIGHT to the pitfall at (26, 3)...")
        if not run_steps([
            ("Up", {"x": 20, "y": 5}),
            ("Up", {"x": 20, "y": 4}),
            ("Up", {"x": 20, "y": 3}),
            ("Right", {"x": 21, "y": 3}),
            ("Right", {"x": 22, "y": 3}),
            ("Right", {"x": 23, "y": 3}),
            ("Right", {"x": 24, "y": 3}),
            ("Right", {"x": 25, "y": 3}),
        ]):
            return
        
        # Step Right onto the actual pitfall tile at (26, 3) to fall
        mgba.press_buttons(["Right"])
        time.sleep(1.5)
        pos = mgba.get_coordinates()
        print("Dropped down successfully! Current position on 1F East inside fenced room:", pos)

if __name__ == "__main__":
    main()
