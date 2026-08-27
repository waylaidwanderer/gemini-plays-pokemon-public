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

# We are at (7, 11) on 2F West.
# Let's walk to 2F East stairs at (15, 11).
# We must walk: (7, 11) -> (5, 11) -> (5, 8) -> (10, 8) -> (15, 8) -> (15, 11).
if pos == {"x": 7, "y": 11}:
    print("Walking to 2F East stairs via Row 8...")
    if not run_steps([
        ("Left", {"x": 6, "y": 11}),
        ("Left", {"x": 5, "y": 11}),
        ("Up", {"x": 5, "y": 10}),
        ("Up", {"x": 5, "y": 9}),
        ("Up", {"x": 5, "y": 8}),
        ("Right", {"x": 6, "y": 8}),
        ("Right", {"x": 7, "y": 8}),
        ("Right", {"x": 8, "y": 8}),
        ("Right", {"x": 9, "y": 8}),
        ("Right", {"x": 10, "y": 8}), # Column 10 open!
        ("Right", {"x": 11, "y": 8}),
        ("Right", {"x": 12, "y": 8}),
        ("Right", {"x": 13, "y": 8}),
        ("Right", {"x": 14, "y": 8}),
        ("Right", {"x": 15, "y": 8}),
        ("Down", {"x": 15, "y": 9}),
        ("Down", {"x": 15, "y": 10}),
        ("Down", {"x": 15, "y": 11}), # Stairs!
    ]):
        print("Failed to reach 2F East stairs")
        exit(1)
    pos = mgba.get_coordinates()

# 2. Climb stairs to 3F East
if pos == {"x": 15, "y": 11}:
    print("Stepping UP to climb to 3F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position on 3F East:", pos)

# 3. Walk LEFT along Row 6 to 3F West
# We land at (16, 11) on 3F East.
# Let's walk to Row 6: (16, 11) -> (16, 10) -> (16, 9) -> (16, 8) -> (16, 7) -> (16, 6) -> (15, 6) -> (10, 6) -> (5, 6) -> (5, 11).
if pos == {"x": 16, "y": 11}:
    print("Walking to 3F East Row 6...")
    if not run_steps([
        ("Up", {"x": 16, "y": 10}),
        ("Up", {"x": 16, "y": 9}),
        ("Up", {"x": 16, "y": 8}),
        ("Up", {"x": 16, "y": 7}),
        ("Up", {"x": 16, "y": 6}),
    ]):
        print("Failed to reach Row 6 on 3F East")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 16, "y": 6}:
    print("Crossing horizontally to 3F West on Row 6...")
    steps_west = []
    for x in range(15, 0, -1):
        steps_west.append(("Left", {"x": x, "y": 6}))
    if not run_steps(steps_west):
        print("Failed to reach Column 1 on Row 6")
        exit(1)
    pos = mgba.get_coordinates()

# 4. We are at (1, 6) on 3F West!
# Let's walk DOWN Column 1 to Row 12: (1, 6) -> (1, 12).
if pos == {"x": 1, "y": 6}:
    print("Walking DOWN Column 1 to Row 12...")
    if not run_steps([
        ("Down", {"x": 1, "y": 7}),
        ("Down", {"x": 1, "y": 8}),
        ("Down", {"x": 1, "y": 9}), # Row 9 gate is OPEN? No, we are on 3F West, is the gate open in State A?
        # Wait, in State A, the Row 9 gate is CLOSED.
        # But wait! If we are on Row 6 of 3F West, can we walk Down Column 5?
        # Column 5 is completely open!
        # Let's see: if Column 1 Row 9 is closed, we can instead walk Column 5 down to Row 13!
        # Let's check where the player is.
    ]):
        print("Column 1 Row 9 is closed (as expected in State A). Bypassing via Column 5...")
        # Walk back up to Row 6
        mgba.get_coordinates()
        # Instead, let's walk via Column 5!
        # From (1, 6), walk to (5, 6)
        if run_steps([
            ("Right", {"x": 2, "y": 6}),
            ("Right", {"x": 3, "y": 6}),
            ("Right", {"x": 4, "y": 6}),
            ("Right", {"x": 5, "y": 6}),
        ]):
            # Walk down Column 5 to Row 13
            if run_steps([
                ("Down", {"x": 5, "y": 7}),
                ("Down", {"x": 5, "y": 8}),
                ("Down", {"x": 5, "y": 9}),
                ("Down", {"x": 5, "y": 10}),
                ("Down", {"x": 5, "y": 11}),
                ("Down", {"x": 5, "y": 12}),
                ("Down", {"x": 5, "y": 13}),
            ]):
                # Walk Left along Row 13 to Column 2
                if run_steps([
                    ("Left", {"x": 4, "y": 13}),
                    ("Left", {"x": 3, "y": 13}),
                    ("Left", {"x": 2, "y": 13}),
                ]):
                    # Walk UP to (2, 12) (which is open in State A!)
                    if run_steps([("Up", {"x": 2, "y": 12})]):
                        print("Arrived at 3F West standing tile (2, 12) in State A!")
                        
    pos = mgba.get_coordinates()

# 5. Stand at (2, 12) facing UP and toggle Mewtwo switch at (2, 11) to State B!
if pos == {"x": 2, "y": 12}:
    print("Facing UP towards 3F West Mewtwo switch...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    print("Pressing A to open switch dialogue...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # We don't use flawed pixel check anymore! We just select YES and toggle.
    print("Toggling switch to State B...")
    mgba.press_buttons(["A", "sleep 1500", "A", "sleep 1200", "A"])
    time.sleep(4.5)
    print("Switch successfully toggled to State B!")
    
    # Now we walk: (2, 12) -> (2, 13) -> (1, 13) -> walk UP Column 1 (Row 9 gate is now OPEN!)
    pos = mgba.get_coordinates()

print("Current position:", pos)
