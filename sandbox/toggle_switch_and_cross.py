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

def main():
    pos = mgba.get_coordinates()
    print("Starting toggle_switch_and_cross.py, current coords:", pos)
    
    if pos != {"x": 2, "y": 13}:
        print("Error: Player is not at (2, 13)!")
        return

    # --- STAGE 1: Toggle Mewtwo statue switch to State B ---
    print("Toggling Mewtwo statue switch to State B...")
    mgba.press_buttons(["A"]) # Interact with statue at (2, 12)
    time.sleep(1.8) # Wait for dialogue
    mgba.press_buttons(["A"]) # Press Yes
    time.sleep(1.8) # Wait for pressed dialogue
    mgba.press_buttons(["A"]) # Dismiss dialogue
    time.sleep(1.0)
    mgba.press_buttons(["B"]) # Leftover text safety
    time.sleep(0.5)
    print("Successfully toggled switch!")
    pos = mgba.get_coordinates()

    # --- STAGE 2: Walk from switch to Column 10 Row 9 on 3F West ---
    print("Navigating from switch to Column 10 Row 9...")
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

    # --- STAGE 3: Cross 3F West to 3F East ---
    if pos == {"x": 10, "y": 9}:
        print("Crossing horizontally to 3F East...")
        mgba.press_buttons(["Right"])
        time.sleep(1.5)
        pos = mgba.get_coordinates()
        print("Landed on 3F East at:", pos)
        
    if pos == {"x": 12, "y": 9}:
        # Step Down to Row 11 to align for the final leg
        print("Aligning on 3F East...")
        if run_steps([
            ("Down", {"x": 12, "y": 10}),
            ("Down", {"x": 12, "y": 11}),
        ]):
            print("Successfully aligned on 3F East at (12, 11) in State B!")

if __name__ == "__main__":
    main()
