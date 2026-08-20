import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

print("Initial pos:", get_pos())

# Press Right to go to (16, 7)
mgba.press_buttons(["Right"])
time.sleep(0.5)
print("After Right:", get_pos())

# Press Down to try to go to (16, 8)
mgba.press_buttons(["Down"])
time.sleep(0.5)
print("After Down:", get_pos())

# Press Down to try to go to (16, 9)
mgba.press_buttons(["Down"])
time.sleep(0.5)
print("After second Down:", get_pos())

# Take screenshot
mgba.take_screenshot()
