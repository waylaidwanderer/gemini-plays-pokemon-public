import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def press_and_wait(btn):
    mgba.press_buttons([btn])
    time.sleep(0.35)
    return get_pos()

# We start at (6, 2)
curr = get_pos()
print(f"Starting bypass routing to Route 8 from {curr}...")

# 1. Walk Down 1 step to (6, 3)
curr = press_and_wait("Down")
print(f"Moved Down to {curr}")

# 2. Walk Right 5 steps to (11, 3)
while curr[0] < 11:
    pos = press_and_wait("Right")
    if pos == curr:
        print(f"Blocked Right at {curr}")
        break
    curr = pos
print(f"Reached {curr}")

# 3. Walk Up 1 step to (11, 2)
curr = press_and_wait("Up")
print(f"Moved Up to {curr}")

# 4. Walk Right to Column 19
while curr[0] < 19:
    pos = press_and_wait("Right")
    if pos == curr:
        print(f"Blocked Right at {curr}")
        break
    curr = pos
print(f"Reached Column 19 at {curr}")

# 5. Try to exit warp by walking Right
print("Testing exit warp to Route 8 from (19, 2)...")
pos = press_and_wait("Right")
if abs(pos[0] - curr[0]) > 1 or abs(pos[1] - curr[1]) > 1:
    print(f"WARPED! New overworld position: {pos}")
else:
    print(f"Warp failed. Current position: {pos}")
