import mgba
import time
from PIL import Image

def handle_any_menu_or_battle():
    # Take a screenshot
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file)
    img_std = img.resize((160, 144), Image.Resampling.NEAREST)
    
    # Check if a text box is active
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
        print(f"Menu/Battle detected! (B/W percentage: {percentage*100:.2f}%)")
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        return True
    return False

def walk_step(direction, expected_coords, retries=15):
    for i in range(retries):
        if handle_any_menu_or_battle():
            pos = mgba.get_coordinates()
            if pos == expected_coords:
                return True
        mgba.press_buttons([direction])
        time.sleep(0.4)
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            print(f"Moved {direction}, current position: {pos}")
            return True
        print(f"Blocked or battle! Retrying {direction} (attempt {i+1}/{retries}), current: {pos}")
        time.sleep(0.3)
    return False

# Starting at (4, 13) on 3F West
success = True

steps = [
    ("Left", {"x": 3, "y": 13}),
    ("Left", {"x": 2, "y": 13}),
    ("Up", {"x": 2, "y": 12}),
]

for d, c in steps:
    if not walk_step(d, c):
        success = False
        break

if success:
    print("Reached (2, 12). Facing UP to toggle switch...")
    mgba.press_buttons(["Up", "sleep 200"])
    # Press A to start switch dialogue
    mgba.press_buttons(["A", "sleep 600"])
    # Press A to select YES
    mgba.press_buttons(["A", "sleep 600"])
    # Press A to dismiss "Who wouldn't?" or "Pressed it!" text
    mgba.press_buttons(["A", "sleep 600"])
    
    print("Toggled switch to State B! Initiating DIG escape...")
    # Open start menu, go to PKMN, select TRUFFLE (Paras), select DIG
    mgba.press_buttons(["Start", "sleep 400", "Down", "sleep 200", "A", "sleep 500"])
    # Go down to 6th slot (TRUFFLE)
    for _ in range(5):
        mgba.press_buttons(["Down", "sleep 150"])
    # Select TRUFFLE
    mgba.press_buttons(["A", "sleep 400"])
    # Select DIG (Option 1)
    mgba.press_buttons(["A", "sleep 3000"]) # wait for DIG warp
    
    print("Escape completed! Final position:", mgba.get_coordinates())
else:
    print("Failed to reach (2, 12)")
