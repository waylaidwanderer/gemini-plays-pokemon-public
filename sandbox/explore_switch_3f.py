import mgba
import time

def check_pos():
    pos = mgba.get_coordinates()
    print("CURRENT POSITION:", pos)
    return pos

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

p = check_pos()

# Let's test all 4 directions from (2, 11) to find the Mewtwo switch!
directions = ["Up", "Right", "Down", "Left"]

for d in directions:
    print(f"Turning {d} and pressing A...")
    mgba.press_buttons([d])
    time.sleep(0.4)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
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
        print(f"SUCCESS! Dialogue opened facing {d}!")
        # Save screenshot
        img.save(f"mansion_switch_dialogue_{d}.png")
        # Toggle it
        mgba.press_buttons(["A"])
        time.sleep(1.5)
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        break
    else:
        print(f"No dialogue facing {d}.")

print("Check finished!")
p = check_pos()
