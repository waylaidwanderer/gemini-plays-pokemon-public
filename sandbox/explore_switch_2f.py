import mgba
import time

# Let's escape the battle first
# We are currently in a wild battle with a Level 30 Ponyta.
# Press A to dismiss "appeared!"
mgba.press_buttons(["A"])
time.sleep(1.2)

# Select RUN
mgba.press_buttons(["Down"])
time.sleep(0.4)
mgba.press_buttons(["Right"])
time.sleep(0.4)
mgba.press_buttons(["A"])
time.sleep(1.5)

# Dismiss run text with B
for _ in range(5):
    mgba.press_buttons(["B"])
    time.sleep(0.3)

pos = mgba.get_coordinates()
print("Position after escape:", pos)

if pos == {"x": 2, "y": 12}:
    print("We are at (2, 12)! Facing UP towards the switch...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    print("Pressing A to interact with the switch...")
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    
    # Check if dialogue is open
    scr = mgba.take_screenshot()
    from PIL import Image
    img = Image.open(scr).resize((160, 144), Image.Resampling.NEAREST)
    black_or_white = 0
    total_pixels = 0
    for y in range(115, 140):
        for x in range(10, 150):
            r, g, b = img.getpixel((x, y))
            total_pixels += 1
            if (r < 50 and g < 50 and b < 50) or (r > 200 and g > 200 and b > 200):
                black_or_white += 1
                
    if black_or_white / total_pixels > 0.90:
        print("Dialogue open! Selecting YES...")
        # Press A on YES, sleep, then press A to dismiss "Whoops! Opened a secret switch!"
        mgba.press_buttons(["A"])
        time.sleep(1.5)
        # Check text box again
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        mgba.press_buttons(["A"])
        time.sleep(1.0)
    else:
        print("Dialogue not open! Let's try pressing A again...")
        mgba.press_buttons(["A"])
        time.sleep(1.0)

else:
    print("Not at (2, 12)")
