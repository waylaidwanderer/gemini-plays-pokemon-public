import mgba
import time
from PIL import Image

# 1. Open Start menu
print("Opening Start menu...")
mgba.press_buttons(["Start"])
time.sleep(0.5)

# 2. Take screenshot to find cursor
sc_path = mgba.take_screenshot()
img = Image.open(sc_path)

# Convert to grayscale
img_gray = img.convert("L")

# Column 10 is from x = 10 * 8 = 80 to x = 88. Center is 84.
# Rows 2, 4, 6, 8, 10, 12, 14 are at y = r * 8 + 4.
rows = [2, 4, 6, 8, 10, 12, 14]
cursor_row = None
for r in rows:
    y = r * 8 + 4
    # Check a few pixels in the tile to see if they are dark
    dark_pixels = 0
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            val = img_gray.getpixel((84 + dx, y + dy))
            if val < 100: # Dark pixel
                dark_pixels += 1
    if dark_pixels > 5:
        cursor_row = r
        break

print("Found cursor at row:", cursor_row)

if cursor_row is not None:
    current_idx = (cursor_row - 2) // 2
    target_idx = 1 # POKéMON
    diff = target_idx - current_idx
    
    if diff > 0:
        buttons = ["Down"] * diff
    elif diff < 0:
        buttons = ["Up"] * abs(diff)
    else:
        buttons = []
    
    buttons.append("A")
    print("Navigating to POKéMON with buttons:", buttons)
    mgba.press_buttons(buttons)
    time.sleep(1.0)
    
    print("Selecting TRUFFLE...")
    # Park at SHELLBY, then Down 1 to TRUFFLE
    buttons = []
    for _ in range(10):
        buttons.extend(["Up", "sleep 100"])
    buttons.extend(["Down", "sleep 100", "A"])
    mgba.press_buttons(buttons)
    time.sleep(1.0)
    
    print("Selecting CUT...")
    # Park at DIG, then Down 1 to CUT
    buttons = []
    for _ in range(10):
        buttons.extend(["Up", "sleep 100"])
    buttons.extend(["Down", "sleep 100", "A"])
    mgba.press_buttons(buttons)
    time.sleep(2.0)
    
    print("Done!")
else:
    print("Error: Cursor not found!")
