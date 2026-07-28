import mgba
import time

# Current position is (20, 8) on overworld
print("Opening Start menu, navigating to ITEM, and opening Bag...")
# We use proper sleep delays between button presses inside mgba.press_buttons!
mgba.press_buttons([
    "Start", "sleep 600",
    "Down", "sleep 300",
    "Down", "sleep 300",
    "A", "sleep 1500"
])

# Capture screenshot of bag
screenshot = mgba.take_screenshot()
print(f"Bag screenshot captured: {screenshot}")

# Exit back to overworld safely
print("Exiting back to overworld...")
mgba.press_buttons(["B", "sleep 400", "B"])
print("Exited.")
