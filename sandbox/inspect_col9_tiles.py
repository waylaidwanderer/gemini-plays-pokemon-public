from PIL import Image
import os

def crop_col9_tiles():
    img_B = Image.open("screenshots/screenshot_1787302854168.png") # State B
    img_A = Image.open("screenshots/screenshot_1787303029159.png") # State A
    
    # We want to crop tile (9, 4) and (9, 6).
    # Player is at (10, 5) in both screenshots.
    # screen_col = 4 + (9 - 10) = 3
    # For (9, 4): screen_row = 4 + (4 - 5) = 3
    # For (9, 6): screen_row = 4 + (6 - 5) = 5
    
    x1 = 3 * 48
    x2 = x1 + 48
    
    os.makedirs("screenshots/cropped", exist_ok=True)
    
    # Crop Row 4
    y1_r4 = 3 * 48
    y2_r4 = y1_r4 + 48
    crop_r4_B = img_B.crop((x1, y1_r4, x2, y2_r4))
    crop_r4_A = img_A.crop((x1, y1_r4, x2, y2_r4))
    crop_r4_B.save("screenshots/cropped/col9_r4_stateB.png")
    crop_r4_A.save("screenshots/cropped/col9_r4_stateA.png")
    
    # Crop Row 6
    y1_r6 = 5 * 48
    y2_r6 = y1_r6 + 48
    crop_r6_B = img_B.crop((x1, y1_r6, x2, y2_r6))
    crop_r6_A = img_A.crop((x1, y1_r6, x2, y2_r6))
    crop_r6_B.save("screenshots/cropped/col9_r6_stateB.png")
    crop_r6_A.save("screenshots/cropped/col9_r6_stateA.png")
    
    print("Cropped and saved all Col 9 tiles!")

crop_col9_tiles()
