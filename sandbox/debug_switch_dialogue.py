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

print("Moving to (2, 12)...")
pos = get_pos()
if pos == (1, 10):
    step("Down")
    step("Down")
    step("Right")
elif pos == (2, 12):
    pass
else:
    print("Warning: unexpected starting position", pos)

print("Facing UP...")
mgba.press_buttons(["Up"])
time.sleep(1.0)

# Press A once
print("Pressing A (1)...")
mgba.press_buttons(["A"])
time.sleep(1.2)
scr1 = mgba.take_screenshot()
print("Saved screenshot 1:", scr1)

# Press A twice
print("Pressing A (2)...")
mgba.press_buttons(["A"])
time.sleep(1.2)
scr2 = mgba.take_screenshot()
print("Saved screenshot 2:", scr2)

# Press A three times
print("Pressing A (3)...")
mgba.press_buttons(["A"])
time.sleep(1.2)
scr3 = mgba.take_screenshot()
print("Saved screenshot 3:", scr3)

# Press A four times
print("Pressing A (4)...")
mgba.press_buttons(["A"])
time.sleep(1.2)
scr4 = mgba.take_screenshot()
print("Saved screenshot 4:", scr4)

# Press A five times
print("Pressing A (5)...")
mgba.press_buttons(["A"])
time.sleep(1.2)
scr5 = mgba.take_screenshot()
print("Saved screenshot 5:", scr5)

print("Final position:", get_pos())
