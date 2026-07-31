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

# We start at B3F (2, 9)
print("Start Position (should be (2, 9)):", mgba.get_coordinates())

# 1. Walk to (1, 19)
mgba.press_buttons(["Left"])
wait_for_movement()
print("At (1, 9):", mgba.get_coordinates())

for i in range(10):
    mgba.press_buttons(["Down"])
    wait_for_movement()
print("At (1, 19):", mgba.get_coordinates())

# 2. Walk to (1, 25)
for i in range(6):
    mgba.press_buttons(["Down"])
    wait_for_movement()
print("At (1, 25):", mgba.get_coordinates())

# 3. Walk Right along Row 25 as far as we can!
# We will count steps and print each position.
walked_right = 0
pos = mgba.get_coordinates()
for i in range(25):
    mgba.press_buttons(["Right"])
    p_new = wait_for_movement()
    if p_new == pos:
        print(f"Blocked going Right along Row 25 at: {pos}")
        break
    pos = p_new
    walked_right += 1
    print(f"Row 25 Right step {i+1}: {pos}")

# Let's take a screenshot of where we ended up on Row 25!
screenshot_path = mgba.take_screenshot()
print("Screenshot:", screenshot_path)
