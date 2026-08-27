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

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

pos = mgba.get_coordinates()
print("Starting position:", pos)

# 1. Walk from current position (6, 12) on 3F West to the stairs at (7, 10) to warp down to 2F West
if pos == {"x": 6, "y": 12}:
    print("Walking up Column 6 to bypass the solid wall at (7, 12)...")
    steps_to_stairs = [
        ("Up", {"x": 6, "y": 11}),
        ("Right", {"x": 7, "y": 11}),
    ]
    if not run_steps(steps_to_stairs):
        print("Failed to reach stairs threshold (7, 11)")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 7, "y": 11}:
    print("Stepping UP onto stairs to warp down to 2F West...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after warping down to 2F West:", pos)

# 2. Once on 2F West (landing at (7, 11)), walk to Column 5
if pos == {"x": 7, "y": 11} or pos == {"x": 7, "y": 10}:
    if pos["y"] == 10:
        walk_step("Down", {"x": 7, "y": 11})
        pos = mgba.get_coordinates()
        
    print("Walking to Column 5 on 2F West...")
    steps_to_col5 = [
        ("Left", {"x": 6, "y": 11}),
        ("Left", {"x": 5, "y": 11}),
    ]
    if not run_steps(steps_to_col5):
        print("Failed to reach Column 5")
        exit(1)
    pos = mgba.get_coordinates()

# 3. Walk UP Column 5 directly to Row 3 (open in State B)
if pos == {"x": 5, "y": 11}:
    print("Walking UP Column 5 to Row 3...")
    steps_up_col5 = []
    for y in range(10, 2, -1):
        steps_up_col5.append(("Up", {"x": 5, "y": y}))
    if not run_steps(steps_up_col5):
        print("Failed to reach Row 3 on Column 5")
        exit(1)
    pos = mgba.get_coordinates()

# 4. Walk RIGHT along Row 3 to Column 18 (crosses West to East)
if pos == {"x": 5, "y": 3}:
    print("Walking RIGHT along Row 3 to Column 18...")
    steps_cross = []
    for x in range(6, 19):
        steps_cross.append(("Right", {"x": x, "y": 3}))
    if not run_steps(steps_cross):
         print("Failed to cross to 2F East on Row 3")
         exit(1)
    pos = mgba.get_coordinates()

# 5. Walk DOWN Column 18 to Row 10
if pos == {"x": 18, "y": 3}:
    print("Walking DOWN Column 18 to Row 10...")
    steps_down_col18 = []
    for y in range(4, 11):
        steps_down_col18.append(("Down", {"x": 18, "y": y}))
    if not run_steps(steps_down_col18):
         print("Failed to reach Row 10 on Column 18")
         exit(1)
    pos = mgba.get_coordinates()

# 6. Walk LEFT along Row 10 to Column 15
if pos == {"x": 18, "y": 10}:
    print("Walking LEFT along Row 10 to Column 15...")
    steps_to_stairs2f = [
        ("Left", {"x": 17, "y": 10}),
        ("Left", {"x": 16, "y": 10}),
        ("Left", {"x": 15, "y": 10}),
    ]
    if not run_steps(steps_to_stairs2f):
        print("Failed to reach Column 15 on Row 10")
        exit(1)
    pos = mgba.get_coordinates()

# 7. Step DOWN onto the stairs at (15, 11) to warp UP to 3F East
if pos == {"x": 15, "y": 10}:
    print("Stepping DOWN onto stairs to warp UP to 3F East...")
    mgba.press_buttons(["Down"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after warping UP to 3F East:", pos)

# 8. On 3F East (landing at (16, 11)), walk RIGHT along Row 11 to Column 20
if pos == {"x": 16, "y": 11} or pos == {"x": 16, "y": 10}:
    if pos["y"] == 10:
        walk_step("Down", {"x": 16, "y": 11})
        pos = mgba.get_coordinates()
        
    print("Walking RIGHT along Row 11 to Column 20...")
    steps_to_col20_3f = [
        ("Right", {"x": 17, "y": 11}),
        ("Right", {"x": 18, "y": 11}),
        ("Right", {"x": 19, "y": 11}),
        ("Right", {"x": 20, "y": 11}),
    ]
    if not run_steps(steps_to_col20_3f):
        print("Failed to reach Column 20 on Row 11")
        exit(1)
    pos = mgba.get_coordinates()

# 9. Walk UP Column 20 to Row 3
if pos == {"x": 20, "y": 11}:
    print("Walking UP Column 20 to Row 3...")
    steps_up_col20_3f = []
    for y in range(10, 2, -1):
         steps_up_col20_3f.append(("Up", {"x": 20, "y": y}))
    if not run_steps(steps_up_col20_3f):
        print("Failed to reach Row 3 on Column 20")
        exit(1)
    pos = mgba.get_coordinates()

# 10. Walk RIGHT along Row 3 to Column 26
if pos == {"x": 20, "y": 3}:
    print("Walking RIGHT along Row 3 to Column 26...")
    steps_to_pit = []
    for x in range(21, 27):
        steps_to_pit.append(("Right", {"x": x, "y": 3}))
    if not run_steps(steps_to_pit):
        print("Failed to reach Column 26 on Row 3")
        exit(1)
    pos = mgba.get_coordinates()

# 11. Step DOWN to drop through the pitfall to 1F East inside the fenced room
if pos == {"x": 26, "y": 3}:
    print("Stepping DOWN to drop through the pitfall to 1F East...")
    mgba.press_buttons(["Down"])
    time.sleep(2.5)
    pos = mgba.get_coordinates()
    print("Position after dropping to 1F East:", pos)

# 12. Walk to B1F East stairs
if pos == {"x": 26, "y": 4}:
    print("Walking to B1F East stairs...")
    steps_to_stairs_1f = [
        ("Left", {"x": 25, "y": 4}),
        ("Left", {"x": 24, "y": 4}),
        ("Left", {"x": 23, "y": 4}),
        ("Left", {"x": 22, "y": 4}),
        ("Up", {"x": 22, "y": 3}),
    ]
    if not run_steps(steps_to_stairs_1f):
        print("Failed to reach 1F East stairs")
        exit(1)
        
    print("Stepping UP to warp down to B1F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after warping down to B1F East:", pos)

# 13. Cross B1F East to B1F West NORTH and retrieve Secret Key!
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

# 14. Standing at (1, 5) facing UP, pick up the Secret Key!
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

# 15. Walk back to B1F East stairs from (1, 5)
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

# 16. Walk out of the Mansion via 1F East -> 1F West Row 5
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
