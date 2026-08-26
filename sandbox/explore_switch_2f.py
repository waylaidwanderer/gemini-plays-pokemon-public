import mgba
import time

def check_pos():
    pos = mgba.get_coordinates()
    print("CURRENT POSITION:", pos)
    return pos

# Dismiss "Got away safely!" if it is still on screen
mgba.press_buttons(["A"])
time.sleep(1.0)

p = check_pos()

# Let's try to find the Mewtwo statue around (1, 11).
# Is there a statue at (2, 11) or (2, 10)?
# Let's walk Right to (2, 11)? Wait, if there's a statue at (2, 11) we can't walk onto it.
# Let's try walking Up to (1, 10).
print("Trying to walk UP to (1, 10)...")
mgba.press_buttons(["Up"])
time.sleep(0.55)
p = check_pos()

if p == {"x": 1, "y": 10}:
    print("We can walk to (1, 10)!")
    # Face RIGHT and press A to see if there is a switch at (2, 10)
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    # Check if a menu/dialogue is open
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
        print("Dialogue open! This might be the switch!")
        # Let's toggle it by selecting YES (A, sleep, A)
        mgba.press_buttons(["A", "sleep 600", "A"])
        time.sleep(1.0)
    else:
        print("No dialogue. Let's try facing DOWN and pressing A")
        mgba.press_buttons(["Down"])
        time.sleep(0.4)
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        # Check again
        scr = mgba.take_screenshot()
        img = Image.open(scr).resize((160, 144), Image.Resampling.NEAREST)
        black_or_white2 = 0
        for y in range(115, 140):
            for x in range(10, 150):
                r, g, b = img.getpixel((x, y))
                if (r < 50 and g < 50 and b < 50) or (r > 200 and g > 200 and b > 200):
                    black_or_white2 += 1
        if black_or_white2 / total_pixels > 0.90:
            print("Dialogue open facing DOWN! Toggling...")
            mgba.press_buttons(["A", "sleep 600", "A"])
            time.sleep(1.0)
        else:
            # Let's walk back DOWN to (1, 11)
            mgba.press_buttons(["Down"])
            time.sleep(0.55)

p = check_pos()
if p == {"x": 1, "y": 11}:
    # Let's try facing RIGHT from (1, 11) and pressing A
    print("Facing RIGHT from (1, 11)...")
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Check dialogue
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
        print("Dialogue open facing RIGHT from (1, 11)! Toggling...")
        mgba.press_buttons(["A", "sleep 600", "A"])
        time.sleep(1.0)

print("Check finished!")
