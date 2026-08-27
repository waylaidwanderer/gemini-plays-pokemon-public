import mgba
import time
from PIL import Image

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

# Walk to (2, 12) and face UP
mgba.press_buttons(["Down"])
time.sleep(0.5)
mgba.press_buttons(["Right"])
time.sleep(0.5)
mgba.press_buttons(["Up"])
time.sleep(0.5)

print("Standing at:", mgba.get_coordinates())

# Press A once to open dialogue
mgba.press_buttons(["A"])
time.sleep(1.0)

# Take screenshot to see if dialogue box is open
scr_file = mgba.take_screenshot()
img = Image.open(scr_file)
img_std = img.resize((160, 144), Image.Resampling.NEAREST)

# Check for text box border or white pixels in the bottom text area
white_count = 0
for y in range(115, 140):
    for x in range(10, 150):
        r, g, b = img_std.getpixel((x, y))[:3]
        if r > 240 and g > 240 and b > 240:
            white_count += 1

print("White pixel count in dialogue area:", white_count)
if white_count > 1000:
    print("Dialogue opened successfully!")
else:
    print("No dialogue opened. We are NOT interacting with the switch.")

# Press B to dismiss any dialogue
mgba.press_buttons(["B"])
time.sleep(0.5)
