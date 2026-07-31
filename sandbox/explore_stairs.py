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

# We are currently at (28, 15)
print("Start Position:", mgba.get_coordinates())

# Walk to the staircase at (27, 8)
path_to_27_8 = ["Up", "Up", "Up", "Up", "Up", "Up", "Left", "Up"]
for idx, move in enumerate(path_to_27_8):
    mgba.press_buttons([move])
    pos = wait_for_movement()
    print(f"Step {idx+1} ({move}):", pos)

# We should have stepped onto (27, 8) staircase!
# Let's wait for any potential map transition
time.sleep(3.0)
pos_final = wait_for_movement()
print("Landed at Position:", pos_final)

# Take screenshot to verify where we warped
screenshot_path = mgba.take_screenshot()
print("Final Screenshot:", screenshot_path)
