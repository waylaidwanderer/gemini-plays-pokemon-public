import mgba
import time
from PIL import Image

def test_interaction(buttons, label):
    print(f"Testing: {label} with buttons {buttons}")
    mgba.press_buttons(buttons)
    time.sleep(0.5)
    img_path = mgba.take_screenshot()
    pos = mgba.get_coordinates()
    print(f"Result position: {pos}")
    # We can inspect the screenshot using PIL to see if a textbox is open (usually white space at the bottom)
    img = Image.open(img_path)
    # Check if pixels in the bottom text area (approx y=112 to 143) are mostly white
    # Standard GBA screen is 240x160. Wait, standard GB/GBC screen in mGBA is 160x144.
    # Let's check the image size:
    width, height = img.size
    print(f"Image size: {width}x{height}")
    # Let's count white pixels at the bottom
    white_pixels = 0
    total_pixels = 0
    for y in range(int(height * 0.8), height - 2):
        for x in range(2, width - 2):
            r, g, b = img.getpixel((x, y))[:3]
            if r > 240 and g > 240 and b > 240:
                white_pixels += 1
            total_pixels += 1
    pct = white_pixels / total_pixels if total_pixels > 0 else 0
    print(f"Bottom white pixel percentage: {pct:.2%}")
    if pct > 0.5:
        print(">>> TEXTBOX DETECTED! <<<")
        return True, img_path
    return False, img_path

# Let's first make sure we are at (2, 5).
# If we are at (2, 5) facing Up, let's try A.
found, path = test_interaction(["A"], "At (2, 5) facing Up, press A")
if not found:
    # Try facing Left
    found, path = test_interaction(["Left", "A"], "At (2, 5) facing Left, press A")
if not found:
    # Try standing at (3, 5) facing Left
    found, path = test_interaction(["Right", "Left", "A"], "At (3, 5) facing Left, press A")
if not found:
    # Try standing at (2, 6) facing Up
    found, path = test_interaction(["Down", "Up", "A"], "At (2, 6) facing Up, press A")
