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

# Ensure any active menus are dismissed
mgba.press_buttons(["B"])
time.sleep(0.4)

# 1. Open Start menu
print("Opening Start menu...")
mgba.press_buttons(["Start"])
time.sleep(0.5)

# 2. Select ITEM
print("Selecting ITEM...")
mgba.press_buttons(["Down", "sleep 150", "A"])
time.sleep(0.5)

# 3. Take screenshot of first page of bag
scr1 = mgba.take_screenshot()
print("Page 1 screenshot saved to:", scr1)
# Crop and save to sandbox/screenshots/bag_page1.png
img1 = Image.open(scr1)
img1.save("bag_page1.png")

# Scroll down to see next page
print("Scrolling down...")
mgba.press_buttons(["Down", "sleep 150", "Down", "sleep 150", "Down", "sleep 150", "Down", "sleep 150"])
time.sleep(0.5)

scr2 = mgba.take_screenshot()
print("Page 2 screenshot saved to:", scr2)
img2 = Image.open(scr2)
img2.save("bag_page2.png")

# Close Start menu
mgba.press_buttons(["B", "sleep 200", "B"])
time.sleep(0.4)

