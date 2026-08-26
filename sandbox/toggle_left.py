import mgba
import time
from PIL import Image

def is_dialogue_open():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file).resize((160, 144), Image.Resampling.NEAREST)
    
    # Check if a horizontal black border line of at least 110 pixels is present at y=112
    black_pixels = 0
    for x in range(10, 150):
        r, g, b = img.getpixel((x, 112))
        if r < 80 and g < 80 and b < 80:
            black_pixels += 1
            
    # Also check if the dialogue box area contains a solid white/cream background
    bg_pixels = 0
    for y in range(116, 140):
        for x in range(20, 140):
            r, g, b = img.getpixel((x, y))
            if r > 200 and g > 200 and b > 200:
                bg_pixels += 1
                
    print(f"DEBUG: black_pixels={black_pixels}, bg_pixels={bg_pixels}")
    return black_pixels > 120 and bg_pixels > 1500

pos = mgba.get_coordinates()
print("Current position:", pos)

if pos == {"x": 1, "y": 12}:
    print("Turning Left...")
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    
    print("Pressing A...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    if is_dialogue_open():
        print("Dialogue opened successfully!")
        mgba.press_buttons(["A"]) # Advance
        time.sleep(1.2)
        mgba.press_buttons(["A"]) # Select YES
        time.sleep(1.2)
        mgba.press_buttons(["A"]) # Dismiss
        time.sleep(1.2)
        print("Switch toggled!")
    else:
        print("Dialogue failed to open.")
        mgba.press_buttons(["B"])
        time.sleep(0.4)

