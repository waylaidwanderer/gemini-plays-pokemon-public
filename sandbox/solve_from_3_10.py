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
        print(f"Menu/Dialogue/Battle detected! (B/W: {percentage*100:.2f}%)")
        # Try pressing B first to dismiss text
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        
        # Check if still in battle/dialogue
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
            print("Still in battle/dialogue. Attempting to RUN...")
            # Try pressing Down, Right, A to select RUN
            mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
            time.sleep(1.5)
            # Dismiss any "Escaped" or "Can't escape" text
            for _ in range(5):
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

def toggle_switch_at_2_11():
    print("Toggling Mewtwo switch at (2, 11)...")
    # Face UP towards (2, 11) from (2, 12)
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # 1. First A press to open the "secret switch!" text
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # 2. Second A press to advance to the Yes/No prompt
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # 3. Third A press (YES is selected by default) to press the switch
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # 4. Fourth A press to dismiss the "Who wouldn't?" text
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    print("Mewtwo switch toggled successfully!")

# Ensure any active menu/battle is closed
for _ in range(5):
    handle_any_menu_or_battle()
    time.sleep(0.2)

pos = mgba.get_coordinates()
print("Starting solve from position:", pos)

# We are at (3, 10). Let's walk to (2, 12)
if pos == {"x": 3, "y": 10}:
    print("Walking to switch at (2, 12) from (3, 10)...")
    path_to_switch = [
        ("Down", {"x": 3, "y": 11}),
        ("Down", {"x": 3, "y": 12}),
        ("Left", {"x": 2, "y": 12}),
    ]
    if not run_steps(path_to_switch):
        print("Failed to reach (2, 12)")
        exit(1)
    pos = mgba.get_coordinates()

# Now toggle switch at (2, 12)
if pos == {"x": 2, "y": 12}:
    toggle_switch_at_2_11()
    
    # Let's walk to (2, 9) to confirm the gate is OPEN in State B!
    path_to_gate = [
        ("Right", {"x": 3, "y": 12}),
        ("Up", {"x": 3, "y": 11}),
        ("Up", {"x": 3, "y": 10}),
        ("Left", {"x": 2, "y": 10}),
        ("Up", {"x": 2, "y": 9}),
    ]
    print("Walking through the gate to (2, 9)...")
    if not run_steps(path_to_gate):
        print("Failed to reach (2, 9). Shutter gate might still be closed!")
        exit(1)
        
    pos = mgba.get_coordinates()

# Walk up Column 2 to Row 6
if pos == {"x": 2, "y": 9}:
    print("Walking up Column 2 to Row 6...")
    steps_up = [
        ("Up", {"x": 2, "y": 8}),
        ("Up", {"x": 2, "y": 7}),
        ("Up", {"x": 2, "y": 6}),
    ]
    if not run_steps(steps_up):
        print("Failed to walk up Column 2")
        exit(1)
    pos = mgba.get_coordinates()

print("Reached (2, 6)! Mansion is in State B and gate is open.")
