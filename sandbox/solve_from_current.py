import mgba
import time
from PIL import Image

def handle_any_menu_or_battle():
    # Add a small delay to avoid map transition / lag black screens
    time.sleep(0.15)
    
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
    # Ignore exactly 100% black or white (fade transitions)
    if 0.90 < percentage < 0.999:
        print(f"Menu/Battle detected! (B/W percentage: {percentage*100:.2f}%)")
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
        
        if 0.90 < percentage2 < 0.999:
            print("Still in battle/menu. Attempting RUN...")
            mgba.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A"])
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

# Start at current position on 2F West (should be 3, 11)
pos = mgba.get_coordinates()
print(f"Starting from 2F West position: {pos}")

success = True

# 1. Walk from current position (3, 11) on 2F West to switch standing position (2, 12)
steps_to_switch = [
    ("Left", {"x": 2, "y": 11}),
    ("Down", {"x": 2, "y": 12}),
]
print("Walking to 2F West switch standing position (2, 12)...")
for d, c in steps_to_switch:
    if not walk_step(d, c):
        success = False
        break
        
if success:
    print("At (2, 12) on 2F West. Facing UP towards switch at (2, 11)...")
    mgba.press_buttons(["Up", "sleep 300"])
    
    # Toggle switch to State B with 2.0s delays
    mgba.press_buttons(["A", "sleep 2000"]) # Opens "A secret switch!"
    mgba.press_buttons(["A", "sleep 2000"]) # Selects YES
    mgba.press_buttons(["A", "sleep 1000"]) # Dismisses dialogue
    
    print("Toggled switch to State B! Proceeding to Column 5 Row 12...")
    
    # 2. Walk to Column 5 Row 12
    steps_to_col5 = [
        ("Right", {"x": 3, "y": 12}),
        ("Right", {"x": 4, "y": 12}),
        ("Right", {"x": 5, "y": 12}),
    ]
    for d, c in steps_to_col5:
        if not walk_step(d, c):
            success = False
            break
            
    if success:
        # 3. Walk UP Column 5 past Row 9 (now open in State B!) to Row 3
        steps_up_col5 = [
            ("Up", {"x": 5, "y": 11}),
            ("Up", {"x": 5, "y": 10}),
            ("Up", {"x": 5, "y": 9}),  # Open gate in State B!
            ("Up", {"x": 5, "y": 8}),
            ("Up", {"x": 5, "y": 7}),
            ("Up", {"x": 5, "y": 6}),
            ("Up", {"x": 5, "y": 5}),
            ("Up", {"x": 5, "y": 4}),
            ("Up", {"x": 5, "y": 3}),
        ]
        print("Walking UP Column 5 to Row 3...")
        for d, c in steps_up_col5:
            if not walk_step(d, c):
                success = False
                break
                
        if success:
            # 4. Walk RIGHT along Row 3 to Column 18, DOWN Column 18 to Row 10, LEFT to Column 15 Row 10
            steps_2f_east = [
                ("Right", {"x": 6, "y": 3}),
                ("Right", {"x": 7, "y": 3}),
                ("Right", {"x": 8, "y": 3}),
                ("Right", {"x": 9, "y": 3}),
                ("Right", {"x": 10, "y": 3}),
                ("Right", {"x": 11, "y": 3}),
                ("Right", {"x": 12, "y": 3}),
                ("Right", {"x": 13, "y": 3}),
                ("Right", {"x": 14, "y": 3}),
                ("Right", {"x": 15, "y": 3}),
                ("Right", {"x": 16, "y": 3}),
                ("Right", {"x": 17, "y": 3}),
                ("Right", {"x": 18, "y": 3}),
                ("Down", {"x": 18, "y": 4}),
                ("Down", {"x": 18, "y": 5}),
                ("Down", {"x": 18, "y": 6}),
                ("Down", {"x": 18, "y": 7}),
                ("Down", {"x": 18, "y": 8}),
                ("Down", {"x": 18, "y": 9}),
                ("Down", {"x": 18, "y": 10}),
                ("Left", {"x": 17, "y": 10}),
                ("Left", {"x": 16, "y": 10}),
                ("Left", {"x": 15, "y": 10}),
            ]
            print("Executing 2F West -> 2F East bypass route...")
            for d, c in steps_2f_east:
                if not walk_step(d, c):
                    success = False
                    break
                    
            if success:
                print("At (15, 10) on 2F East! Stepping DOWN onto stairs to warp UP to 3F East...")
                mgba.press_buttons(["Down"])
                time.sleep(1.5)
                pos = mgba.get_coordinates()
                print(f"Warped UP to 3F East! Landing position: {pos}")
                
                # 5. 3F East to Pitfall
                steps_3f_east_pit = [
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
                print("Walking from 3F East landing to pitfall at (26, 3)...")
                for d, c in steps_3f_east_pit:
                    if not walk_step(d, c):
                        success = False
                        break
                        
                if success:
                    print("At (26, 3) on 3F East! Stepping DOWN onto pitfall...")
                    mgba.press_buttons(["Down"])
                    time.sleep(2.0)
                    pos = mgba.get_coordinates()
                    print(f"Landed on 1F East inside fenced room! Position: {pos}")
                    
                    # 6. Dynamic 1F East navigation
                    while pos['y'] > 3:
                        if not walk_step("Up", {"x": pos['x'], "y": pos['y'] - 1}):
                            break
                        pos = mgba.get_coordinates()
                    while pos['x'] > 22:
                        if not walk_step("Left", {"x": pos['x'] - 1, "y": 3}):
                            break
                        pos = mgba.get_coordinates()
                        
                    if pos == {"x": 22, "y": 3}:
                        print("At (22, 3) on 1F East fenced room! Stepping UP onto stairs to warp DOWN to B1F East...")
                        mgba.press_buttons(["Up"])
                        time.sleep(1.5)
                        pos = mgba.get_coordinates()
                        print(f"Warped to B1F East! Position: {pos}")
                        
                        # 7. B1F East to B1F West
                        steps_b1f = [
                            ("Left", {"x": 21, "y": 3}),
                            ("Down", {"x": 21, "y": 4}),
                            ("Left", {"x": 20, "y": 4}),
                            ("Left", {"x": 19, "y": 4}),
                            ("Down", {"x": 19, "y": 5}),
                        ]
                        print("Executing B1F East -> B1F West horizontal bypass...")
                        for d, c in steps_b1f:
                            if not walk_step(d, c):
                                success = False
                                break
                                
                        if success:
                            print("Bypassed B1F East wall! Walking LEFT along Row 5 to the Secret Key room...")
                            curr = mgba.get_coordinates()
                            while curr['x'] > 1:
                                if not walk_step("Left", {"x": curr['x'] - 1, "y": 5}):
                                    success = False
                                    break
                                curr = mgba.get_coordinates()
                                
                            if success:
                                print("Reached (1, 5) on B1F West! Stepping UP and retrieving the Secret Key...")
                                mgba.press_buttons(["Up", "sleep 300"])
                                mgba.press_buttons(["A", "sleep 600"]) # Opens "Obtained the SECRET KEY!"
                                mgba.press_buttons(["A", "sleep 600"]) # Dismiss text
                                time.sleep(1.0)
                                print("Secret Key retrieved successfully! Current position:", mgba.get_coordinates())
                                
                                # 8. DIG escape
                                print("Executing DIG escape...")
                                mgba.press_buttons(["Start", "sleep 400", "Down", "sleep 200", "A", "sleep 500"])
                                for _ in range(5):
                                    mgba.press_buttons(["Down", "sleep 150"])
                                mgba.press_buttons(["A", "sleep 400", "A", "sleep 3000"])
                                print("Warped out! Final position:", mgba.get_coordinates())
                            else:
                                print("Failed to reach B1F West.")
                        else:
                            print("Failed to navigate B1F East.")
                    else:
                        print("Failed to align at (22, 3) on 1F East.")
                else:
                    print("Failed to reach pitfall on 3F East.")
            else:
                print("Failed to navigate 2F East.")
        else:
            print("Failed to navigate Column 5 UP to Row 3.")
    else:
        print("Failed to navigate to Column 5.")
else:
    print("Failed to reach switch on 2F West.")
