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

# Ensure any menus/dialogues are closed
mgba.press_buttons(["B"])
time.sleep(0.4)

pos = mgba.get_coordinates()
print("Current position:", pos)

# 1. Walk back to (2, 12)
if pos == {"x": 1, "y": 10}:
    print("Walking to (2, 12)...")
    run_steps([
        ("Down", {"x": 1, "y": 11}),
        ("Down", {"x": 1, "y": 12}),
        ("Right", {"x": 2, "y": 12}),
    ])
    pos = mgba.get_coordinates()

# 2. Toggle switch to State B!
if pos == {"x": 2, "y": 12}:
    print("Toggling switch to State B...")
    mgba.press_buttons(["Up", "sleep 400", "A", "sleep 1000", "A", "sleep 1000", "A", "sleep 1000", "A"])
    time.sleep(4.0)
    pos = mgba.get_coordinates()

# 3. Test Column 3 Row 9
print("Testing Column 3 Row 9 in State B...")
if walk_step("Right", {"x": 3, "y": 12}):
    if walk_step("Up", {"x": 3, "y": 11}):
        if walk_step("Up", {"x": 3, "y": 10}):
            success = walk_step("Up", {"x": 3, "y": 9}, retries=2)
            if success:
                print("Column 3 Row 9 is OPEN in State B!")
                # Walk UP to Row 6 and complete route!
                run_steps([
                    ("Up", {"x": 3, "y": 8}),
                    ("Up", {"x": 3, "y": 7}),
                    ("Up", {"x": 3, "y": 6}),
                ])
                # Walk RIGHT to Column 26
                steps_east = []
                for x in range(4, 27):
                    steps_east.append(("Right", {"x": x, "y": 6}))
                run_steps(steps_east)
                exit(0)
            else:
                print("Column 3 Row 9 is CLOSED.")
                walk_step("Down", {"x": 3, "y": 11})
                walk_step("Down", {"x": 3, "y": 12})
                pos = mgba.get_coordinates()

# 4. Test Column 4 Row 9
if pos == {"x": 3, "y": 12}:
    print("Testing Column 4 Row 9 in State B...")
    if walk_step("Right", {"x": 4, "y": 12}):
        if walk_step("Up", {"x": 4, "y": 11}):
            if walk_step("Up", {"x": 4, "y": 10}):
                success = walk_step("Up", {"x": 4, "y": 9}, retries=2)
                if success:
                    print("Column 4 Row 9 is OPEN in State B!")
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
                    print("Column 4 Row 9 is CLOSED.")
                    walk_step("Down", {"x": 4, "y": 11})
                    walk_step("Down", {"x": 4, "y": 12})
                    pos = mgba.get_coordinates()

# 5. Test Column 5 Row 9
if pos == {"x": 4, "y": 12}:
    print("Testing Column 5 Row 9 in State B...")
    if walk_step("Right", {"x": 5, "y": 12}):
        if walk_step("Up", {"x": 5, "y": 11}):
            # Note: (5, 10) is the stairs down. Walking onto (5, 10) will warp us!
            # Wait, can we walk UP Column 5 without warping?
            # Let's check: (5, 10) warps us to 2F West. So we cannot use Column 5!
            print("Column 5 is blocked by stairs down at (5, 10).")
            walk_step("Down", {"x": 5, "y": 12})
            pos = mgba.get_coordinates()

# 6. Test Column 6 Row 9
if pos == {"x": 5, "y": 12}:
    print("Testing Column 6 Row 9 in State B...")
    if walk_step("Right", {"x": 6, "y": 12}):
        if walk_step("Up", {"x": 6, "y": 11}):
            # Is (6, 10) open?
            if walk_step("Up", {"x": 6, "y": 10}):
                success = walk_step("Up", {"x": 6, "y": 9}, retries=2)
                if success:
                    print("Column 6 Row 9 is OPEN in State B!")
                    run_steps([
                        ("Up", {"x": 6, "y": 8}),
                        ("Up", {"x": 6, "y": 7}),
                        ("Up", {"x": 6, "y": 6}),
                    ])
                    steps_east = []
                    for x in range(7, 27):
                        steps_east.append(("Right", {"x": x, "y": 6}))
                    run_steps(steps_east)
                    exit(0)
                else:
                    print("Column 6 Row 9 is CLOSED.")
                    walk_step("Down", {"x": 6, "y": 11})
                    walk_step("Down", {"x": 6, "y": 12})
                    pos = mgba.get_coordinates()

# 7. Test Column 7 Row 9
if pos == {"x": 6, "y": 12}:
    print("Testing Column 7 Row 9 in State B...")
    if walk_step("Right", {"x": 7, "y": 12}):
        if walk_step("Up", {"x": 7, "y": 11}):
            # (7, 10) is stairs, so we can't use Column 7 either!
            print("Column 7 is blocked by stairs at (7, 10).")
            walk_step("Down", {"x": 7, "y": 12})
            pos = mgba.get_coordinates()

print("All tested columns on Row 9 are blocked!")
