import mgba
import time

print("--- INSPECTING BAG FOR HM04 (STRENGTH) ---")

# 1. Open START menu
mgba.press_buttons(["Start"])
time.sleep(0.5)

# 2. Force cursor to top (POKEDEX)
for _ in range(7):
    mgba.press_buttons(["Up"])
    time.sleep(0.1)

# 3. Go Down twice to highlight ITEM
# POKEDEX -> POKEMON -> ITEM
mgba.press_buttons(["Down", "sleep 200", "Down"])
time.sleep(0.5)

# 4. Select ITEM
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
print("Done inspecting bag!")
