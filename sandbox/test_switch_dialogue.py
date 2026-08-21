import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

# Walk Down to (1, 11) from (1, 10)
mgba.press_buttons(["Down"])
time.sleep(0.5)

print("At:", get_pos(), "Facing Down. Turning Right...")
mgba.press_buttons(["Right"])
time.sleep(0.5)

print("Facing Right at:", get_pos())

# Press A once to open the switch textbox
print("Pressing A...")
mgba.press_buttons(["A"])
time.sleep(2.0)

# Take screenshot to see dialogue
mgba.take_screenshot()
