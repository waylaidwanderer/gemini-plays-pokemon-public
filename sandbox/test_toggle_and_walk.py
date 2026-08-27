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
        
        # Check if still in battle
        scr_file2 = mgba.take_screenshot()
        img2 = Image.open(scr_file2)
        img_std2 = img2.resize((160, 144), Image.Resampling.NEAREST)
        black_or_white2 = 0
        for y in range(115, 140):
            for x in range(10, 150):
                r, g, b = img_std2.getpixel((x, y))[:3]
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

# Close any open menu
mgba.press_buttons(["B"])
time.sleep(0.3)

pos = mgba.get_coordinates()
print("Starting position:", pos)

# We are at (14, 3) on 2F West. Walk DOWN Column 14 to Row 11, then LEFT to (2, 12)
if pos == {"x": 14, "y": 3}:
    print("Walking down Column 14 to Row 11...")
    steps = []
    for y in range(4, 12):
        steps.append(("Down", {"x": 14, "y": y}))
    if not run_steps(steps):
        print("Failed to walk down Column 14")
        exit(1)
    pos = mgba.get_coordinates()

# Now on (14, 11). Walk LEFT along Row 11 to Column 2 (2, 11) then DOWN to (2, 12)
if pos == {"x": 14, "y": 11}:
    print("Walking left along Row 11 to Column 2...")
    steps = []
    for x in range(13, 1, -1):
        steps.append(("Left", {"x": x, "y": 11}))
    steps.append(("Down", {"x": 2, "y": 12}))
    if not run_steps(steps):
        print("Failed to reach (2, 12)")
        exit(1)
    pos = mgba.get_coordinates()

# Stand at (2, 12) facing UP to toggle the Mewtwo switch at (2, 11)
if pos == {"x": 2, "y": 12}:
    print("Aligning UP towards the Mewtwo switch at (2, 11)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    print("Interacting with Mewtwo switch...")
    # Toggling switch requires 4 A-presses:
    # 1. "A secret switch!"
    # 2. "Press it?" -> Yes/No prompt
    # 3. YES selected -> "Who wouldn't?"
    # 4. Dismiss dialogue box.
    mgba.press_buttons([
        "A", "sleep 1000",
        "A", "sleep 1000",
        "A", "sleep 1000",
        "A", "sleep 1000"
    ])
    time.sleep(5.0)
    
    pos = mgba.get_coordinates()
    print("Position after switch interaction:", pos)

# Walk back to Column 14 Row 11, then UP to Row 3 (14, 3)
if pos == {"x": 2, "y": 12}:
    print("Walking back to (14, 11)...")
    steps = [("Up", {"x": 2, "y": 11})]
    for x in range(3, 15):
        steps.append(("Right", {"x": x, "y": 11}))
    if not run_steps(steps):
        print("Failed to return to (14, 11)")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 14, "y": 11}:
    print("Walking up Column 14 to Row 3...")
    steps = []
    for y in range(10, 2, -1):
        steps.append(("Up", {"x": 14, "y": y}))
    if not run_steps(steps):
        print("Failed to reach (14, 3)")
        exit(1)
    pos = mgba.get_coordinates()

# Take a screenshot to inspect if the Column 15 gate is now open!
mgba.take_screenshot()
print("Screenshot taken of final overworld state after toggling!")

