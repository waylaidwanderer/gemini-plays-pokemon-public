import mgba
import time

print("--- SELF-CORRECTING SAFARI NAVIGATION (AREA 1 EAST) ---")

def get_pos():
    return mgba.get_coordinates()

# Current position is (11, 19) facing RIGHT.
# 1. Walk Right to Column 12 on Row 19
print("Step 1: Walking Right to Column 12")
for _ in range(5):
    pos = get_pos()
    if pos and pos['x'] == 12:
        print("Arrived at Column 12!")
        break
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
else:
    print("Failed to reach Column 12!")

# 2. Walk Down to Row 22 on Column 12 (descending stairs at (12, 21))
print("Step 2: Walking Down to Row 22 (descending plateau)")
for _ in range(10):
    pos = get_pos()
    if pos and pos['y'] == 22:
        print("Arrived at Row 22 (ground level)!")
        break
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
else:
    print("Failed to reach Row 22!")

# 3. Walk Left to Column 8 on Row 22
print("Step 3: Walking Left to Column 8")
for _ in range(10):
    pos = get_pos()
    if pos and pos['x'] == 8:
        print("Arrived at Column 8!")
        break
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
else:
    print("Failed to reach Column 8!")

# 4. Walk UP Column 8 to Row 8
print("Step 4: Walking UP Column 8 to Row 8")
for _ in range(20):
    pos = get_pos()
    if pos and pos['y'] == 8:
        print("Arrived at Row 8!")
        break
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
else:
    print("Failed to reach Row 8!")

mgba.take_screenshot()
print("Final Position after script:", get_pos())
