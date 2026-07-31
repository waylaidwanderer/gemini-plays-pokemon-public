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

# We start at (3, 19)
print("Start Position:", mgba.get_coordinates())

# Move Left 2
mgba.press_buttons(["Left", "Left"])
pos = wait_for_movement()
print("After Left 2:", pos)

# Move Down 5 (or until we hit the bottom wall)
for i in range(5):
    mgba.press_buttons(["Down"])
    pos = wait_for_movement()
    print(f"After Down {i+1}:", pos)

# Let's take a screenshot to inspect current layout at the bottom
mgba.take_screenshot()
