import mgba
import time

print("--- CONTINUING PHASE 1 FROM (22, 22) AFTER BATTLE ---")

def get_pos():
    return mgba.get_coordinates()

# 1. Clear "Got away safely!" text
print("Clearing battle text...")
mgba.press_buttons(["B", "sleep 500"])

# 2. Walk RIGHT 6 steps to (28, 22)
print("Step 1: RIGHT 6 steps")
for _ in range(6):
    mgba.press_buttons(["Right"])
    time.sleep(0.3)

# 3. Walk UP 12 steps to (28, 10)
print("Step 2: UP 12 steps")
for _ in range(12):
    mgba.press_buttons(["Up"])
    time.sleep(0.3)

# 4. Walk RIGHT 2 steps to transition at (30, 10)
print("Step 3: RIGHT 2 steps to transition")
for _ in range(2):
    mgba.press_buttons(["Right"])
    time.sleep(0.4)

time.sleep(1.5) # Wait for map transition to load
print("Arrived at:", get_pos())
