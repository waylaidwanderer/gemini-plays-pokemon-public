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
    print("Starting solve from current position:", pos)
    
    # Check if we are at (5, 11) on 2F West
    if pos == {"x": 5, "y": 11}:
        # 1. Walk RIGHT along Row 11 to Column 12
        if not run_steps([
            ("Right", {"x": 6, "y": 11}),
            ("Right", {"x": 7, "y": 11}),
            ("Right", {"x": 8, "y": 11}),
            ("Right", {"x": 9, "y": 11}),
            ("Right", {"x": 10, "y": 11}),
            ("Right", {"x": 11, "y": 11}),
            ("Right", {"x": 12, "y": 11}),
        ]):
            print("Failed to walk to Column 12.")
            return
            
        # 2. Walk UP Column 12 to Row 1
        print("Walking UP Column 12 to Row 1...")
        for y in range(10, 0, -1):
            if not walk_step("Up", {"x": 12, "y": y}):
                print("Failed to walk UP Column 12.")
                return
                
    pos = mgba.get_coordinates()
    # Now we are at (12, 1) on 2F East
    if pos == {"x": 12, "y": 1}:
        # 3. Walk DOWN Column 12 to Row 7
        if not run_steps([
            ("Down", {"x": 12, "y": 2}),
            ("Down", {"x": 12, "y": 3}),
            ("Down", {"x": 12, "y": 4}),
            ("Down", {"x": 12, "y": 5}),
            ("Down", {"x": 12, "y": 6}),
            ("Down", {"x": 12, "y": 7}),
        ]):
            print("Failed to walk DOWN Column 12 to Row 7.")
            return
            
    pos = mgba.get_coordinates()
    if pos == {"x": 12, "y": 7}:
        # 4. Walk RIGHT along Row 7 to Column 18
        if not run_steps([
            ("Right", {"x": 13, "y": 7}),
            ("Right", {"x": 14, "y": 7}),
            ("Right", {"x": 15, "y": 7}),
            ("Right", {"x": 16, "y": 7}),
            ("Right", {"x": 17, "y": 7}),
            ("Right", {"x": 18, "y": 7}),
        ]):
            print("Failed to walk RIGHT along Row 7.")
            return

    pos = mgba.get_coordinates()
    if pos == {"x": 18, "y": 7}:
        # 5. Walk DOWN Column 18 to Row 11
        if not run_steps([
            ("Down", {"x": 18, "y": 8}),
            ("Down", {"x": 18, "y": 9}),
            ("Down", {"x": 18, "y": 10}),
            ("Down", {"x": 18, "y": 11}),
        ]):
            print("Failed to walk DOWN Column 18.")
            return

    pos = mgba.get_coordinates()
    if pos == {"x": 18, "y": 11}:
        # 6. Walk LEFT along Row 11 to Column 15 stairs
        if not run_steps([
            ("Left", {"x": 17, "y": 11}),
            ("Left", {"x": 16, "y": 11}),
        ]):
            print("Failed to walk LEFT Row 11.")
            return
            
        print("At (16, 11)! Stepping LEFT onto stairs to warp UP to 3F East...")
        mgba.press_buttons(["Left"])
        time.sleep(1.5)
        
    pos = mgba.get_coordinates()
    if pos == {"x": 16, "y": 11}:
        # 7. On 3F East, walk RIGHT to Column 18
        if not run_steps([
            ("Right", {"x": 17, "y": 11}),
            ("Right", {"x": 18, "y": 11}),
        ]):
            print("Failed to walk RIGHT on 3F East.")
            return
            
    pos = mgba.get_coordinates()
    if pos == {"x": 18, "y": 11}:
        # 8. Walk UP Column 18 to Row 7
        if not run_steps([
            ("Up", {"x": 18, "y": 10}),
            ("Up", {"x": 18, "y": 9}),
            ("Up", {"x": 18, "y": 8}),
            ("Up", {"x": 18, "y": 7}),
        ]):
            print("Failed to walk UP Column 18 on 3F East.")
            return

    pos = mgba.get_coordinates()
    if pos == {"x": 18, "y": 7}:
        # 9. Walk LEFT along Row 7 to Column 12
        if not run_steps([
            ("Left", {"x": 17, "y": 7}),
            ("Left", {"x": 16, "y": 7}),
            ("Left", {"x": 15, "y": 7}),
            ("Left", {"x": 14, "y": 7}),
            ("Left", {"x": 13, "y": 7}),
            ("Left", {"x": 12, "y": 7}),
        ]):
            print("Failed to walk LEFT Row 7 on 3F East.")
            return

    pos = mgba.get_coordinates()
    if pos == {"x": 12, "y": 7}:
        # 10. Walk DOWN Column 12 to Row 12
        if not run_steps([
            ("Down", {"x": 12, "y": 8}),
            ("Down", {"x": 12, "y": 9}),
            ("Down", {"x": 12, "y": 10}),
            ("Down", {"x": 12, "y": 11}),
            ("Down", {"x": 12, "y": 12}),
        ]):
            print("Failed to walk DOWN Column 12 to Row 12.")
            return

    pos = mgba.get_coordinates()
    if pos == {"x": 12, "y": 12}:
        # 11. Toggle switch at (12, 11) to State B
        print("At (12, 12) on 3F East! Facing UP towards switch at (12, 11)...")
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        mgba.press_buttons(["A"]) # "A secret switch!"
        time.sleep(0.8)
        mgba.press_buttons(["A"]) # select YES
        time.sleep(0.8)
        mgba.press_buttons(["A"]) # "Pressed it!"
        time.sleep(0.8)
        print("Successfully toggled switch to State B!")
        
        # B1. Walk UP Column 12 to Row 6
        if not run_steps([
            ("Up", {"x": 12, "y": 11}),
            ("Up", {"x": 12, "y": 10}),
            ("Up", {"x": 12, "y": 9}),
            ("Up", {"x": 12, "y": 8}),
            ("Up", {"x": 12, "y": 7}),
            ("Up", {"x": 12, "y": 6}),
        ]):
            print("Failed to walk UP Column 12 to Row 6.")
            return

    pos = mgba.get_coordinates()
    if pos == {"x": 12, "y": 6}:
        # B2. Walk RIGHT along Row 6 to Column 21
        for x in range(13, 22):
            if not walk_step("Right", {"x": x, "y": 6}):
                print("Failed to walk RIGHT along Row 6.")
                return

    pos = mgba.get_coordinates()
    if pos == {"x": 21, "y": 6}:
        # B3. Walk LEFT 2 steps to (19, 6)
        if not run_steps([
            ("Left", {"x": 20, "y": 6}),
            ("Left", {"x": 19, "y": 6}),
        ]):
            print("Failed to walk LEFT to (19, 6).")
            return

    pos = mgba.get_coordinates()
    if pos == {"x": 19, "y": 6}:
        # B4. Walk UP to (19, 5), UP to (19, 4), RIGHT to (20, 4), UP to (20, 3)
        if not run_steps([
            ("Up", {"x": 19, "y": 5}),
            ("Up", {"x": 19, "y": 4}),
            ("Right", {"x": 20, "y": 4}),
            ("Up", {"x": 20, "y": 3}),
        ]):
            print("Failed to bypass Row 3 Column 19 wall.")
            return

    pos = mgba.get_coordinates()
    if pos == {"x": 20, "y": 3}:
        # B5. Walk RIGHT along Row 3 to Column 26
        for x in range(21, 27):
            if not walk_step("Right", {"x": x, "y": 3}):
                print("Failed to walk RIGHT along Row 3.")
                return

    pos = mgba.get_coordinates()
    if pos == {"x": 26, "y": 3}:
        # B6. Step DOWN onto pitfall at (26, 4)
        print("At (26, 3) on 3F East! Stepping DOWN onto pitfall...")
        mgba.press_buttons(["Down"])
        time.sleep(2.0)
        
    pos = mgba.get_coordinates()
    # We should have landed on 1F East inside the fenced room at (26, 4) or (25, 6)
    if pos['x'] in [25, 26] and pos['y'] in [4, 5, 6]:
        print("Landed on 1F East inside fenced room! Position:", pos)
        # First align to (26, 3)
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
    if pos == {"x": 22, "y": 3}:
        # B8. Cross B1F East to B1F West
        if not run_steps([
            ("Left", {"x": 21, "y": 3}),
            ("Down", {"x": 21, "y": 4}),
            ("Left", {"x": 20, "y": 4}),
            ("Left", {"x": 19, "y": 4}),
            ("Down", {"x": 19, "y": 5}),
        ]):
            print("Failed to navigate B1F East.")
            return

    pos = mgba.get_coordinates()
    if pos == {"x": 19, "y": 5}:
        # Walk Left along Row 5 to Column 10
        print("Bypassed wall! Walking LEFT to Column 10...")
        for x in range(18, 9, -1):
            if not walk_step("Left", {"x": x, "y": 5}):
                print("Failed to walk LEFT to Column 10.")
                return

    pos = mgba.get_coordinates()
    if pos == {"x": 10, "y": 5}:
        # Walk LEFT through open Column 9 gate on Row 5 directly to B1F West
        print("At (10, 5)! Walking LEFT through Column 9 gate directly to B1F West...")
        for x in range(9, 0, -1):
            if not walk_step("Left", {"x": x, "y": 5}):
                print("Failed to walk through B1F gate.")
                return

    pos = mgba.get_coordinates()
    if pos == {"x": 1, "y": 5}:
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
        
        # DIG escape!
        print("Using DIG to escape...")
        mgba.press_buttons(["Start", "sleep 300", "Down", "A", "sleep 300"])
        for _ in range(5):
            mgba.press_buttons(["Down", "sleep 150"])
        mgba.press_buttons(["A", "sleep 300", "A"])
        time.sleep(3.0)
        print("Warped out successfully! Final position:", mgba.get_coordinates())

main()
