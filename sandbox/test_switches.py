import mgba
import time
from PIL import Image

def get_unique_colors_bottom():
    shot = mgba.take_screenshot()
    img = Image.open(shot)
    cropped = img.crop((0, 96, 160, 144))
    colors = cropped.getcolors()
    return len(colors) if colors else 1000

# 1. Test switch at (2, 11)
print("Testing switch at (2, 11)...")
print("Pressing Left to face left...")
mgba.press_buttons(["Left"])
time.sleep(0.5)
print("Pressing A...")
mgba.press_buttons(["A"])
time.sleep(0.5)
colors_11 = get_unique_colors_bottom()
print("Unique colors at bottom after (2, 11) A-press:", colors_11)

# If unique colors is small (e.g. 6), it means no textbox. If large (e.g. >20), it's a textbox!
if colors_11 < 10:
    print("(2, 11) is INACTIVE! No textbox opened.")
else:
    print("(2, 11) is ACTIVE! Textbox opened.")

# Let's dismiss textbox if it opened
if colors_11 >= 10:
    for _ in range(3):
        mgba.press_buttons(["A"])
        time.sleep(0.5)

# 2. Walk to (2, 6) to test switch at (2, 5)
print("Walking to (2, 6)...")
# Path from (3, 11) to (2, 6) in State B:
# (3, 11) -> (10, 11) -> (10, 6) -> (2, 6)
path = [
    ("Right", 7),
    ("Up", 5),
    ("Left", 8)
]

for direction, count in path:
    for _ in range(count):
        mgba.press_buttons([direction])
        time.sleep(0.35)

print("Reached (2, 6)? Coordinates are:", mgba.get_coordinates())

print("Testing switch at (2, 5) from (2, 6)...")
print("Pressing Up to face up...")
mgba.press_buttons(["Up"])
time.sleep(0.5)
print("Pressing A...")
mgba.press_buttons(["A"])
time.sleep(0.5)
colors_5 = get_unique_colors_bottom()
print("Unique colors at bottom after (2, 5) A-press:", colors_5)

if colors_5 < 10:
    print("(2, 5) is INACTIVE! No textbox opened.")
else:
    print("(2, 5) is ACTIVE! Textbox opened.")

# Dismis textbox if it opened
if colors_5 >= 10:
    for _ in range(3):
        mgba.press_buttons(["A"])
        time.sleep(0.5)
