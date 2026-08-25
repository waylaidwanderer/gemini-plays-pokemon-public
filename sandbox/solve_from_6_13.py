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

def toggle_switch_to_a():
    print("Toggling switch to State A (pressing A without UP to select YES)...")
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    mgba.press_buttons(["A"]) # YES
    time.sleep(1.2)
    mgba.press_buttons(["A"]) # Press A on "Pressed it!"
    time.sleep(1.2)
    
    # Dismiss any leftover text boxes
    for _ in range(4):
        mgba.press_buttons(["B"])
        time.sleep(0.3)
        
    pos = mgba.get_coordinates()
    print(f"Toggle to State A complete! Position: {pos}")
    return True

def toggle_switch_to_b():
    print("Toggling switch to State B (pressing A without UP to select YES)...")
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    mgba.press_buttons(["A"]) # YES
    time.sleep(1.2)
    mgba.press_buttons(["A"]) # Press A on "Pressed it!"
    time.sleep(1.2)
    
    # Dismiss any leftover text boxes
    for _ in range(4):
        mgba.press_buttons(["B"])
        time.sleep(0.3)
        
    pos = mgba.get_coordinates()
    print(f"Toggle to State B complete! Position: {pos}")
    return True

# Starting at (6, 13) on Cinnabar Island (State B)
success = True

# 1. Walk UP Column 6 to enter the Mansion door at (6, 3) on Cinnabar Island
print("Entering Pok�mon Mansion...")
steps_into_mansion = []
for y in range(12, 2, -1):
    steps_into_mansion.append(("Up", {"x": 6, "y": y}))
for d, c in steps_into_mansion:
    if not walk_step(d, c):
        success = False
        break

if success:
    print("Stepping UP onto doormat to enter...")
    mgba.press_buttons(["Up"])
    time.sleep(1.5)
    pos = mgba.get_coordinates()
    print(f"Entered Mansion 1F West! Position: {pos}")
    
    # 2. Walk to stairs at (5, 10) on 1F West (landing at 5, 27)
    if pos == {"x": 5, "y": 27}:
        print("Walking to stairs at (5, 10) on 1F West...")
        steps_1f_stairs = []
        for y in range(26, 9, -1):
            steps_1f_stairs.append(("Up", {"x": 5, "y": y}))
        for d, c in steps_1f_stairs:
            if not walk_step(d, c):
                success = False
                break
                
        if success:
            print("Stepping UP onto stairs to warp UP to 2F West...")
            mgba.press_buttons(["Up"])
            time.sleep(1.5)
            pos = mgba.get_coordinates()
            print(f"Warped UP to 2F West! Landing position: {pos}")
            
            # 3. Walk to (2, 12) on 2F West (landing at 5, 11)
            # Safe route using Column 5 Row 13 to avoid Column 2 balcony drop!
            print("Walking to (2, 12) on 2F West...")
            steps_to_2_12 = [
                ("Down", {"x": 5, "y": 12}),
                ("Down", {"x": 5, "y": 13}),
                ("Left", {"x": 4, "y": 13}),
                ("Left", {"x": 3, "y": 13}),
                ("Left", {"x": 2, "y": 13}),
                ("Up", {"x": 2, "y": 12}),
            ]
            for d, c in steps_to_2_12:
                if not walk_step(d, c):
                    success = False
                    break
                    
            if success:
                # 4. Face UP towards (2, 11) and toggle switch to State A
                print("Reached (2, 12)! Facing UP to toggle switch to State A...")
                mgba.press_buttons(["Up"])
                time.sleep(0.5)
                toggle_switch_to_a()
                
                # 5. Walk to (5, 11) on 2F West
                print("Walking to (5, 11)...")
                steps_back_to_5_11 = [
                    ("Down", {"x": 2, "y": 13}),
                    ("Right", {"x": 3, "y": 13}),
                    ("Right", {"x": 4, "y": 13}),
                    ("Right", {"x": 5, "y": 13}),
                    ("Up", {"x": 5, "y": 12}),
                    ("Up", {"x": 5, "y": 11}),
                ]
                for d, c in steps_back_to_5_11:
                    if not walk_step(d, c):
                        success = False
                        break
                        
                if success:
                    # 6. Walk RIGHT along Row 11 to Column 12 on 2F East
                    print("Walking RIGHT along Row 11 to (12, 11)...")
                    steps_right_row11 = []
                    for x in range(6, 13):
                        steps_right_row11.append(("Right", {"x": x, "y": 11}))
                    for d, c in steps_right_row11:
                        if not walk_step(d, c):
                            success = False
                            break
                            
                    if success:
                        # 7. Walk UP Column 12 to Row 7
                        print("Reached (12, 11)! Walking UP Column 12 to Row 7...")
                        steps_up_col12 = [
                            ("Up", {"x": 12, "y": 10}),
                            ("Up", {"x": 12, "y": 9}),
                            ("Up", {"x": 12, "y": 8}),
                            ("Up", {"x": 12, "y": 7}),
                        ]
                        for d, c in steps_up_col12:
                            if not walk_step(d, c):
                                success = False
                                break
                                
                        if success:
                            # 8. Walk RIGHT Row 7 to Column 15 on 2F East
                            print("Reached (12, 7)! Walking RIGHT to (15, 7)...")
                            steps_right_row7_stairs = [
                                ("Right", {"x": 13, "y": 7}),
                                ("Right", {"x": 14, "y": 7}),
                                ("Right", {"x": 15, "y": 7}),
                            ]
                            for d, c in steps_right_row7_stairs:
                                if not walk_step(d, c):
                                    success = False
                                    break
                                    
                            if success:
                                # 9. Walk RIGHT to Column 16, then DOWN Column 16 to Row 10 (OPEN in State A!)
                                print("Reached (15, 7)! Walking RIGHT to Column 16...")
                                success = walk_step("Right", {"x": 16, "y": 7})
                                
                                if success:
                                    print("Walking DOWN Column 16 to Row 10...")
                                    steps_down_col16 = [
                                        ("Down", {"x": 16, "y": 8}),
                                        ("Down", {"x": 16, "y": 9}),
                                        ("Down", {"x": 16, "y": 10}),
                                    ]
                                    for d, c in steps_down_col16:
                                        if not walk_step(d, c):
                                            success = False
                                            break
                                            
                                    if success:
                                        # 10. Walk LEFT to Column 15 Row 10, then step DOWN onto stairs at (15, 11) to warp UP to 3F East!
                                        print("Reached (16, 10)! Walking LEFT to (15, 10)...")
                                        success = walk_step("Left", {"x": 15, "y": 10})
                                        
                                        if success:
                                            print("Reached (15, 10)! Stepping DOWN onto stairs at (15, 11)...")
                                            mgba.press_buttons(["Down"])
                                            time.sleep(1.5)
                                            pos = mgba.get_coordinates()
                                            print(f"Warped UP to 3F East! Landing position: {pos}")
                                            
                                            # 11. On 3F East (landing at 16, 11), use Row 12 bypass to reach switch at (12, 11)
                                            print("Using Row 12 bypass on 3F East to reach switch...")
                                            steps_left_row12_3f = [
                                                ("Down", {"x": 16, "y": 12}), # Open in State A!
                                                ("Left", {"x": 15, "y": 12}),
                                                ("Left", {"x": 14, "y": 12}),
                                                ("Left", {"x": 13, "y": 12}),
                                                ("Left", {"x": 12, "y": 12}),
                                            ]
                                            for d, c in steps_left_row12_3f:
                                                if not walk_step(d, c):
                                                    success = False
                                                    break
                                                    
                                            if success:
                                                print("Reached (12, 12) on 3F East! Facing UP to toggle switch to State B...")
                                                mgba.press_buttons(["Up"])
                                                time.sleep(0.5)
                                                toggle_switch_to_b()
                                                
                                                # 12. Walk to Column 20 on 3F East (State B)
                                                print("Walking UP to (12, 11)...")
                                                success = walk_step("Up", {"x": 12, "y": 11})
                                                if success:
                                                    print("Walking RIGHT along Row 11 to Column 20...")
                                                    steps_to_col20 = [
                                                        ("Right", {"x": 13, "y": 11}),
                                                        ("Right", {"x": 14, "y": 11}),
                                                        ("Right", {"x": 15, "y": 11}),
                                                        ("Right", {"x": 16, "y": 11}),
                                                        ("Right", {"x": 17, "y": 11}),
                                                        ("Right", {"x": 18, "y": 11}),
                                                        ("Right", {"x": 19, "y": 11}),
                                                        ("Right", {"x": 20, "y": 11}),
                                                        ("Up", {"x": 20, "y": 10}),
                                                    ]
                                                    for d, c in steps_to_col20:
                                                        if not walk_step(d, c):
                                                            success = False
                                                            break
                                                            
                                                    if success:
                                                        # 13. Walk UP Column 20 to Row 3, RIGHT to (26, 3), and step DOWN to drop through pitfall!
                                                        print("Reached (20, 11)! Walking UP Column 20 to Row 3...")
                                                        steps_up_col20_3f = []
                                                        for y in range(10, 2, -1):
                                                            steps_up_col20_3f.append(("Up", {"x": 20, "y": y}))
                                                        for d, c in steps_up_col20_3f:
                                                            if not walk_step(d, c):
                                                                success = False
                                                                break
                                                                
                                                        if success:
                                                            print("Reached (20, 3)! Walking RIGHT along Row 3 to (26, 3)...")
                                                            steps_right_row3_3f = []
                                                            for x in range(21, 27):
                                                                steps_right_row3_3f.append(("Right", {"x": x, "y": 3}))
                                                            for d, c in steps_right_row3_3f:
                                                                if not walk_step(d, c):
                                                                    success = False
                                                                    break
                                                                    
                                                            if success:
                                                                # 14. Step DOWN to trigger pitfall
                                                                print("Reached (26, 3)! Stepping DOWN to trigger pitfall...")
                                                                mgba.press_buttons(["Down"])
                                                                time.sleep(2.0)
                                                                pos = mgba.get_coordinates()
                                                                print(f"Landed on 1F East inside fenced room! Position: {pos}")
                                                                
                                                                # 15. Walk to B1F East stairs
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
                                                                    
                                                                    # 16. On B1F East
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
