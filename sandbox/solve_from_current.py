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

# Starting at (5, 11) on 2F West (State A)
print("Starting Mansion final stage from (5, 11)...")
success = True

# 1. Walk RIGHT to Column 12
steps_to_col12 = [
    ("Right", {"x": 6, "y": 11}),
    ("Right", {"x": 7, "y": 11}),
    ("Right", {"x": 8, "y": 11}),
    ("Right", {"x": 9, "y": 11}),
    ("Right", {"x": 10, "y": 11}),
    ("Right", {"x": 11, "y": 11}),
    ("Right", {"x": 12, "y": 11}),
]
print("Walking RIGHT along Row 11 to Column 12...")
for d, c in steps_to_col12:
    if not walk_step(d, c):
        success = False
        break
        
if success:
    # 2. Walk UP Column 12 to Row 1
    print("Walking UP Column 12 to Row 1...")
    for y in range(10, 0, -1):
        if not walk_step("Up", {"x": 12, "y": y}):
            success = False
            break
            
    if success:
        print("Successfully reached (12, 1) on 2F East! Now proceeding with key complete logic...")
        
        # 3. Walk DOWN Column 12 to Row 7
        print("Walking DOWN Column 12 to Row 7...")
        steps_down_col12 = [
            ("Down", {"x": 12, "y": 2}),
            ("Down", {"x": 12, "y": 3}),
            ("Down", {"x": 12, "y": 4}),
            ("Down", {"x": 12, "y": 5}),
            ("Down", {"x": 12, "y": 6}),
            ("Down", {"x": 12, "y": 7}),
        ]
        for d, c in steps_down_col12:
            if not walk_step(d, c):
                success = False
                break

        if success:
            # 4. Walk RIGHT along Row 7 to Column 18
            print("Walking RIGHT along Row 7 to Column 18...")
            steps_right_row7 = [
                ("Right", {"x": 13, "y": 7}),
                ("Right", {"x": 14, "y": 7}),
                ("Right", {"x": 15, "y": 7}),
                ("Right", {"x": 16, "y": 7}),
                ("Right", {"x": 17, "y": 7}),
                ("Right", {"x": 18, "y": 7}),
            ]
            for d, c in steps_right_row7:
                if not walk_step(d, c):
                    success = False
                    break

        if success:
            # 5. Walk DOWN Column 18 to Row 11
            print("Walking DOWN Column 18 to Row 11...")
            steps_down_col18 = [
                ("Down", {"x": 18, "y": 8}),
                ("Down", {"x": 18, "y": 9}),
                ("Down", {"x": 18, "y": 10}),
                ("Down", {"x": 18, "y": 11}),
            ]
            for d, c in steps_down_col18:
                if not walk_step(d, c):
                    success = False
                    break
                    
            if success:
                # 6. Walk LEFT along Row 11 to Column 15 stairs
                print("Walking LEFT to stairs at (15, 11)...")
                steps_to_stairs = [
                    ("Left", {"x": 17, "y": 11}),
                    ("Left", {"x": 16, "y": 11}),
                ]
                for d, c in steps_to_stairs:
                    if not walk_step(d, c):
                        success = False
                        break
                        
                if success:
                    print("At (16, 11)! Stepping LEFT onto stairs to warp UP to 3F East...")
                    mgba.press_buttons(["Left"])
                    time.sleep(1.5)
                    pos = mgba.get_coordinates()
                    print(f"Warped UP to 3F East! Position: {pos}")
                    
                    # 7. On 3F East, walk RIGHT to Column 18
                    steps_3f_east_stairs = [
                        ("Right", {"x": 17, "y": 11}),
                        ("Right", {"x": 18, "y": 11}),
                    ]
                    print("Walking RIGHT to Column 18 on 3F East...")
                    for d, c in steps_3f_east_stairs:
                        if not walk_step(d, c):
                            success = False
                            break
                            
                    if success:
                        print("Walking UP Column 18 to Row 7...")
                        steps_up_col18_3f = [
                            ("Up", {"x": 18, "y": 10}),
                            ("Up", {"x": 18, "y": 9}),
                            ("Up", {"x": 18, "y": 8}),
                            ("Up", {"x": 18, "y": 7}),
                        ]
                        for d, c in steps_up_col18_3f:
                            if not walk_step(d, c):
                                success = False
                                break
                                
                    if success:
                        # Walk LEFT along Row 7 to Column 12
                        print("Walking LEFT along Row 7 to Column 12...")
                        steps_left_row7_3f = [
                            ("Left", {"x": 17, "y": 7}),
                            ("Left", {"x": 16, "y": 7}),
                            ("Left", {"x": 15, "y": 7}),
                            ("Left", {"x": 14, "y": 7}),
                            ("Left", {"x": 13, "y": 7}),
                            ("Left", {"x": 12, "y": 7}),
                        ]
                        for d, c in steps_left_row7_3f:
                            if not walk_step(d, c):
                                success = False
                                break
                                
                    if success:
                        # Walk DOWN Column 12 to Row 12
                        print("Walking DOWN Column 12 to Row 12...")
                        steps_down_col12_3f = [
                            ("Down", {"x": 12, "y": 8}),
                            ("Down", {"x": 12, "y": 9}),
                            ("Down", {"x": 12, "y": 10}),
                            ("Down", {"x": 12, "y": 11}),
                            ("Down", {"x": 12, "y": 12}),
                        ]
                        for d, c in steps_down_col12_3f:
                            if not walk_step(d, c):
                                success = False
                                break
                                
                    if success:
                        print("At (12, 12) on 3F East! Facing UP towards switch at (12, 11)...")
                        mgba.press_buttons(["Up"])
                        time.sleep(0.4)
                        # Toggle switch to State B
                        mgba.press_buttons(["A"]) # "A secret switch!"
                        time.sleep(0.8)
                        mgba.press_buttons(["A"]) # select YES
                        time.sleep(0.8)
                        mgba.press_buttons(["A"]) # "Pressed it!"
                        time.sleep(0.8)
                        print("Successfully toggled switch to State B!")
                        
                        # B1. Walk UP Column 12 to Row 6
                        steps_up_col12_to_row6 = [
                            ("Up", {"x": 12, "y": 11}),
                            ("Up", {"x": 12, "y": 10}),
                            ("Up", {"x": 12, "y": 9}),
                            ("Up", {"x": 12, "y": 8}),
                            ("Up", {"x": 12, "y": 7}),
                            ("Up", {"x": 12, "y": 6}),
                        ]
                        print("Walking UP Column 12 to Row 6...")
                        for d, c in steps_up_col12_to_row6:
                            if not walk_step(d, c):
                                success = False
                                break
                                
                        if success:
                            # B2. Walk RIGHT along Row 6 to Column 21
                            print("Walking RIGHT along Row 6 to Column 21...")
                            for x in range(13, 22):
                                if not walk_step("Right", {"x": x, "y": 6}):
                                    success = False
                                    break
                                    
                            if success:
                                # B3. Walk LEFT 2 steps to (19, 6)
                                print("Walking LEFT to (19, 6)...")
                                steps_left_to_19 = [
                                    ("Left", {"x": 20, "y": 6}),
                                    ("Left", {"x": 19, "y": 6}),
                                ]
                                for d, c in steps_left_to_19:
                                    if not walk_step(d, c):
                                        success = False
                                        break
                                        
                                if success:
                                    # B4. Walk UP to (19, 5), UP to (19, 4), RIGHT to (20, 4), UP to (20, 3) (to bypass the Row 3 Column 19 wall!)
                                    steps_bypass_row3 = [
                                        ("Up", {"x": 19, "y": 5}),
                                        ("Up", {"x": 19, "y": 4}),
                                        ("Right", {"x": 20, "y": 4}),
                                        ("Up", {"x": 20, "y": 3}),
                                    ]
                                    print("Bypassing Row 3 Column 19 wall...")
                                    for d, c in steps_bypass_row3:
                                        if not walk_step(d, c):
                                            success = False
                                            break
                                            
                                    if success:
                                        # B5. Walk RIGHT to Column 26
                                        print("Walking RIGHT along Row 3 to Column 26...")
                                        for x in range(21, 27):
                                            if not walk_step("Right", {"x": x, "y": 3}):
                                                success = False
                                                break
                                                
                                        if success:
                                            # B6. Step DOWN onto pitfall at (26, 4)
                                            print("At (26, 3) on 3F East! Stepping DOWN onto pitfall...")
                                            mgba.press_buttons(["Down"])
                                            time.sleep(2.0)
                                            pos = mgba.get_coordinates()
                                            print(f"Landed on 1F East inside fenced room! Position: {pos}")
                                            
                                            # B7. Walk to B1F East stairs
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
                                                
                                                # B8. Cross B1F East to B1F West
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
                                                            
                                                            # B9. DIG escape!
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
                                        print("Failed to bypass Row 3 Column 19 wall.")
                                 else:
                                    print("Failed to reach (19, 6).")
                            else:
                                print("Failed to navigate Row 6 horizontally.")
                        else:
                            print("Failed to navigate Column 12 UP to Row 6.")
                    else:
                        print("Failed to navigate DOWN Column 12.")
                else:
                    print("Failed to navigate Row 7.")
            else:
                print("Failed to reach Row 7 Column 18.")
        else:
            print("Failed to reach Row 11 Column 18.")
    else:
        print("Failed to navigate Row 7 horizontally.")
else:
    print("Failed to navigate Column 12 UP.")
else:
    print("Failed to reach Column 12.")
