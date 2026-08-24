import mgba
import time
from PIL import Image

def get_pos():
    return mgba.get_coordinates()

# Starting at (5, 10) on 3F West
print("Starting position:", get_pos())

# 1. Walk Left to (2, 12)
# (5, 10) -> (5, 11) -> (5, 12) -> (2, 12)
mgba.press_buttons(["Down", "sleep 150", "Down", "sleep 150"])
mgba.press_buttons(["Left", "sleep 150", "Left", "sleep 150", "Left", "sleep 150"])
# Turn UP to face statue
mgba.press_buttons(["Up", "sleep 200"])
print("Position 1 (should be 2, 12 facing UP):", get_pos())

# Take screenshot BEFORE toggle
sc_before = mgba.take_screenshot()
print("Screenshot BEFORE toggle:", sc_before)

# 2. Talk to the statue and select YES
mgba.press_buttons(["A", "sleep 800"]) # "A secret switch!"
mgba.press_buttons(["A", "sleep 800"]) # "Press it?" -> YES
mgba.press_buttons(["A", "sleep 500"]) # "Who wouldn't?" -> close

# Take screenshot AFTER toggle
sc_after = mgba.take_screenshot()
print("Screenshot AFTER toggle:", sc_after)

# Let's crop the Row 9 gate area in both screenshots and compare them
img_b = Image.open(sc_before)
img_a = Image.open(sc_after)

# Crop Row 9 gate area (e.g. columns 1 to 6 on Row 9)
# Let's save them as 6_7_before.png and 6_7_after.png to Sandboxed screenshots
img_b.crop((0, 0, 160, 144)).save("screenshots/cropped/6_7_before.png")
img_a.crop((0, 0, 160, 144)).save("screenshots/cropped/6_7_after.png")

print("Saved before/after crops!")
