import mgba
import time

print("--- COMPLETING PHASE 2 NAVIGATION TO AREA 2 (NORTH) ---")

def get_pos():
    return mgba.get_coordinates()

# Current position is (20, 6) in the overworld facing UP (after clearing the escape screen).
# 0. Clear the "Got away safely!" text box.
mgba.press_buttons(["A"])
time.sleep(1.0)
print("Returned to overworld. Current Position:", get_pos())

# 1. Walk UP Column 20 to Row 3: (20, 3)
print("Step 1: Walking UP Column 20 to Row 3")
for _ in range(10):
    pos = get_pos()
    if pos and pos['y'] == 3:
        print("Arrived at Row 3!")
        break
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
else:
    print("Failed to reach Row 3!")

# 2. Walk Left along Row 3 to Column 7: (7, 3)
print("Step 2: Walking Left to Column 7")
for _ in range(20):
    pos = get_pos()
    if pos and pos['x'] == 7:
        print("Arrived at Column 7!")
        break
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
else:
    print("Failed to reach Column 7!")

# 3. Walk Down to Row 5 on Column 7: (7, 5)
print("Step 3: Walking Down to Row 5")
for _ in range(5):
    pos = get_pos()
    if pos and pos['y'] == 5:
        print("Arrived at Row 5!")
        break
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
else:
    print("Failed to reach Row 5!")

# 4. Walk Left to transition to Area 2 (North) at (0, 5)
# During transition, x changes from 0 to 39.
print("Step 4: Walking Left to transition to Area 2 (North)")
for _ in range(10):
    pos = get_pos()
    if pos and pos['x'] == 39:
        print("Successfully warped into Area 2 (North)!")
        break
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
else:
    print("Failed to detect warp, but finished pressing Left.")

mgba.take_screenshot()
print("Final Position:", get_pos())
