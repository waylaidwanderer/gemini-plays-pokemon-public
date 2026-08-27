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

# We are at (2, 12).
# Let's walk to (3, 13): Down to (2, 13), Right to (3, 13)
mgba.press_buttons(["Down"])
time.sleep(0.45)
print("Position after Down:", mgba.get_coordinates())

mgba.press_buttons(["Right"])
time.sleep(0.45)
print("Position after Right:", mgba.get_coordinates())

# Face UP
mgba.press_buttons(["Up"])
time.sleep(0.4)

# Press A
print("Pressing A...")
mgba.press_buttons(["A"])
time.sleep(0.8)

if is_dialogue_open():
    print("SUCCESS! Dialogue opened from (3, 13) facing UP!")
    # Toggle it to State B
    mgba.press_buttons(["A"]) # YES
    time.sleep(1.0)
    mgba.press_buttons(["A"]) # Result
    time.sleep(1.0)
    mgba.press_buttons(["A"]) # Dismiss
    time.sleep(1.0)
    print("Switch toggled!")
else:
    print("Dialogue did not open. Trying to face UP from (3, 11) towards (3, 10)...")
    mgba.press_buttons(["B"])
    time.sleep(0.3)
    
    # Let's go to (3, 11): Up to (3, 12) -> wait, (3, 12) is solid!
    # So we walk Left to (2, 13), Up to (2, 11), Right to (3, 11), Face UP
    mgba.press_buttons(["Left"])
    time.sleep(0.45)
    mgba.press_buttons(["Up"])
    time.sleep(0.45)
    mgba.press_buttons(["Up"])
    time.sleep(0.45)
    mgba.press_buttons(["Right"])
    time.sleep(0.45)
    print("Position at second target:", mgba.get_coordinates())
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    print("Pressing A...")
    mgba.press_buttons(["A"])
    time.sleep(0.8)
    
    if is_dialogue_open():
        print("SUCCESS! Dialogue opened from (3, 11) facing UP!")
        mgba.press_buttons(["A"]) # YES
        time.sleep(1.0)
        mgba.press_buttons(["A"]) # Result
        time.sleep(1.0)
        mgba.press_buttons(["A"]) # Dismiss
        time.sleep(1.0)
    else:
        print("Dialogue did not open at (3, 11) either.")
        mgba.press_buttons(["B"])
        time.sleep(0.3)
