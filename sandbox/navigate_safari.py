import mgba
import time

print("--- SELF-CORRECTING SAFARI NAVIGATION (PHASE 4 AREA 3 WEST) ---")

def get_pos():
    return mgba.get_coordinates()

# Current position is (26, 0) inside Area 3 (West) facing DOWN.
# 1. Walk DOWN to Row 2
print("Step 1: Walking DOWN to Row 2")
for _ in range(5):
    pos = get_pos()
    if pos and pos['y'] == 2:
        print("Arrived at Row 2!")
        break
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
else:
    print("Failed to reach Row 2!")

# 2. Walk LEFT to Column 25
print("Step 2: Walking LEFT to Column 25")
for _ in range(5):
    pos = get_pos()
    if pos and pos['x'] == 25:
        print("Arrived at Column 25!")
        break
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
else:
    print("Failed to reach Column 25!")

# 3. Walk DOWN Column 25 to Row 18
print("Step 3: Walking DOWN to Row 18")
for _ in range(25):
    pos = get_pos()
    if pos and pos['y'] == 18:
        print("Arrived at Row 18!")
        break
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
else:
    print("Failed to reach Row 18!")

# 4. Walk LEFT to Column 21 on Row 18
print("Step 4: Walking LEFT to Column 21")
for _ in range(10):
    pos = get_pos()
    if pos and pos['x'] == 21:
        print("Arrived at Column 21!")
        break
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
else:
    print("Failed to reach Column 21!")

# 5. Walk DOWN Column 21 to Row 26
print("Step 5: Walking DOWN to Row 26")
for _ in range(15):
    pos = get_pos()
    if pos and pos['y'] == 26:
        print("Arrived at Row 26!")
        break
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
else:
    print("Failed to reach Row 26!")

# 6. Walk LEFT to Column 19 on Row 26 (directly below the teeth!)
print("Step 6: Walking LEFT to Column 19")
for _ in range(5):
    pos = get_pos()
    if pos and pos['x'] == 19:
        print("Arrived at Column 19!")
        break
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
else:
    print("Failed to reach Column 19!")

# 7. Face UP and press A to retrieve the Gold Teeth!
print("Step 7: Facing UP and retrieving Gold Teeth")
mgba.press_buttons(["Up"])
time.sleep(0.4)
mgba.press_buttons(["A"])
time.sleep(1.0)

# Clear any text boxes
mgba.press_buttons(["A"])
time.sleep(0.6)

mgba.take_screenshot()
print("Final Position after script:", get_pos())
