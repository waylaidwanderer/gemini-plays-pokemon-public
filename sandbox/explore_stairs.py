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

# We are currently at (17, 13)
print("Start Position:", mgba.get_coordinates())

# 1. Walk to (24, 15)
path_to_24_15 = ["Right", "Right", "Right", "Right", "Right", "Down", "Right", "Down", "Right"]
for idx, move in enumerate(path_to_24_15):
    mgba.press_buttons([move])
    pos = wait_for_movement()
    print(f"To 24_15 Step {idx+1} ({move}):", pos)

# 2. From (24, 15), let's walk Up as much as possible!
print("At (24, 15). Trying to walk Up...")
pos = mgba.get_coordinates()
for i in range(10):
    mgba.press_buttons(["Up"])
    p_new = wait_for_movement()
    if p_new == pos:
        print(f"Blocked going Up at: {pos}")
        break
    pos = p_new
    print(f"Up step {i+1}: {pos}")

# 3. From furthest Up in Column 24, let's test if we can walk Right or Left to explore Columns 25-28!
print("From furthest Up in Column 24, exploring Right...")
for i in range(5):
    mgba.press_buttons(["Right"])
    p_new = wait_for_movement()
    if p_new == pos:
        print(f"Blocked going Right at: {pos}")
        break
    pos = p_new
    print(f"Right step {i+1}: {pos}")

# Take a screenshot of the far-right room
screenshot_path = mgba.take_screenshot()
print("Screenshot:", screenshot_path)
