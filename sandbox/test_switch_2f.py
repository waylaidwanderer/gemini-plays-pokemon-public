import mgba
import time
from PIL import Image

def is_dialogue_open():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file).resize((160, 144), Image.Resampling.NEAREST)
    cropped = img.crop((0, 104, 160, 144))
    white_cream_pixels = 0
    for y in range(cropped.height):
        for x in range(cropped.width):
            r, g, b = cropped.getpixel((x, y))[:3]
            if r > 200 and g > 200 and b > 200:
                white_cream_pixels += 1
    return white_cream_pixels > 3000

pos = mgba.get_coordinates()
print("Starting search for 2F West switch from:", pos)

# Walk left along Row 11 to Column 2 (2, 11)
steps = []
for x in range(pos["x"] - 1, 1, -1):
    steps.append(("Left", {"x": x, "y": 11}))

for d, c in steps:
    mgba.press_buttons([d])
    time.sleep(0.45)
    
pos = mgba.get_coordinates()
print("Position after walking left:", pos)

if pos == {"x": 2, "y": 11}:
    # Walk down to (2, 12)
    mgba.press_buttons(["Down"])
    time.sleep(0.45)
    pos = mgba.get_coordinates()
    print("Position after walking down to Row 12:", pos)

if pos == {"x": 2, "y": 12}:
    # Face UP towards (2, 11)
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    # Try to open switch dialogue
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    if is_dialogue_open():
        print("Mewtwo switch dialogue is OPEN at (2, 11) on 2F West!")
        # Choose YES
        mgba.press_buttons(["A"])
        time.sleep(1.2)
        mgba.press_buttons(["A"])
        time.sleep(1.2)
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        print("Switch toggled successfully!")
    else:
        print("No dialogue box opened. (2, 11) on 2F West is NOT a switch.")
        mgba.press_buttons(["B"])
        time.sleep(0.3)
