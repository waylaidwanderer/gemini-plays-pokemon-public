import mgba
import time

print("--- WALKING TO PC IN POKEMON CENTER (SAFE ROUTE) ---")

def get_pos():
    return mgba.get_coordinates()

# Current position is (3, 7) (doormat)
# 1. Walk UP 2 steps to (3, 5)
print("Step 1: UP 2 steps")
for _ in range(2):
    mgba.press_buttons(["Up"])
    time.sleep(0.3)

# 2. Walk RIGHT 10 steps to (13, 5)
print("Step 2: RIGHT 10 steps")
for _ in range(10):
    mgba.press_buttons(["Right"])
    time.sleep(0.3)

# 3. Walk UP 1 step to (13, 4)
print("Step 3: UP 1 step")
mgba.press_buttons(["Up"])
time.sleep(0.3)

# 4. Face UP and press A to turn on PC
print("Turning on PC...")
mgba.press_buttons(["Up", "sleep 100", "A"])
time.sleep(1.0)

print("Current Position:", get_pos())
mgba.take_screenshot()
