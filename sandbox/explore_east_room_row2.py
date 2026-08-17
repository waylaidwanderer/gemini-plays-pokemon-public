import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def press_and_wait(btn):
    mgba.press_buttons([btn])
    time.sleep(0.35)
    return get_pos()

# We start at (19, 5).
# Path: Walk Left to Column 15, Up to Row 2, Right to Column 19.
curr = get_pos()
print(f"Starting Row 2 exit exploration from {curr}...")

# Walk Left 4 steps to (15, 5)
while curr[0] > 15:
    pos = press_and_wait("Left")
    if pos == curr:
        print(f"Blocked Left at {curr}")
        break
    curr = pos
print(f"Reached {curr}")

# Walk Up 3 steps to (15, 2)
while curr[1] > 2:
    pos = press_and_wait("Up")
    if pos == curr:
        print(f"Blocked Up at {curr}")
        break
    curr = pos
print(f"Reached {curr}")

# Walk Right 4 steps to (19, 2)
while curr[0] < 19:
    pos = press_and_wait("Right")
    if pos == curr:
        print(f"Blocked Right at {curr}")
        break
    curr = pos
print(f"Reached {curr}")

# Try to warp by walking Right again
print("Testing exit warp from (19, 2)...")
pos = press_and_wait("Right")
if abs(pos[0] - curr[0]) > 1 or abs(pos[1] - curr[1]) > 1:
    print(f"WARPED from Row 2! New position: {pos}")
else:
    print(f"Warp failed. Current position: {pos}")
