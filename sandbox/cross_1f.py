import mgba
import time

# We are at (7, 10) on 3F West.
print("Current position:", mgba.get_coordinates())

# 1. Warp to 2F West by stepping Down to (7, 11) and Up to (7, 10)
print("Stepping Down then Up to warp to 2F West...")
mgba.press_buttons(["Down", "sleep 200", "Up"])
time.sleep(1.0)
pos = mgba.get_coordinates()
print("Position after warp attempt:", pos)

# We should be on 2F West at (7, 11) now.
# Let's walk to (5, 11)
print("Walking to (5, 11)...")
mgba.press_buttons(["Left", "sleep 200", "Left"])
time.sleep(0.5)
pos = mgba.get_coordinates()
print("At:", pos)

# Let's try walking UP to (5, 10)
print("Stepping Up to (5, 10)...")
mgba.press_buttons(["Up"])
time.sleep(0.3)
pos = mgba.get_coordinates()
print("At (5, 10)?", pos)

# Check if we warped to 1F (large coordinate change)
if pos['y'] > 15 or pos['x'] != 5:
    print("WARPED TO 1F!!!")
else:
    # Try different actions on (5, 10)
    print("Trying extra Up on (5, 10)...")
    mgba.press_buttons(["Up"])
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print("Position after extra Up:", pos)
    
    if pos['y'] > 15:
        print("WARPED TO 1F with extra Up!")

print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
