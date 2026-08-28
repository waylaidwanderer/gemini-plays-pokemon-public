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

# Ensure any menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

path = ["Up", "Right", "Up", "Up", "Up", "Up", "Up"]
current_pos = mgba.get_coordinates()
print(f"Starting path execution from: {current_pos}")

success = True
for i, d in enumerate(path):
    print(f"Step {i+1}: Pressing {d}...")
    mgba.press_buttons([d])
    time.sleep(0.4)
    handle_any_menu_or_battle()
    
    pos = mgba.get_coordinates()
    print(f"Position now: {pos}")
    
    # If we got into a battle, we might still be on the same tile after escaping, so we re-try the step if needed.
    # But let's check if the position changed.
    if pos == current_pos:
        print("Position did not change! Re-trying step...")
        mgba.press_buttons([d])
        time.sleep(0.4)
        handle_any_menu_or_battle()
        pos = mgba.get_coordinates()
        print(f"Position after re-try: {pos}")
        if pos == current_pos:
            print("Step failed permanently. Path blocked.")
            success = False
            break
    current_pos = pos

if success:
    print("Reached the stairs area at:", current_pos)
    print("Stepping UP to warp to 1F...")
    mgba.press_buttons(["Up"])
    time.sleep(2.5)
    print("Final position after warping:", mgba.get_coordinates())
else:
    print("Path execution failed. Current position:", current_pos)
