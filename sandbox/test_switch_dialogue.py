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
        return True
    return False

# 1. Dismiss "Got away safely!" text first
print("Dismissing 'Got away safely!' text...")
mgba.press_buttons(["B"])
time.sleep(1.0)

pos = mgba.get_coordinates()
print(f"Position in overworld: {pos}")

# If we are at (1, 12), let's test interacting in all 4 directions!
directions = ["Up", "Down", "Left", "Right"]

for d in directions:
    print(f"Facing {d} and pressing A...")
    mgba.press_buttons([d, "sleep 300", "A"])
    time.sleep(1.0)
    
    # Check if dialogue is open
    scr = mgba.take_screenshot()
    img = Image.open(scr).resize((160, 144), Image.Resampling.NEAREST)
    cropped_dialogue = img.crop((0, 104, 160, 144))
    
    black_pixels = 0
    for y in range(cropped_dialogue.height):
        for x in range(cropped_dialogue.width):
            r, g, b = cropped_dialogue.getpixel((x, y))
            if r < 50 and g < 50 and b < 50:
                black_pixels += 1
    print(f"-> Black pixels for direction {d}: {black_pixels}")
    
    if black_pixels > 200:
        print(f"SUCCESS! Dialogue opened when facing {d}!")
        # Let's toggle the switch to State B!
        mgba.press_buttons(["A", "sleep 1500", "A", "sleep 1500", "A"])
        time.sleep(4.0)
        print("Switch successfully toggled to State B!")
        break
    else:
        # Just in case we didn't open anything, press B to clear any unintended selection
        mgba.press_buttons(["B"])
        time.sleep(0.5)
