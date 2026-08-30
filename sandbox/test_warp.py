import mgba
import time

def step_strict(direction, target_x, target_y):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos_after = mgba.get_coordinates()
    
    if pos_before != pos_after and (abs(pos_after['x'] - pos_before['x']) > 5 or abs(pos_after['y'] - pos_before['y']) > 5):
        print(f"WARPED! From {pos_before} to {pos_after}")
        return "WARPED"
    if pos_after['x'] == target_x and pos_after['y'] == target_y:
        return "SUCCESS"
    if pos_before == pos_after:
        return "BLOCKED"
    return "SUCCESS"

# We are at (22, 2). Let's test the surrounding tiles of (22, 1) to find the warp DOWN to 2F!
print("Testing UP to (22, 1)...")
res = step_strict("Up", 22, 1)
if res == "WARPED":
    exit()

print("Testing UP to (22, 0)...")
res = step_strict("Up", 22, 0)
if res == "WARPED":
    exit()

print("Testing LEFT to (21, 1)...")
res = step_strict("Left", 21, 1)
if res == "WARPED":
    exit()

# Go back to (22, 1)
step_strict("Right", 22, 1)

print("Testing RIGHT to (23, 1)...")
res = step_strict("Right", 23, 1)
if res == "WARPED":
    exit()
