import mgba
import time
from PIL import Image

def handle_any_menu_or_battle():
    # Take a screenshot
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file)
    img_std = img.resize((160, 144), Image.Resampling.NEAREST)
    
    # Check if a text box is active
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
        
        # Re-check if still in battle
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

# Step 1: Use DIG to warp to Cinnabar Island
print("Executing DIG escape...")
mgba.press_buttons(["Start", "sleep 400"])
handle_any_menu_or_battle()
mgba.press_buttons(["Down", "sleep 150", "A", "sleep 500"]) # opens PKMN menu
# Go to Slot 6 (TRUFFLE)
for _ in range(5):
    mgba.press_buttons(["Down", "sleep 150"])
mgba.press_buttons(["A", "sleep 400"]) # Selects TRUFFLE
mgba.press_buttons(["A", "sleep 3000"]) # Selects DIG (1st move option)

pos = mgba.get_coordinates()
print("Warped out! Position:", pos)
if pos == {"x": 11, "y": 12}:
    print("Successfully escaped to Cinnabar Island!")
else:
    print("Warning: unexpected coordinates after DIG:", pos)

# Step 2: Walk to Mansion entrance (6, 3) and enter
steps_to_mansion = [
    ("Right", {"x": 12, "y": 12}),
    ("Right", {"x": 13, "y": 12}),
    ("Right", {"x": 14, "y": 12}),
    ("Right", {"x": 15, "y": 12}),
    ("Right", {"x": 16, "y": 12}),
    ("Right", {"x": 17, "y": 12}),
    ("Right", {"x": 18, "y": 12}),
    ("Up", {"x": 18, "y": 11}),
    ("Up", {"x": 18, "y": 10}),
    ("Up", {"x": 18, "y": 9}),
    ("Up", {"x": 18, "y": 8}),
    ("Up", {"x": 18, "y": 7}),
    ("Up", {"x": 18, "y": 6}),
    ("Up", {"x": 18, "y": 5}),
    ("Left", {"x": 17, "y": 5}),
    ("Left", {"x": 16, "y": 5}),
    ("Left", {"x": 15, "y": 5}),
    ("Left", {"x": 14, "y": 5}),
    ("Left", {"x": 13, "y": 5}),
    ("Left", {"x": 12, "y": 5}),
    ("Left", {"x": 11, "y": 5}),
    ("Left", {"x": 10, "y": 5}),
    ("Left", {"x": 9, "y": 5}),
    ("Left", {"x": 8, "y": 5}),
    ("Left", {"x": 7, "y": 5}),
    ("Left", {"x": 6, "y": 5}),
    ("Up", {"x": 6, "y": 4}),
    ("Up", {"x": 6, "y": 3}),
]
print("Walking to Mansion entrance...")
success = True
for d, c in steps_to_mansion:
    if not walk_step(d, c):
        success = False
        break

if success:
    print("At (6, 3) on Cinnabar Island. Stepping UP into Mansion 1F West...")
    mgba.press_buttons(["Up"])
    time.sleep(1.5)
    pos = mgba.get_coordinates()
    print("Inside Mansion 1F West! Position:", pos)
    
    # Step 3: Inside 1F West (State A), walk up Column 5 to Row 11
    # Walk to (5, 11) -> (8, 11) -> (8, 10) -> (5, 10) -> warp to 2F West (5, 11)
    # Let's walk UP Column 5 first from (5, 27) to (5, 11)
    print("Walking UP Column 5 to Row 11...")
    for y in range(26, 10, -1):
        if not walk_step("Up", {"x": 5, "y": y}):
            success = False
            break
            
    if success:
        steps_1f_stairs = [
            ("Right", {"x": 6, "y": 11}),
            ("Right", {"x": 7, "y": 11}),
            ("Right", {"x": 8, "y": 11}),
            ("Up", {"x": 8, "y": 10}),
            ("Left", {"x": 7, "y": 10}),
            ("Left", {"x": 6, "y": 10}),
            ("Left", {"x": 5, "y": 10}),
        ]
        print("Walking to stairs at (5, 10)...")
        for d, c in steps_1f_stairs:
            if not walk_step(d, c):
                success = False
                break
                
        if success:
            print("At (5, 10) on 1F West! Stepping LEFT to warp to 2F West...")
            mgba.press_buttons(["Left"])
            time.sleep(1.5)
            pos = mgba.get_coordinates()
            print("Landed on 2F West! Position:", pos)
            
            # Step 4: On 2F West, walk UP Column 5 to Row 6, then RIGHT to Column 12, then UP to Row 1
            if pos == {"x": 5, "y": 11}:
                steps_2f_east = [
                    ("Up", {"x": 5, "y": 10}),
                    ("Up", {"x": 5, "y": 9}),
                    ("Up", {"x": 5, "y": 8}),
                    ("Up", {"x": 5, "y": 7}),
                    ("Up", {"x": 5, "y": 6}),
                    ("Right", {"x": 6, "y": 6}),
                    ("Right", {"x": 7, "y": 6}),
                    ("Right", {"x": 8, "y": 6}),
                    ("Right", {"x": 9, "y": 6}),
                    ("Right", {"x": 10, "y": 6}),
                    ("Right", {"x": 11, "y": 6}),
                    ("Right", {"x": 12, "y": 6}),
                    ("Up", {"x": 12, "y": 5}),
                    ("Up", {"x": 12, "y": 4}),
                    ("Up", {"x": 12, "y": 3}),
                    ("Up", {"x": 12, "y": 2}),
                    ("Up", {"x": 12, "y": 1}),
                ]
                print("Walking to 2F East (12, 1)...")
                for d, c in steps_2f_east:
                    if not walk_step(d, c):
                        success = False
                        break
                        
                if success:
                    print("Successfully reached (12, 1) on 2F East! Now proceeding with key complete logic...")
                    
                    # 5. Walk DOWN Column 12 to Row 7
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
                        # 6. Walk RIGHT along Row 7 to Column 15
                        print("Walking RIGHT along Row 7 to Column 15...")
                        steps_right_row7 = [
                            ("Right", {"x": 13, "y": 7}),
                            ("Right", {"x": 14, "y": 7}),
                            ("Right", {"x": 15, "y": 7}),
                        ]
                        for d, c in steps_right_row7:
                            if not walk_step(d, c):
                                success = False
                                break

                    if success:
                        # 7. Walk DOWN Column 15 to stairs at (15, 11) to warp UP to 3F East
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
                            print("Walking DOWN onto stairs at (15, 11) to warp UP...")
                            mgba.press_buttons(["Down"])
                            time.sleep(1.5)
                            pos = mgba.get_coordinates()
                            print(f"Warped UP to 3F East! Position: {pos}")
                            
                            # 8. On 3F East, walk LEFT to (12, 11)
                            steps_3f_switch = [
                                ("Left", {"x": 14, "y": 11}),
                                ("Left", {"x": 13, "y": 11}),
                                ("Left", {"x": 12, "y": 11}),
                            ]
                            for d, c in steps_3f_switch:
                                if not walk_step(d, c):
                                    success = False
                                    break
                                    
                            if success:
                                print("At (12, 11) on 3F East! Checking gate state...")
                                if walk_step("Down", {"x": 12, "y": 12}, retries=2):
                                    print("Mansion is in STATE A. Toggling to STATE B...")
                                    mgba.press_buttons(["Up"])
                                    time.sleep(0.3)
                                    mgba.press_buttons(["A"]) # "A secret switch!"
                                    time.sleep(0.8)
                                    mgba.press_buttons(["A"]) # select YES
                                    time.sleep(0.8)
                                    mgba.press_buttons(["A"]) # "Pressed it!"
                                    time.sleep(0.8)
                                    walk_step("Up", {"x": 12, "y": 11})
                                else:
                                    print("Mansion is ALREADY in STATE B. Skipping toggle!")
                                    
                                # 9. Walk to pitfall at (26, 3) and DOWN to drop
                                steps_to_drop = [
                                    ("Up", {"x": 12, "y": 11}),
                                    ("Right", {"x": 13, "y": 11}),
                                    ("Right", {"x": 14, "y": 11}),
                                    ("Right", {"x": 15, "y": 11}),
                                    ("Right", {"x": 16, "y": 11}),
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
                                for d, c in steps_to_drop:
                                    if not walk_step(d, c):
                                        success = False
                                        break
                                        
                                if success:
                                    print("At (26, 3) on 3F East! Stepping DOWN onto pitfall...")
                                    mgba.press_buttons(["Down"])
                                    time.sleep(2.0)
                                    pos = mgba.get_coordinates()
                                    print(f"Landed on 1F East inside fenced room! Position: {pos}")
                                    
                                    # 10. Walk to B1F East stairs
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
                                        print("At (22, 3) on 1F East! Stepping UP to warp DOWN to B1F East...")
                                        mgba.press_buttons(["Up"])
                                        time.sleep(1.5)
                                        pos = mgba.get_coordinates()
                                        print(f"Warped DOWN to B1F East! Position: {pos}")
                                        
                                        # 11. Cross B1F East to B1F West
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
                                                    
                                                    # 12. DIG escape!
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
                                print("Failed to reach (12, 11) on 3F East.")
                        else:
                            print("Failed to reach stairs at (15, 11).")
                    else:
                        print("Failed to navigate 2F East.")
                else:
                    print("Failed to navigate 2F West.")
            else:
                print("Failed to reach (5, 11) on 2F West.")
        else:
            print("Failed to reach (5, 10) on 1F West.")
    else:
        print("Failed to navigate Column 5 UP to Row 11.")
else:
    print("Failed to reach Cinnabar Mansion entrance.")
