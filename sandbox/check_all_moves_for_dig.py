# Let's inspect NIBBLES and NIDORAN to see who has DIG!
# We are currently on the Party menu screen with the cursor on NIBBLES.
import mgba
import time

# 1. Press A on NIBBLES
print("Pressing A on NIBBLES...")
mgba.press_buttons(["A"])
time.sleep(1.0)
mgba.take_screenshot()

# 2. Press B to close submenu
mgba.press_buttons(["B"])
time.sleep(0.5)

# 3. Move down to NIDORAN (from NIBBLES, press Down twice)
print("Moving down to NIDORAN...")
mgba.press_buttons(["Down", "sleep 100", "Down", "sleep 100", "A"])
time.sleep(1.0)
mgba.take_screenshot()

# 4. Press B to close submenu, B to close Party list
mgba.press_buttons(["B", "sleep 400", "B"])
time.sleep(0.5)
print("Done!")
