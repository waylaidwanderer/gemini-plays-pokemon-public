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

# Dismiss any active menus first
mgba.press_buttons(["B"])
time.sleep(0.4)

pos = mgba.get_coordinates()
print("Starting position:", pos)

# Walk down Column 1 to Row 13
if pos["x"] == 1 and pos["y"] < 13:
    print("Walking down to (1, 13)...")
    for y in range(pos["y"] + 1, 14):
        mgba.press_buttons(["Down"])
        time.sleep(0.45)
    pos = mgba.get_coordinates()

if pos == {"x": 1, "y": 13}:
    print("Facing UP towards the switch at (1, 12)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    # Exactly 3 A presses!
    print("Press 1: Opening switch dialogue...")
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    
    print("Press 2: Selecting YES...")
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    
    print("Press 3: Dismissing 'Pressed it!'...")
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    
    print("Switch successfully toggled!")
else:
    print("Failed to stand at (1, 13)")
