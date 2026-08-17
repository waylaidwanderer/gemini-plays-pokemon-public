import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def press_and_wait(btn):
    mgba.press_buttons([btn])
    time.sleep(0.3)
    return get_pos()

# We start at (19, 2).
# Walk back to the stairs at (1, 1).
curr = get_pos()
print(f"Walking back to stairs from {curr}...")

# 1. Left 4 steps to (15, 2)
while curr[0] > 15:
    pos = press_and_wait("Left")
    if pos == curr:
        print(f"Blocked at {curr}")
        break
    curr = pos

# 2. Down 3 steps to (15, 5)
while curr[1] < 5:
    pos = press_and_wait("Down")
    if pos == curr:
        print(f"Blocked at {curr}")
        break
    curr = pos

# 3. Left 14 steps to (1, 5)
while curr[0] > 1:
    pos = press_and_wait("Left")
    if pos == curr:
        print(f"Blocked at {curr}")
        break
    curr = pos

# 4. Up 3 steps to (1, 2)
while curr[1] > 2:
    pos = press_and_wait("Up")
    if pos == curr:
        print(f"Blocked at {curr}")
        break
    curr = pos

print("Reached stairs landing at:", get_pos())
