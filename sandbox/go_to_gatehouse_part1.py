import mgba
import time

print("--- EXECUTING GATEHOUSE PATH PART 1 FROM (3, 16) TO (18, 9) ---")

def get_pos():
    return mgba.get_coordinates()

# Current position is (3, 16) facing LEFT
# 1. Walk DOWN 12 steps to (3, 28)
print("Step 1: DOWN 12 steps")
for _ in range(12):
    mgba.press_buttons(["Down"])
    time.sleep(0.3)

# 2. Walk RIGHT 10 steps to (13, 28)
print("Step 2: RIGHT 10 steps")
for _ in range(10):
    mgba.press_buttons(["Right"])
    time.sleep(0.3)

# 3. Walk UP 14 steps to (13, 14)
print("Step 3: UP 14 steps")
for _ in range(14):
    mgba.press_buttons(["Up"])
    time.sleep(0.3)

# 4. Walk RIGHT 22 steps to (35, 14)
print("Step 4: RIGHT 22 steps")
for _ in range(22):
    mgba.press_buttons(["Right"])
    time.sleep(0.3)

# 5. Walk UP 5 steps to (35, 9)
print("Step 5: UP 5 steps")
for _ in range(5):
    mgba.press_buttons(["Up"])
    time.sleep(0.3)

# 6. Walk LEFT 17 steps to (18, 9)
print("Step 6: LEFT 17 steps")
for _ in range(17):
    mgba.press_buttons(["Left"])
    time.sleep(0.3)

print("Arrived at:", get_pos())
mgba.take_screenshot()
