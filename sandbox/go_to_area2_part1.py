import mgba
import time

print("--- EXECUTING PHASE 2 PART 1: AREA 1 (EAST) TO PLATEAU DESCENT (12, 22) ---")

def get_pos():
    return mgba.get_coordinates()

# Current position is (5, 21)
# 1. Walk DOWN 3 steps to (5, 24)
print("Step 1: DOWN 3 steps")
for _ in range(3):
    mgba.press_buttons(["Down"])
    time.sleep(0.3)

# 2. Walk RIGHT 15 steps to (20, 24)
print("Step 2: RIGHT 15 steps")
for _ in range(15):
    mgba.press_buttons(["Right"])
    time.sleep(0.3)

# 3. Walk UP 4 steps (climb stairs to 20, 20)
print("Step 3: UP 4 steps")
for _ in range(4):
    mgba.press_buttons(["Up"])
    time.sleep(0.3)

# 4. Walk LEFT 8 steps to (12, 20)
print("Step 4: LEFT 8 steps")
for _ in range(8):
    mgba.press_buttons(["Left"])
    time.sleep(0.3)

# 5. Walk DOWN 2 steps (descend stairs to 12, 22)
print("Step 5: DOWN 2 steps")
for _ in range(2):
    mgba.press_buttons(["Down"])
    time.sleep(0.3)

time.sleep(0.5)
print("Arrived at:", get_pos())
