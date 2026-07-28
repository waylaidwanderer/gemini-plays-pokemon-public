import mgba
import time

# Open Start Menu
print("Opening Start Menu...")
mgba.press_buttons(["Start"])
time.sleep(0.5)

# Move down to POKeMON
print("Moving Down to POKeMON...")
mgba.press_buttons(["Down"])
time.sleep(0.3)

# Press A and wait for party menu to open
print("Opening POKeMON Party Menu...")
mgba.press_buttons(["A"])
time.sleep(1.5)  # Longer wait to ensure transition completes

# Capture the Party Menu screenshot
screenshot = mgba.take_screenshot()
print(f"Party Menu screenshot captured: {screenshot}")

# Exit back to overworld
print("Exiting back to overworld...")
mgba.press_buttons(["B", "sleep 400", "B", "sleep 400", "B"])
print("Exited.")
