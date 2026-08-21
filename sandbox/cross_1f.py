import mgba
import time

# We are at (7, 11) on 2F West.
# Let's test walking UP onto the stairs at (7, 10) to see where it warps us!
print("Current position:", mgba.get_coordinates())

print("Step UP onto (7, 10)...")
mgba.press_buttons(["Up"])
time.sleep(0.3)
pos = mgba.get_coordinates()
print("Position after Up:", pos)

# If we warped, let's print and warp back if possible
if pos['y'] != 10 or pos['x'] != 7:
    print("WARPED!")
else:
    # Walk back Down to (7, 11)
    mgba.press_buttons(["Down"])
    time.sleep(0.3)

print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
