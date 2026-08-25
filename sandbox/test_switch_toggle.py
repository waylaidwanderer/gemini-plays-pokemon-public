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
    print("Testing switch interaction starting from:", pos)
    
    # Dismiss any text
    mgba.press_buttons(["B"])
    time.sleep(0.3)
    
    # 1. Walk from current position (15, 7) back to (12, 7)
    if pos == {"x": 15, "y": 7}:
        if not run_steps([
            ("Left", {"x": 14, "y": 7}),
            ("Left", {"x": 13, "y": 7}),
            ("Left", {"x": 12, "y": 7}),
        ]):
            return
            
    pos = mgba.get_coordinates()
    if pos == {"x": 12, "y": 7}:
        # 2. Walk UP to Row 4
        if not run_steps([
            ("Up", {"x": 12, "y": 6}),
            ("Up", {"x": 12, "y": 5}),
            ("Up", {"x": 12, "y": 4}),
        ]):
            return
            
    pos = mgba.get_coordinates()
    if pos == {"x": 12, "y": 4}:
        # 3. Walk LEFT to Column 10
        for x in range(11, 9, -1):
            if not walk_step("Left", {"x": x, "y": 4}):
                return
                
    pos = mgba.get_coordinates()
    if pos == {"x": 10, "y": 4}:
        # 4. Walk DOWN Column 10 to Row 11
        for y in range(5, 12):
            if not walk_step("Down", {"x": 10, "y": y}):
                return
                
    pos = mgba.get_coordinates()
    if pos == {"x": 10, "y": 11}:
        # 5. Walk LEFT along Row 11 to Column 3
        for x in range(9, 2, -1):
            if not walk_step("Left", {"x": x, "y": 11}):
                return
                
    pos = mgba.get_coordinates()
    if pos == {"x": 3, "y": 11}:
        # 6. Walk to (2, 12)
        if not run_steps([
            ("Down", {"x": 3, "y": 12}),
            ("Left", {"x": 2, "y": 12}),
        ]):
            return
            
    pos = mgba.get_coordinates()
    if pos == {"x": 2, "y": 12}:
        print("At (2, 12)! Turning UP and starting slow toggle with screenshot captures...")
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        
        # Step 1: Press A to trigger dialogue
        print("Pressing A (Step 1)...")
        mgba.press_buttons(["A"])
        time.sleep(0.8)
        img1 = mgba.take_screenshot()
        os.rename(img1, "switch_step_1.png")
        print("Captured switch_step_1.png")
        
        # Step 2: Press A to select YES on prompt
        print("Pressing A (Step 2)...")
        mgba.press_buttons(["A"])
        time.sleep(0.8)
        img2 = mgba.take_screenshot()
        os.rename(img2, "switch_step_2.png")
        print("Captured switch_step_2.png")
        
        # Step 3: Press A to dismiss "Pressed it!"
        print("Pressing A (Step 3)...")
        mgba.press_buttons(["A"])
        time.sleep(0.8)
        img3 = mgba.take_screenshot()
        os.rename(img3, "switch_step_3.png")
        print("Captured switch_step_3.png")
        
        # Step 4: Final confirmation screenshot
        img4 = mgba.take_screenshot()
        os.rename(img4, "switch_step_4.png")
        print("Captured switch_step_4.png")

import os
main()
