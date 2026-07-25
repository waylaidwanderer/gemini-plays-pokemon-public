import mgba
import time

# Current position is (20, 8) on overworld
# Open Start Menu
print("Opening Start Menu...")
mgba.press_buttons(["Start"])
time.sleep(0.5)

# Move down to ITEM (which is the third option)
print("Moving Down to ITEM...")
mgba.press_buttons(["Down", "Down"])
time.sleep(0.3)

# Press A to open bag
print("Opening Bag...")
mgba.press_buttons(["A"])
time.sleep(1.0)

# Capture screenshot of bag
screenshot = mgba.take_screenshot()
print(f"Bag screenshot captured: {screenshot}")

# Exit back to overworld
print("Exiting back to overworld...")
mgba.press_buttons(["B", "sleep 300", "B"])
print("Exited.")
