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

# Starting at (12, 10) on 2F East (in battle)
success = True

# 1. Escape battle
print("Escaping battle first...")
for _ in range(3):
    if handle_any_menu_or_battle():
        break
    time.sleep(0.5)

# Wait a moment to ensure overworld is stable
time.sleep(1.0)
pos = mgba.get_coordinates()
print(f"Current Position after battle escape: {pos}")

# 2. Walk UP Column 12 to Row 7
print("Walking UP Column 12 to Row 7...")
steps_up_col12 = [
    ("Up", {"x": 12, "y": 9}),
    ("Up", {"x": 12, "y": 8}),
    ("Up", {"x": 12, "y": 7}),
]
for d, c in steps_up_col12:
    if not walk_step(d, c):
        success = False
        break

if success:
    # 3. Walk RIGHT along Row 7 to Column 14
    print("Reached (12, 7)! Walking RIGHT along Row 7 to Column 14...")
    steps_right_row7 = [
        ("Right", {"x": 13, "y": 7}),
        ("Right", {"x": 14, "y": 7}),
    ]
    for d, c in steps_right_row7:
        if not walk_step(d, c):
            success = False
            break

if success:
    # 4. Walk DOWN Column 14 to Row 10
    print("Reached (14, 7)! Walking DOWN Column 14 to Row 10...")
    steps_down_col14 = [
        ("Down", {"x": 14, "y": 8}),
        ("Down", {"x": 14, "y": 9}),
        ("Down", {"x": 14, "y": 10}),
    ]
    for d, c in steps_down_col14:
        if not walk_step(d, c):
            success = False
            break

if success:
    # 5. Walk RIGHT to Column 15 Row 10
    print("Reached (14, 10)! Walking RIGHT to Column 15...")
    success = walk_step("Right", {"x": 15, "y": 10})
    
    if success:
        # 6. Step DOWN onto stairs at (15, 11) to warp UP to 3F East
        print("Reached (15, 10)! Stepping DOWN onto stairs to warp UP...")
        mgba.press_buttons(["Down"])
        time.sleep(1.5)
        pos = mgba.get_coordinates()
        print(f"Warped UP to 3F East! Landing position: {pos}")
        
        # 7. Walk RIGHT to Column 20, UP to Row 3, RIGHT to (26, 3) and DOWN to drop
        steps_to_drop = [
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
            # 8. Step DOWN to trigger pitfall
            print("Reached (26, 3) on 3F East! Stepping DOWN to trigger pitfall...")
            mgba.press_buttons(["Down"])
            time.sleep(2.0)
            pos = mgba.get_coordinates()
            print(f"Landed on 1F East inside fenced room! Position: {pos}")
            
            # 9. On 1F East fenced room: walk UP to (26, 3), LEFT to (22, 3), UP onto stairs at (22, 2)
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
                
                # 10. On B1F East (State B)
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
                            
                            # 11. Use DIG to escape to Cinnabar Island!
                            print("Using DIG to escape...")
                            mgba.press_buttons(["Start", "sleep 300", "Down", "A", "sleep 300"])
                            for _ in range(5):
                                mgba.press_buttons(["Down", "sleep 150"])
                            mgba.press_buttons(["A", "sleep 300", "A"])
                            time.sleep(3.0)
                            print("Warped out! Final position:", mgba.get_coordinates())
