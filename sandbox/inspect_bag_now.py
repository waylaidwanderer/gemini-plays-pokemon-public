import mgba
import time

print("--- INSPECTING ACTUAL BAG ---")

# The cursor is currently pointing at POKEMON.
# 1. Press Down to highlight ITEM
mgba.press_buttons(["Down"])
time.sleep(0.5)

# 2. Select ITEM
mgba.press_buttons(["A"])
time.sleep(0.5)

# Take screenshot of page 1
p1 = mgba.take_screenshot()
print("Bag Page 1:", p1)

# Scroll down to page 2 (press Down 5 times)
for i in range(5):
    mgba.press_buttons(["Down"])
    time.sleep(0.1)
time.sleep(0.5)

p2 = mgba.take_screenshot()
print("Bag Page 2:", p2)

# Scroll down more (press Down 5 more times)
for i in range(5):
    mgba.press_buttons(["Down"])
    time.sleep(0.1)
time.sleep(0.5)

p3 = mgba.take_screenshot()
print("Bag Page 3:", p3)

# Exit menu
mgba.press_buttons(["B", "sleep 200", "B"])
time.sleep(0.5)
print("Done!")
