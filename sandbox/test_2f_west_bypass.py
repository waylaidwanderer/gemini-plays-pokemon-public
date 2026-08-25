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

# Starting at (5, 8) on 3F West
# Let's walk to the stairs at (5, 10) on 3F West to warp DOWN to 2F West first
print("Walking DOWN to stairs at (5, 10)...")
success = walk_step("Down", {"x": 5, "y": 9})
if success:
    success = walk_step("Down", {"x": 5, "y": 10})

if success:
    print("Stepping UP onto stairs to warp DOWN to 2F West...")
    mgba.press_buttons(["Up"])
    time.sleep(1.5)
    pos = mgba.get_coordinates()
    print(f"Warped DOWN to 2F West! Landing position: {pos}")
    
    # Now we are at (5, 10) on 2F West. Walk DOWN to (5, 13)
    print("Walking DOWN Column 5 to Row 13...")
    steps_down = [
        ("Down", {"x": 5, "y": 11}),
        ("Down", {"x": 5, "y": 12}),
        ("Down", {"x": 5, "y": 13}),
    ]
    for d, c in steps_down:
        if not walk_step(d, c):
            success = False
            break
            
    if success:
        # Walk LEFT along Row 13 to Column 2
        print("Reached (5, 13) on 2F West! Walking LEFT along Row 13 to Column 2...")
        steps_left = [
            ("Left", {"x": 4, "y": 13}),
            ("Left", {"x": 3, "y": 13}),
            ("Left", {"x": 2, "y": 13}),
        ]
        for d, c in steps_left:
            if not walk_step(d, c):
                success = False
                break
                
        if success:
            # Walk UP to (2, 12)
            print("Reached (2, 13)! Attempting to walk UP to (2, 12)...")
            if walk_step("Up", {"x": 2, "y": 12}):
                print("Reached (2, 12) on 2F West! Facing UP to toggle switch...")
                mgba.press_buttons(["Up"])
                time.sleep(0.5)
                
                # Toggle switch to State A robustly
                print("Toggling the switch at (2, 11) to State A...")
                mgba.press_buttons(["A"])
                time.sleep(1.0)
                mgba.press_buttons(["A"]) # YES
                time.sleep(1.0)
                mgba.press_buttons(["A"]) # Dismiss
                time.sleep(1.0)
                print("Toggled successfully! Current position:", mgba.get_coordinates())
            else:
                print("Failed! (2, 12) is blocked.")
