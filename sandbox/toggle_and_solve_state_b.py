import mgba
import time
import sys
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
print("Starting Self-Correcting State B Solver from:", pos)

# Walk back to Column 1 Row 12
if pos == {"x": 4, "y": 10}:
    print("Walking to (1, 12)...")
    run_steps([
        ("Down", {"x": 4, "y": 11}),
        ("Down", {"x": 4, "y": 12}),
        ("Left", {"x": 3, "y": 12}),
        ("Left", {"x": 2, "y": 12}),
        ("Left", {"x": 1, "y": 12}),
    ])
    pos = mgba.get_coordinates()

# Test Column 1 Row 9
is_column1_open = False
if pos == {"x": 1, "y": 12}:
    if walk_step("Up", {"x": 1, "y": 11}):
        if walk_step("Up", {"x": 1, "y": 10}):
            success = walk_step("Up", {"x": 1, "y": 9}, retries=2)
            if success:
                print("Column 1 Row 9 is OPEN! Mansion is in State B.")
                is_column1_open = True
            else:
                print("Column 1 Row 9 is BLOCKED. Mansion is in State A.")
                is_column1_open = False
                # Walk back down
                walk_step("Down", {"x": 1, "y": 11})
                walk_step("Down", {"x": 1, "y": 12})

# If it is blocked, toggle the switch to change State A -> State B!
if not is_column1_open:
    pos = mgba.get_coordinates()
    if pos == {"x": 1, "y": 12}:
        print("Walking to the switch at (2, 12)...")
        walk_step("Right", {"x": 2, "y": 12})
        pos = mgba.get_coordinates()
        
    if pos == {"x": 2, "y": 12}:
        print("Toggling the switch to State B...")
        mgba.press_buttons(["Up", "sleep 400", "A", "sleep 1000", "A", "sleep 1000", "A", "sleep 1000", "A"])
        time.sleep(4.0)
        
        # Verify switch was toggled by walking back to Column 1 and trying to walk UP
        print("Verifying if Column 1 Row 9 is now open...")
        if walk_step("Left", {"x": 1, "y": 12}):
            if walk_step("Up", {"x": 1, "y": 11}):
                if walk_step("Up", {"x": 1, "y": 10}):
                    success = walk_step("Up", {"x": 1, "y": 9}, retries=4)
                    if success:
                        print("Column 1 Row 9 is now OPEN! Successfully toggled to State B.")
                        is_column1_open = True
                    else:
                        print("CRITICAL ERROR: Column 1 Row 9 is STILL blocked after toggle!")
                        exit(1)

# Now complete the Master Route to retrieve the Secret Key!
if is_column1_open:
    pos = mgba.get_coordinates()
    if pos == {"x": 1, "y": 9}:
        print("Completing route up Column 1 to Row 6...")
        steps_to_row6 = [
            ("Up", {"x": 1, "y": 8}),
            ("Up", {"x": 1, "y": 7}),
            ("Up", {"x": 1, "y": 6}),
        ]
        if not run_steps(steps_to_row6):
            print("Failed to reach Row 6")
            exit(1)
        pos = mgba.get_coordinates()
        
    if pos == {"x": 1, "y": 6}:
        print("Walking RIGHT along Row 6 to 3F East (Column 26)...")
        steps_east = []
        for x in range(2, 27):
            steps_east.append(("Right", {"x": x, "y": 6}))
        if not run_steps(steps_east):
            print("Failed to reach (26, 6) on 3F East")
            exit(1)
        pos = mgba.get_coordinates()
        
    # On 3F East at (26, 6), we walk up to (26, 3) (which is Row 3) and fall through the pitfall
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
        
    # Step DOWN/RIGHT onto the pitfall to fall to 1F East inside the fenced room!
    if pos == {"x": 26, "y": 3}:
        print("Stepping DOWN to fall through the pitfall...")
        mgba.press_buttons(["Down"])
        time.sleep(2.5)
        pos = mgba.get_coordinates()
        print("Position after dropping to 1F East:", pos)
        
    # From 1F East fenced room at (26, 4), walk to the B1F East stairs at (22, 2) and warp down
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
        
    # On B1F East stairs landing, cross horizontally to B1F West NORTH and pick up the Secret Key!
    # Landing on B1F East stairs is at (22, 2).
    # Wait, the stairs warp is at (22, 2).
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
        
    # Stand at (1, 5) facing UP, pick up the Secret Key!
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
    print("Failed to ensure Column 1 Row 9 is OPEN!")
    exit(1)

print("Secret Key master route completed successfully!")
