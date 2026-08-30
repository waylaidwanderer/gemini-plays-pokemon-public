from PIL import Image

def analyze():
    # Load current screen to calibrate the player's red cap RGB color
    # The current screen on disk is 'state_current.png' or we can take a screenshot
    img_curr = Image.open("state_current.png")
    # Resize to 160x144 to get the original Game Boy pixels
    img_curr_160 = img_curr.resize((160, 144), Image.Resampling.NEAREST)
    
    # Let's inspect the colors in the middle of the screen (columns 75-85, rows 68-76)
    print("Calibrating player red cap color...")
    red_colors = []
    for y in range(60, 80):
        for x in range(70, 90):
            r, g, b = img_curr_160.getpixel((x, y))[:3]
            # Print reddish colors
            if r > 150 and g < 120 and b < 120:
                print(f"Found reddish pixel at ({x}, {y}): RGB=({r}, {g}, {b})")
                red_colors.append((r, g, b))
                
    if not red_colors:
        print("No reddish pixels found on current screen center. Printing center pixel colors:")
        for y in range(70, 74):
            for x in range(78, 82):
                print(f"Pixel at ({x}, {y}): RGB={img_curr_160.getpixel((x, y))[:3]}")
                
    # Now let's inspect the target screenshot at Turn 68272
    target_path = "screenshots/screenshot_1788093216840.png"
    print(f"\nAnalyzing {target_path}...")
    try:
        img_tgt = Image.open(target_path)
        img_tgt_160 = img_tgt.resize((160, 144), Image.Resampling.NEAREST)
        
        # Let's print out all reddish pixels on the target image to find where the player was!
        found = False
        for y in range(144):
            for x in range(160):
                r, g, b = img_tgt_160.getpixel((x, y))[:3]
                # Match reddish cap
                if r > 150 and g < 120 and b < 120:
                    print(f"Target reddish pixel at ({x}, {y}): RGB=({r}, {g}, {b})")
                    found = True
        if not found:
            print("No matching reddish pixels in target screenshot.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    analyze()
