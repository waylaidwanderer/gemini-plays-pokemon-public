import mgba
import time
from PIL import Image

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

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

def safe_step(direction, expected_coords=None):
    old_pos = get_pos()
    mgba.press_buttons([direction])
    time.sleep(0.45)
    new_pos = get_pos()
    
    if new_pos != old_pos:
        if expected_coords and new_pos != expected_coords:
            print(f"Moved {direction} but landed at unexpected position: {new_pos} (expected {expected_coords})")
        else:
            print(f"Successfully stepped {direction} to {new_pos}")
        return True
        
    # If we didn't move, check for battle or dialogue
    if handle_any_menu_or_battle():
        print(f"Handled battle/dialogue. Retrying step {direction}...")
        mgba.press_buttons([direction])
        time.sleep(0.45)
        new_pos = get_pos()
        if new_pos != old_pos:
            print(f"Successfully stepped {direction} to {new_pos} after retry")
            return True
            
    print(f"BLOCKED: Could not step {direction} from {old_pos}")
    return False

def run_safe_steps(steps):
    for d, c in steps:
        if not safe_step(d, c):
            return False
    return True

print("Start position:", get_pos())

# Walk from (7, 11) to (2, 12)
steps_to_2_12 = [
    ("Left", (6, 11)),
    ("Left", (5, 11)),
    ("Left", (4, 11)),
    ("Left", (3, 11)),
    ("Down", (3, 12)),
    ("Left", (2, 12)),
]
print("Walking to (2, 12)...")
if not run_safe_steps(steps_to_2_12):
    print("Failed to reach (2, 12)")
    exit(1)

# Turn UP and press A to see if there is a switch!
print("Turning UP...")
mgba.press_buttons(["Up"])
time.sleep(0.5)

print("Interacting with Mewtwo statue...")
mgba.press_buttons(["A"])
time.sleep(1.0)
mgba.take_screenshot()

print("Verification complete!")
