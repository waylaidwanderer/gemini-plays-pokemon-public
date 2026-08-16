import mgba
import time

print("--- EXITING BAG AND MENU ---")

# 1. Press A on CANCEL to exit bag
mgba.press_buttons(["A", "sleep 500"])

# 2. Press B to close start menu
mgba.press_buttons(["B", "sleep 500"])

# 3. Take a screenshot of the overworld
scr = mgba.take_screenshot()
print("Overworld Screen:", scr)
print("Position:", mgba.get_coordinates())
