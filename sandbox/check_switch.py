import mgba
import time
from PIL import Image

if __name__ == "__main__":
    # We are at (2, 6). Face UP
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # Press A
    print("Pressing A facing UP towards (2, 5)...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Take screenshot
    img_path = mgba.take_screenshot()
    print(f"Screenshot taken: {img_path}")
    
    # Let's crop the text box at the bottom (y from 112 to 144, x from 0 to 160)
    img = Image.open(img_path)
    # The Game Boy resolution is 160x144. Let's find the dimensions of the screenshot.
    width, height = img.size
    print(f"Screenshot size: {width}x{height}")
    # The bottom text box is roughly y from 112/144 * height to height
    crop_box = (0, int(112/144 * height), width, height)
    cropped_text = img.crop(crop_box)
    cropped_text.save("screenshots/cropped_text_check.png")
    print("Cropped text check saved.")
    
    # Dismiss any dialogue
    mgba.press_buttons(["B"])
    time.sleep(0.5)
