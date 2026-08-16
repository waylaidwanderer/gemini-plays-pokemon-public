import mgba
import time

print("--- REBUILT CUT BUSH AND WALK TO POKEMON CENTER ---")

def get_pos():
    return mgba.get_coordinates()

# Current position is (26, 14) facing UP.
# 1. Use CUT on the bush at (26, 13)
print("Using CUT on the bush...")
mgba.press_buttons(["Start"])
time.sleep(0.6)

# Select POKEMON (second option)
mgba.press_buttons(["Down", "sleep 100", "A"])
time.sleep(1.0)

# Select TRUFFLE (first slot)
mgba.press_buttons(["A"])
time.sleep(1.0)

# Select CUT (second option in submenu: DIG, CUT, STATS, CANCEL)
mgba.press_buttons(["Down", "sleep 100", "A"])
time.sleep(3.0) # wait for CUT animation

# Clear dialogue box
mgba.press_buttons(["A"])
time.sleep(1.0)

# 2. Walk Up 12 steps to Row 2: (26, 2)
print("Step 2: Walking Up Column 26 to Row 2")
for _ in range(12):
    mgba.press_buttons(["Up"])
    time.sleep(0.35)
time.sleep(1.0)
print("Position:", get_pos())

# 3. Walk Left 13 steps along Row 2 to Column 13: (13, 2)
print("Step 3: Walking Left to Column 13")
for _ in range(13):
    mgba.press_buttons(["Left"])
    time.sleep(0.35)
time.sleep(1.0)
print("Position:", get_pos())

# 4. Walk Down 12 steps along Column 13 to Row 14: (13, 14)
print("Step 4: Walking Down to Row 14")
for _ in range(12):
    mgba.press_buttons(["Down"])
    time.sleep(0.35)
time.sleep(1.0)
print("Position:", get_pos())

# 5. Walk Left 12 steps to Column 1: (1, 14)
print("Step 5: Walking Left to Column 1")
for _ in range(12):
    mgba.press_buttons(["Left"])
    time.sleep(0.35)
time.sleep(1.0)
print("Position:", get_pos())

# 6. Walk Down 18 steps along Column 1 to Row 32: (1, 32)
print("Step 6: Walking Down to Row 32")
for _ in range(18):
    mgba.press_buttons(["Down"])
    time.sleep(0.35)
time.sleep(1.0)
print("Position:", get_pos())

# 7. Walk Right 7 steps along Row 32 to Column 8: (8, 32)
print("Step 7: Walking Right to (8, 32)")
for _ in range(7):
    mgba.press_buttons(["Right"])
    time.sleep(0.35)
time.sleep(1.0)
print("Position:", get_pos())

# 8. Walk Up 4 steps along Column 8 to Row 28: (8, 28)
print("Step 8: Walking Up to (8, 28)")
for _ in range(4):
    mgba.press_buttons(["Up"])
    time.sleep(0.35)
time.sleep(1.0)
print("Position:", get_pos())

# 9. Walk Right 11 steps along Row 28 to Column 19: (19, 28)
print("Step 9: Walking Right to (19, 28)")
for _ in range(11):
    mgba.press_buttons(["Right"])
    time.sleep(0.35)
time.sleep(1.0)
print("Position:", get_pos())

# 10. Walk Up 1 step to enter Pokémon Center (19, 27)
print("Step 10: Entering Pokémon Center...")
mgba.press_buttons(["Up"])
time.sleep(2.0) # wait for transition

print("Final Position inside PC:", get_pos())
mgba.take_screenshot()
