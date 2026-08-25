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

# Starting at (10, 3) on 2F East (State B)
success = True

# 1. Walk DOWN Column 10 to Row 9
print("Walking DOWN Column 10 to Row 9...")
steps_down_col10 = [
    ("Down", {"x": 10, "y": 4}),
    ("Down", {"x": 10, "y": 5}),
    ("Down", {"x": 10, "y": 6}),
    ("Down", {"x": 10, "y": 7}),
    ("Down", {"x": 10, "y": 8}),
    ("Down", {"x": 10, "y": 9}),
]
for d, c in steps_down_col10:
    if not walk_step(d, c):
        success = False
        break

if success:
    # 2. Walk LEFT Row 9 to Column 2
    print("Reached (10, 9)! Walking LEFT on Row 9 to Column 2...")
    steps_left_row9 = [
        ("Left", {"x": 9, "y": 9}), # Open gate in State B!
        ("Left", {"x": 8, "y": 9}),
        ("Left", {"x": 7, "y": 9}),
        ("Left", {"x": 6, "y": 9}),
        ("Left", {"x": 5, "y": 9}),
        ("Left", {"x": 4, "y": 9}),
        ("Left", {"x": 3, "y": 9}),
        ("Left", {"x": 2, "y": 9}),
    ]
    for d, c in steps_left_row9:
        if not walk_step(d, c):
            success = False
            break

if success:
    # 3. Walk DOWN to (2, 12) with automatic Column 1 bypass
    print("Reached (2, 9)! Attempting to walk DOWN to (2, 12)...")
    success_down = True
    for y in [10, 11, 12]:
        if not walk_step("Down", {"x": 2, "y": y}, retries=3):
            success_down = False
            break
            
    if not success_down:
        print("Blocked on Column 2! Attempting bypass via Column 1...")
        curr = mgba.get_coordinates()
        if curr['y'] > 9:
            walk_step("Up", {"x": 2, "y": curr['y'] - 1})
        if walk_step("Left", {"x": 1, "y": 9}):
            for y in [10, 11, 12]:
                walk_step("Down", {"x": 1, "y": y})
            walk_step("Right", {"x": 2, "y": 12})
            
    pos = mgba.get_coordinates()
    print("Reached target column 2 area! Position:", pos)
    
    # 4. Toggle the switch to State A
    # First, let's try from (2, 12) facing UP
    if pos == {"x": 2, "y": 12}:
        print("Standing at (2, 12). Facing UP towards statue...")
        mgba.press_buttons(["Up"])
        time.sleep(0.3)
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
        # Check if dialogue box opened
        scr_file = mgba.take_screenshot()
        img = Image.open(scr_file)
        img_std = img.resize((160, 144), Image.Resampling.NEAREST)
        black_or_white = 0
        for y in range(115, 140):
            for x in range(10, 150):
                r, g, b = img_std.getpixel((x, y))
                is_bw = (r < 50 and g < 50 and b < 50) or (r > 200 and g > 200 and b > 200)
                if is_bw:
                    black_or_white += 1
        percentage = black_or_white / 3500
        
        if percentage > 0.90:
            print("Successfully opened switch dialog at (2, 12)!")
            mgba.press_buttons(["A"]) # YES
            time.sleep(1.0)
            mgba.press_buttons(["A"]) # Dismiss
            time.sleep(1.0)
        else:
            print("Statue not at (2, 11) or non-interactive from (2, 12). Trying (2, 11)...")
            # Walk UP to (2, 11) and try facing UP
            if walk_step("Up", {"x": 2, "y": 11}):
                mgba.press_buttons(["Up"])
                time.sleep(0.3)
                mgba.press_buttons(["A"])
                time.sleep(1.0)
                mgba.press_buttons(["A"]) # YES
                time.sleep(1.0)
                mgba.press_buttons(["A"]) # Dismiss
                time.sleep(1.0)
                
    # 5. Now we are in State A! Walk to the stairs via Column 11/12
    # From wherever we are (2, 12 or 2, 11), walk to (2, 3)
    print("Walking UP Column 2 to (2, 3)...")
    curr = mgba.get_coordinates()
    while curr['y'] > 3:
        walk_step("Up", {"x": 2, "y": curr['y'] - 1})
        curr = mgba.get_coordinates()
        
    print("Reached (2, 3)! Walking RIGHT along Row 3 to Column 12...")
    steps_right_row3 = []
    for x in range(3, 13):
        steps_right_row3.append(("Right", {"x": x, "y": 3}))
    for d, c in steps_right_row3:
        if not walk_step(d, c):
            success = False
            break
            
    if success:
        # Walk DOWN to Row 7
        print("Reached (12, 3)! Walking DOWN Column 12 to (12, 7)...")
        steps_down_col12 = [
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
            # Walk RIGHT to Column 15 Row 7
            print("Reached (12, 7)! Walking RIGHT along Row 7 to Column 15...")
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
                # Walk DOWN Column 15 directly onto stairs at (15, 11) to warp UP to 3F East
                print("Reached (15, 7)! Walking DOWN Column 15 directly onto stairs to warp UP...")
                steps_down_col15 = [
                    ("Down", {"x": 15, "y": 8}), # OPEN in State A!
                    ("Down", {"x": 15, "y": 9}),
                    ("Down", {"x": 15, "y": 10}),
                ]
                for d, c in steps_down_col15:
                    if not walk_step(d, c):
                        success = False
                        break
                        
                if success:
                    print("Reached (15, 10)! Standing next to stairs. Walking DOWN onto stairs at (15, 11)...")
                    mgba.press_buttons(["Down"])
                    time.sleep(1.5)
                    pos = mgba.get_coordinates()
                    print(f"Warped UP to 3F East! Landing position: {pos}")
                    
                    # 6. On 3F East, walk LEFT to (12, 11)
                    steps_3f_east = [
                        ("Left", {"x": 14, "y": 11}),
                        ("Left", {"x": 13, "y": 11}),
                        ("Left", {"x": 12, "y": 11}),
                    ]
                    for d, c in steps_3f_east:
                        if not walk_step(d, c):
                            success = False
                            break
                            
                    if success:
                        print("Reached (12, 11) on 3F East! Walking DOWN to (12, 12) to face UP towards the switch...")
                        if walk_step("Down", {"x": 12, "y": 12}, retries=2):
                            mgba.press_buttons(["Up"]) # Face UP towards switch at (12, 11)
                            time.sleep(0.3)
                            mgba.press_buttons(["A"]) # "A secret switch!"
                            time.sleep(0.8)
                            mgba.press_buttons(["A"]) # select YES
                            time.sleep(0.8)
                            mgba.press_buttons(["A"]) # "Pressed it!"
                            time.sleep(0.8)
                            # Walk UP to (12, 11)
                            walk_step("Up", {"x": 12, "y": 11})
                        else:
                            print("Mansion is already in STATE B. Skipping 3F toggle.")
                            
                        # 7. On 3F East (State B), walk RIGHT to Column 20, UP to Row 3, RIGHT to (26, 3) and DOWN to drop
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
                            ("Up", {"x": 20, "y": 3}),  # Open vertical passage!
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
                            print("Reached (26, 3) on 3F East! Stepping DOWN to trigger pitfall...")
                            mgba.press_buttons(["Down"])
                            time.sleep(2.0)
                            pos = mgba.get_coordinates()
                            print(f"Landed on 1F East inside fenced room! Position: {pos}")
                            
                            # 8. On 1F East fenced room (State B)
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
                                
                                # 9. On B1F East (State B)
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
                                            
                                            # 10. Use DIG to escape to Cinnabar Island!
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
