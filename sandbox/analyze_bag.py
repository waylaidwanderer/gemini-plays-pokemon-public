from PIL import Image
import os

def analyze_bag_page(filename):
    if not os.path.exists(filename):
        print(f"File {filename} does not exist!")
        return
    img = Image.open(filename).resize((160, 144), Image.Resampling.NEAREST)
    # The bag items are listed on the right side of the screen
    # In Gen 1, the item list starts around x=40 (or column 5) to x=150, and y=16 to y=112 (rows 2 to 14)
    # Let's save a crop of the item list to sandbox to look at it, and print out some basic stats
    cropped = img.crop((40, 8, 150, 120))
    cropped.save(f"cropped_{filename}")
    print(f"Saved cropped image for {filename}")

analyze_bag_page("bag_page1.png")
analyze_bag_page("bag_page2.png")
