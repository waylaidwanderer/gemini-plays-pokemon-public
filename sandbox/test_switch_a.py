import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

print("Testing single A press from:", get_pos())

# Press A
mgba.press_buttons(["A"])
time.sleep(0.5)

# Take screenshot to see if dialogue opened
screenshot_file = mgba.take_screenshot()
print("Screenshot taken after A:", screenshot_file)
