import mgba
import time

def wait_for_movement():
    p1 = mgba.get_coordinates()
    time.sleep(0.15)
    p2 = mgba.get_coordinates()
    while p1 != p2:
        p1 = p2
        time.sleep(0.15)
        p2 = mgba.get_coordinates()
    return p1

# We are at (24, 15) on B3F
print("Start Position:", mgba.get_coordinates())

# 1. Walk to (19, 15)
print("Walking Left to (19, 15)...")
for _ in range(5):
    mgba.press_buttons(["Left"])
    wait_for_movement()
print("At:", mgba.get_coordinates())

# 2. Walk Up to (19, 13)
print("Walking Up to (19, 13)...")
for _ in range(2):
    mgba.press_buttons(["Up"])
    wait_for_movement()
print("At:", mgba.get_coordinates())

# 3. Walk Left to (16, 13) stopper
print("Walking Left to (16, 13)...")
for _ in range(3):
    mgba.press_buttons(["Left"])
    wait_for_movement()
print("At (16, 13) stopper:", mgba.get_coordinates())

# 4. Now, let's explore walking Left into the Left Room from (16, 13) stopper.
# Let's walk Left 5 steps to see if we can reach the Left Room!
print("Walking Left from (16, 13)...")
for i in range(1, 6):
    mgba.press_buttons(["Left"])
    pos = wait_for_movement()
    print(f"Step {i} Left: {pos}")

# Let's see where we are
pos = mgba.get_coordinates()
print("Position after walking Left:", pos)

# Take screenshot
screenshot_path = mgba.take_screenshot()
print("Screenshot:", screenshot_path)
