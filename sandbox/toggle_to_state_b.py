import mgba
import time

def get_pos():
    return mgba.get_coordinates()

# Starting at (1, 11) on 3F West facing RIGHT towards the statue at (2, 11)
print("Starting position:", get_pos())

# 1. Press A to interact with the secret switch
print("Interacting with secret switch...")
mgba.press_buttons(["A", "sleep 800"])

# 2. Press A to select YES
print("Selecting YES...")
mgba.press_buttons(["A", "sleep 800"])

# 3. Press A to clear "Who wouldn't?"
print("Clearing dialogue...")
mgba.press_buttons(["A", "sleep 500"])

# 4. Check position and take screenshot
print("Final position after toggle:", get_pos())
sc = mgba.take_screenshot()
print("Screenshot after toggling switch:", sc)
