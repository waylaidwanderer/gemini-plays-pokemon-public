from PIL import Image

def analyze_landing():
    path = "screenshots/screenshot_1788117708230.png"
    print(f"Analyzing {path}...")
    try:
        img = Image.open(path)
        img_160 = img.resize((160, 144), Image.Resampling.NEAREST)
        
        # Let's find the reddish pixel bounding box to see where the player was centered
        red_pixels = []
        for y in range(144):
            for x in range(160):
                r, g, b = img_160.getpixel((x, y))[:3]
                if r > 150 and g < 100 and b < 100:
                    red_pixels.append((x, y))
                    
        if red_pixels:
            min_x = min(p[0] for p in red_pixels)
            max_x = max(p[0] for p in red_pixels)
            min_y = min(p[1] for p in red_pixels)
            max_y = max(p[1] for p in red_pixels)
            print(f"Player sprite found at pixel box: ({min_x}, {min_y}) to ({max_x}, {max_y})")
        else:
            print("No player sprite found on landing screen.")
            
        # Let's crop and inspect the center 10x10 of the screenshot
        print("Center 10x10 pixel colors:")
        for y in range(68, 78):
            row = []
            for x in range(75, 85):
                r, g, b = img_160.getpixel((x, y))[:3]
                row.append(f"{r:02x}{g:02x}{b:02x}")
            print("  ", " ".join(row))
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    analyze_landing()
