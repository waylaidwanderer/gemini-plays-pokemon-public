import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def press_and_wait(btn):
    mgba.press_buttons([btn])
    time.sleep(0.35)
    return get_pos()

# We start on 2F at (1, 3).
curr = get_pos()
print(f"Starting 2F horizontal exploration from {curr}...")

# 1. Walk Up to (1, 2)
curr = press_and_wait("Up")
print(f"Moved UP to {curr}")

# 2. Walk Right up to 20 steps
print("Walking Right along Row 2...")
for i in range(20):
    pos = press_and_wait("Right")
    if pos == curr:
        print(f"Blocked at {curr}")
        break
    curr = pos

print("Exploration complete. Final position:", get_pos())
