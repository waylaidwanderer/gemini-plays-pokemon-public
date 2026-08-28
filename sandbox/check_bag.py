import mgba
import time

# Open start menu
mgba.press_buttons(["Start"])
time.sleep(0.5)

# Scroll to BAG (2 Down presses)
mgba.press_buttons(["Down", "sleep 150", "Down", "sleep 150", "A"])
time.sleep(1.0)
mgba.take_screenshot()

# Scroll down to see more items (if any)
for _ in range(5):
    mgba.press_buttons(["Down"])
    time.sleep(0.2)
mgba.take_screenshot()

# Close menu
mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
time.sleep(0.5)
