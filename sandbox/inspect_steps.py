from PIL import Image
import glob
import os

# Get the last 16 screenshots
screenshot_files = sorted(glob.glob("screenshots/screenshot_*.png"), key=os.path.getmtime)[-16:]

print("Cropping and saving text boxes...")
for i, f in enumerate(screenshot_files):
    img = Image.open(f)
    w, h = img.size
    # Crop the bottom textbox area
    textbox = img.crop((0, int(h * 0.7), w, h))
    
    # Save cropped version
    out_name = f"step_{i}.png"
    textbox.save(out_name)
    print(f"Saved: {out_name}")
