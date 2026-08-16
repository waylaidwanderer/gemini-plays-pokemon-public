import mgba
import time

print("--- EXECUTING PHASE 1: SAFARI ZONE CENTER TO AREA 1 (EAST) ---")

def get_pos():
    return mgba.get_coordinates()

# Current position is (15, 25)
# 1. Walk UP 3 steps to (15, 22)
print("Step 1: UP 3 steps")
for _ in range(3):
    mgba.press_buttons(["Up"])
    time.sleep(0.3)

# 2. Walk RIGHT 13 steps to (28, 22)
print("Step 2: RIGHT 13 steps")
for _ in range(13):
    mgba.press_buttons(["Right"])
    time.sleep(0.3)

# 3. Walk UP 12 steps to (28, 10)
print("Step 3: UP 12 steps")
for _ in range(12):
    mgba.press_buttons(["Up"])
    time.sleep(0.3)

# 4. Walk RIGHT 2 steps to transition at (30, 10)
print("Step 4: RIGHT 2 steps to transition")
for _ in range(2):
    mgba.press_buttons(["Right"])
    time.sleep(0.4)

time.sleep(1.5) # Wait for map transition to load
print("Arrived at:", get_pos())
