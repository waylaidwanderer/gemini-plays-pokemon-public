import mgba
import time

def walk_step(direction):
    mgba.press_buttons([direction])
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    return pos

print("Starting walk to Route 24 script...")

# 1. We are at (27, 9). Walk Left 1 step to (26, 9)
print("Walking Left to (26, 9)...")
walk_step("Left")

# 2. Walk Down 3 steps to (26, 12)
print("Walking Down to (26, 12)...")
for i in range(3):
    walk_step("Down")

# 3. Walk Left 6 steps to (20, 12)
print("Walking Left to (20, 12)...")
for i in range(6):
    walk_step("Left")

# 4. Walk Up 12 steps to transition to Route 24
print("Walking Up to transition to Route 24...")
for i in range(12):
    walk_step("Up")

time.sleep(1.0) # Wait for map load
pos = mgba.get_coordinates()
print(f"Final coordinates: {pos}")
