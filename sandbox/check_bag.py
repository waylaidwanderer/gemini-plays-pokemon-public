import mgba
import time

# Step 1: Open Start Menu
mgba.press_buttons(["Start"])
time.sleep(0.5)

# Step 2: Move down twice to "ITEM" and select
mgba.press_buttons(["Down", "sleep 100", "Down", "sleep 100", "A"])
time.sleep(0.8)

# Step 3: Take screenshot of the Bag page 1
bag_p1 = mgba.take_screenshot()
print("Saved bag page 1 screenshot to:", bag_p1)

# Step 4: Scroll down 7 times to see page 2 items (if any)
mgba.press_buttons(["Down", "sleep 100", "Down", "sleep 100", "Down", "sleep 100", "Down", "sleep 100", "Down", "sleep 100", "Down", "sleep 100", "Down", "sleep 100"])
time.sleep(0.8)

# Step 5: Take screenshot of the Bag page 2
bag_p2 = mgba.take_screenshot()
print("Saved bag page 2 screenshot to:", bag_p2)

# Step 6: Close the menu and return to overworld
mgba.press_buttons(["B", "sleep 200", "B", "sleep 200", "B"])
time.sleep(0.5)
