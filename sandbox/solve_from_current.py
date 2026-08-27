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
        mgba.press_buttons(["Right", "sleep 150", "Down", "sleep 150", "A"])
        time.sleep(1.5)
        for _ in range(8):
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

if pos == {"x": 19, "y": 4}:
    print("Walking LEFT along Row 4 to Column 16...")
    steps = [
        ("Left", {"x": 18, "y": 4}),
        ("Left", {"x": 17, "y": 4}),
        ("Left", {"x": 16, "y": 4}),
    ]
    if not run_steps(steps):
        print("Failed to reach (16, 4)")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 16, "y": 4}:
    print("Walking UP Column 16 to Row 1...")
    steps = [
        ("Up", {"x": 16, "y": 3}),
        ("Up", {"x": 16, "y": 2}),
        ("Up", {"x": 16, "y": 1}),
    ]
    if not run_steps(steps):
        print("Failed to reach (16, 1)")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 16, "y": 1}:
    print("Walking RIGHT along Row 1 to Column 21...")
    steps = [
        ("Right", {"x": 17, "y": 1}),
        ("Right", {"x": 18, "y": 1}),
        ("Right", {"x": 19, "y": 1}),
        ("Right", {"x": 20, "y": 1}),
        ("Right", {"x": 21, "y": 1}),
    ]
    if not run_steps(steps):
        print("Failed to reach (21, 1)")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 21, "y": 1}:
    print("Walking DOWN Column 21 to Row 2...")
    steps = [
        ("Down", {"x": 21, "y": 2}),
    ]
    if not run_steps(steps):
        print("Failed to reach (21, 2)")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 21, "y": 2}:
    print("Stepping RIGHT to B1F East stairs warp...")
    steps = [
        ("Right", {"x": 22, "y": 2}),
    ]
    if not run_steps(steps):
        print("Failed to reach (22, 2) on 1F East")
        exit(1)
    pos = mgba.get_coordinates()

if pos == {"x": 22, "y": 2}:
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
    print("Walking LEFT along Row 5 across Column 9 open gate to B1F West NORTH...")
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
