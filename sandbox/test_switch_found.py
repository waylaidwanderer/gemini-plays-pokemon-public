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
    print(f"  Dialogue check: white_cream_pixels={white_cream_pixels}")
    return white_cream_pixels > 3000

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

pos = mgba.get_coordinates()
print("Current position:", pos)

print("Pressing A to see if dialogue opens...")
mgba.press_buttons(["A"])
time.sleep(1.0)

if is_dialogue_open():
    print("SUCCESS! Switch dialogue opened at (2, 11) facing UP!")
    # Toggling switch...
    mgba.press_buttons(["A"]) # Select YES
    time.sleep(1.2)
    mgba.press_buttons(["A"]) # Dismiss "Toggled!"
    time.sleep(1.2)
    mgba.press_buttons(["A"]) # Dismiss dialogue
    time.sleep(1.0)
    print("Switch toggled successfully!")
else:
    print("Failed to open switch dialogue at (2, 11) facing UP.")
    mgba.press_buttons(["B"])
