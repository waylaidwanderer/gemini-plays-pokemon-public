import mgba
import time
from PIL import Image

def is_in_battle_or_menu():
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
    return percentage > 0.85

def escape_battle_safely():
    if not is_in_battle_or_menu():
        return False
        
    print("Battle or menu detected! Attempting escape...")
    mgba.press_buttons(["B"])
    time.sleep(0.4)
    
    if is_in_battle_or_menu():
        print("Still in battle menu. Pressing RUN...")
        mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
        time.sleep(1.5)
        for _ in range(5):
            mgba.press_buttons(["B"])
            time.sleep(0.2)
    return True

def walk_step(direction, expected_coords, retries=15):
    for i in range(retries):
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            return True
            
        if escape_battle_safely():
            time.sleep(0.5)
            pos = mgba.get_coordinates()
            if pos == expected_coords:
                return True
                
        mgba.press_buttons([direction])
        time.sleep(0.5)
        
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            print(f"Moved {direction} to {pos}")
            return True
            
        print(f"Move {direction} failed. Current: {pos}, Expected: {expected_coords}. Retrying...")
        time.sleep(0.3)
    return False

def run_steps(steps):
    for d, c in steps:
        if not walk_step(d, c):
            return False
    return True

# Current position
pos = mgba.get_coordinates()
print("Starting from:", pos)

if pos == {"x": 14, "y": 3}:
    print("Navigating from (14, 3) to Row 6 on 2F West...")
    steps = [
        ("Down", {"x": 14, "y": 4}),
        ("Down", {"x": 14, "y": 5}),
        ("Down", {"x": 14, "y": 6}),
    ]
    if not run_steps(steps):
        print("Failed to reach (14, 6)")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 14, "y": 6}:
    print("Crossing horizontally on Row 6 to Column 18...")
    steps = [
        ("Right", {"x": 15, "y": 6}),
        ("Right", {"x": 16, "y": 6}),
        ("Right", {"x": 17, "y": 6}),
        ("Right", {"x": 18, "y": 6}),
    ]
    if not run_steps(steps):
        print("Failed to reach (18, 6)")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 18, "y": 6}:
    print("Walking down to Row 10 on 2F East...")
    steps = [
        ("Down", {"x": 18, "y": 7}),
        ("Down", {"x": 18, "y": 8}),
        ("Down", {"x": 18, "y": 9}),
        ("Down", {"x": 18, "y": 10}),
    ]
    if not run_steps(steps):
        print("Failed to reach (18, 10)")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 18, "y": 10}:
    print("Walking left to Column 15...")
    steps = [
        ("Left", {"x": 17, "y": 10}),
        ("Left", {"x": 16, "y": 10}),
        ("Left", {"x": 15, "y": 10}),
    ]
    if not run_steps(steps):
        print("Failed to reach (15, 10)")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 15, "y": 10}:
    print("Stepping DOWN to warp up to 3F East...")
    mgba.press_buttons(["Down"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after warp to 3F East:", pos)

if pos == {"x": 16, "y": 11}:
    print("Navigating Row 11 on 3F East to Column 20...")
    steps = [
        ("Right", {"x": 17, "y": 11}),
        ("Right", {"x": 18, "y": 11}),
        ("Right", {"x": 19, "y": 11}),
        ("Right", {"x": 20, "y": 11}),
    ]
    if not run_steps(steps):
        print("Failed to reach (20, 11) on 3F East")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 20, "y": 11}:
    print("Walking UP Column 20 to Row 3...")
    steps = [
        ("Up", {"x": 20, "y": 10}),
        ("Up", {"x": 20, "y": 9}),
        ("Up", {"x": 20, "y": 8}),
        ("Up", {"x": 20, "y": 7}),
        ("Up", {"x": 20, "y": 6}),
        ("Up", {"x": 20, "y": 5}),
        ("Up", {"x": 20, "y": 4}),
        ("Up", {"x": 20, "y": 3}),
    ]
    if not run_steps(steps):
        print("Failed to reach (20, 3) on 3F East")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 20, "y": 3}:
    print("Walking RIGHT Row 3 to Column 26...")
    steps = [
        ("Right", {"x": 21, "y": 3}),
        ("Right", {"x": 22, "y": 3}),
        ("Right", {"x": 23, "y": 3}),
        ("Right", {"x": 24, "y": 3}),
        ("Right", {"x": 25, "y": 3}),
        ("Right", {"x": 26, "y": 3}),
    ]
    if not run_steps(steps):
        print("Failed to reach (26, 3) on 3F East")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 26, "y": 3}:
    print("Stepping DOWN to drop through pitfall to 1F East fenced room...")
    mgba.press_buttons(["Down"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after dropping to 1F East:", pos)

if pos == {"x": 26, "y": 4}:
    print("Walking LEFT Row 4 to Column 22...")
    steps = [
        ("Left", {"x": 25, "y": 4}),
        ("Left", {"x": 24, "y": 4}),
        ("Left", {"x": 23, "y": 4}),
        ("Left", {"x": 22, "y": 4}),
    ]
    if not run_steps(steps):
        print("Failed to reach (22, 4) on 1F East")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 22, "y": 4}:
    print("Walking UP Column 22 to B1F East stairs warp...")
    steps = [
        ("Up", {"x": 22, "y": 3}),
    ]
    if not run_steps(steps):
        print("Failed to reach (22, 3) on 1F East")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 22, "y": 3}:
    print("Stepping UP to warp down to B1F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after warp down to B1F East:", pos)

if pos == {"x": 22, "y": 2}:
    print("Walking DOWN to Row 5...")
    steps = [
        ("Down", {"x": 22, "y": 3}),
        ("Down", {"x": 22, "y": 4}),
        ("Down", {"x": 22, "y": 5}),
    ]
    if not run_steps(steps):
        print("Failed to reach (22, 5) on B1F East")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 22, "y": 5}:
    print("Walking LEFT along Row 5 across Column 9 gate to B1F West...")
    steps = [
        ("Left", {"x": 21, "y": 5}),
        ("Left", {"x": 20, "y": 5}),
        ("Left", {"x": 19, "y": 5}),
        ("Left", {"x": 18, "y": 5}),
        ("Left", {"x": 17, "y": 5}),
        ("Left", {"x": 16, "y": 5}),
        ("Left", {"x": 15, "y": 5}),
        ("Left", {"x": 14, "y": 5}),
        ("Left", {"x": 13, "y": 5}),
        ("Left", {"x": 12, "y": 5}),
        ("Left", {"x": 11, "y": 5}),
        ("Left", {"x": 10, "y": 5}),
        ("Left", {"x": 9, "y": 5}),  # B1F Column 9 Shutter Gate (open in State B)
        ("Left", {"x": 8, "y": 5}),
        ("Left", {"x": 7, "y": 5}),
        ("Left", {"x": 6, "y": 5}),
        ("Left", {"x": 5, "y": 5}),
        ("Left", {"x": 4, "y": 5}),
        ("Left", {"x": 3, "y": 5}),
        ("Left", {"x": 2, "y": 5}),
        ("Left", {"x": 1, "y": 5}),  # Secret Key room pre-pickup
    ]
    if not run_steps(steps):
        print("Failed to reach (1, 5) on B1F West")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 1, "y": 5}:
    print("Secret Key reached! Facing UP to collect the Secret Key...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    # Interact with Secret Key
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    # Dismiss dialogue "ACE found SECRET KEY!"
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    pos = mgba.get_coordinates()
    print("Current position after collecting key:", pos)

print("Finished script!")
