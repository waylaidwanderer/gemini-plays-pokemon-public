import mgba
import time

print("--- EXECUTING PERFECT PATH TO SAFARI ZONE CENTER VIA CUT ---")

def get_pos():
    return mgba.get_coordinates()

# Current position is (20, 16) in Fuchsia City facing LEFT
# 1. Walk to (24, 16): RIGHT 4 steps
print("Step 1: RIGHT 4 steps")
for _ in range(4):
    mgba.press_buttons(["Right"])
    time.sleep(0.3)

# 2. Walk to (24, 21): DOWN 5 steps
print("Step 2: DOWN 5 steps")
for _ in range(5):
    mgba.press_buttons(["Down"])
    time.sleep(0.3)

# 3. Walk to (26, 21): RIGHT 2 steps
print("Step 3: RIGHT 2 steps")
for _ in range(2):
    mgba.press_buttons(["Right"])
    time.sleep(0.3)

# 4. Walk to (26, 14): UP 7 steps
print("Step 4: UP 7 steps")
for _ in range(7):
    mgba.press_buttons(["Up"])
    time.sleep(0.3)

# Verify position at (26, 14) facing UP
print("Position before CUT:", get_pos())

# 5. Use CUT on the bush at (26, 13)
print("Using CUT on the bush...")
mgba.press_buttons(["Start", "sleep 500"])

# Select POKEMON (second option)
mgba.press_buttons(["Down", "sleep 100", "A", "sleep 600"])

# Select TRUFFLE (first slot)
mgba.press_buttons(["A", "sleep 500"])

# Select CUT (second option in submenu: DIG, CUT, STATS, CANCEL)
mgba.press_buttons(["Down", "sleep 100", "A", "sleep 3000"]) # wait for CUT animation

# Clear dialogue box
mgba.press_buttons(["A", "sleep 500"])

# 6. Walk to (26, 9): UP 5 steps
print("Step 6: UP 5 steps")
for _ in range(5):
    mgba.press_buttons(["Up"])
    time.sleep(0.3)

# 7. Walk to (18, 9): LEFT 8 steps
print("Step 7: LEFT 8 steps")
for _ in range(8):
    mgba.press_buttons(["Left"])
    time.sleep(0.3)

# 8. Walk RIGHT to Column 37 (Row 7 bypass)
print("Step 8: RIGHT 19 steps to Column 37")
for _ in range(19):
    mgba.press_buttons(["Right"])
    time.sleep(0.3)

# 9. Walk UP to Row 2
print("Step 9: UP 7 steps to Row 2")
for _ in range(7):
    mgba.press_buttons(["Up"])
    time.sleep(0.3)

# 10. Walk LEFT to Column 22
print("Step 10: LEFT 15 steps to Column 22")
for _ in range(15):
    mgba.press_buttons(["Left"])
    time.sleep(0.3)

# 11. Walk DOWN to Row 4
print("Step 11: DOWN 2 steps to Row 4")
for _ in range(2):
    mgba.press_buttons(["Down"])
    time.sleep(0.3)

# 12. Walk LEFT to Column 18
print("Step 12: LEFT 4 steps to Column 18")
for _ in range(4):
    mgba.press_buttons(["Left"])
    time.sleep(0.3)

# 13. Enter Gatehouse
print("Step 13: UP 2 steps to enter Gatehouse")
for _ in range(2):
    mgba.press_buttons(["Up"])
    time.sleep(0.4)

time.sleep(1.5) # Wait for Gatehouse to load
print("Position inside Gatehouse:", get_pos())
mgba.take_screenshot()
