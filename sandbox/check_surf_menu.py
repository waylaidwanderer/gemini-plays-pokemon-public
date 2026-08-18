import mgba
import time

# Step 1: Turn Right to face the water at (8, 25)
mgba.press_buttons(["Right"])
time.sleep(0.3)

# Step 2: Open Start Menu
mgba.press_buttons(["Start"])
time.sleep(0.5)

# Step 3: Go down to POKéMON (2nd option, so press Down once) and select
mgba.press_buttons(["Down", "sleep 100", "A"])
time.sleep(0.5)

# Step 4: Select SHELLBY (1st in party)
mgba.press_buttons(["A"])
time.sleep(0.5)

# Take screenshot to verify the submenu options
screenshot_path = mgba.take_screenshot()
print("Saved party submenu screenshot to:", screenshot_path)
