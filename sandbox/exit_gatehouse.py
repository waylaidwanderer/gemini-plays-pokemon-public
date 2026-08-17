import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def press_and_wait(btn):
    mgba.press_buttons([btn])
    time.sleep(0.3)
    return get_pos()

# We start at (12, 2) on Saffron East Gatehouse 1F / Route 15/16/18 Gatehouse 1F West Room
start = get_pos()
print(f"Starting exit path from {start}...")

# 1. Right 2 steps to (14, 2)
curr = start
while curr[0] < 14:
    pos = press_and_wait("Right")
    if pos == curr:
        print(f"Blocked Right at {curr}")
        break
    curr = pos

# 2. Down 3 steps to (14, 5)
while curr[1] < 5:
    pos = press_and_wait("Down")
    if pos == curr:
        print(f"Blocked Down at {curr}")
        break
    curr = pos

# 3. Left 14 steps along Row 5 to (0, 5)
while curr[0] > 0:
    pos = press_and_wait("Left")
    if pos == curr:
        print(f"Blocked Left at {curr}")
        break
    curr = pos

# 4. Try to warp to overworld by walking Left from (0, 5)
print(f"Reached {curr}. Triggering exit warp to the West overworld...")
pos = press_and_wait("Left")
if abs(pos[0] - curr[0]) > 1 or abs(pos[1] - curr[1]) > 1:
    print(f"WARPED! New overworld position: {pos}")
else:
    print(f"Warp failed. Current position: {pos}")
