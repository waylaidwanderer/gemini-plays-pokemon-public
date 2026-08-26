import mgba
import time
from PIL import Image

def handle_any_menu_or_battle():
    time.sleep(0.15)
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
        print(f"Menu/Dialogue detected! (B/W: {percentage*100:.2f}%)")
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        
        # Check if still in battle
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

# Ensure any active menus/dialogues are closed
mgba.press_buttons(["B"])
time.sleep(0.4)

pos = mgba.get_coordinates()
print("Starting 2F West Switch Bypass Route from:", pos)

if pos == {"x": 9, "y": 10}:
    print("Walking the bypass route to (12, 10)...")
    steps = [
        ("Down", {"x": 9, "y": 11}),
        ("Left", {"x": 8, "y": 11}),
        ("Left", {"x": 7, "y": 11}),
        ("Left", {"x": 6, "y": 11}),
        ("Left", {"x": 5, "y": 11}),
        ("Up", {"x": 5, "y": 10}),
        ("Up", {"x": 5, "y": 9}),
        ("Up", {"x": 5, "y": 8}),
        ("Up", {"x": 5, "y": 7}),
        ("Right", {"x": 6, "y": 7}),
        ("Right", {"x": 7, "y": 7}),
        ("Right", {"x": 8, "y": 7}),
        ("Right", {"x": 9, "y": 7}),
        ("Right", {"x": 10, "y": 7}),
        ("Right", {"x": 11, "y": 7}),
        ("Right", {"x": 12, "y": 7}),
        ("Right", {"x": 13, "y": 7}),
        ("Down", {"x": 13, "y": 8}),
        ("Down", {"x": 13, "y": 9}),
        ("Down", {"x": 13, "y": 10}),
        ("Left", {"x": 12, "y": 10}),
    ]
    if not run_steps(steps):
        print("Bypass route failed!")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 12, "y": 10}:
    print("Successfully reached (12, 10) in front of the switch! Turning UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    print("Toggling the 2F West switch...")
    mgba.press_buttons(["A", "sleep 800", "A", "sleep 800", "A", "sleep 800", "A"])
    time.sleep(4.0)
    
    # After toggling, walk back to the stairs at (7, 10) to warp up to 3F West!
    # Path: (12, 10) -> Right to (13, 10) -> Up to (13, 7) -> Left to (12, 7) -> ... -> Left to (7, 7) -> Down to (7, 10)
    print("Walking to the stairs at (7, 10)...")
    stairs_steps = [
        ("Right", {"x": 13, "y": 10}),
        ("Up", {"x": 13, "y": 9}),
        ("Up", {"x": 13, "y": 8}),
        ("Up", {"x": 13, "y": 7}),
        ("Left", {"x": 12, "y": 7}),
        ("Left", {"x": 11, "y": 7}),
        ("Left", {"x": 10, "y": 7}),
        ("Left", {"x": 9, "y": 7}),
        ("Left", {"x": 8, "y": 7}),
        ("Left", {"x": 7, "y": 7}),
        ("Down", {"x": 7, "y": 8}),
        ("Down", {"x": 7, "y": 9}),
        ("Down", {"x": 7, "y": 10}), # This is the stairs warp tile!
    ]
    if not run_steps(stairs_steps):
        print("Failed to reach stairs")
        exit(1)
        
    print("Warping up to 3F West...")
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after warping UP:", pos)
    
    # We should land at (7, 11) on 3F West!
    if pos == {"x": 7, "y": 11}:
        print("We successfully warped UP to 3F West in State B!")
        # Complete the master route:
        # (7, 11) -> (6, 11) -> (6, 10) -> (6, 9) (now open!) -> (6, 8) -> (7, 8) -> (7, 7) -> (7, 6) -> (11, 6) -> ...
        steps_3f = [
            ("Left", {"x": 6, "y": 11}),
            ("Up", {"x": 6, "y": 10}),
            ("Up", {"x": 6, "y": 9}),
            ("Up", {"x": 6, "y": 8}),
            ("Right", {"x": 7, "y": 8}),
            ("Up", {"x": 7, "y": 7}),
            ("Up", {"x": 7, "y": 6}),
        ]
        if not run_steps(steps_3f):
            print("Failed on 3F West route")
            exit(1)
        pos = mgba.get_coordinates()
        
    if pos == {"x": 7, "y": 6}:
        print("Walking to 3F East (Column 26)...")
        steps_east = []
        for x in range(8, 27):
            steps_east.append(("Right", {"x": x, "y": 6}))
        if not run_steps(steps_east):
            print("Failed to reach 3F East")
            exit(1)
        pos = mgba.get_coordinates()
        
    # On 3F East at (26, 6), walk UP to (26, 3) and fall
    if pos == {"x": 26, "y": 6}:
        print("Walking UP Column 26 to Row 3...")
        steps_up = [
            ("Up", {"x": 26, "y": 5}),
            ("Up", {"x": 26, "y": 4}),
            ("Up", {"x": 26, "y": 3}),
        ]
        if not run_steps(steps_up):
            print("Failed to reach Row 3 pitfall")
            exit(1)
        pos = mgba.get_coordinates()
        
    if pos == {"x": 26, "y": 3}:
        print("Stepping DOWN to fall through the pitfall...")
        mgba.press_buttons(["Down"])
        time.sleep(2.5)
        pos = mgba.get_coordinates()
        print("Position after dropping to 1F East:", pos)
        
    if pos == {"x": 26, "y": 4}:
        print("Walking to B1F East stairs...")
        steps_to_stairs = [
            ("Left", {"x": 25, "y": 4}),
            ("Left", {"x": 24, "y": 4}),
            ("Left", {"x": 23, "y": 4}),
            ("Left", {"x": 22, "y": 4}),
            ("Up", {"x": 22, "y": 3}),
            ("Up", {"x": 22, "y": 2}),  # This is the stairs warp tile!
        ]
        if not run_steps(steps_to_stairs):
            print("Failed to reach B1F East stairs warp")
            exit(1)
        time.sleep(2.0)
        pos = mgba.get_coordinates()
        print("Position after warping down to B1F East:", pos)
        
    if pos == {"x": 22, "y": 2}:
        print("Crossing B1F East to B1F West NORTH...")
        steps_b1f = [
            ("Down", {"x": 22, "y": 3}),
            ("Down", {"x": 22, "y": 4}),
            ("Left", {"x": 21, "y": 4}),
            ("Left", {"x": 20, "y": 4}),
            ("Left", {"x": 19, "y": 4}),
            ("Down", {"x": 19, "y": 5}),
        ]
        if not run_steps(steps_b1f):
            print("Failed to reach Row 5 on B1F East")
            exit(1)
            
        steps_left = []
        for x in range(18, 0, -1):
            steps_left.append(("Left", {"x": x, "y": 5}))
        if not run_steps(steps_left):
            print("Failed to reach (1, 5)")
            exit(1)
        pos = mgba.get_coordinates()
        
    if pos == {"x": 1, "y": 5}:
        print("Aligning UP towards the Secret Key...")
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        
        print("Retrieving the Secret Key...")
        mgba.press_buttons([
            "A", "sleep 2500",
            "A", "sleep 2500",
            "A", "sleep 2500"
        ])
        time.sleep(8.5)
        pos = mgba.get_coordinates()
        print("Final position after picking up Secret Key:", pos)
        
else:
    print("Failed to start bypass route from (9, 10)")
    exit(1)

print("Secret Key master route completed successfully!")
