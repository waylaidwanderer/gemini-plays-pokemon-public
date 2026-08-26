import mgba
import time
from PIL import Image

def is_dialogue_open():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file).resize((160, 144), Image.Resampling.NEAREST)
    black_pixels = 0
    for x in range(10, 150):
        r, g, b = img.getpixel((x, 112))
        if r < 80 and g < 80 and b < 80:
            black_pixels += 1
    bg_pixels = 0
    for y in range(116, 140):
        for x in range(20, 140):
            r, g, b = img.getpixel((x, y))
            if r > 200 and g > 200 and b > 200:
                bg_pixels += 1
    return black_pixels > 120 and bg_pixels > 1500

# Start menu is currently open pointing to POKéMON.
# Let's open the POKéMON list.
print("Opening POKéMON menu...")
mgba.press_buttons(["A"])
time.sleep(0.8)

# For each Pokémon slot (1 to 5), let's inspect STATS page 2 (moves)
for slot in range(1, 6):
    print(f"Inspecting Slot {slot}...")
    # Select the slot (already on slot 1, then go down for subsequent slots)
    if slot > 1:
        mgba.press_buttons(["Down"])
        time.sleep(0.3)
        
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    
    # Select STATS (STATS is top option, so press A)
    mgba.press_buttons(["A"])
    time.sleep(0.8)
    
    # Page 1 of stats is shown. Press A to go to Page 2 (moves)
    mgba.press_buttons(["A"])
    time.sleep(0.8)
    
    # Take screenshot of moves
    scr = mgba.take_screenshot()
    print(f"Slot {slot} moves screenshot saved to: {scr}")
    img = Image.open(scr)
    img.save(f"slot_{slot}_moves.png")
    
    # Return to PKMN list (press B twice)
    mgba.press_buttons(["B", "sleep 200", "B"])
    time.sleep(0.8)

# Return to Start menu (press B from PKMN list)
mgba.press_buttons(["B"])
time.sleep(0.6)

# Open ITEM (ITEM is 1 step down from POKéMON)
print("Opening ITEM menu...")
mgba.press_buttons(["Down", "sleep 150", "A"])
time.sleep(0.8)

# Capture Page 1 of Bag
scr_bag1 = mgba.take_screenshot()
img_bag1 = Image.open(scr_bag1)
img_bag1.save("real_bag_p1.png")
print("Saved real_bag_p1.png")

# Scroll down 4 times to see Page 2
mgba.press_buttons(["Down", "sleep 150", "Down", "sleep 150", "Down", "sleep 150", "Down", "sleep 150"])
time.sleep(0.6)

scr_bag2 = mgba.take_screenshot()
img_bag2 = Image.open(scr_bag2)
img_bag2.save("real_bag_p2.png")
print("Saved real_bag_p2.png")

# Close start menu
mgba.press_buttons(["B", "sleep 200", "B"])
time.sleep(0.4)

