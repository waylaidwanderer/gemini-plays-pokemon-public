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

# Dismiss any menus
mgba.press_buttons(["B"])
time.sleep(0.4)

pos = mgba.get_coordinates()
print("Starting B1F Secret Key Master Route Solver from:", pos)

# Let's verify we are at (2, 12)
if pos != {"x": 2, "y": 12}:
    print("Unexpected starting position. Walking to (2, 12)...")
    # Walk to (2, 12) if nearby
    # For now, let's assume we are at (2, 12)

# Step 1: Check if switch can be toggled
print("Toggling switch to ensure State B...")
mgba.press_buttons(["Up", "sleep 400", "A", "sleep 1000", "A", "sleep 1000", "A", "sleep 1000", "A"])
time.sleep(4.0)

# Let's check our position after toggle
pos = mgba.get_coordinates()
print("Position after toggling:", pos)

# Step 2: Walk LEFT to Column 1 and try walking UP to Row 6
print("Testing Column 1 route...")
if walk_step("Left", {"x": 1, "y": 12}):
    if walk_step("Up", {"x": 1, "y": 11}):
        if walk_step("Up", {"x": 1, "y": 10}):
            # Try to cross Row 9 on Column 1
            success = walk_step("Up", {"x": 1, "y": 9}, retries=2)
            if success:
                print("Column 1 is WALKABLE at Row 9!")
                # Walk UP to Row 6
                run_steps([
                    ("Up", {"x": 1, "y": 8}),
                    ("Up", {"x": 1, "y": 7}),
                    ("Up", {"x": 1, "y": 6}),
                ])
                print("Successfully crossed to Row 6 on Column 1!")
                # Complete the route to 3F East
                steps_east = []
                for x in range(2, 27):
                    steps_east.append(("Right", {"x": x, "y": 6}))
                run_steps(steps_east)
                exit(0)
            else:
                print("Column 1 Row 9 is BLOCKED.")

# Step 3: If Column 1 is blocked, walk to Column 3 and try walking UP
print("Testing Column 3/Column 2 route...")
pos = mgba.get_coordinates()
if pos == {"x": 1, "y": 10}:
    walk_step("Down", {"x": 1, "y": 11})
    walk_step("Down", {"x": 1, "y": 12})
    pos = mgba.get_coordinates()

if pos == {"x": 1, "y": 12}:
    walk_step("Right", {"x": 2, "y": 12})
    pos = mgba.get_coordinates()

if pos == {"x": 2, "y": 12}:
    if walk_step("Right", {"x": 3, "y": 12}):
        if walk_step("Up", {"x": 3, "y": 11}):
            if walk_step("Up", {"x": 3, "y": 10}):
                # Try to cross Row 9 on Column 3
                success = walk_step("Up", {"x": 3, "y": 9}, retries=2)
                if success:
                    print("Column 3 Row 9 is OPEN!")
                    # Walk to Row 6 on Column 3
                    run_steps([
                        ("Up", {"x": 3, "y": 8}),
                        ("Up", {"x": 3, "y": 7}),
                        ("Up", {"x": 3, "y": 6}),
                    ])
                    # Complete the route to 3F East
                    steps_east = []
                    for x in range(4, 27):
                        steps_east.append(("Right", {"x": x, "y": 6}))
                    run_steps(steps_east)
                    exit(0)
                else:
                    print("Column 3 Row 9 is BLOCKED.")
                    
                # Try walking LEFT to Column 2 on Row 10
                print("Testing if we can cross via Column 2...")
                # We can't walk Left on Row 10 because (2,10) is the statue.
                # Let's try Column 4
                walk_step("Down", {"x": 3, "y": 11})
                walk_step("Down", {"x": 3, "y": 12})
                pos = mgba.get_coordinates()

if pos == {"x": 3, "y": 12}:
    if walk_step("Right", {"x": 4, "y": 12}):
        if walk_step("Up", {"x": 4, "y": 11}):
            if walk_step("Up", {"x": 4, "y": 10}):
                success = walk_step("Up", {"x": 4, "y": 9}, retries=2)
                if success:
                    print("Column 4 Row 9 is OPEN!")
                    run_steps([
                        ("Up", {"x": 4, "y": 8}),
                        ("Up", {"x": 4, "y": 7}),
                        ("Up", {"x": 4, "y": 6}),
                    ])
                    steps_east = []
                    for x in range(5, 27):
                        steps_east.append(("Right", {"x": x, "y": 6}))
                    run_steps(steps_east)
                    exit(0)
                else:
                    print("Column 4 Row 9 is BLOCKED.")

print("All tested Row 9 columns are BLOCKED! Switch might be in State A.")
