import mgba
import time

print("--- EXECUTING PERFECT PATH TO SAFARI ZONE CENTER ---")

def get_pos():
    return mgba.get_coordinates()

# Current position is (24, 21) in Fuchsia City
# 1. Walk UP 7 steps to (24, 14)
print("Step 1: UP 7 steps")
for _ in range(7):
    mgba.press_buttons(["Up"])
    time.sleep(0.3)

# 2. Walk RIGHT 11 steps to (35, 14)
print("Step 2: RIGHT 11 steps")
for _ in range(11):
    mgba.press_buttons(["Right"])
    time.sleep(0.3)

# 3. Walk UP 5 steps to (35, 9)
print("Step 3: UP 5 steps")
for _ in range(5):
    mgba.press_buttons(["Up"])
    time.sleep(0.3)

# 4. Walk LEFT 17 steps to (18, 9)
print("Step 4: LEFT 17 steps")
for _ in range(17):
    mgba.press_buttons(["Left"])
    time.sleep(0.3)

# 5. Walk RIGHT to Column 37 (Row 7 bypass)
print("Step 5: RIGHT 19 steps to Column 37")
for _ in range(19):
    mgba.press_buttons(["Right"])
    time.sleep(0.3)

# 6. Walk UP to Row 2
print("Step 6: UP 7 steps to Row 2")
for _ in range(7):
    mgba.press_buttons(["Up"])
    time.sleep(0.3)

# 7. Walk LEFT to Column 22
print("Step 7: LEFT 15 steps to Column 22")
for _ in range(15):
    mgba.press_buttons(["Left"])
    time.sleep(0.3)

# 8. Walk DOWN to Row 4
print("Step 8: DOWN 2 steps to Row 4")
for _ in range(2):
    mgba.press_buttons(["Down"])
    time.sleep(0.3)

# 9. Walk LEFT to Column 18
print("Step 9: LEFT 4 steps to Column 18")
for _ in range(4):
    mgba.press_buttons(["Left"])
    time.sleep(0.3)

# 10. Enter Gatehouse
print("Step 10: UP 2 steps to enter Gatehouse")
for _ in range(2):
    mgba.press_buttons(["Up"])
    time.sleep(0.4)

time.sleep(1.5) # Wait for Gatehouse to load
print("Position inside Gatehouse:", get_pos())
mgba.take_screenshot()
