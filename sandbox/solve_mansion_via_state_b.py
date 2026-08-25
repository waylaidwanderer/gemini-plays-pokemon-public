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
    print("Starting State B mansion solver from current position:", pos)
    
    # Dismiss any text
    mgba.press_buttons(["B"])
    time.sleep(0.3)
    
    success = True
    
    # 1. Walk from (15, 7) on 2F East back to 2F West switch stand position (2, 12)
    if pos == {"x": 15, "y": 7}:
        print("Walking back to 2F West switch from (15, 7) via Row 4 Column 10...")
        if not run_steps([
            ("Left", {"x": 14, "y": 7}),
            ("Left", {"x": 13, "y": 7}),
            ("Left", {"x": 12, "y": 7}),
            ("Up", {"x": 12, "y": 6}),
            ("Up", {"x": 12, "y": 5}),
            ("Up", {"x": 12, "y": 4}),
        ]):
            success = False
            
        if success:
            # Walk LEFT along Row 4 to Column 10
            for x in range(11, 9, -1):
                if not walk_step("Left", {"x": x, "y": 4}):
                    success = False
                    break
                    
        if success:
            # Walk DOWN Column 10 to Row 11
            for y in range(5, 12):
                if not walk_step("Down", {"x": 10, "y": y}):
                    success = False
                    break
                    
        if success:
            # Walk LEFT on Row 11 to Column 3
            for x in range(9, 2, -1):
                if not walk_step("Left", {"x": x, "y": 11}):
                    success = False
                    break
                    
        if success:
            # Walk to (2, 12) standing position
            if not run_steps([
                ("Down", {"x": 3, "y": 12}),
                ("Left", {"x": 2, "y": 12}),
            ]):
                success = False

    pos = mgba.get_coordinates()
    if success and pos == {"x": 2, "y": 12}:
        # 2. Toggle switch to State B
        print("At (2, 12) on 2F West! Facing UP and toggling switch to State B...")
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        mgba.press_buttons(["A"]) # "A secret switch!"
        time.sleep(0.8)
        mgba.press_buttons(["A"]) # select YES
        time.sleep(0.8)
        mgba.press_buttons(["A"]) # "Pressed it!"
        time.sleep(0.8)
        print("Switch toggled to State B!")
        
        # 3. Walk to Row 11 Column 10
        if not run_steps([
            ("Right", {"x": 3, "y": 12}),
            ("Up", {"x": 3, "y": 11}),
        ]):
            success = False
            
        if success:
            curr_x = mgba.get_coordinates()['x']
            while curr_x < 10:
                if not walk_step("Right", {"x": curr_x + 1, "y": 11}):
                    success = False
                    break
                curr_x = mgba.get_coordinates()['x']
                
    pos = mgba.get_coordinates()
    if success and pos == {"x": 10, "y": 11}:
        # 4. Walk UP Column 10 to Row 4
        print("Walking UP Column 10 to Row 4...")
        for y in range(10, 3, -1):
            if not walk_step("Up", {"x": 10, "y": y}):
                success = False
                break
                
    pos = mgba.get_coordinates()
    if success and pos == {"x": 10, "y": 4}:
        # 5. Walk LEFT along Row 4 to Column 5
        print("Walking LEFT along Row 4 to Column 5...")
        for x in range(9, 4, -1):
            if not walk_step("Left", {"x": x, "y": 4}):
                success = False
                break
                
    pos = mgba.get_coordinates()
    if success and pos == {"x": 5, "y": 4}:
        # 6. Walk UP Column 5 to Row 3
        if not walk_step("Up", {"x": 5, "y": 3}):
            success = False
            
    pos = mgba.get_coordinates()
    if success and pos == {"x": 5, "y": 3}:
        # 7. Walk RIGHT along Row 3 to Column 18
        print("Walking RIGHT along Row 3 to Column 18...")
        for x in range(6, 19):
            if not walk_step("Right", {"x": x, "y": 3}):
                success = False
                break
                
    pos = mgba.get_coordinates()
    if success and pos == {"x": 18, "y": 3}:
        # 8. Walk DOWN Column 18 to Row 7
        print("Walking DOWN Column 18 to Row 7...")
        for y in range(4, 8):
            if not walk_step("Down", {"x": 18, "y": y}):
                success = False
                break
                
    pos = mgba.get_coordinates()
    if success and pos == {"x": 18, "y": 7}:
        # 9. Walk LEFT along Row 7 to Column 15
        print("Walking LEFT along Row 7 to Column 15...")
        for x in range(17, 14, -1):
            if not walk_step("Left", {"x": x, "y": 7}):
                success = False
                break
                
    pos = mgba.get_coordinates()
    if success and pos == {"x": 15, "y": 7}:
        # 10. Walk DOWN Column 15 directly to stairs at (15, 11) (OPEN in State B!)
        print("Walking DOWN Column 15 to stairs...")
        steps_down_col15 = [
            ("Down", {"x": 15, "y": 8}),
            ("Down", {"x": 15, "y": 9}),
            ("Down", {"x": 15, "y": 10}),
        ]
        for d, c in steps_down_col15:
            if not walk_step(d, c):
                success = False
                break
                
        if success:
            print("At (15, 10)! Stepping DOWN onto stairs to warp UP to 3F East...")
            mgba.press_buttons(["Down"])
            time.sleep(1.5)
            
    pos = mgba.get_coordinates()
    if success and (pos == {"x": 16, "y": 11} or pos == {"x": 15, "y": 11}):
        # 11. On 3F East (landing at (16, 11) or (15, 11)):
        # Since we are already in State B, we don't need to toggle any switch on 3F East!
        # We just walk directly from (16, 11) to the pitfall at (26, 3)!
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
        # 12. Cross B1F East to B1F West
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
        
        # 13. DIG escape!
        print("Using DIG to escape...")
        mgba.press_buttons(["Start", "sleep 300", "Down", "A", "sleep 300"])
        for _ in range(5):
            mgba.press_buttons(["Down", "sleep 150"])
        mgba.press_buttons(["A", "sleep 300", "A"])
        time.sleep(3.0)
        print("Warped out successfully! Final position:", mgba.get_coordinates())

main()
