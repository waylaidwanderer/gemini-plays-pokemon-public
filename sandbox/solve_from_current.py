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
    print("Starting master solver from position:", pos)
    
    # Dismiss any text
    mgba.press_buttons(["B"])
    time.sleep(0.3)
    
    success = True
    
    # 1. We are at (8, 11) on 3F West in State B
    if pos == {"x": 8, "y": 11}:
        print("STAGE 4c: Walking back to switch standing position at (2, 13)...")
        if not run_steps([
            ("Left", {"x": 7, "y": 11}),
            ("Left", {"x": 6, "y": 11}),
            ("Left", {"x": 5, "y": 11}),
            ("Down", {"x": 5, "y": 12}),
            ("Down", {"x": 5, "y": 13}),
            ("Left", {"x": 4, "y": 13}),
            ("Left", {"x": 3, "y": 13}),
            ("Left", {"x": 2, "y": 13}),
        ]):
            success = False
            
    pos = mgba.get_coordinates()
    if success and pos == {"x": 2, "y": 13}:
        # Toggle switch to State A
        print("At (2, 13) on 3F West! Facing UP to toggle switch to State A...")
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        mgba.press_buttons(["A"]) # "A secret switch!"
        time.sleep(1.8) # Wait for text to print
        mgba.press_buttons(["A"]) # select YES
        time.sleep(1.8) # Wait for "Pressed it!"
        mgba.press_buttons(["A"]) # Dismiss "Pressed it!"
        time.sleep(1.0)
        mgba.press_buttons(["B"]) # Dismiss leftover text
        time.sleep(0.5)
        print("Successfully toggled switch back to State A!")
        
        # Use DIG to escape
        print("Using DIG to escape...")
        mgba.press_buttons(["Start", "sleep 300", "Down", "A", "sleep 300"])
        time.sleep(1.0)
        for _ in range(5):
            mgba.press_buttons(["Down"])
            time.sleep(0.15)
        mgba.press_buttons(["A"])
        time.sleep(0.5)
        mgba.press_buttons(["A"])
        time.sleep(0.5)
        mgba.press_buttons(["A"])
        time.sleep(3.0)
        print("DIG successful! Escaped to overworld:", mgba.get_coordinates())

if __name__ == "__main__":
    main()
