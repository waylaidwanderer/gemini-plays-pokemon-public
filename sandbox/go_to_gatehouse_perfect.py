import mgba
import time

print("--- EXECUTING PERFECT 61-STEP PATH TO SAFARI ZONE ---")

def get_pos():
    return mgba.get_coordinates()

# Current position is (25, 26) in Fuchsia City facing UP
# 1. Walk LEFT 1 step to (24, 26)
print("Step 1: LEFT 1 step")
mgba.press_buttons(["Left"])
time.sleep(0.3)

# 2. Walk UP 12 steps to (24, 14)
print("Step 2: UP 12 steps")
for _ in range(12):
    mgba.press_buttons(["Up"])
    time.sleep(0.3)

# 3. Walk RIGHT 11 steps to (35, 14)
print("Step 3: RIGHT 11 steps")
for _ in range(11):
    mgba.press_buttons(["Right"])
    time.sleep(0.3)

# 4. Walk UP 5 steps to (35, 9)
print("Step 4: UP 5 steps")
for _ in range(5):
    mgba.press_buttons(["Up"])
    time.sleep(0.3)

# 5. Walk RIGHT 2 steps to (37, 9) (Bypassing the 36-step redundant detour!)
print("Step 5: RIGHT 2 steps to Column 37")
for _ in range(2):
    mgba.press_buttons(["Right"])
    time.sleep(0.3)

# 6. Walk UP 7 steps to Row 2
print("Step 6: UP 7 steps to Row 2")
for _ in range(7):
    mgba.press_buttons(["Up"])
    time.sleep(0.3)

# 7. Walk LEFT 15 steps to Column 22
print("Step 7: LEFT 15 steps to Column 22")
for _ in range(15):
    mgba.press_buttons(["Left"])
    time.sleep(0.3)

# 8. Walk DOWN 2 steps to Row 4
print("Step 8: DOWN 2 steps to Row 4")
for _ in range(2):
    mgba.press_buttons(["Down"])
    time.sleep(0.3)

# 9. Walk LEFT 4 steps to Column 18
print("Step 9: LEFT 4 steps to Column 18")
for _ in range(4):
    mgba.press_buttons(["Left"])
    time.sleep(0.3)

# 10. Enter Gatehouse (UP 2 steps)
print("Step 10: UP 2 steps to enter Gatehouse")
for _ in range(2):
    mgba.press_buttons(["Up"])
    time.sleep(0.4)

time.sleep(1.5) # Wait for Gatehouse to load
print("Position inside Gatehouse:", get_pos())
mgba.take_screenshot()
