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

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

pos = mgba.get_coordinates()
print("Starting position:", pos)

# We are at (2, 11). Walk to (1, 13)
# Walk DOWN to (2, 13)
# Walk LEFT to (1, 13)
if pos != {"x": 1, "y": 13}:
    mgba.press_buttons([
        "Down", "sleep 450",
        "Down", "sleep 450",
        "Left"
    ])
    time.sleep(1.5)
    pos = mgba.get_coordinates()
    print("Position after walking to (1, 13):", pos)

# Stand at (1, 13) and face UP
if pos == {"x": 1, "y": 13}:
    print("Aligning UP towards (1, 12)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    print("Pressing A to see if dialogue opens...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    if is_dialogue_open():
        print("SUCCESS! Switch dialogue opened at (1, 13) facing UP!")
        mgba.press_buttons(["A"]) # YES
        time.sleep(1.2)
        mgba.press_buttons(["A"]) # Result
        time.sleep(1.2)
        mgba.press_buttons(["A"]) # Dismiss
        time.sleep(1.0)
        print("Switch toggled successfully to State B!")
    else:
        print("Failed to open switch dialogue at (1, 13) facing UP.")
        mgba.press_buttons(["B"])
