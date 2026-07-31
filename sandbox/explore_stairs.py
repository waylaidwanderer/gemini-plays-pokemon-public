import mgba
import time

def wait_for_movement():
    p1 = mgba.get_coordinates()
    time.sleep(0.12)
    p2 = mgba.get_coordinates()
    while p1 != p2:
        p1 = p2
        time.sleep(0.12)
        p2 = mgba.get_coordinates()
    return p1

# We are currently at (22, 13) in the Right Room
print("Start Position:", mgba.get_coordinates())

# Let's walk back to the Left Room via (18, 11) gap
path_back = ["Left", "Left", "Left", "Up", "Up", "Left", "Left"]
for idx, move in enumerate(path_back):
    mgba.press_buttons([move])
    pos = wait_for_movement()
    print(f"Step {idx+1} ({move}):", pos)

# We should be in the Left Room around (17, 11).
# Now, let's walk down to the bottom area of the Left Room (Row 24, 25)
# Let's see: from (17, 11), can we walk Left or Down?
# Let's walk Left and Down to reach (1, 24) or (1, 25) which we know is walkable!
# Wait, can we walk Down Column 17 or Column 16?
# No, let's walk back to the start stopper (2, 9) or (8, 11).
# Actually, let's see where we end up and print the position!
screenshot_path = mgba.take_screenshot()
print("Screenshot:", screenshot_path)
