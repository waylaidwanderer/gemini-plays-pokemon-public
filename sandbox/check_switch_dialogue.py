from PIL import Image
import os

def crop_text(src_path, dest_path):
    img = Image.open(src_path)
    img_res = img.resize((160, 144), Image.Resampling.NEAREST)
    cropped = img_res.crop((0, 100, 160, 144))
    cropped.save(dest_path)

screenshots = [
    "screenshots/screenshot_1787948115403.png",
    "screenshots/screenshot_1787948117286.png",
    "screenshots/screenshot_1787948119145.png",
    "screenshots/screenshot_1787948120996.png"
]

for i, src in enumerate(screenshots):
    dest = f"screenshots/cropped_text_screenshot_{i}.png"
    crop_text(src, dest)
    
    img_crop = Image.open(dest)
    white_pixels = 0
    total = 0
    for y in range(8, 40):
        for x in range(8, 152):
            r, g, b = img_crop.getpixel((x, y))[:3]
            total += 1
            if r > 240 and g > 240 and b > 240:
                white_pixels += 1
    pct = white_pixels / total
    print(f"Crop {i}: White pixel pct = {pct:.2f}% (Bytes: {os.path.getsize(dest)})")
