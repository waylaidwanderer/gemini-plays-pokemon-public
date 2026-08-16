import mgba
import time

print("--- OPENING MENU AND INSPECTING BAG ---")

# 1. Open the menu
mgba.press_buttons(["Start", "sleep 500"])

# 2. Make sure we are at the top (POKEDEX)
mgba.press_buttons(["Up", "Up", "Up", "Up", "Up", "sleep 200"])

# 3. Move down to ITEM (2 steps down from POKEDEX)
mgba.press_buttons(["Down", "Down", "sleep 200"])

# 4. Press A to select ITEM
mgba.press_buttons(["A", "sleep 500"])

# Take screenshot of page 1
p1 = mgba.take_screenshot()
print("Bag Page 1:", p1)

# Press Down 4 times to scroll down to see more items
for i in range(4):
    mgba.press_buttons(["Down", "sleep 100"])
time.sleep(0.5)

p2 = mgba.take_screenshot()
print("Bag Page 2:", p2)

# Press Down 4 more times
for i in range(4):
    mgba.press_buttons(["Down", "sleep 100"])
time.sleep(0.5)

p3 = mgba.take_screenshot()
print("Bag Page 3:", p3)

# Exit bag and menu
mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
print("Done!")
