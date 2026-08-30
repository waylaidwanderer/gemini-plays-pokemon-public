from PIL import Image
import os

def find_player_in_screenshot(path):
    print(f"Inspecting {path}...")
    try:
        img = Image.open(path)
        # Since the coordinate labels are rendered on the screenshot as text or overlays,
        # let's look at the clean image vs labeled image if they exist,
        # or we can print out the image dimensions and inspect the labels visually.
        # But wait! The coordinates might be written in the file name or we can extract the player sprite.
        print("  Size:", img.size)
    except Exception as e:
        print("  Error:", e)

find_player_in_screenshot("screenshots/screenshot_1788093216840.png")
find_player_in_screenshot("screenshots/screenshot_1788093259922.png")
