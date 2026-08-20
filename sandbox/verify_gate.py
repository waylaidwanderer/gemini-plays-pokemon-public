import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

print("Testing gate at (20, 5) from:", get_pos())

# We are at (21, 6). Let's step Left to (20, 6)
mgba.press_buttons(["Left"])
time.sleep(0.5)
print("Pos after Left:", get_pos())

# Try to step Up to (20, 5)
mgba.press_buttons(["Up"])
time.sleep(0.5)
print("Pos after Up:", get_pos())

mgba.take_screenshot()
