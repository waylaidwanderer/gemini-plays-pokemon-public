import mgba
import time

print("--- CLERK POSITION TEST ---")

def get_pos():
    return mgba.get_coordinates()

# We start at (3, 3).
# Let's try to walk to (6, 3) facing UP and press A to see if the clerk at (6, 2) talks to us!
print("Walking to (6, 3)...")
for _ in range(3):
    mgba.press_buttons(["Right"])
    time.sleep(0.4)

# Face UP
mgba.press_buttons(["Up"])
time.sleep(0.4)

# Press A
print("Pressing A...")
mgba.press_buttons(["A"])
time.sleep(1.0)

mgba.take_screenshot()
print("Final Position:", get_pos())
