import mgba
import time

# Walk from current (1, 12) to (5, 11) then UP to (5, 10) to warp
print("Walking to stairs at (5, 10)...")
mgba.press_buttons(["Right", "sleep 450", "Right", "sleep 450", "Right", "sleep 450", "Right", "sleep 450", "Up"])
time.sleep(2.5)

pos = mgba.get_coordinates()
print("Position after warping:", pos)
