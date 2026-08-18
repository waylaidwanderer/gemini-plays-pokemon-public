import mgba
import time

# Step 1: Open Start Menu
mgba.press_buttons(["Start"])
time.sleep(0.5)

# Step 2: Go down to POKéMON (2nd option) and select
mgba.press_buttons(["Down", "sleep 100", "A"])
time.sleep(0.8)

# Take screenshot of the party list to verify TRUFFLE's index
party_screenshot = mgba.take_screenshot()
print("Saved party list screenshot to:", party_screenshot)

# Step 3: Close menu to return to overworld
mgba.press_buttons(["B", "sleep 200", "B", "sleep 200", "B"])
time.sleep(0.5)
