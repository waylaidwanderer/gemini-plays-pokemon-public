import mgba
import time
from PIL import Image

def walk_step(direction, expected_coords, retries=15):
    for i in range(retries):
        mgba.press_buttons([direction])
        time.sleep(0.3)
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            print(f"Moved {direction}, current position: {pos}")
            return True
        print(f"Blocked! Retrying {direction} to {expected_coords} (attempt {i+1}/{retries}), current: {pos}")
        time.sleep(0.2)
    return False

# Starting at (4, 11) on 2F West
# 1. Warp UP to 3F West
success = walk_step("Right", {"x": 5, "y": 11})
if success:
    print("Stepping UP onto stairs to warp UP...")
    mgba.press_buttons(["Up"])
    time.sleep(1.5)
    pos = mgba.get_coordinates()
    print(f"Warped UP to 3F West! Landing position: {pos}")
    
    # 2. On 3F West, walk UP Column 7 to Row 8
    steps_up = [
        ("Up", {"x": 7, "y": 10}),
        ("Up", {"x": 7, "y": 9}),
        ("Up", {"x": 7, "y": 8}),
    ]
    for d, c in steps_up:
        if not walk_step(d, c):
            success = False
            break
            
    if success:
        # 3. Walk LEFT along Row 8 to Column 2
        print("Reached (7, 8)! Walking LEFT to Column 2...")
        steps_left = [
            ("Left", {"x": 6, "y": 8}),
            ("Left", {"x": 5, "y": 8}),
            ("Left", {"x": 4, "y": 8}),
            ("Left", {"x": 3, "y": 8}),
            ("Left", {"x": 2, "y": 8}),
        ]
        for d, c in steps_left:
            if not walk_step(d, c):
                success = False
                break
                
        if success:
            # 4. Walk DOWN Column 2 to Row 10
            print("Reached (2, 8)! Walking DOWN Column 2 to (2, 10)...")
            steps_down = [
                ("Down", {"x": 2, "y": 9}),
                ("Down", {"x": 2, "y": 10}),
            ]
            for d, c in steps_down:
                if not walk_step(d, c):
                    success = False
                    break
                    
            if success:
                print("Reached (2, 10) on 3F West! Facing DOWN towards switch...")
                mgba.press_buttons(["Down"])
                time.sleep(0.5)
                
                # Check if dialogue opens
                print("Pressing A to check switch...")
                mgba.press_buttons(["A"])
                time.sleep(1.5)
                
                # Take screenshot to verify
                img = mgba.take_screenshot()
                print("Saved screenshot:", img)
                
                # Check B/W percentage
                pil_img = Image.open(img)
                img_std = pil_img.resize((160, 144), Image.Resampling.NEAREST)
                black_or_white = 0
                for y in range(115, 140):
                    for x in range(10, 150):
                        r, g, b = img_std.getpixel((x, y))
                        if (r < 50 and g < 50 and b < 50) or (r > 200 and g > 200 and b > 200):
                            black_or_white += 1
                percentage = black_or_white / 3500
                print(f"Dialogue B/W percentage: {percentage*100:.2f}%")
                
                if percentage > 0.90:
                    print("Success! Switch dialogue box opened from (2, 10) facing DOWN!")
                    # Press A to select YES
                    mgba.press_buttons(["A"])
                    time.sleep(1.2)
                    mgba.press_buttons(["A"]) # Dismiss
                    time.sleep(1.0)
                    print("Toggled! Current position:", mgba.get_coordinates())
                else:
                    print("Failed! Dialogue box did not open.")
else:
    print("Failed to warp up to 3F West.")
