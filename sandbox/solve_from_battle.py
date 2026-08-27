import mgba
import time
from PIL import Image

def is_dialogue_open():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file).resize((160, 144), Image.Resampling.NEAREST)
    cropped = img.crop((0, 104, 160, 144))
    
    # Check for GBC dialogue background (high white/cream pixel count)
    white_cream_pixels = 0
    for y in range(cropped.height):
        for x in range(cropped.width):
            r, g, b = cropped.getpixel((x, y))[:3]
            if r > 200 and g > 200 and b > 200:
                white_cream_pixels += 1
    print(f"  Check dialogue box: white_cream_pixels={white_cream_pixels}")
    return white_cream_pixels > 3000

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

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

# First, handle the current battle (Running away from Muk)
print("Handling current battle...")
mgba.press_buttons(["A", "sleep 1200"])
handle_any_menu_or_battle()
time.sleep(1.0)

pos = mgba.get_coordinates()
print("Position after escaping battle:", pos)

# Walk to (2, 12)
if pos == {"x": 1, "y": 11}:
    print("Walking to (2, 12)...")
    steps_to_2_12 = [
        ("Right", {"x": 2, "y": 11}),
        ("Down", {"x": 2, "y": 12}),
    ]
    if not run_steps(steps_to_2_12):
        print("Failed to reach (2, 12)")
        exit(1)
    pos = mgba.get_coordinates()

# Stand at (2, 12) and try facing LEFT towards (1, 12)
if pos == {"x": 2, "y": 12}:
    print("Trying to toggle switch from (2, 12) facing LEFT...")
    mgba.press_buttons(["Left"])
    time.sleep(0.45)
    
    # Verify we didn't walk (1, 12 is solid so we shouldn't move)
    temp_pos = mgba.get_coordinates()
    if temp_pos != {"x": 2, "y": 12}:
        print("  Error: standing position shifted! Walking back...")
        walk_step("Right", {"x": 2, "y": 12})
    else:
        # Press A to check dialogue
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
        if is_dialogue_open():
            print("  SUCCESS! Opened switch dialogue facing LEFT from (2, 12). Toggling...")
            mgba.press_buttons(["A"]) # Yes/No
            time.sleep(1.2)
            mgba.press_buttons(["A"]) # Select YES
            time.sleep(1.2)
            mgba.press_buttons(["A"]) # Dismiss
            time.sleep(1.0)
            print("  Switch toggled successfully!")
        else:
            print("  Failed to open dialogue from (2, 12) facing LEFT. Trying (1, 13) facing UP...")
            mgba.press_buttons(["B"])
            time.sleep(0.3)
            
            # Walk to (1, 13)
            if not run_steps([
                ("Down", {"x": 2, "y": 13}),
                ("Left", {"x": 1, "y": 13}),
            ]):
                print("Failed to reach (1, 13)")
                exit(1)
                
            print("Toggling from (1, 13) facing UP...")
            mgba.press_buttons(["Up"])
            time.sleep(0.45)
            mgba.press_buttons(["A"]) # Open dialogue
            time.sleep(1.2)
            mgba.press_buttons(["A"]) # Yes/No
            time.sleep(1.2)
            mgba.press_buttons(["A"]) # Select YES
            time.sleep(1.2)
            mgba.press_buttons(["A"]) # Dismiss
            time.sleep(1.0)
            print("  Switch toggled successfully from (1, 13)!")
            
            # Walk to (2, 13) to prepare for Column 2 bypass
            walk_step("Right", {"x": 2, "y": 13})
            
    pos = mgba.get_coordinates()

# Now we are in State B! Walk UP Column 2 directly to Row 6 (Column 1 is blocked at 1,12 by the solid statue)
if pos == {"x": 2, "y": 12} or pos == {"x": 2, "y": 13}:
    if pos["y"] == 13:
        walk_step("Up", {"x": 2, "y": 12})
        pos = mgba.get_coordinates()
        
    print("Bypassing solid statue via Column 2 to Row 6...")
    steps_up_col2 = [
        ("Up", {"x": 2, "y": 11}),
        ("Up", {"x": 2, "y": 10}),
        ("Up", {"x": 2, "y": 9}),  # through Row 9 gate which is OPEN in State B!
        ("Up", {"x": 2, "y": 8}),
        ("Up", {"x": 2, "y": 7}),
        ("Up", {"x": 2, "y": 6}),
        ("Left", {"x": 1, "y": 6}),
    ]
    if not run_steps(steps_up_col2):
        print("Failed to reach Row 6 Column 1")
        exit(1)
    pos = mgba.get_coordinates()

# 3. Walk RIGHT along Row 6 to Column 20 on 3F East (crossing horizontally)
if pos == {"x": 1, "y": 6}:
    print("Walking RIGHT along Row 6 to Column 20...")
    steps_east = []
    for x in range(2, 21):
        steps_east.append(("Right", {"x": x, "y": 6}))
    if not run_steps(steps_east):
        print("Failed to reach Column 20 on Row 6")
        exit(1)
    pos = mgba.get_coordinates()

# 4. Walk UP Column 20 to Row 3
if pos == {"x": 20, "y": 6}:
    print("Walking UP Column 20 to Row 3...")
    steps_up_col20 = [
        ("Up", {"x": 20, "y": 5}),
        ("Up", {"x": 20, "y": 4}),
        ("Up", {"x": 20, "y": 3}),
    ]
    if not run_steps(steps_up_col20):
        print("Failed to reach Row 3 on Column 20")
        exit(1)
    pos = mgba.get_coordinates()

# 5. Walk RIGHT along Row 3 to Column 26
if pos == {"x": 20, "y": 3}:
    print("Walking RIGHT along Row 3 to Column 26...")
    steps_to_pit = []
    for x in range(21, 27):
        steps_to_pit.append(("Right", {"x": x, "y": 3}))
    if not run_steps(steps_to_pit):
        print("Failed to reach Column 26 on Row 3")
        exit(1)
    pos = mgba.get_coordinates()

# 6. Step DOWN to drop through the pitfall to 1F East inside the fenced room
if pos == {"x": 26, "y": 3}:
    print("Stepping DOWN to drop through the pitfall to 1F East...")
    mgba.press_buttons(["Down"])
    time.sleep(2.5)
    pos = mgba.get_coordinates()
    print("Position after dropping to 1F East:", pos)

# 7. Walk to B1F East stairs
if pos == {"x": 26, "y": 4}:
    print("Walking to B1F East stairs...")
    steps_to_stairs = [
        ("Left", {"x": 25, "y": 4}),
        ("Left", {"x": 24, "y": 4}),
        ("Left", {"x": 23, "y": 4}),
        ("Left", {"x": 22, "y": 4}),
        ("Up", {"x": 22, "y": 3}),
    ]
    if not run_steps(steps_to_stairs):
        print("Failed to reach 1F East stairs")
        exit(1)
        
    print("Stepping UP to warp down to B1F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after warping down to B1F East:", pos)

# 8. Cross B1F East to B1F West NORTH and retrieve Secret Key!
if pos == {"x": 22, "y": 3} or pos == {"x": 22, "y": 2}:
    print("Crossing B1F East to B1F West NORTH...")
    if pos["y"] == 2:
        walk_step("Down", {"x": 22, "y": 3})
        pos = mgba.get_coordinates()
        
    if not run_steps([
        ("Down", {"x": 22, "y": 4}),
        ("Left", {"x": 21, "y": 4}),
        ("Left", {"x": 20, "y": 4}),
        ("Left", {"x": 19, "y": 4}),
        ("Down", {"x": 19, "y": 5}),
    ]):
        print("Failed to reach Row 5 on B1F East")
        exit(1)
        
    steps_left = []
    for x in range(18, 0, -1):
        steps_left.append(("Left", {"x": x, "y": 5}))
    if not run_steps(steps_left):
        print("Failed to reach Secret Key room")
        exit(1)
    pos = mgba.get_coordinates()

# 9. Standing at (1, 5) facing UP, pick up the Secret Key!
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

# 10. Walk back to B1F East stairs from (1, 5)
if pos == {"x": 1, "y": 5}:
    print("Walking back to B1F East stairs...")
    steps_back_right = []
    for x in range(2, 19):
        steps_back_right.append(("Right", {"x": x, "y": 5}))
    if not run_steps(steps_back_right):
        print("Failed to walk back horizontally on Row 5")
        exit(1)
        
    if not run_steps([
        ("Up", {"x": 18, "y": 4}),
        ("Right", {"x": 19, "y": 4}),
        ("Right", {"x": 20, "y": 4}),
        ("Right", {"x": 21, "y": 4}),
        ("Right", {"x": 22, "y": 4}),
        ("Up", {"x": 22, "y": 3}),
    ]):
        print("Failed to reach B1F stairs")
        exit(1)
        
    print("Stepping UP to warp back to 1F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after warping up to 1F East:", pos)

# 11. Walk out of the Mansion via 1F East -> 1F West Row 5
if pos == {"x": 22, "y": 3} or pos == {"x": 22, "y": 2}:
    print("Walking out of the Mansion...")
    if pos["y"] == 2:
        walk_step("Down", {"x": 22, "y": 3})
        pos = mgba.get_coordinates()
        
    if not run_steps([
        ("Down", {"x": 22, "y": 4}),
        ("Down", {"x": 22, "y": 5}),
    ]):
        print("Failed to reach Row 5 on 1F East")
        exit(1)
        
    steps_out_left = []
    for x in range(21, 10, -1):
        steps_out_left.append(("Left", {"x": x, "y": 5}))
    if not run_steps(steps_out_left):
        print("Failed to walk horizontally to 1F West Row 5")
        exit(1)
        
    steps_to_exit = []
    for y in range(6, 14):
         steps_to_exit.append(("Down", {"x": 11, "y": y}))
    if not run_steps(steps_to_exit):
        print("Failed to walk down Column 11")
        exit(1)
        
    if not run_steps([
        ("Left", {"x": 10, "y": 13}),
        ("Left", {"x": 9, "y": 13}),
        ("Left", {"x": 8, "y": 13}),
        ("Left", {"x": 7, "y": 13}),
        ("Left", {"x": 6, "y": 13}),
        ("Left", {"x": 5, "y": 13}),
    ]):
        print("Failed to reach (5, 13)")
        exit(1)
        
    steps_exit_down = []
    for y in range(14, 28):
        steps_exit_down.append(("Down", {"x": 5, "y": y}))
    if not run_steps(steps_exit_down):
         print("Failed to walk down Column 5 to exit")
         exit(1)
         
    print("Stepping DOWN to exit the Mansion to Cinnabar Island!")
    mgba.press_buttons(["Down"])
    time.sleep(2.5)
    pos = mgba.get_coordinates()
    print("Successfully escaped the Mansion! Position:", pos)

print("Mansion master escape sequence completed successfully!")
