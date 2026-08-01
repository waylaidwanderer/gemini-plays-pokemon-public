import mgba
import time

# Start at (3, 15)
mgba.press_buttons(["Right", "sleep 2500"])
pos = mgba.get_coordinates()
print("Position after sliding Right from (3, 15):", pos)
