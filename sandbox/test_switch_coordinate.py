import mgba
import time

# Let's walk to (2, 16), then Left to (1, 16), then press UP and check the coordinates!
pos = mgba.get_coordinates()
print("Current position:", pos)

# We are at (1, 12). Let's walk down to (1, 16)
steps = []
for y in range(13, 17):
    steps.append(("Down", {"x": 1, "y": y}))

for d, c in steps:
    mgba.press_buttons([d])
    time.sleep(0.45)
    print(f"Moved {d}, current position: {mgba.get_coordinates()}")

# At (1, 16), press UP
print("At (1, 16), pressing UP...")
mgba.press_buttons(["Up"])
time.sleep(0.45)
print("Position after UP:", mgba.get_coordinates())

# Press A
print("Pressing A...")
mgba.press_buttons(["A"])
time.sleep(0.8)

# Check if dialogue is open
import time
from PIL import Image
scr_file = mgba.take_screenshot()
img = Image.open(scr_file).resize((160, 144), Image.Resampling.NEAREST)
cropped = img.crop((0, 104, 160, 144))

white_cream_pixels = 0
for y in range(cropped.height):
    for x in range(cropped.width):
        r, g, b = cropped.getpixel((x, y))[:3]
        if r > 200 and g > 200 and b > 200:
            white_cream_pixels += 1

print("Dialogue cream pixels:", white_cream_pixels)
if white_cream_pixels > 3000:
    print("SUCCESS! Switch dialogue opened!")
    # Dismiss dialogue
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
else:
    print("Dialogue did not open.")
    mgba.press_buttons(["B"])
    time.sleep(0.3)
