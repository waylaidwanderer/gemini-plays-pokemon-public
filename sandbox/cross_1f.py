import mgba
import time

# We are at (5, 8) on 2F West.
# Let's walk DOWN Column 5 to see if we warp to 1F West!
path = ["Down", "Down", "Down", "Down", "Down"]

print("Walking DOWN Column 5 to find 1F warp...")
for idx, direction in enumerate(path):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.3)
    pos_after = mgba.get_coordinates()
    print(f"Step {idx} ({direction}): {pos_before} -> {pos_after}")
    if pos_before == pos_after:
        print(f"Blocked at {pos_before}")
        break
    # If we warped (large coordinate change), stop!
    if abs(pos_before['x'] - pos_after['x']) > 2 or abs(pos_before['y'] - pos_after['y']) > 2:
        print("WARPED!")
        break

print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
