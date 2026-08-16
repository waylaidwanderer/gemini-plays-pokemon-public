import mgba
import time

print("--- SELF-CORRECTING SAFARI NAVIGATION (PHASE 2 NORTH) ---")

def get_pos():
    return mgba.get_coordinates()

# Current position is (8, 8) facing UP.
# 1. Walk Right to Column 12 on Row 8: (12, 8)
print("Step 1: Walking Right to Column 12")
for _ in range(10):
    pos = get_pos()
    if pos and pos['x'] == 12:
        print("Arrived at Column 12!")
        break
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
else:
    print("Failed to reach Column 12!")

# 2. Walk UP to Row 6 on Column 12: (12, 6) (climbing stairs)
print("Step 2: Walking UP to Row 6 (climbing stairs)")
for _ in range(5):
    pos = get_pos()
    if pos and pos['y'] == 6:
        print("Arrived at Row 6!")
        break
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
else:
    print("Failed to reach Row 6!")

# 3. Walk Right to Column 17 on Row 6: (17, 6)
print("Step 3: Walking Right to Column 17")
for _ in range(10):
    pos = get_pos()
    if pos and pos['x'] == 17:
        print("Arrived at Column 17!")
        break
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
else:
    print("Failed to reach Column 17!")

# 4. Walk Down to Row 8 on Column 17: (17, 8) (descending stairs)
print("Step 4: Walking Down to Row 8 (descending stairs)")
for _ in range(5):
    pos = get_pos()
    if pos and pos['y'] == 8:
        print("Arrived at Row 8!")
        break
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
else:
    print("Failed to reach Row 8!")

# 5. Walk Right to Column 20 on Row 8: (20, 8)
print("Step 5: Walking Right to Column 20")
for _ in range(5):
    pos = get_pos()
    if pos and pos['x'] == 20:
        print("Arrived at Column 20!")
        break
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
else:
    print("Failed to reach Column 20!")

# 6. Walk UP Column 20 to Row 3: (20, 3)
print("Step 6: Walking UP Column 20 to Row 3")
for _ in range(10):
    pos = get_pos()
    if pos and pos['y'] == 3:
        print("Arrived at Row 3!")
        break
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
else:
    print("Failed to reach Row 3!")

# 7. Walk Left along Row 3 to Column 7: (7, 3)
print("Step 7: Walking Left along Row 3 to Column 7")
for _ in range(20):
    pos = get_pos()
    if pos and pos['x'] == 7:
        print("Arrived at Column 7!")
        break
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
else:
    print("Failed to reach Column 7!")

# 8. Walk Down to Row 5 on Column 7: (7, 5)
print("Step 8: Walking Down to Row 5")
for _ in range(5):
    pos = get_pos()
    if pos and pos['y'] == 5:
        print("Arrived at Row 5!")
        break
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
else:
    print("Failed to reach Row 5!")

# 9. Walk Left to transition to Area 2 (North) at (0, 5)
# During transition, x changes from 0 to 39 (or map changes).
print("Step 9: Walking Left to transition to Area 2 (North)")
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
