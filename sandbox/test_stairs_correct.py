import mgba
import time

print("Walking to stairs at (5, 10) correctly via Row 11...")
mgba.press_buttons([
    "Right", "sleep 450",
    "Right", "sleep 450",
    "Right", "sleep 450",
    "Up"
])
time.sleep(2.5)

pos = mgba.get_coordinates()
print("Position after warping:", pos)
