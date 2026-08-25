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

def toggle_switch_robust():
    print("Toggling switch with overworld B/W feedback...")
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    # Press UP to select YES
    mgba.press_buttons(["Up", "sleep 200", "A"])
    time.sleep(1.2)
    mgba.press_buttons(["A"]) # Press A on "Pressed it!"
    time.sleep(1.2)
    
    # Dismiss any leftover text boxes
    for _ in range(4):
        mgba.press_buttons(["B"])
        time.sleep(0.3)
        
    pos = mgba.get_coordinates()
    print(f"Toggle complete! Position: {pos}")
    return True

# Starting at (15, 7) on 2F East (State B)
success = True

# 1. Walk back LEFT along Row 7 to Column 12
print("Walking LEFT to (12, 7)...")
steps_left_row7 = [
    ("Left", {"x": 14, "y": 7}),
    ("Left", {"x": 13, "y": 7}),
    ("Left", {"x": 12, "y": 7}),
]
for d, c in steps_left_row7:
    if not walk_step(d, c):
        success = False
        break

if success:
    # 2. Walk DOWN Column 12 to Row 11
    print("Walking DOWN to (12, 11)...")
    steps_down_col12 = [
        ("Down", {"x": 12, "y": 8}),
        ("Down", {"x": 12, "y": 9}),
        ("Down", {"x": 12, "y": 10}),
        ("Down", {"x": 12, "y": 11}),
    ]
    for d, c in steps_down_col12:
        if not walk_step(d, c):
            success = False
            break

if success:
    # 3. Walk LEFT along Row 11 to Column 5 on 2F West
    print("Walking LEFT along Row 11 to Column 5...")
    steps_left_row11 = []
    for x in range(11, 4, -1):
        steps_left_row11.append(("Left", {"x": x, "y": 11}))
    for d, c in steps_left_row11:
        if not walk_step(d, c):
            success = False
            break

if success:
    # 4. Walk to (2, 12)
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
        # 5. Face UP and toggle switch at (2, 11) to State A
        print("Reached (2, 12)! Facing UP and toggling switch to STATE A...")
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        toggle_switch_robust()
        
        # 6. Walk back to (5, 11)
        print("Walking to (5, 11) on 2F West...")
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
            # 7. Walk RIGHT along Row 11 directly onto stairs at (15, 11) (OPEN in State A!)
            print("Walking RIGHT directly onto stairs at (15, 11) on 2F East...")
            steps_right_stairs = []
            for x in range(6, 16):
                steps_right_stairs.append(("Right", {"x": x, "y": 11}))
            for d, c in steps_right_stairs:
                if not walk_step(d, c):
                    success = False
                    break
                    
            if success:
                print("Reached stairs at (15, 11)! Warping UP to 3F East...")
                time.sleep(1.5)
                pos = mgba.get_coordinates()
                print(f"Warped UP to 3F East! Landing position: {pos}")
                
                # 8. On 3F East, walk LEFT along Row 11 to (12, 11)
                print("Walking LEFT to (12, 11) on 3F East...")
                steps_left_3f = [
                    ("Left", {"x": 14, "y": 11}),
                    ("Left", {"x": 13, "y": 11}),
                    ("Left", {"x": 12, "y": 11}),
                ]
                for d, c in steps_left_3f:
                    if not walk_step(d, c):
                        success = False
                        break
                        
                if success:
                    # 9. Walk DOWN to (12, 12), face UP and toggle switch at (12, 11) to State B
                    print("Walking to (12, 12)...")
                    success = walk_step("Down", {"x": 12, "y": 12})
                    if success:
                        mgba.press_buttons(["Up"])
                        time.sleep(0.5)
                        toggle_switch_robust()
                        
                        # 10. Walk to Column 20 on 3F East (State B)
                        print("Walking to (20, 11)...")
                        steps_to_col20 = [
                            ("Right", {"x": 13, "y": 12}),
                            ("Right", {"x": 14, "y": 12}),
                            ("Right", {"x": 15, "y": 12}),
                            ("Right", {"x": 16, "y": 12}),
                            ("Right", {"x": 17, "y": 12}),
                            ("Right", {"x": 18, "y": 12}),
                            ("Right", {"x": 19, "y": 12}),
                            ("Right", {"x": 20, "y": 12}),
                            ("Up", {"x": 20, "y": 11}),
                        ]
                        for d, c in steps_to_col20:
                            if not walk_step(d, c):
                                success = False
                                break
                                
                        if success:
                            # 11. Walk UP Column 20 to Row 3, RIGHT to (26, 3), and step DOWN to drop through pitfall!
                            print("Walking UP Column 20 to Row 3...")
                            steps_up_col20 = []
                            for y in range(10, 2, -1):
                                steps_up_col20.append(("Up", {"x": 20, "y": y}))
                            for d, c in steps_up_col20:
                                if not walk_step(d, c):
                                    success = False
                                    break
                                    
                            if success:
                                print("Walking RIGHT to (26, 3)...")
                                steps_right_row3 = []
                                for x in range(21, 27):
                                    steps_right_row3.append(("Right", {"x": x, "y": 3}))
                                for d, c in steps_right_row3:
                                    if not walk_step(d, c):
                                        success = False
                                        break
                                        
                                if success:
                                    # 12. Step DOWN to trigger pitfall
                                    print("Stepping DOWN to trigger pitfall...")
                                    mgba.press_buttons(["Down"])
                                    time.sleep(2.0)
                                    pos = mgba.get_coordinates()
                                    print(f"Landed on 1F East inside fenced room! Position: {pos}")
                                    
                                    # 13. Walk to B1F East stairs
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
                                        
                                        # 14. On B1F East
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
                                                    
                                                    # 15. Use DIG to escape to Cinnabar Island!
                                                    print("Using DIG to escape...")
                                                    mgba.press_buttons(["Start", "sleep 300", "Down", "A", "sleep 300"])
                                                    for _ in range(5):
                                                        mgba.press_buttons(["Down", "sleep 150"])
                                                    mgba.press_buttons(["A", "sleep 300", "A"])
                                                    time.sleep(3.0)
                                                    print("Warped out! Final position:", mgba.get_coordinates())
