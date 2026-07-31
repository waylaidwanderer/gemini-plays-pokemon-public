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

# We are at (16, 13) on B3F
print("Start Position:", mgba.get_coordinates())

# 1. Walk Right 9 steps to (25, 13)
print("Walking to (25, 13)...")
for _ in range(9):
    mgba.press_buttons(["Right"])
    wait_for_movement()
print("At:", mgba.get_coordinates())

# 2. Walk Up 5 steps to (25, 8)
print("Walking to (25, 8)...")
for _ in range(5):
    mgba.press_buttons(["Up"])
    wait_for_movement()
print("At:", mgba.get_coordinates())

# 3. Walk Right 2 steps to (27, 8)
print("Walking to (27, 8)...")
for _ in range(2):
    mgba.press_buttons(["Right"])
    wait_for_movement()
print("At:", mgba.get_coordinates())

# 4. Step Up/Down onto stairs at (27, 8) -> should warp to B2F!
# Some stairs warp when you walk Up onto them, others just by stepping.
# Let's try walking Up.
print("Stepping onto stairs...")
mgba.press_buttons(["Up"])
time.sleep(3.0) # wait for map transition
pos = wait_for_movement()
print("Position after stepping onto stairs:", pos)

# Take screenshot
screenshot_path = mgba.take_screenshot()
print("Screenshot:", screenshot_path)
