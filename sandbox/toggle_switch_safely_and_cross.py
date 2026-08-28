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
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        
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
            mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
            time.sleep(1.5)
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
        print(f"Successfully stepped {direction} to {new_pos}")
        return True
        
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

def toggle_switch_once():
    print("Toggling Mewtwo switch...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    for i in range(4):
        mgba.press_buttons(["A"])
        time.sleep(1.0)
    print("Switch toggle complete!")

def test_column_1_crossing():
    print("Testing walking UP Column 1...")
    # Walk UP Column 1 to Row 6
    if not safe_step("Up", (1, 11)): return False
    if not safe_step("Up", (1, 10)): return False
    if not safe_step("Up", (1, 9)): return False # The gate!
    if not safe_step("Up", (1, 8)): return False
    if not safe_step("Up", (1, 7)): return False
    if not safe_step("Up", (1, 6)): return False
    return True

# Start from (1, 10)
print("Start position:", get_pos())

# Walk to (2, 12)
steps_to_switch = [
    ("Down", (1, 11)),
    ("Down", (1, 12)),
    ("Right", (2, 12)),
]
if not run_safe_steps(steps_to_switch):
    print("Failed to reach switch")
    exit(1)

# FIRST TOGGLE TRY
toggle_switch_once()

# Walk to (1, 12)
if not safe_step("Left", (1, 12)):
    print("Failed to step Left to (1, 12)")
    exit(1)

# Test crossing
if test_column_1_crossing():
    print("SUCCESS: Crossed on the first toggle try!")
else:
    print("FAILED on first toggle. Trying second toggle...")
    # We are currently at (1, 10) or (1, 11) or (1, 12)
    # Let's walk back to (2, 12) safely
    pos = get_pos()
    if pos[1] == 10:
        safe_step("Down")
        safe_step("Down")
        safe_step("Right")
    elif pos[1] == 11:
        safe_step("Down")
        safe_step("Right")
    elif pos[1] == 12:
        safe_step("Right")
        
    # SECOND TOGGLE TRY
    toggle_switch_once()
    
    # Walk to (1, 12)
    if not safe_step("Left", (1, 12)):
        print("Failed to step Left to (1, 12) on 2nd try")
        exit(1)
        
    # Test crossing again
    if test_column_1_crossing():
        print("SUCCESS: Crossed on the second toggle try!")
    else:
        print("CRITICAL FAILURE: Column 1 is still blocked after both toggles!")
        exit(1)

# Now walk RIGHT along Row 6 to Column 20
steps_row_6 = []
for x in range(2, 21):
    steps_row_6.append(("Right", (x, 6)))
print("Walking RIGHT along Row 6 to Column 20...")
if not run_safe_steps(steps_row_6):
    print("Failed walking RIGHT along Row 6")
    exit(1)

print("MASTER CROSSING COMPLETE!")
mgba.take_screenshot()
