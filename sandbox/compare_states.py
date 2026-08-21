from PIL import Image
import os

def crop_and_compare():
    # Let's crop the gate areas on the two screenshots
    # 1. screenshots/screenshot_1787302854168.png (before toggle)
    # 2. screenshots/screenshot_1787303029159.png (after toggle)
    
    img1_path = "screenshots/screenshot_1787302854168.png"
    img2_path = "screenshots/screenshot_1787303029159.png"
    
    if not os.path.exists(img1_path) or not os.path.exists(img2_path):
        print("Screenshots not found!")
        return
        
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)
    
    # Let's crop the region around col 9 row 4-5
    # The clean screen is 240x160. Let's find out the pixel coordinates.
    # The grid tiles are 16x16 (no, the Game Boy screen is 160x144 pixels, wait, standard Game Boy resolution is 160x144).
    # Wait, the screenshots taken by mgba are usually 160x144 or 240x160 depending on scaling/borders.
    # Let's print the size of the images first.
    print(f"Image 1 size: {img1.size}")
    print(f"Image 2 size: {img2.size}")
    
    # Let's save a crop of col 9 row 4-5 and col 6 row 6-7 from both
    # to see if the gate at (9, 4)/(9, 5) changed, or if (6, 6)/(6, 7) changed.
    # Let's crop the entire left half of the screen (columns 3-9) for both.
    width, height = img1.size
    
    # Save the cropped images directly to sandbox/screenshots/cropped/
    os.makedirs("screenshots/cropped", exist_ok=True)
    
    crop1 = img1.crop((0, 0, width, height))
    crop2 = img2.crop((0, 0, width, height))
    
    # Let's do a pixel diff to see if they are identical or different!
    diff = 0
    for x in range(width):
        for y in range(height):
            p1 = img1.getpixel((x, y))
            p2 = img2.getpixel((x, y))
            if p1 != p2:
                diff += 1
                
    print(f"Number of differing pixels: {diff}")
    if diff == 0:
        print("The screenshots are IDENTICAL! The switch did NOT toggle, or did not change anything on screen.")
    else:
        print("The screenshots are DIFFERENT! Something changed.")

crop_and_compare()
