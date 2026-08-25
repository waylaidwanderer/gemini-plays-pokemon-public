import mgba
import time
from PIL import Image

def handle_any_menu_or_battle():
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
        print(f"Menu/Battle detected! (B/W percentage: {percentage*100:.2f}%)")
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        
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
            print("Still in battle/menu. Attempting RUN...")
            mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A"])
            time.sleep(1.5)
            for _ in range(4):
                mgba.press_buttons(["B"])
                time.sleep(0.3)
        else:
            print("Successfully dismissed dialogue!")
        return True
    return False

def walk_step(direction, expected_coords, retries=15):
    for i in range(retries):
        if handle_any_menu_or_battle():
            pos = mgba.get_coordinates()
            if pos == expected_coords:
                print(f"Reached expected {expected_coords} after battle.")
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

# Starting at (2, 13) on 2F West (State B)
success = True

# 1. Walk to Column 5 Row 11 on 2F West
print("Walking to (5, 11) on 2F West...")
steps_to_5_11 = [
    ("Right", {"x": 3, "y": 13}),
    ("Right", {"x": 4, "y": 13}),
    ("Right", {"x": 5, "y": 13}),
    ("Up", {"x": 5, "y": 12}),
    ("Up", {"x": 5, "y": 11}),
]
for d, c in steps_to_5_11:
    if not walk_step(d, c):
        success = False
        break

if success:
    # 2. Walk to (6, 11)
    print("Walking to (6, 11)...")
    success = walk_step("Right", {"x": 6, "y": 11})
    
    if success:
        # 3. Walk UP Column 6 to Row 3 (Open in State B!)
        print("Walking UP Column 6 to Row 3...")
        steps_up_col6 = []
        for y in range(10, 2, -1):
            steps_up_col6.append(("Up", {"x": 6, "y": y}))
        for d, c in steps_up_col6:
            if not walk_step(d, c):
                success = False
                break
                
        if success:
            # 4. Walk RIGHT along Row 3 to Column 18 on 2F East
            print("Walking RIGHT along Row 3 to Column 18...")
            steps_right_row3 = []
            for x in range(7, 19):
                steps_right_row3.append(("Right", {"x": x, "y": 3}))
            for d, c in steps_right_row3:
                if not walk_step(d, c):
                    success = False
                    break
                    
            if success:
                # 5. Walk DOWN Column 18 to Row 10 (OPEN in State B!)
                print("Walking DOWN Column 18 to Row 10...")
                steps_down_col18 = []
                for y in range(4, 11):
                    steps_down_col18.append(("Down", {"x": 18, "y": y}))
                for d, c in steps_down_col18:
                    if not walk_step(d, c):
                        success = False
                        break
                        
                if success:
                    # 6. Walk LEFT along Row 10 to Column 15 Row 10
                    print("Walking LEFT along Row 10 to Column 15...")
                    steps_left_row10 = [
                        ("Left", {"x": 17, "y": 10}),
                        ("Left", {"x": 16, "y": 10}),
                        ("Left", {"x": 15, "y": 10}),
                    ]
                    for d, c in steps_left_row10:
                        if not walk_step(d, c):
                            success = False
                            break
                            
                    if success:
                        # 7. Step DOWN onto stairs at (15, 11) to warp UP to 3F East
                        print("Stepping DOWN onto stairs to warp UP...")
                        mgba.press_buttons(["Down"])
                        time.sleep(1.5)
                        pos = mgba.get_coordinates()
                        print(f"Warped UP to 3F East! Landing position: {pos}")
                        
                        # 8. On 3F East (landing at 16, 11), walk RIGHT to Column 20 (OPEN in State B!)
                        print("Walking RIGHT along Row 11 to Column 20...")
                        steps_to_col20_3f = []
                        for x in range(17, 21):
                            steps_to_col20_3f.append(("Right", {"x": x, "y": 11}))
                        for d, c in steps_to_col20_3f:
                            if not walk_step(d, c):
                                success = False
                                break
                                
                        if success:
                            # 9. Walk UP Column 20 to Row 3
                            print("Walking UP Column 20 to Row 3...")
                            steps_up_col20_3f = []
                            for y in range(10, 2, -1):
                                steps_up_col20_3f.append(("Up", {"x": 20, "y": y}))
                            for d, c in steps_up_col20_3f:
                                if not walk_step(d, c):
                                    success = False
                                    break
                                    
                            if success:
                                # 10. Walk RIGHT along Row 3 to Column 26 Row 3
                                print("Walking RIGHT along Row 3 to (26, 3)...")
                                steps_right_row3_3f = []
                                for x in range(21, 27):
                                    steps_right_row3_3f.append(("Right", {"x": x, "y": 3}))
                                for d, c in steps_right_row3_3f:
                                    if not walk_step(d, c):
                                        success = False
                                        break
                                        
                                if success:
                                    # 11. Step DOWN to trigger pitfall
                                    print("Stepping DOWN to trigger pitfall...")
                                    mgba.press_buttons(["Down"])
                                    time.sleep(2.0)
                                    pos = mgba.get_coordinates()
                                    print(f"Landed on 1F East inside fenced room! Position: {pos}")
                                    
                                    # 12. Walk to B1F East stairs
                                    steps_1f_east = [
                                        ("Up", {"x": 26, "y": 3}),
                                        ("Left", {"x": 25, "y": 3}),
                                        ("Left", {"x": 24, "y": 3}),
                                        ("Left", {"x": 23, "y": 3}),
                                        ("Left", {"x": 22, "y": 3}),
                                    ]
                                    for d, c in steps_1f_east:
                                        if not walk_step(d, c):
                                            success = False
                                            break
                                            
                                    if success:
                                        print("Reached (22, 3) on 1F East! Stepping UP onto stairs at (22, 2) to warp DOWN to B1F East...")
                                        mgba.press_buttons(["Up"])
                                        time.sleep(1.5)
                                        pos = mgba.get_coordinates()
                                        print(f"Warped DOWN to B1F East! Landing position: {pos}")
                                        
                                        # 13. On B1F East
                                        if pos == {"x": 22, "y": 3}:
                                            steps_b1f = [
                                                ("Left", {"x": 21, "y": 3}),
                                                ("Down", {"x": 21, "y": 4}),
                                                ("Left", {"x": 20, "y": 4}),
                                                ("Left", {"x": 19, "y": 4}),
                                                ("Down", {"x": 19, "y": 5}),
                                            ]
                                            for d, c in steps_b1f:
                                                if not walk_step(d, c):
                                                    success = False
                                                    break
                                                    
                                            if success:
                                                print("Successfully bypassed B1F East wall! Walking Left along Row 5 to the Secret Key...")
                                                curr = mgba.get_coordinates()
                                                while curr['x'] > 1:
                                                    if not walk_step("Left", {"x": curr['x'] - 1, "y": 5}):
                                                        success = False
                                                        break
                                                    curr = mgba.get_coordinates()
                                                    
                                                if success:
                                                    print("Successfully reached (1, 5) on B1F West! Standing facing UP and retrieving the Secret Key...")
                                                    mgba.press_buttons(["Up"])
                                                    time.sleep(0.3)
                                                    mgba.press_buttons(["A"])
                                                    time.sleep(1.5)
                                                    mgba.press_buttons(["A"])
                                                    time.sleep(1.0)
                                                    pos = mgba.get_coordinates()
                                                    print(f"Secret Key retrieved successfully! Current position: {pos}")
                                                    
                                                    # 17. Use DIG to escape to Cinnabar Island!
                                                    print("Using DIG to escape...")
                                                    mgba.press_buttons(["Start", "sleep 300", "Down", "A", "sleep 300"])
                                                    for _ in range(5):
                                                        mgba.press_buttons(["Down", "sleep 150"])
                                                    mgba.press_buttons(["A", "sleep 300", "A"])
                                                    time.sleep(3.0)
                                                    print("Warped out! Final position:", mgba.get_coordinates())
