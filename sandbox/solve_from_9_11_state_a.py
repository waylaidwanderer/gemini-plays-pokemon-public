import mgba
import time
from PIL import Image

def get_dialogue_percentage():
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
    return black_or_white / total_pixels

def handle_any_menu_or_battle():
    percentage = get_dialogue_percentage()
    if percentage > 0.90:
        print(f"Menu/Battle detected! (B/W percentage: {percentage*100:.2f}%)")
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        
        percentage2 = get_dialogue_percentage()
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

def toggle_switch_robust(target_statue_coords):
    print(f"Toggling switch at {target_statue_coords} with overworld B/W feedback...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Loop pressing A until B/W percentage is low (overworld level, usually < 40%)
    for attempt in range(12):
        percentage = get_dialogue_percentage()
        print(f"Attempt {attempt+1}: dialogue B/W percentage: {percentage*100:.2f}%")
        if percentage < 0.40:
            print("Dialogue successfully dismissed! Back in overworld.")
            return True
        # Press A to advance text/select YES/dismiss
        mgba.press_buttons(["A"])
        time.sleep(1.0)
    return False

# Starting at (9, 11) on 2F West/East boundary (State A)
success = True

# 1. Walk LEFT to Column 5 Row 11
print("Walking LEFT to Column 5...")
steps_left = [
    ("Left", {"x": 8, "y": 11}),
    ("Left", {"x": 7, "y": 11}),
    ("Left", {"x": 6, "y": 11}),
    ("Left", {"x": 5, "y": 11}),
]
for d, c in steps_left:
    if not walk_step(d, c):
        success = False
        break

if success:
    # 2. Walk DOWN Column 5 to Row 13
    print("Reached (5, 11)! Walking DOWN to Row 13...")
    steps_down_col5 = [
        ("Down", {"x": 5, "y": 12}),
        ("Down", {"x": 5, "y": 13}),
    ]
    for d, c in steps_down_col5:
        if not walk_step(d, c):
            success = False
            break

if success:
    # 3. Walk LEFT Row 13 to Column 2 on 2F West (completely open hallway!)
    print("Reached (5, 13)! Walking LEFT along Row 13 to Column 2...")
    steps_left_row13 = [
        ("Left", {"x": 4, "y": 13}),
        ("Left", {"x": 3, "y": 13}),
        ("Left", {"x": 2, "y": 13}),
    ]
    for d, c in steps_left_row13:
        if not walk_step(d, c):
            success = False
            break

if success:
    # 4. Walk UP Column 2 to Row 12 (open in State A!)
    print("Reached (2, 13)! Walking UP to (2, 12)...")
    success = walk_step("Up", {"x": 2, "y": 12})

if success:
    # 5. Stand at (2, 12) facing UP and toggle switch at (2, 11) to State B
    print("Reached (2, 12) on 2F West! Facing UP to toggle switch to STATE B...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    success = toggle_switch_robust((2, 11))

if success:
    # 6. Walk DOWN Column 2 to Row 13
    print("Switched to STATE B! Walking DOWN to (2, 13)...")
    success = walk_step("Down", {"x": 2, "y": 13})

if success:
    # 7. Walk RIGHT along Row 13 to Column 5
    print("Reached (2, 13)! Walking RIGHT along Row 13 to Column 5...")
    steps_right_row13 = [
        ("Right", {"x": 3, "y": 13}),
        ("Right", {"x": 4, "y": 13}),
        ("Right", {"x": 5, "y": 13}),
    ]
    for d, c in steps_right_row13:
        if not walk_step(d, c):
            success = False
            break

if success:
    # 8. Walk UP Column 5 to Row 10 (stairs are at 5, 10 on 2F West)
    print("Reached (5, 13)! Walking UP to stairs at (5, 10)...")
    steps_up_col5 = [
        ("Up", {"x": 5, "y": 12}),
        ("Up", {"x": 5, "y": 11}),
    ]
    for d, c in steps_up_col5:
        if not walk_step(d, c):
            success = False
            break
            
    if success:
        # 9. Step UP onto stairs to warp UP to 3F West
        print("Stepping UP onto stairs to warp UP...")
        mgba.press_buttons(["Up"])
        time.sleep(1.5)
        pos = mgba.get_coordinates()
        print(f"Warped UP to 3F West! Landing position: {pos}")
        
        # 10. Walk UP Column 5 to Row 8
        print("Walking UP Column 5 to Row 8...")
        steps_up_3f = [
            ("Up", {"x": 5, "y": 9}), # OPEN gate in State B!
            ("Up", {"x": 5, "y": 8}),
        ]
        for d, c in steps_up_3f:
            if not walk_step(d, c):
                success = False
                break
                
        if success:
            # 11. Walk LEFT along Row 8 to Column 1 (Row 8 is always open!)
            print("Reached (5, 8) on 3F West! Walking LEFT to Column 1...")
            steps_left_row8 = [
                ("Left", {"x": 4, "y": 8}),
                ("Left", {"x": 3, "y": 8}),
                ("Left", {"x": 2, "y": 8}),
                ("Left", {"x": 1, "y": 8}),
            ]
            for d, c in steps_left_row8:
                if not walk_step(d, c):
                    success = False
                    break
                    
            if success:
                # 12. Walk UP Column 1 past Row 7 (open on Column 1!) to Row 6: (1, 6)
                print("Reached (1, 8)! Walking UP Column 1 to Row 6...")
                steps_up_col1 = [
                    ("Up", {"x": 1, "y": 7}), # OPEN on Column 1!
                    ("Up", {"x": 1, "y": 6}),
                ]
                for d, c in steps_up_col1:
                    if not walk_step(d, c):
                        success = False
                        break
                        
                if success:
                    # 13. Walk RIGHT along Row 6 to Column 20 on 3F East (permanently open crossing)
                    print("Reached (1, 6)! Walking RIGHT to Column 20...")
                    steps_right_row6 = []
                    for x in range(2, 21):
                        steps_right_row6.append(("Right", {"x": x, "y": 6}))
                    for d, c in steps_right_row6:
                        if not walk_step(d, c):
                            success = False
                            break
                            
                    if success:
                        # 14. Walk UP Column 20 to Row 3 (bypassing pitfalls on Rows 5/6)
                        print("Reached (20, 6)! Walking UP Column 20 to Row 3...")
                        steps_up_col20 = [
                            ("Up", {"x": 20, "y": 5}),
                            ("Up", {"x": 20, "y": 4}),
                            ("Up", {"x": 20, "y": 3}),
                        ]
                        for d, c in steps_up_col20:
                            if not walk_step(d, c):
                                success = False
                                break
                                
                        if success:
                            # 15. Walk RIGHT along Row 3 to Column 26
                            print("Reached (20, 3)! Walking RIGHT along Row 3 to Column 26...")
                            steps_right_row3_3f = [
                                ("Right", {"x": 21, "y": 3}),
                                ("Right", {"x": 22, "y": 3}),
                                ("Right", {"x": 23, "y": 3}),
                                ("Right", {"x": 24, "y": 3}),
                                ("Right", {"x": 25, "y": 3}),
                                ("Right", {"x": 26, "y": 3}),
                            ]
                            for d, c in steps_right_row3_3f:
                                if not walk_step(d, c):
                                    success = False
                                    break
                                    
                            if success:
                                # 16. Step DOWN onto Column 26 to fall through pit
                                print("Reached (26, 3)! Stepping DOWN to trigger pitfall...")
                                mgba.press_buttons(["Down"])
                                time.sleep(2.0) # wait for drop animation
                                pos = mgba.get_coordinates()
                                print(f"Landed on 1F East inside fenced room! Position: {pos}")
                                
                                # 17. On 1F East fenced room, walk UP to (26, 3), LEFT to (22, 3), UP onto stairs at (22, 2)
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
                                    print("Reached (22, 3) on 1F East! Stepping UP onto stairs to warp DOWN to B1F East...")
                                    mgba.press_buttons(["Up"])
                                    time.sleep(1.5)
                                    pos = mgba.get_coordinates()
                                    print(f"Warped DOWN to B1F East! Landing position: {pos}")
                                    
                                    # 18. On B1F East (State B)
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
                                                mgba.press_buttons(["A"])   # Opens "Obtained the SECRET KEY!"
                                                time.sleep(1.5)
                                                mgba.press_buttons(["A"])   # Dismiss obtain text
                                                time.sleep(1.0)
                                                pos = mgba.get_coordinates()
                                                print(f"Secret Key retrieved successfully! Current position: {pos}")
                                                
                                                # 19. Use DIG to escape to Cinnabar Island!
                                                print("Using DIG to escape...")
                                                mgba.press_buttons(["Start", "sleep 300", "Down", "A", "sleep 300"]) # opens PKMN menu
                                                for _ in range(5):
                                                    mgba.press_buttons(["Down", "sleep 150"])
                                                mgba.press_buttons(["A", "sleep 300", "A"]) # selects TRUFFLE, then selects DIG
                                                time.sleep(3.0) # wait for warp animation
                                                print("Warped out! Final position:", mgba.get_coordinates())
                            else:
                                print("Failed to reach Secret Key on B1F West.")
                        else:
                            print("Failed to navigate B1F East.")
                    else:
                        print(f"Unexpected landing position on B1F East: {pos}")
                else:
                    print("Failed to navigate 1F East fenced room.")
            else:
                print("Failed to reach (26, 3) on 3F East.")
        else:
            print("Failed to navigate 3F East.")
else:
    print("Mansion key retrieve route failed.")
