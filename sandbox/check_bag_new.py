import mgba
import time

print("Moving cursor from SAVE to ITEM...")
mgba.press_buttons(["Up", "sleep 150", "Up", "sleep 150"])
time.sleep(0.5)

print("Opening BAG...")
mgba.press_buttons(["A"])
time.sleep(1.0)

img1 = mgba.take_screenshot()
print("Bag Page 1 screenshot:", img1)

# Scroll down to see page 2
for _ in range(5):
    mgba.press_buttons(["Down"])
    time.sleep(0.15)
    
img2 = mgba.take_screenshot()
print("Bag Page 2 screenshot:", img2)

# Close bag and start menu
mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
time.sleep(0.5)
