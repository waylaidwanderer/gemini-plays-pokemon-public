import mgba
import time
from PIL import Image

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def step(direction):
    old_pos = get_pos()
    mgba.press_buttons([direction])
    time.sleep(0.55)
    return get_pos()

print("Current position:", get_pos())

# 1. Walk to switch standing position (2, 12)
# Currently at (3, 10)
print("Walking to switch standing position...")
step("Down") # to (3, 11)
step("Down") # to (3, 12)
step("Left") # to (2, 12)

print("Facing UP...")
mgba.press_buttons(["Up"])
time.sleep(1.0)

# 2. Press A once
print("Pressing A (1)...")
mgba.press_buttons(["A"])
time.sleep(1.5)
scr1 = mgba.take_screenshot()
print("Saved screenshot 1:", scr1)

# Press A twice
print("Pressing A (2)...")
mgba.press_buttons(["A"])
time.sleep(1.5)
scr2 = mgba.take_screenshot()
print("Saved screenshot 2:", scr2)

# Press A three times
print("Pressing A (3)...")
mgba.press_buttons(["A"])
time.sleep(1.5)
scr3 = mgba.take_screenshot()
print("Saved screenshot 3:", scr3)

# Press A four times
print("Pressing A (4)...")
mgba.press_buttons(["A"])
time.sleep(1.5)
scr4 = mgba.take_screenshot()
print("Saved screenshot 4:", scr4)

# Walk back to Column 3 Row 10
print("Walking to (3, 10)...")
step("Down") # to (2, 13)
step("Right") # to (3, 13)
step("Right") # to (4, 13)
step("Up") # to (4, 12)
step("Up") # to (4, 11)
step("Left") # to (3, 11)
step("Up") # to (3, 10)

print("Testing Column 3 Row 9...")
mgba.press_buttons(["Up"])
time.sleep(0.55)
print("Final Position:", get_pos())
mgba.take_screenshot()
