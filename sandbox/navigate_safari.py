import mgba
import time

print("--- SELF-CORRECTING SAFARI NAVIGATION (PHASE 3 AREA 2 NORTH) ---")

def get_pos():
    return mgba.get_coordinates()

# Current position is (39, 31) in Area 2 (North) facing LEFT.
# 1. Walk Left to Column 22 on Row 31: (22, 31)
print("Step 1: Walking Left to Column 22")
for _ in range(25):
    pos = get_pos()
    if pos and pos['x'] == 22:
        print("Arrived at Column 22!")
        break
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
else:
    print("Failed to reach Column 22!")

# 2. Walk UP to Row 22 on Column 22: (22, 22) (climbing stairs at (22, 23))
print("Step 2: Walking UP to Row 22 (climbing stairs)")
for _ in range(15):
    pos = get_pos()
    if pos and pos['y'] == 22:
        print("Arrived at Row 22!")
        break
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
else:
    print("Failed to reach Row 22!")

# 3. Walk Left to Column 16 on Row 22: (16, 22)
print("Step 3: Walking Left to Column 16")
for _ in range(10):
    pos = get_pos()
    if pos and pos['x'] == 16:
        print("Arrived at Column 16!")
        break
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
else:
    print("Failed to reach Column 16!")

# 4. Walk Down to Row 28 on Column 16: (16, 28) (descending stairs at (16, 27))
print("Step 4: Walking Down to Row 28 (descending stairs)")
for _ in range(10):
    pos = get_pos()
    if pos and pos['y'] == 28:
        print("Arrived at Row 28!")
        break
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
else:
    print("Failed to reach Row 28!")

# 5. Walk Left to Column 12 on Row 28: (12, 28)
print("Step 5: Walking Left to Column 12")
for _ in range(10):
    pos = get_pos()
    if pos and pos['x'] == 12:
        print("Arrived at Column 12!")
        break
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
else:
    print("Failed to reach Column 12!")

# 6. Walk Down to Row 30 on Column 12: (12, 30) (bypassing pond)
print("Step 6: Walking Down to Row 30")
for _ in range(5):
    pos = get_pos()
    if pos and pos['y'] == 30:
        print("Arrived at Row 30!")
        break
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
else:
    print("Failed to reach Row 30!")

# 7. Walk Left to Column 8 on Row 30: (8, 30)
print("Step 7: Walking Left to Column 8")
for _ in range(10):
    pos = get_pos()
    if pos and pos['x'] == 8:
        print("Arrived at Column 8!")
        break
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
else:
    print("Failed to reach Column 8!")

# 8. Walk Down Column 8 to Row 34: (8, 34) (just above transition to verify!)
print("Step 8: Walking Down Column 8 to Row 34")
for _ in range(10):
    pos = get_pos()
    if pos and pos['y'] == 34:
        print("Arrived at Row 34! Stopping to verify transition points!")
        break
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
else:
    print("Failed to reach Row 34!")

mgba.take_screenshot()
print("Final Position before verification:", get_pos())
