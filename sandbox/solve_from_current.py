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
    print("Starting ultimate State B solver from position:", pos)
    
    # Dismiss any text
    mgba.press_buttons(["B"])
    time.sleep(0.3)
    
    success = True
    
    # 1. Walk from (15, 7) to Column 18 Row 7
    if pos == {"x": 15, "y": 7}:
        print("Walking RIGHT along Row 7 to Column 18...")
        for x in range(16, 19):
            if not walk_step("Right", {"x": x, "y": 7}):
                success = False
                break
                
    pos = mgba.get_coordinates()
    if success and pos == {"x": 18, "y": 7}:
        # 2. Walk DOWN Column 18 to Row 10
        print("Walking DOWN Column 18 to Row 10...")
        for y in range(8, 11):
            if not walk_step("Down", {"x": 18, "y": y}):
                success = False
                break
                
    pos = mgba.get_coordinates()
    if success and pos == {"x": 18, "y": 10}:
        # 3. Walk LEFT along Row 10 to Column 15
        print("Walking LEFT along Row 10 to Column 15...")
        for x in range(17, 14, -1):
            if not walk_step("Left", {"x": x, "y": 10}):
                success = False
                break
                
    pos = mgba.get_coordinates()
    if success and pos == {"x": 15, "y": 10}:
        # 4. Step DOWN onto stairs at (15, 11) to warp UP to 3F East (OPEN in State B!)
        print("At (15, 10)! Stepping DOWN onto stairs to warp UP...")
        mgba.press_buttons(["Down"])
        time.sleep(1.5)
        
    pos = mgba.get_coordinates()
    if success and (pos == {"x": 16, "y": 11} or pos == {"x": 15, "y": 11}):
        # 5. On 3F East (landing at (16, 11) or (15, 11)):
        # Walk directly from (16, 11) to the pitfall at (26, 3) (already in State B!)
        print("Landed on 3F East! Walking directly to pitfall at (26, 3)...")
        steps_to_pit = [
            ("Right", {"x": 16, "y": 11}), # Ensure aligned
            ("Right", {"x": 17, "y": 11}),
            ("Right", {"x": 18, "y": 11}),
            ("Right", {"x": 19, "y": 11}),
            ("Right", {"x": 20, "y": 11}),
            ("Up", {"x": 20, "y": 10}),
            ("Up", {"x": 20, "y": 9}),
            ("Up", {"x": 20, "y": 8}),
            ("Up", {"x": 20, "y": 7}),
            ("Up", {"x": 20, "y": 6}),
            ("Up", {"x": 20, "y": 5}),
            ("Up", {"x": 20, "y": 4}),
            ("Up", {"x": 20, "y": 3}),
            ("Right", {"x": 21, "y": 3}),
            ("Right", {"x": 22, "y": 3}),
            ("Right", {"x": 23, "y": 3}),
            ("Right", {"x": 24, "y": 3}),
            ("Right", {"x": 25, "y": 3}),
            ("Right", {"x": 26, "y": 3}),
        ]
        for d, c in steps_to_pit:
            if not walk_step(d, c):
                success = False
                break
                
        if success:
            print("At (26, 3) on 3F East! Stepping DOWN onto pitfall...")
            mgba.press_buttons(["Down"])
            time.sleep(2.0)
            
    pos = mgba.get_coordinates()
    if success and pos['x'] in [25, 26] and pos['y'] in [4, 5, 6]:
        print("Landed on 1F East inside fenced room! Position:", pos)
        # Align to Row 3
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
        # 13. Cross B1F East to B1F West
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
        # Walk Left along Row 5 to Column 10
        print("Bypassed wall! Walking LEFT to Column 10...")
        for x in range(18, 9, -1):
            if not walk_step("Left", {"x": x, "y": 5}):
                success = False
                break

    pos = mgba.get_coordinates()
    if success and pos == {"x": 10, "y": 5}:
        # Walk LEFT through open Column 9 gate on Row 5 directly to B1F West
        print("At (10, 5)! Walking LEFT through Column 9 gate directly to B1F West...")
        for x in range(9, 0, -1):
            if not walk_step("Left", {"x": x, "y": 5}):
                success = False
                break

    pos = mgba.get_coordinates()
    if success and pos == {"x": 1, "y": 5}:
        # Facing UP towards Secret Key at (1, 4)
        print("Facing UP towards Secret Key...")
        mgba.press_buttons(["Up"])
        time.sleep(0.3)
        
        # Press A to retrieve Secret Key
        print("Retrieving Secret Key...")
        mgba.press_buttons(["A"])
        time.sleep(1.5)
        # Dismiss "Obtained the SECRET KEY!"
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        print("Obtained Secret Key! Current position:", mgba.get_coordinates())
        
        # 14. DIG escape!
        print("Using DIG to escape...")
        mgba.press_buttons(["Start", "sleep 300", "Down", "A", "sleep 300"])
        for _ in range(5):
            mgba.press_buttons(["Down", "sleep 150"])
        mgba.press_buttons(["A", "sleep 300", "A"])
        time.sleep(3.0)
        print("Warped out successfully! Final position:", mgba.get_coordinates())

if not success:
    print("Mansion complete solve aborted.")

if __name__ == "__main__":
    main()
