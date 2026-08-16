import mgba
import time

print("--- WALKING TO PC IN POKEMON CENTER ---")

def get_pos():
    return mgba.get_coordinates()

# Current position is (3, 7) (doormat)
# 1. Walk RIGHT 10 steps to (13, 7)
print("Step 1: RIGHT 10 steps")
for _ in range(10):
    mgba.press_buttons(["Right"])
    time.sleep(0.3)

# 2. Walk UP 3 steps to (13, 4)
print("Step 2: UP 3 steps")
for _ in range(3):
    mgba.press_buttons(["Up"])
    time.sleep(0.3)

# 3. Face UP and press A to turn on PC
print("Turning on PC...")
mgba.press_buttons(["Up", "sleep 100", "A"])
time.sleep(1.0)

print("Current Position:", get_pos())
mgba.take_screenshot()
