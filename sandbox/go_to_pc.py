import mgba
import time

print("--- WALKING TO PC FROM CURRENT POSITION ---")

def get_pos():
    return mgba.get_coordinates()

# Current position is (6, 3)
# 1. Walk DOWN 1 step to (6, 4)
mgba.press_buttons(["Down"])
time.sleep(0.3)

# 2. Walk RIGHT 7 steps to (13, 4)
for _ in range(7):
    mgba.press_buttons(["Right"])
    time.sleep(0.3)

# 3. Face UP and press A to turn on PC
mgba.press_buttons(["Up", "sleep 100", "A"])
time.sleep(1.0)

print("Current Position:", get_pos())
mgba.take_screenshot()
