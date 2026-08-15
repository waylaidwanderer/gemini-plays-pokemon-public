import os
from PIL import Image

def analyze():
    print("Analyzing gold_teeth_check_clean.png...")
    if os.path.exists("screenshots/cropped/gold_teeth_check_clean.png"):
        img = Image.open("screenshots/cropped/gold_teeth_check_clean.png")
        print(f"Size: {img.size}")
        # Save as a text representation or inspect pixels
    else:
        print("gold_teeth_check_clean.png does not exist")

    print("\nAnalyzing player_around_teeth_check.png...")
    if os.path.exists("screenshots/cropped/player_around_teeth_check.png"):
        img2 = Image.open("screenshots/cropped/player_around_teeth_check.png")
        print(f"Size: {img2.size}")
    else:
        print("player_around_teeth_check.png does not exist")

if __name__ == "__main__":
    analyze()
