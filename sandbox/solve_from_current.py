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
    
    # Dismiss "The door is locked..."
    mgba.press_buttons(["B"])
    time.sleep(0.4)
    
    success = True
    
    # We are at (18, 4) on Cinnabar Island overworld
    if pos == {"x": 18, "y": 4}:
        print("STAGE 1: Walking LEFT along Row 4 to Column 6...")
        for x in range(17, 5, -1):
            if not walk_step("Left", {"x": x, "y": 4}):
                success = False
                break
                
    pos = mgba.get_coordinates()
    if success and pos == {"x": 6, "y": 4}:
        print("Entering Mansion...")
        mgba.press_buttons(["Up"])
        time.sleep(2.0) # Wait for map transition
        
    pos = mgba.get_coordinates()
    # 2. Inside Mansion 1F West (landing at (5, 27))
    if success and pos == {"x": 5, "y": 27}:
        print("STAGE 2: Inside Mansion 1F West! Walking UP Column 5 to stairs at (5, 10)...")
        for y in range(26, 9, -1):
            if not walk_step("Up", {"x": 5, "y": y}):
                success = False
                break
                
        if success:
            print("Warping UP to 2F West...")
            time.sleep(1.5) # Wait for warp transition
            
    pos = mgba.get_coordinates()
    # 3. Inside Mansion 2F West (landing at (5, 11))
    if success and pos == {"x": 5, "y": 11}:
        print("STAGE 3: Inside 2F West! Walking to stairs at (7, 10)...")
        if not run_steps([
            ("Right", {"x": 6, "y": 11}),
            ("Right", {"x": 7, "y": 11}),
        ]):
            success = False
            
        if success:
            print("Stepping UP onto stairs at (7, 10) to warp UP to 3F West...")
            mgba.press_buttons(["Up"])
            time.sleep(1.5) # Wait for warp transition
            
    pos = mgba.get_coordinates()
    # 4. Landed on 3F West at (7, 10) or (7, 11)
    if success and pos['y'] in [10, 11] and pos['x'] == 7:
        print("STAGE 4: Landed on 3F West! Walking DOWN to Row 11...")
        if pos['y'] == 10:
            if not walk_step("Down", {"x": 7, "y": 11}):
                success = False
                
    pos = mgba.get_coordinates()
    if success and pos == {"x": 7, "y": 11}:
        print("Walking LEFT along Row 11 to Column 3...")
        for x in range(6, 2, -1):
            if not walk_step("Left", {"x": x, "y": 11}):
                success = False
                break
                
    pos = mgba.get_coordinates()
    if success and pos == {"x": 3, "y": 11}:
        print("Walking to switch standing position at (2, 12)...")
        if not run_steps([
            ("Down", {"x": 3, "y": 12}),
            ("Left", {"x": 2, "y": 12}),
        ]):
            success = False
            
    pos = mgba.get_coordinates()
    if success and pos == {"x": 2, "y": 12}:
        # Toggle switch carefully to State B
        print("At (2, 12) on 3F West! Facing UP to toggle switch...")
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
        print("Successfully toggled switch to State B!")
        
        # Walk back to Column 10 Row 11 on 3F West
        print("Walking to Column 10 Row 11...")
        if not run_steps([
            ("Left", {"x": 1, "y": 12}),
            ("Up", {"x": 1, "y": 11}),
            ("Down", {"x": 1, "y": 12}),
            ("Right", {"x": 2, "y": 12}),
            ("Right", {"x": 3, "y": 12}),
            ("Right", {"x": 4, "y": 12}),
            ("Right", {"x": 5, "y": 12}),
            ("Right", {"x": 6, "y": 12}),
            ("Right", {"x": 7, "y": 12}),
            ("Up", {"x": 7, "y": 11}),
            ("Right", {"x": 8, "y": 11}),
            ("Right", {"x": 9, "y": 11}),
            ("Right", {"x": 10, "y": 11}),
        ]):
            success = False
                
    pos = mgba.get_coordinates()
    if success and pos == {"x": 10, "y": 11}:
        print("Walking UP Column 10 to Row 7...")
        if not run_steps([
            ("Up", {"x": 10, "y": 10}),
            ("Up", {"x": 10, "y": 9}),
            ("Up", {"x": 10, "y": 8}),
            ("Up", {"x": 10, "y": 7}),
        ]):
            success = False
            
    pos = mgba.get_coordinates()
    if success and pos == {"x": 10, "y": 7}:
        print("Walking RIGHT along Row 7 to Column 19 on 3F East...")
        for x in range(11, 20):
            if not walk_step("Right", {"x": x, "y": 7}):
                success = False
                break
                
    pos = mgba.get_coordinates()
    if success and pos == {"x": 19, "y": 7}:
        print("Walking UP Column 19 to Row 4...")
        for y in range(6, 3, -1):
            if not walk_step("Up", {"x": 19, "y": y}):
                success = False
                break
                
    pos = mgba.get_coordinates()
    if success and pos == {"x": 19, "y": 4}:
        print("Bypassing Row 3 Column 19 wall...")
        if not run_steps([
            ("Right", {"x": 20, "y": 4}),
            ("Up", {"x": 20, "y": 3}),
        ]):
            success = False
            
    pos = mgba.get_coordinates()
    if success and pos == {"x": 20, "y": 3}:
        print("Walking RIGHT along Row 3 to Column 26...")
        for x in range(21, 27):
            if not walk_step("Right", {"x": x, "y": 3}):
                success = False
                break
                
    pos = mgba.get_coordinates()
    if success and pos == {"x": 26, "y": 3}:
        print("At (26, 3) on 3F East! Stepping DOWN onto pitfall...")
        mgba.press_buttons(["Down"])
        time.sleep(2.0)
        
    pos = mgba.get_coordinates()
    if success and pos['x'] in [25, 26] and pos['y'] in [4, 5, 6, 7]:
        print("Landed on 1F East inside fenced room! Position:", pos)
        while pos['y'] > 3:
            if not walk_step("Up", {"x": pos['x'], "y": pos['y'] - 1}):
                break
            pos = mgba.get_coordinates()
        while pos['x'] > 22:
            if not walk_step("Left", {"x": pos['x'] - 1, "y": 3}):
                break
            pos = mgba.get_coordinates()
            
        if pos == {"x": 22, "y": 3}:
            print("At (22, 3) on 1F East! Stepping UP to warp DOWN to B1F East...")
            mgba.press_buttons(["Up"])
            time.sleep(1.5)
            
    pos = mgba.get_coordinates()
    if success and pos == {"x": 22, "y": 3}:
        print("Landed on B1F East! Walking to Column 19 Row 5...")
        if not run_steps([
            ("Left", {"x": 21, "y": 3}),
            ("Down", {"x": 21, "y": 4}),
            ("Left", {"x": 20, "y": 4}),
            ("Left", {"x": 19, "y": 4}),
            ("Down", {"x": 19, "y": 5}),
        ]):
            success = False

    pos = mgba.get_coordinates()
    if success and pos == {"x": 19, "y": 5}:
        print("Walking UP Column 18 to Row 6...")
        if not run_steps([
            ("Down", {"x": 19, "y": 6}),
            ("Left", {"x": 18, "y": 6}),
        ]):
            success = False

    pos = mgba.get_coordinates()
    if success and pos == {"x": 18, "y": 6}:
        print("Walking LEFT along Row 6 to Column 10...")
        for x in range(17, 9, -1):
            if not walk_step("Left", {"x": x, "y": 6}):
                success = False
                break

    pos = mgba.get_coordinates()
    if success and pos == {"x": 10, "y": 6}:
        print("Walking UP Column 10 to Row 5...")
        if not walk_step("Up", {"x": 10, "y": 5}):
            success = False

    pos = mgba.get_coordinates()
    if success and pos == {"x": 10, "y": 5}:
        print("At (10, 5)! Walking LEFT through Column 9 gate directly to B1F West...")
        for x in range(9, 0, -1):
            if not walk_step("Left", {"x": x, "y": 5}):
                success = False
                break

    pos = mgba.get_coordinates()
    if success and pos == {"x": 1, "y": 5}:
        print("Facing UP towards Secret Key...")
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        
        print("Retrieving Secret Key...")
        mgba.press_buttons(["A"])
        time.sleep(1.5)
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        print("Obtained Secret Key! Current position:", mgba.get_coordinates())
        
        print("Using DIG to escape...")
        mgba.press_buttons(["Start", "sleep 300", "Down", "A", "sleep 300"])
        for _ in range(5):
            mgba.press_buttons(["Down", "sleep 150"])
        mgba.press_buttons(["A", "sleep 300", "A"])
        time.sleep(3.0)
        print("Warped out successfully! Final position:", mgba.get_coordinates())

if __name__ == "__main__":
    main()
