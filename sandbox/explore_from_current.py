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

# We are at (2, 9)
print("Start Position:", mgba.get_coordinates())

# Let's walk Down Column 2 and see how far we can go!
print("Walking Down Column 2...")
for i in range(1, 18):
    mgba.press_buttons(["Down"])
    pos = wait_for_movement()
    print(f"Step {i} Down: {pos}")

# Let's see if we can walk Right or Down further to find the boundaries of Column 15.
# Let's walk to Column 14 at the deepest Row we reached!
pos = mgba.get_coordinates()
deepest_row = pos['y']
print(f"Deepest row reached on Column 2: {deepest_row}")

# Try to walk Right to Column 14
print("Walking Right to Column 14...")
for i in range(1, 14):
    mgba.press_buttons(["Right"])
    pos = wait_for_movement()
    print(f"Step {i} Right: {pos}")

# From our current position, let's try walking Down to see how deep we can go on each Column!
# Let's try to go Down as far as possible
print("Trying to go Down further...")
for i in range(1, 8):
    mgba.press_buttons(["Down"])
    pos = wait_for_movement()
    print(f"Step {i} Down: {pos}")

# Take a screenshot to visualize
screenshot_path = mgba.take_screenshot()
print("Screenshot:", screenshot_path)
