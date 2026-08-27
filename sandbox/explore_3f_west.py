import mgba
import time

def handle_any_menu_or_battle():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    from PIL import Image
    img = Image.open(scr_file)
    img_std = img.resize((160, 144), Image.Resampling.NEAREST)
    
    black_or_white = 0
    total_pixels = 0
    for y in range(115, 140):
        for x in range(10, 150):
            r, g, b = img_std.getpixel((x, y))[:3]
            total_pixels += 1
            is_bw = (r < 50 and g < 50 and b < 50) or (r > 200 and g > 200 and b > 200)
            if is_bw:
                black_or_white += 1
                
    percentage = black_or_white / total_pixels
    if percentage > 0.90:
        print(f"Menu/Dialogue detected! (B/W: {percentage*100:.2f}%)")
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        return True
    return False

def walk_step(direction, expected_coords, retries=15):
    for i in range(retries):
        if handle_any_menu_or_battle():
            pos = mgba.get_coordinates()
            if pos == expected_coords:
                return True
        mgba.press_buttons([direction])
        time.sleep(0.45)
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            print(f"Moved {direction}, current position: {pos}")
            return True
        print(f"Blocked or battle! Retrying {direction} to {expected_coords} (attempt {i+1}/{retries}), current: {pos}")
        time.sleep(0.3)
    return False

def run_steps(steps):
    for d, c in steps:
        if not walk_step(d, c):
            return False
    return True

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

pos = mgba.get_coordinates()
print("Starting position:", pos)

# 1. Walk to stairs at (7, 11) on 2F West
if pos == {"x": 2, "y": 13}:
    print("Walking to 2F West stairs at (7, 11)...")
    if not run_steps([
        ("Right", {"x": 3, "y": 13}),
        ("Right", {"x": 4, "y": 13}),
        ("Right", {"x": 5, "y": 13}),
        ("Up", {"x": 5, "y": 12}),
        ("Up", {"x": 5, "y": 11}),
        ("Right", {"x": 6, "y": 11}),
        ("Right", {"x": 7, "y": 11}),
    ]):
        print("Failed to reach stairs")
        exit(1)
    pos = mgba.get_coordinates()

# 2. Climb stairs to 3F West
if pos == {"x": 7, "y": 11}:
    print("Stepping UP to climb to 3F West...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position on 3F West:", pos)

# 3. Test walkability of various tiles on 3F West
if pos == {"x": 7, "y": 11}:
    print("Testing walkability on 3F West...")
    # Walk to (5, 11)
    if run_steps([("Left", {"x": 6, "y": 11}), ("Left", {"x": 5, "y": 11})]):
        # Let's test walking to (4, 11)
        print("Testing (4, 11)...")
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
        print("Position after Left from (5, 11):", mgba.get_coordinates())
        
        # Test walking UP to (5, 10)
        print("Testing (5, 10)...")
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        print("Position after Up from (5, 11):", mgba.get_coordinates())
        
        # Walk back to (5, 11) if we moved
        pos = mgba.get_coordinates()
        if pos == {"x": 5, "y": 10}:
            mgba.press_buttons(["Down"])
            time.sleep(0.5)
            
        # Walk DOWN to (5, 13)
        print("Walking to (5, 13)...")
        if run_steps([("Down", {"x": 5, "y": 12}), ("Down", {"x": 5, "y": 13})]):
            # Test walking Left along Row 13
            print("Testing Row 13 walkability...")
            for x in range(4, 0, -1):
                mgba.press_buttons(["Left"])
                time.sleep(0.5)
                print(f"Position after Left to Column {x}:", mgba.get_coordinates())
                
            # From (1, 13), test walking UP Column 1
            pos = mgba.get_coordinates()
            if pos == {"x": 1, "y": 13}:
                print("Testing Column 1 walkability going UP...")
                for y in range(12, 8, -1):
                    mgba.press_buttons(["Up"])
                    time.sleep(0.5)
                    print(f"Position after Up to Row {y}:", mgba.get_coordinates())
                    
                # From current position, test walking RIGHT into Column 2
                pos = mgba.get_coordinates()
                print("Testing walking RIGHT into Column 2 from current...")
                mgba.press_buttons(["Right"])
                time.sleep(0.5)
                print("Position after Right into Column 2:", mgba.get_coordinates())
                
print("Systematic walkability exploration complete.")
