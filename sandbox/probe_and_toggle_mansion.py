import mgba
import sys
import time
from PIL import Image

def get_pos():
    return mgba.get_coordinates()

# Currently at (1, 10).
print("Start position:", get_pos())

# 1. Walk to (2, 12) and face UP
mgba.press_buttons(["Down", "sleep 600"]) # to (1, 11)
mgba.press_buttons(["Down", "sleep 600"]) # to (1, 12)
mgba.press_buttons(["Right", "sleep 600"]) # to (2, 12)
mgba.press_buttons(["Up", "sleep 400"]) # face UP
print("Facing UP at:", get_pos())

# 2. Check if we can open dialogue
print("Pressing A (1)...")
mgba.press_buttons(["A", "sleep 1200"])
img1 = mgba.take_screenshot()
pil_img1 = Image.open(img1)
cropped = pil_img1.crop((0, 112, 160, 144))
pixels = list(cropped.getdata())
white_pixels = sum(1 for p in pixels if p[0] > 200 and p[1] > 200 and p[2] > 200)
ratio = white_pixels / len(pixels)
print("Dialogue open ratio:", ratio)

if ratio > 0.5:
    print("Dialogue opened! Advancing and selecting YES...")
    mgba.press_buttons(["A", "sleep 1200"]) # opens YES/NO
    mgba.press_buttons(["A", "sleep 1200"]) # selects YES (toggles!)
    mgba.press_buttons(["A", "sleep 1200"]) # advances "Who wouldn't?"
    mgba.press_buttons(["B", "sleep 600"]) # closes dialogue
    print("Toggle complete!")
else:
    print("No dialogue opened. Try turning and pressing A again?")
    mgba.press_buttons(["B", "sleep 300"])

print("Final position:", get_pos())
mgba.take_screenshot()
