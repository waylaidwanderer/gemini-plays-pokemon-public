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

# We are at (19, 15) on B3F
print("Start Position:", mgba.get_coordinates())

# Let's explore the area to the right!
# We can walk to (20, 15), (21, 15), (22, 15), (23, 15), (24, 15), etc.
# Let's systematically walk Right until we hit a wall.
print("Walking Right...")
for i in range(1, 10):
    mgba.press_buttons(["Right"])
    pos = wait_for_movement()
    print(f"Step {i} Right: {pos}")

# Now let's try walking Up 5 steps
print("Walking Up...")
for i in range(1, 6):
    mgba.press_buttons(["Up"])
    pos = wait_for_movement()
    print(f"Step {i} Up: {pos}")

# Now let's try walking Right more if possible
print("Walking Right...")
for i in range(1, 5):
    mgba.press_buttons(["Right"])
    pos = wait_for_movement()
    print(f"Step {i} Right: {pos}")

# Let's take a screenshot to see where we ended up!
screenshot_path = mgba.take_screenshot()
print("Screenshot after exploring right/up:", screenshot_path)
