import mgba
import time

print("--- EXECUTING GATEHOUSE PATH PART 1 FROM (19, 28) TO (18, 9) ---")

def get_pos():
    return mgba.get_coordinates()

# Current position is (19, 28) facing UP
# 1. Walk LEFT 11 steps to (8, 28)
print("Step 1: LEFT 11 steps")
for _ in range(11):
    mgba.press_buttons(["Left"])
    time.sleep(0.3)

# 2. Walk DOWN 4 steps to (8, 32)
print("Step 2: DOWN 4 steps")
for _ in range(4):
    mgba.press_buttons(["Down"])
    time.sleep(0.3)

# 3. Walk LEFT 7 steps to (1, 32)
print("Step 3: LEFT 7 steps")
for _ in range(7):
    mgba.press_buttons(["Left"])
    time.sleep(0.3)

# 4. Walk UP 18 steps to (1, 14)
print("Step 4: UP 18 steps")
for _ in range(18):
    mgba.press_buttons(["Up"])
    time.sleep(0.3)

# 5. Walk RIGHT 12 steps to (13, 14)
print("Step 5: RIGHT 12 steps")
for _ in range(12):
    mgba.press_buttons(["Right"])
    time.sleep(0.3)

# 6. Walk UP 5 steps to (13, 9)
print("Step 6: UP 5 steps")
for _ in range(5):
    mgba.press_buttons(["Up"])
    time.sleep(0.3)

# 7. Walk RIGHT 5 steps to (18, 9)
print("Step 7: RIGHT 5 steps")
for _ in range(5):
    mgba.press_buttons(["Right"])
    time.sleep(0.3)

print("Arrived at:", get_pos())
mgba.take_screenshot()
