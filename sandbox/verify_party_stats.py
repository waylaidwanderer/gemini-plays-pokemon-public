import mgba
import time

# Current position is (18, 7) on overworld
# Open Start Menu
print("Opening Start Menu...")
mgba.press_buttons(["Start"])
time.sleep(0.3)

# Go to POKeMON (which is the second option)
print("Moving Down to POKeMON...")
mgba.press_buttons(["Down"])
time.sleep(0.18)

# Press A to open party menu
print("Opening POKeMON Party Menu...")
mgba.press_buttons(["A"])
time.sleep(0.5)

# Take a screenshot to verify all party members' HP and levels
screenshot = mgba.take_screenshot()
print(f"Party Menu screenshot: {screenshot}")

# Exit back to overworld by pressing B several times
print("Exiting back to overworld...")
mgba.press_buttons(["B", "sleep 300", "B", "sleep 300", "B"])
print("Back on overworld.")
