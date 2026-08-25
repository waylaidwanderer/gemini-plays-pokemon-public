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
            print("Still in battle/menu. Attempting SURF battle routine...")
            # Fight (A) -> Select Move 4 SURF (Down, Down, Down, A)
            mgba.press_buttons(["A", "sleep 400", "Down", "sleep 150", "Down", "sleep 150", "Down", "sleep 150", "A"])
            time.sleep(2.0)
            for _ in range(12):
                mgba.press_buttons(["A"])
                time.sleep(0.4)
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
    print("Toggling switch to State B...")
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

# Starting at (11, 12) on Cinnabar Island (State A)
success = True

# 1. Walk to (6, 3) on Cinnabar Island using safe Row 4 path to bypass Center and Lab door warps!
print("Walking to Mansion entrance...")
steps_cinnabar = [
    ("Up", {"x": 11, "y": 4}),
    ("Left", {"x": 10, "y": 4}),
    ("Left", {"x": 9, "y": 4}),
    ("Left", {"x": 8, "y": 4}),
    ("Left", {"x": 7, "y": 4}),
    ("Left", {"x": 6, "y": 4}),
    ("Up", {"x": 6, "y": 3}),
]
for d, c in steps_cinnabar:
    if not walk_step(d, c):
        success = False
        break

if success:
    print("Stepping UP to enter Pokémon Mansion...")
    mgba.press_buttons(["Up"])
    time.sleep(1.5)
    pos = mgba.get_coordinates()
    print(f"Entered Mansion 1F West! Position: {pos}")
    
    # 2. Walk to stairs at (5, 10) on 1F West
    if pos == {"x": 5, "y": 27}:
        print("Walking to stairs at (5, 10)...")
        steps_1f = []
        for y in range(26, 9, -1):
            steps_1f.append(("Up", {"x": 5, "y": y}))
        for d, c in steps_1f:
            if not walk_step(d, c):
                success = False
                break
                
        if success:
            print("Stepping UP to warp to 2F West...")
            mgba.press_buttons(["Up"])
            time.sleep(1.5)
            pos = mgba.get_coordinates()
            print(f"Warped UP to 2F West! Landing position: {pos}")
            
            # 3. Walk to stairs at (7, 10) on 2F West
            if pos == {"x": 5, "y": 11}:
                print("Walking to stairs at (7, 10) on 2F West...")
                steps_2f = [
                    ("Right", {"x": 6, "y": 11}),
                    ("Right", {"x": 7, "y": 11}),
                ]
                for d, c in steps_2f:
                    if not walk_step(d, c):
                        success = False
                        break
                        
                if success:
                    print("Stepping UP to warp to 3F West...")
                    mgba.press_buttons(["Up"])
                    time.sleep(1.5)
                    pos = mgba.get_coordinates()
                    print(f"Warped UP to 3F West! Landing position: {pos}")
                    
                    # 4. Walk to (2, 12) on 3F West (Mansion is currently in State A!)
                    if pos == {"x": 7, "y": 11}:
                        print("Walking to (2, 12) on 3F West...")
                        steps_to_row13 = [
                            ("Down", {"x": 7, "y": 12}),
                            ("Down", {"x": 7, "y": 13}),
                        ]
                        for d, c in steps_to_row13:
                            if not walk_step(d, c):
                                success = False
                                break
                                
                        if success:
                            print("Walking LEFT along Row 13 to Column 1...")
                            steps_left_row13 = []
                            for x in range(6, 0, -1):
                                steps_left_row13.append(("Left", {"x": x, "y": 13}))
                            for d, c in steps_left_row13:
                                if not walk_step(d, c):
                                    success = False
                                    break
                                    
                            if success:
                                print("Walking around solid diary to (2, 12)...")
                                steps_to_2_12 = [
                                    ("Up", {"x": 1, "y": 12}),
                                    ("Right", {"x": 2, "y": 12}),
                                ]
                                for d, c in steps_to_2_12:
                                    if not walk_step(d, c):
                                        success = False
                                        break
                                        
                                if success:
                                    print("Facing UP towards switch at (2, 11)...")
                                    mgba.press_buttons(["Up"])
                                    time.sleep(0.5)
                                    toggle_switch_to_b()
                                    
                                    # 5. Mansion is now in State B! Walk LEFT back to (1, 12)
                                    print("Walking LEFT to (1, 12)...")
                                    if walk_step("Left", {"x": 1, "y": 12}):
                                        # 6. Walk to (5, 11) using Row 13 bypass
                                        print("Walking to (5, 11)...")
                                        steps_to_5_11 = [
                                            ("Down", {"x": 1, "y": 13}),
                                            ("Right", {"x": 2, "y": 13}),
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
                                            # 7. Walk UP Column 6 to Row 8 (open in State B!)
                                            print("Walking UP Column 6 to Row 8...")
                                            steps_up_col6 = [
                                                ("Right", {"x": 6, "y": 11}),
                                                ("Up", {"x": 6, "y": 10}),
                                                ("Up", {"x": 6, "y": 9}),
                                                ("Up", {"x": 6, "y": 8}),
                                            ]
                                            for d, c in steps_up_col6:
                                                if not walk_step(d, c):
                                                    success = False
                                                    break
                                                    
                                            if success:
                                                # 8. Walk LEFT to (5, 8)
                                                print("Walking LEFT to (5, 8)...")
                                                if walk_step("Left", {"x": 5, "y": 8}):
                                                    # 9. Walk UP Column 5 to Row 3
                                                    print("Walking UP Column 5 to Row 3...")
                                                    steps_up_col5 = [
                                                        ("Up", {"x": 5, "y": 7}),
                                                        ("Up", {"x": 5, "y": 6}),
                                                        ("Up", {"x": 5, "y": 5}),
                                                        ("Up", {"x": 5, "y": 4}),
                                                        ("Up", {"x": 5, "y": 3}),
                                                    ]
                                                    for d, c in steps_up_col5:
                                                        if not walk_step(d, c):
                                                            success = False
                                                            break
                                                            
                                                    if success:
                                                        # 10. Walk RIGHT along Row 3 to (26, 3) on 3F East
                                                        print("Walking RIGHT along Row 3 to (26, 3)...")
                                                        steps_right_row3 = []
                                                        for x in range(6, 27):
                                                            steps_right_row3.append(("Right", {"x": x, "y": 3}))
                                                        for d, c in steps_right_row3:
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
                                                            
                                                            # 12. Walk to B1F East stairs (stairs are at 22, 2)
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
                                                                print("Stepping UP onto stairs to warp DOWN to B1F East...")
                                                                mgba.press_buttons(["Up"])
                                                                time.sleep(1.5)
                                                                pos = mgba.get_coordinates()
                                                                print(f"Warped DOWN to B1F East! Position: {pos}")
                                                                
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
                                                                            
                                                                            # 14. Use DIG to escape to Cinnabar Island!
                                                                            print("Using DIG to escape...")
                                                                            mgba.press_buttons(["Start", "sleep 300", "Down", "A", "sleep 300"])
                                                                            for _ in range(5):
                                                                                mgba.press_buttons(["Down", "sleep 150"])
                                                                            mgba.press_buttons(["A", "sleep 300", "A"])
                                                                            time.sleep(3.0)
                                                                            print("Mansion completely solved! Final position:", mgba.get_coordinates())
else:
    print("Execution failed.")
