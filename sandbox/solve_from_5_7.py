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

# Starting at (5, 7) on 1F West (State A)
success = True

# 1. Walk UP Column 5 to Row 4
print("Walking UP Column 5 to Row 4...")
steps_up_col5 = [
    ("Up", {"x": 5, "y": 6}),
    ("Up", {"x": 5, "y": 5}),
    ("Up", {"x": 5, "y": 4}),
]
for d, c in steps_up_col5:
    if not walk_step(d, c):
        success = False
        break

if success:
    # 2. Walk LEFT along Row 4 to Column 0
    print("Walking LEFT along Row 4 to Column 0...")
    steps_left_row4 = [
        ("Left", {"x": 4, "y": 4}),
        ("Left", {"x": 3, "y": 4}),
        ("Left", {"x": 2, "y": 4}),
        ("Left", {"x": 1, "y": 4}),
        ("Left", {"x": 0, "y": 4}), # Stairs entrance
    ]
    for d, c in steps_left_row4:
        if not walk_step(d, c):
            success = False
            break
            
    if success:
        # 3. Step UP onto stairs at (0, 3) to warp UP to 2F West
        print("Stepping UP onto stairs to warp UP...")
        mgba.press_buttons(["Up"])
        time.sleep(1.5)
        pos = mgba.get_coordinates()
        print(f"Warped UP to 2F West! Landing position: {pos}")
        
        # 4. Walk RIGHT along Row 4 to Column 15 on 2F East
        print("Walking RIGHT along Row 4 to Column 15 on 2F East...")
        # Note: landing is typically (0, 4) on 2F West. We walk right to (15, 4).
        curr = mgba.get_coordinates()
        while curr['x'] < 15:
            if not walk_step("Right", {"x": curr['x'] + 1, "y": 4}):
                success = False
                break
            curr = mgba.get_coordinates()
            
        if success:
            # 5. Walk DOWN Column 15 directly onto stairs at (15, 11) (OPEN in State A!)
            print("Reached (15, 4)! Walking DOWN Column 15 to stairs...")
            steps_down_col15 = []
            for y in range(5, 11):
                steps_down_col15.append(("Down", {"x": 15, "y": y}))
            for d, c in steps_down_col15:
                if not walk_step(d, c):
                    success = False
                    break
                    
            if success:
                print("Reached (15, 10)! Stepping DOWN onto stairs at (15, 11)...")
                mgba.press_buttons(["Down"])
                time.sleep(1.5)
                pos = mgba.get_coordinates()
                print(f"Warped UP to 3F East! Landing position: {pos}")
                
                # 6. On 3F East (landing at 16, 11), walk LEFT along Row 11 to (12, 11)
                print("Walking LEFT to (12, 11) on 3F East...")
                steps_left_3f = [
                    ("Left", {"x": 15, "y": 11}), # Open on Row 11 in State A? Yes!
                    ("Left", {"x": 14, "y": 11}),
                    ("Left", {"x": 13, "y": 11}),
                    ("Left", {"x": 12, "y": 11}),
                ]
                # Wait! If the gate on Row 11 of 3F East is CLOSED in State A:
                # We can bypass it by walking RIGHT to Column 20, UP Column 20 to Row 3...
                # Oh! But the switch is at (12, 11). How do we reach (12, 11) to toggle State B?
                # Wait! If we are on 3F East in State A, can we walk left?
                # "while Row 11 gates are CLOSED in State A and OPEN in State B"
                # So Row 11 gate on 3F East is CLOSED in State A!
                # But Row 12 gates are OPEN in State A!
                # "Row 12 gates on 3F East are OPEN in State A and CLOSED in State B!"
                # So we can walk LEFT along Row 12 to (12, 12)!
                # Let's use Row 12 instead of Row 11 to go left:
                # From (16, 11) on 3F East:
                # - Walk DOWN to (16, 12).
                # - Walk LEFT along Row 12 to (12, 12): (16, 12) -> (15, 12) -> (14, 12) -> (13, 12) -> (12, 12). (OPEN in State A!).
                # - Face UP towards (12, 11) and toggle to State B!
                print("Using Row 12 bypass to reach switch in State A...")
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
                    
                    # 7. Walk to Column 20 on 3F East (State B)
                    # Note: Row 12 gates are now CLOSED in State B!
                    # But Row 11 gates are now OPEN in State B!
                    # So we walk UP to Row 11: (12, 11)
                    # Walk RIGHT along Row 11 to Column 20: (12, 11) -> (20, 11) (OPEN in State B!)
                    print("Walking UP to (12, 11)...")
                    success = walk_step("Up", {"x": 12, "y": 11})
                    if success:
                        print("Walking RIGHT along Row 11 to Column 20...")
                        steps_to_col20_3f = []
                        for x in range(13, 21):
                            steps_to_col20_3f.append(("Right", {"x": x, "y": 11}))
                        for d, c in steps_to_col20_3f:
                            if not walk_step(d, c):
                                success = False
                                break
                                
                        if success:
                            # 8. Walk UP Column 20 to Row 3
                            print("Walking UP Column 20 to Row 3...")
                            steps_up_col20_3f = []
                            for y in range(10, 2, -1):
                                steps_up_col20_3f.append(("Up", {"x": 20, "y": y}))
                            for d, c in steps_up_col20_3f:
                                if not walk_step(d, c):
                                    success = False
                                    break
                                    
                            if success:
                                # 9. Walk RIGHT along Row 3 to Column 26 Row 3
                                print("Walking RIGHT along Row 3 to (26, 3)...")
                                steps_right_row3_3f = []
                                for x in range(21, 27):
                                    steps_right_row3_3f.append(("Right", {"x": x, "y": 3}))
                                for d, c in steps_right_row3_3f:
                                    if not walk_step(d, c):
                                        success = False
                                        break
                                        
                                if success:
                                    # 10. Step DOWN to trigger pitfall
                                    print("Stepping DOWN to trigger pitfall...")
                                    mgba.press_buttons(["Down"])
                                    time.sleep(2.0)
                                    pos = mgba.get_coordinates()
                                    print(f"Landed on 1F East inside fenced room! Position: {pos}")
                                    
                                    # 11. Walk to B1F East stairs
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
                                        
                                        # 12. On B1F East
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
                                                    
                                                    # 13. Use DIG to escape to Cinnabar Island!
                                                    print("Using DIG to escape...")
                                                    mgba.press_buttons(["Start", "sleep 300", "Down", "A", "sleep 300"])
                                                    for _ in range(5):
                                                        mgba.press_buttons(["Down", "sleep 150"])
                                                    mgba.press_buttons(["A", "sleep 300", "A"])
                                                    time.sleep(3.0)
                                                    print("Warped out! Final position:", mgba.get_coordinates())
