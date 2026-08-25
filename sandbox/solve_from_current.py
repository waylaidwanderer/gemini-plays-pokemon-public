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

# Starting at (19, 4) on 3F East (State B)
print("Starting Mansion final stage from (19, 4)...")
success = True

# 1. Walk RIGHT to (20, 4)
if walk_step("Right", {"x": 20, "y": 4}):
    # 2. Walk UP to (20, 3)
    if walk_step("Up", {"x": 20, "y": 3}):
        # 3. Walk RIGHT along Row 3 to Column 26
        print("On Row 3! Walking RIGHT to Column 26...")
        for x in range(21, 27):
            if not walk_step("Right", {"x": x, "y": 3}):
                success = False
                break
                
        if success:
            # 4. Step DOWN onto pitfall at (26, 4)
            print("At (26, 3) on 3F East! Stepping DOWN onto pitfall...")
            mgba.press_buttons(["Down"])
            time.sleep(2.0)
            pos = mgba.get_coordinates()
            print(f"Landed on 1F East inside fenced room! Position: {pos}")
            
            # 5. Walk to B1F East stairs
            steps_1f_east = [
                ("Up", {"x": 26, "y": 3}),
                ("Left", {"x": 25, "y": 3}),
                ("Left", {"x": 24, "y": 3}),
                ("Left", {"x": 23, "y": 3}),
                ("Left", {"x": 22, "y": 3}),
            ]
            print("Walking to stairs inside 1F East fenced room...")
            for d, c in steps_1f_east:
                if not walk_step(d, c):
                    success = False
                    break
                    
            if success:
                print("At (22, 3) on 1F East! Stepping UP to warp DOWN to B1F East...")
                mgba.press_buttons(["Up"])
                time.sleep(1.5)
                pos = mgba.get_coordinates()
                print(f"Warped DOWN to B1F East! Position: {pos}")
                
                # 6. Cross B1F East to B1F West
                if pos == {"x": 22, "y": 3}:
                    steps_b1f = [
                        ("Left", {"x": 21, "y": 3}),
                        ("Down", {"x": 21, "y": 4}),
                        ("Left", {"x": 20, "y": 4}),
                        ("Left", {"x": 19, "y": 4}),
                        ("Down", {"x": 19, "y": 5}),
                    ]
                    print("Navigating B1F East...")
                    for d, c in steps_b1f:
                        if not walk_step(d, c):
                            success = False
                            break
                            
                    if success:
                        print("Bypassed wall! Walking Left along Row 5 to the Secret Key...")
                        curr = mgba.get_coordinates()
                        while curr['x'] > 1:
                            if not walk_step("Left", {"x": curr['x'] - 1, "y": 5}):
                                success = False
                                break
                            curr = mgba.get_coordinates()
                            
                        if success:
                            print("Reached (1, 5) on B1F West! Retrieving Secret Key...")
                            mgba.press_buttons(["Up"])
                            time.sleep(0.3)
                            mgba.press_buttons(["A"]) # "Obtained the SECRET KEY!"
                            time.sleep(1.5)
                            mgba.press_buttons(["A"]) # Dismiss
                            time.sleep(1.0)
                            pos = mgba.get_coordinates()
                            print(f"Secret Key retrieved successfully! Current position: {pos}")
                            
                            # 7. DIG escape!
                            print("Using DIG to escape...")
                            mgba.press_buttons(["Start", "sleep 300", "Down", "A", "sleep 300"])
                            for _ in range(5):
                                mgba.press_buttons(["Down", "sleep 150"])
                            mgba.press_buttons(["A", "sleep 300", "A"])
                            time.sleep(3.0)
                            print("Warped out! Final position:", mgba.get_coordinates())
                        else:
                            print("Failed to reach B1F West.")
                    else:
                        print("Failed to navigate B1F East.")
                else:
                    print(f"Unexpected B1F East landing: {pos}")
            else:
                print("Failed to navigate 1F East fenced room.")
        else:
            print("Failed to reach (26, 3) on 3F East.")
    else:
        print("Failed to navigate UP to (20, 3).")
else:
    print("Failed to navigate RIGHT to (20, 4).")
