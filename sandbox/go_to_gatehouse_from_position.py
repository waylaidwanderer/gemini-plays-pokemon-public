import mgba
import time

print("--- EXECUTING PERFECT 73-STEP PATH TO SAFARI ZONE ---")

def get_pos():
    return mgba.get_coordinates()

# Current position is (24, 21) in Fuchsia City facing DOWN
# 1. Walk DOWN 9 steps to (24, 30)
print("Step 1: DOWN 9 steps")
for _ in range(9):
    mgba.press_buttons(["Down"])
    time.sleep(0.3)

# 2. Walk RIGHT 11 steps to (35, 30) (through the fence gap at 25, 30)
print("Step 2: RIGHT 11 steps")
for _ in range(11):
    mgba.press_buttons(["Right"])
    time.sleep(0.3)

# 3. Walk UP 21 steps to (35, 9)
print("Step 3: UP 21 steps")
for _ in range(21):
    mgba.press_buttons(["Up"])
    time.sleep(0.3)

# 4. Walk RIGHT 2 steps to (37, 9)
print("Step 4: RIGHT 2 steps")
for _ in range(2):
    mgba.press_buttons(["Right"])
    time.sleep(0.3)

# 5. Walk UP 7 steps to Row 2
print("Step 5: UP 7 steps to Row 2")
for _ in range(7):
    mgba.press_buttons(["Up"])
    time.sleep(0.3)

# 6. Walk LEFT 15 steps to Column 22
print("Step 6: LEFT 15 steps to Column 22")
for _ in range(15):
    mgba.press_buttons(["Left"])
    time.sleep(0.3)

# 7. Walk DOWN 2 steps to Row 4
print("Step 7: DOWN 2 steps to Row 4")
for _ in range(2):
    mgba.press_buttons(["Down"])
    time.sleep(0.3)

# 8. Walk LEFT 4 steps to Column 18
print("Step 8: LEFT 4 steps to Column 18")
for _ in range(4):
    mgba.press_buttons(["Left"])
    time.sleep(0.3)

# 9. Enter Gatehouse (UP 2 steps)
print("Step 9: UP 2 steps to enter Gatehouse")
for _ in range(2):
    mgba.press_buttons(["Up"])
    time.sleep(0.4)

time.sleep(1.5) # Wait for Gatehouse to load
print("Position inside Gatehouse:", get_pos())
mgba.take_screenshot()
