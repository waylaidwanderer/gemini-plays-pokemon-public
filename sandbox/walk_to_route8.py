import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def press_and_wait(btn):
    mgba.press_buttons([btn])
    time.sleep(0.35)
    return get_pos()

# Let's execute the precise, verified path to exit Saffron East Gatehouse 1F to Route 8
print("Starting exit pathing from (1, 2) to Route 8...")
curr = get_pos()

# Step 1: Down 3 steps to (1, 5)
for _ in range(3):
    curr = press_and_wait("Down")
print(f"Reached Row 5 at {curr}")

# Step 2: Right 13 steps along Row 5 to (14, 5)
while curr[0] < 14:
    pos = press_and_wait("Right")
    if pos == curr:
        print(f"Blocked at {curr}")
        break
    curr = pos
print(f"Reached Column 14 at {curr}")

# Step 3: Up 1 step to (14, 4)
curr = press_and_wait("Up")
print(f"Moved Up to {curr}")

# Step 4: Right 5 steps along Row 4 to Column 19
while curr[0] < 19:
    pos = press_and_wait("Right")
    if pos == curr:
        print(f"Blocked at {curr}")
        break
    curr = pos
print(f"Reached Column 19 at {curr}")

# Step 5: Right 1 step to trigger exit warp to Route 8
print("Triggering exit warp to Route 8...")
pos = press_and_wait("Right")
if abs(pos[0] - curr[0]) > 1 or abs(pos[1] - curr[1]) > 1:
    print(f"WARPED! New overworld position: {pos}")
else:
    print(f"Warp failed. Current position: {pos}")
