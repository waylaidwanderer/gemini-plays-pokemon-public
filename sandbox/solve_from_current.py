import mgba
import time
from PIL import Image

def is_dialogue_open():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file).resize((160, 144), Image.Resampling.NEAREST)
    cropped = img.crop((0, 104, 160, 144))
    
    white_cream_pixels = 0
    for y in range(cropped.height):
        for x in range(cropped.width):
            r, g, b = cropped.getpixel((x, y))[:3]
            if r > 200 and g > 200 and b > 200:
                white_cream_pixels += 1
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

pos = mgba.get_coordinates()
print("Starting position:", pos)

# We are at (5, 10) on 2F West. Walk to Column 14 Row 11
if pos == {"x": 5, "y": 10}:
    print("Walking to Row 11 Column 14...")
    steps = [
        ("Down", {"x": 5, "y": 11}),
        ("Right", {"x": 6, "y": 11}),
        ("Right", {"x": 7, "y": 11}),
        ("Right", {"x": 8, "y": 11}),
        ("Right", {"x": 9, "y": 11}),
        ("Right", {"x": 10, "y": 11}),
        ("Right", {"x": 11, "y": 11}),
        ("Right", {"x": 12, "y": 11}),
        ("Right", {"x": 13, "y": 11}),
        ("Right", {"x": 14, "y": 11}),
    ]
    if not run_steps(steps):
        print("Failed to reach (14, 11)")
        exit(1)
    pos = mgba.get_coordinates()

# Now on (14, 11). Walk UP Column 14 to Row 3 (14, 3)
if pos == {"x": 14, "y": 11}:
    print("Walking UP Column 14 directly to Row 3...")
    steps = []
    for y in range(10, 2, -1):
        steps.append(("Up", {"x": 14, "y": y}))
    if not run_steps(steps):
        print("Failed to reach (14, 3) on 2F West")
        exit(1)
    pos = mgba.get_coordinates()

# Walk RIGHT along Row 3 to Column 18 (crosses horizontally to 2F East)
if pos == {"x": 14, "y": 3}:
    print("Crossing horizontally to 2F East along Row 3...")
    steps = []
    for x in range(15, 19):
        steps.append(("Right", {"x": x, "y": 3}))
    if not run_steps(steps):
        print("Failed to reach (18, 3) on 2F East")
        exit(1)
    pos = mgba.get_coordinates()

# Walk DOWN Column 18 to Row 10 (18, 10)
if pos == {"x": 18, "y": 3}:
    print("Walking DOWN Column 18 to Row 10...")
    steps = []
    for y in range(4, 11):
        steps.append(("Down", {"x": 18, "y": y}))
    if not run_steps(steps):
        print("Failed to reach (18, 10) on 2F East")
        exit(1)
    pos = mgba.get_coordinates()

# Walk LEFT along Row 10 to Column 15 (15, 10)
if pos == {"x": 18, "y": 10}:
    print("Walking LEFT along Row 10 to (15, 10)...")
    steps = [
        ("Left", {"x": 17, "y": 10}),
        ("Left", {"x": 16, "y": 10}),
        ("Left", {"x": 15, "y": 10}),
    ]
    if not run_steps(steps):
        print("Failed to reach (15, 10) on 2F East")
        exit(1)
    pos = mgba.get_coordinates()

# Step DOWN onto stairs at (15, 11) to warp
if pos == {"x": 15, "y": 10}:
    print("Stepping DOWN onto stairs to test floor warp...")
    mgba.press_buttons(["Down"])
    time.sleep(2.5)
    pos = mgba.get_coordinates()
    print("Position after warping:", pos)

# We are testing which floor we landed on!
# If we are in State B, we land on 3F East (16, 11 or 15, 11).
# If we are in State A, we land on 1F East (15, 11).
# We can check which floor by taking a step and checking the coordinates/behavior.
# Wait, let's walk LEFT on Row 11:
# On 3F East, Row 11 is blocked at Column 13 in State A, but in State B we came from 3F East.
# Actually, the easiest way is to just walk to (11, 11) or check coordinates.
# Let's walk RIGHT to (20, 11).
# On 3F East, (20, 11) is a walkable tile leading UP to (20, 3).
# On 1F East, (20, 11) is NOT a walkable tile (or has different obstacles).
# Let's walk RIGHT. If we are on 3F East:
# Let's try to execute the 3F East to B1F West route!
# If we fail, it means we landed on 1F East (State A).

# Now on 3F East (landing at 16, 11 or 15, 11). Walk RIGHT along Row 11 to Column 20
if pos == {"x": 16, "y": 11} or pos == {"x": 15, "y": 11}:
    pos_x = pos["x"]
    print("Attempting to walk RIGHT along Row 11 to Column 20 (assuming we are on 3F East)...")
    steps = []
    for x in range(pos_x + 1, 21):
        steps.append(("Right", {"x": x, "y": 11}))
    
    if run_steps(steps):
        pos = mgba.get_coordinates()
        if pos == {"x": 20, "y": 11}:
            print("Successfully reached (20, 11)! We are on 3F East (State B)!")
            
            # Continue the master State B solve!
            # Walk UP Column 20 to Row 3 (20, 3)
            print("Walking UP Column 20 to Row 3...")
            steps = []
            for y in range(10, 2, -1):
                steps.append(("Up", {"x": 20, "y": y}))
            if not run_steps(steps):
                print("Failed to reach (20, 3) on 3F East")
                exit(1)
            pos = mgba.get_coordinates()

            # Walk RIGHT along Row 3 to Column 26
            if pos == {"x": 20, "y": 3}:
                print("Walking RIGHT along Row 3 to Column 26...")
                steps = []
                for x in range(21, 27):
                    steps.append(("Right", {"x": x, "y": 3}))
                if not run_steps(steps):
                    print("Failed to reach (26, 3) on 3F East")
                    exit(1)
                pos = mgba.get_coordinates()

            # Step DOWN to drop through the pitfall to 1F East inside the fenced room (landing at 26, 4)
            if pos == {"x": 26, "y": 3}:
                print("Stepping DOWN to drop through the pitfall to 1F East...")
                mgba.press_buttons(["Down"])
                time.sleep(2.5)
                pos = mgba.get_coordinates()
                print("Position after dropping to 1F East:", pos)

            # Now inside the fenced room at (26, 4). Walk LEFT along Row 4 to Column 22
            if pos == {"x": 26, "y": 4} or pos == {"x": 25, "y": 4}:
                pos_x = pos["x"]
                print("Walking LEFT along Row 4 to Column 22...")
                steps = []
                for x in range(pos_x - 1, 21, -1):
                    steps.append(("Left", {"x": x, "y": 4}))
                if not run_steps(steps):
                    print("Failed to reach (22, 4) on 1F East")
                    exit(1)
                pos = mgba.get_coordinates()

            # Walk UP to (22, 3)
            if pos == {"x": 22, "y": 4}:
                print("Walking UP to (22, 3)...")
                if not walk_step("Up", {"x": 22, "y": 3}):
                    print("Failed to reach (22, 3)")
                    exit(1)
                pos = mgba.get_coordinates()

            # Step UP to warp down to B1F East (landing at 22, 3 or 22, 2)
            if pos == {"x": 22, "y": 3}:
                print("Stepping UP to warp down to B1F East...")
                mgba.press_buttons(["Up"])
                time.sleep(2.0)
                pos = mgba.get_coordinates()
                print("Position after warping down to B1F East:", pos)

            # Now on B1F East (landing at 22, 3 or 22, 2). Walk to Row 5
            if pos["x"] == 22 and (pos["y"] == 2 or pos["y"] == 3):
                print("Walking to Row 5...")
                steps = []
                for y in range(pos["y"] + 1, 6):
                    steps.append(("Down", {"x": 22, "y": y}))
                if not run_steps(steps):
                    print("Failed to reach (22, 5) on B1F East")
                    exit(1)
                pos = mgba.get_coordinates()

            # Cross B1F East to B1F West NORTH along Row 5 across Column 9 gate
            if pos == {"x": 22, "y": 5}:
                print("Walking LEFT along Row 5 to Column 19...")
                steps = [
                    ("Left", {"x": 21, "y": 5}),
                    ("Left", {"x": 20, "y": 5}),
                    ("Left", {"x": 19, "y": 5}),
                ]
                if not run_steps(steps):
                    print("Failed to reach (19, 5) on B1F East")
                    exit(1)
                pos = mgba.get_coordinates()

            if pos == {"x": 19, "y": 5}:
                print("Walking LEFT along Row 5 to B1F West NORTH (Secret Key Room)...")
                steps = []
                for x in range(18, 0, -1):
                    steps.append(("Left", {"x": x, "y": 5}))
                if not run_steps(steps):
                    print("Failed to reach (1, 5) on B1F West NORTH")
                    exit(1)
                pos = mgba.get_coordinates()

            # Standing at (1, 5) facing UP, pick up the Secret Key!
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

            print("Mansion master route completed successfully!")
            exit(0)

    # If we get here, it means we are in State A (since the 3F East stairs route failed or we landed on 1F East).
    print("Detected State A! Performing State A to State B recovery route...")
    
    # We are on 1F East (landing at 15, 11). Walk back to 1F West to warp UP.
    pos = mgba.get_coordinates()
    print("Current position on 1F East:", pos)
    
    # Walk left on Row 11 to Column 14 (14, 11)
    if pos["y"] == 11 and pos["x"] > 14:
        steps_left = []
        for x in range(pos["x"] - 1, 13, -1):
            steps_left.append(("Left", {"x": x, "y": 11}))
        if not run_steps(steps_left):
            print("Failed to reach (14, 11) on 1F East/West")
            exit(1)
        pos = mgba.get_coordinates()
        
    # On 1F West, Column 13 Row 11 is blocked by a Scientist NPC, but Column 14 Row 11 is completely open!
    # Wait, can we walk left from (14, 11) to (5, 11) on 1F West?
    # Yes, Column 5 to Column 14 on Row 11 is completely open on 1F!
    if pos == {"x": 14, "y": 11}:
        print("Walking LEFT along Row 11 on 1F West to Column 5...")
        steps_left_1f = []
        for x in range(13, 4, -1):
            steps_left_1f.append(("Left", {"x": x, "y": 11}))
        if not run_steps(steps_left_1f):
            print("Failed to reach (5, 11) on 1F West")
            exit(1)
        pos = mgba.get_coordinates()

    # Now at (5, 11) on 1F West. Walk UP to (5, 10)
    if pos == {"x": 5, "y": 11}:
        print("Walking UP to (5, 10) on 1F West...")
        if not walk_step("Up", {"x": 5, "y": 10}):
            print("Failed to reach (5, 10)")
            exit(1)
        pos = mgba.get_coordinates()

    # Step LEFT onto stairs at (5, 10) to warp UP to 2F West (landing at 5, 11)
    if pos == {"x": 5, "y": 10}:
        print("Stepping LEFT onto stairs to warp UP to 2F West...")
        mgba.press_buttons(["Left"])
        time.sleep(2.0)
        pos = mgba.get_coordinates()
        print("Position after warping UP to 2F West:", pos)

    # Now on 2F West (landing at 5, 11). Walk to (7, 11) and warp UP to 3F West (landing at 7, 11)
    if pos == {"x": 5, "y": 11}:
        print("Walking to 3F West stairs...")
        steps_to_3f = [
            ("Right", {"x": 6, "y": 11}),
            ("Right", {"x": 7, "y": 11}),
            ("Up", {"x": 7, "y": 10}),
        ]
        if not run_steps(steps_to_3f):
            print("Failed to reach 3F West stairs")
            exit(1)
        
        print("Stepping UP to warp to 3F West...")
        mgba.press_buttons(["Up"])
        time.sleep(2.0)
        pos = mgba.get_coordinates()
        print("Position after warping UP to 3F West:", pos)

    # Walk to (1, 13) on 3F West
    if pos["x"] == 7 and (pos["y"] == 11 or pos["y"] == 10):
        pos_y = pos["y"]
        print("Walking to (1, 13) on 3F West...")
        steps = []
        if pos_y == 10:
            steps.append(("Down", {"x": 7, "y": 11}))
        steps.extend([
            ("Left", {"x": 6, "y": 11}),
            ("Left", {"x": 5, "y": 11}),
            ("Left", {"x": 4, "y": 11}),
            ("Left", {"x": 3, "y": 11}),
            ("Left", {"x": 2, "y": 11}),
            ("Down", {"x": 2, "y": 12}),
            ("Down", {"x": 2, "y": 13}),
            ("Left", {"x": 1, "y": 13}),
        ])
        if not run_steps(steps):
            print("Failed to reach (1, 13) on 3F West")
            exit(1)
        pos = mgba.get_coordinates()

    # Stand at (1, 13) facing UP and toggle the Mewtwo switch at (1, 12)
    if pos == {"x": 1, "y": 13}:
        print("Aligning UP towards (1, 12)...")
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        
        print("Pressing A to toggle switch...")
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
        print("Selecting YES to toggle switch...")
        mgba.press_buttons(["A"])
        time.sleep(1.2)
        
        # Dismiss result
        mgba.press_buttons(["A"])
        time.sleep(1.2)
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
        print("Mansion gates toggled to State B!")
        pos = mgba.get_coordinates()

    # Now in State B! Walk UP Column 2 (since the Row 9 gate at 2,9 is now open!) to Row 6 (2, 6)
    if pos == {"x": 1, "y": 13}:
        print("Walking to Row 6 in State B...")
        steps_to_row6 = [
            ("Right", {"x": 2, "y": 13}),
            ("Up", {"x": 2, "y": 12}),
            ("Up", {"x": 2, "y": 11}),
            ("Up", {"x": 2, "y": 10}),
            ("Up", {"x": 2, "y": 9}),  # Through open Row 9 gate!
            ("Up", {"x": 2, "y": 8}),
            ("Up", {"x": 2, "y": 7}),
            ("Up", {"x": 2, "y": 6}),
        ]
        if not run_steps(steps_to_row6):
            print("Failed to reach (2, 6)")
            exit(1)
        pos = mgba.get_coordinates()

    # Walk RIGHT along Row 6 to Column 20 on 3F East (crossing horizontally)
    if pos == {"x": 2, "y": 6}:
        print("Walking RIGHT along Row 6 to Column 20...")
        steps_east = []
        for x in range(3, 21):
            steps_east.append(("Right", {"x": x, "y": 6}))
        if not run_steps(steps_east):
            print("Failed to reach Column 20 on Row 6")
            exit(1)
        pos = mgba.get_coordinates()

    # Walk UP Column 20 to Row 3
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

    # Walk RIGHT along Row 3 to Column 26
    if pos == {"x": 20, "y": 3}:
        print("Walking RIGHT along Row 3 to Column 26...")
        steps_to_pit = []
        for x in range(21, 27):
            steps_to_pit.append(("Right", {"x": x, "y": 3}))
        if not run_steps(steps_to_pit):
            print("Failed to reach Column 26 on Row 3")
            exit(1)
        pos = mgba.get_coordinates()

    # Step DOWN to drop through the pitfall to 1F East inside the fenced room
    if pos == {"x": 26, "y": 3}:
        print("Stepping DOWN to drop through the pitfall to 1F East...")
        mgba.press_buttons(["Down"])
        time.sleep(2.5)
        pos = mgba.get_coordinates()
        print("Position after dropping to 1F East:", pos)

    # Now inside the fenced room at (26, 4). Walk LEFT along Row 4 to Column 22
    if pos == {"x": 26, "y": 4} or pos == {"x": 25, "y": 4}:
        pos_x = pos["x"]
        print("Walking LEFT along Row 4 to Column 22...")
        steps = []
        for x in range(pos_x - 1, 21, -1):
            steps.append(("Left", {"x": x, "y": 4}))
        if not run_steps(steps):
            print("Failed to reach (22, 4) on 1F East")
            exit(1)
        pos = mgba.get_coordinates()

    # Walk UP to (22, 3)
    if pos == {"x": 22, "y": 4}:
        print("Walking UP to (22, 3)...")
        if not walk_step("Up", {"x": 22, "y": 3}):
            print("Failed to reach (22, 3)")
            exit(1)
        pos = mgba.get_coordinates()

    # Step UP to warp down to B1F East (landing at 22, 3 or 22, 2)
    if pos == {"x": 22, "y": 3}:
        print("Stepping UP to warp down to B1F East...")
        mgba.press_buttons(["Up"])
        time.sleep(2.0)
        pos = mgba.get_coordinates()
        print("Position after warping down to B1F East:", pos)

    # Now on B1F East (landing at 22, 3 or 22, 2). Walk to Row 5
    if pos["x"] == 22 and (pos["y"] == 2 or pos["y"] == 3):
        print("Walking to Row 5...")
        steps = []
        for y in range(pos["y"] + 1, 6):
            steps.append(("Down", {"x": 22, "y": y}))
        if not run_steps(steps):
            print("Failed to reach (22, 5) on B1F East")
            exit(1)
        pos = mgba.get_coordinates()

    # Cross B1F East to B1F West NORTH along Row 5 across Column 9 gate
    if pos == {"x": 22, "y": 5}:
        print("Walking LEFT along Row 5 to Column 19...")
        steps = [
            ("Left", {"x": 21, "y": 5}),
            ("Left", {"x": 20, "y": 5}),
            ("Left", {"x": 19, "y": 5}),
        ]
        if not run_steps(steps):
            print("Failed to reach (19, 5) on B1F East")
            exit(1)
        pos = mgba.get_coordinates()

    if pos == {"x": 19, "y": 5}:
        print("Walking LEFT along Row 5 to B1F West NORTH (Secret Key Room)...")
        steps = []
        for x in range(18, 0, -1):
            steps.append(("Left", {"x": x, "y": 5}))
        if not run_steps(steps):
            print("Failed to reach (1, 5) on B1F West NORTH")
            exit(1)
        pos = mgba.get_coordinates()

    # Standing at (1, 5) facing UP, pick up the Secret Key!
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

    print("Mansion master route completed successfully!")
