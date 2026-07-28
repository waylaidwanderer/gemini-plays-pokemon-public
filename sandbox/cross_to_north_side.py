import mgba
import time

def walk_step(direction):
    mgba.press_buttons([direction])
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    return pos

print("Starting cross to north side script...")

# 1. We are at (19, 18). Let's walk Left 4 steps to (15, 18).
print("Walking Left to (15, 18)...")
for i in range(4):
    walk_step("Left")

# 2. Walk Up 2 steps to (15, 16)
print("Walking Up to (15, 16)...")
for i in range(2):
    walk_step("Up")

# 3. Walk Left 15 steps to (0, 16)
print("Walking Left to (0, 16)...")
for i in range(15):
    walk_step("Left")

# 4. Walk Left 1 step to transition to Route 4 at (89, 8)
print("Transitioning to Route 4...")
walk_step("Left")
time.sleep(1.0) # Wait for map load

# 5. Walk Up 4 steps on Route 4 to (89, 4)
print("Walking Up 4 steps on Route 4...")
for i in range(4):
    walk_step("Up")

# 6. Walk Right 1 step to transition to Cerulean City (North side) at (0, 12)
print("Transitioning back to Cerulean City (North side)...")
walk_step("Right")
time.sleep(1.0) # Wait for map load

# 7. Walk Right 20 steps to (20, 12) on the North side
print("Walking Right to (20, 12)...")
for i in range(20):
    walk_step("Right")

# 8. Walk Up 12 steps to (20, 0) to transition to Route 24
print("Walking Up to transition to Route 24...")
for i in range(12):
    walk_step("Up")

time.sleep(1.0) # Wait for map load
pos = mgba.get_coordinates()
print(f"Final coordinates: {pos}")
