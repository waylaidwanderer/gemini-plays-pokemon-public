import mgba
import time

print("--- CUT BUSH AND WALK TO (26, 9) ---")

def get_pos():
    return mgba.get_coordinates()

# Current position is (25, 16) facing RIGHT
# 1. Walk LEFT 1 step to (24, 16)
print("Step 1: LEFT 1 step")
mgba.press_buttons(["Left"])
time.sleep(0.3)

# 2. Walk DOWN 11 steps to (24, 27)
print("Step 2: DOWN 11 steps")
for _ in range(11):
    mgba.press_buttons(["Down"])
    time.sleep(0.3)

# 3. Walk RIGHT 2 steps to (26, 27) (through the gap at 25, 27)
print("Step 3: RIGHT 2 steps")
for _ in range(2):
    mgba.press_buttons(["Right"])
    time.sleep(0.3)

# 4. Walk UP 13 steps to (26, 14)
print("Step 4: UP 13 steps")
for _ in range(13):
    mgba.press_buttons(["Up"])
    time.sleep(0.3)

print("Position before CUT:", get_pos())

# 5. Use CUT on the bush at (26, 13)
print("Using CUT on the bush...")
mgba.press_buttons(["Start", "sleep 500"])

# Select POKEMON (second option)
mgba.press_buttons(["Down", "sleep 100", "A", "sleep 600"])

# Select TRUFFLE (first slot)
mgba.press_buttons(["A", "sleep 500"])

# Select CUT (second option in submenu)
mgba.press_buttons(["Down", "sleep 100", "A", "sleep 3000"]) # wait for CUT animation

# Clear dialogue box
mgba.press_buttons(["A", "sleep 500"])

# 6. Walk UP 5 steps to (26, 9)
print("Step 6: UP 5 steps through the cut bush")
for _ in range(5):
    mgba.press_buttons(["Up"])
    time.sleep(0.3)

print("Arrived at:", get_pos())
mgba.take_screenshot()
