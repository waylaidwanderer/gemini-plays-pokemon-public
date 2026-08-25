import mgba
import time
from PIL import Image

def walk_step(direction, expected_coords, retries=15):
    for i in range(retries):
        mgba.press_buttons([direction])
        time.sleep(0.3)
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            print(f"Moved {direction}, current position: {pos}")
            return True
        print(f"Blocked! Retrying {direction} to {expected_coords} (attempt {i+1}/{retries}), current: {pos}")
        time.sleep(0.2)
    return False

# Currently at (12, 11) on 2F East
# 1. Walk to (13, 12) to face UP towards the statue at (13, 11)
success = walk_step("Down", {"x": 12, "y": 12})
if success:
    success = walk_step("Right", {"x": 13, "y": 12})

if success:
    print("Reached (13, 12)! Turning UP towards the statue...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    img_before = mgba.take_screenshot()
    print("Screenshot before A:", img_before)
    
    print("Pressing A (1st time)...")
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    img_after = mgba.take_screenshot()
    print("Screenshot after A:", img_after)
    
    # Check if a text box is active
    img = Image.open(img_after)
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
    print(f"B/W percentage in dialog area after pressing A: {percentage*100:.2f}%")
    
    if percentage > 0.90:
        print("Success! Dialogue box opened successfully!")
        # Press A to select YES
        print("Pressing A (2nd time) to select YES...")
        mgba.press_buttons(["A"])
        time.sleep(1.5)
        
        # Press A to dismiss
        print("Pressing A (3rd time) to dismiss dialogue...")
        mgba.press_buttons(["A"])
        time.sleep(1.5)
        print("Successfully toggled! Final position:", mgba.get_coordinates())
    else:
        print("Failed! Dialogue box did not open.")
else:
    print("Failed to reach (13, 12).")
