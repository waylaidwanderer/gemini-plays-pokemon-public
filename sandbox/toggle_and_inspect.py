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
    new_pos = get_pos()
    print(f"Stepped {direction}: {old_pos} -> {new_pos}")
    return new_pos

print("Start position:", get_pos())

# 1. Walk to (2, 12)
step("Down")
step("Down")
step("Right")

# 2. Face UP
mgba.press_buttons(["Up"])
time.sleep(1.0)

# 3. Press A once
print("Pressing A 1...")
mgba.press_buttons(["A"])
time.sleep(1.5)
scr1 = mgba.take_screenshot()
print("Screenshot 1:", scr1)

# 4. Press A twice
print("Pressing A 2...")
mgba.press_buttons(["A"])
time.sleep(1.5)
scr2 = mgba.take_screenshot()
print("Screenshot 2:", scr2)

# 5. Press A thrice
print("Pressing A 3...")
mgba.press_buttons(["A"])
time.sleep(1.5)
scr3 = mgba.take_screenshot()
print("Screenshot 3:", scr3)

# 6. Press A 4 times
print("Pressing A 4...")
mgba.press_buttons(["A"])
time.sleep(1.5)
scr4 = mgba.take_screenshot()
print("Screenshot 4:", scr4)

# 7. Press A 5 times (just in case!)
print("Pressing A 5...")
mgba.press_buttons(["A"])
time.sleep(1.5)
scr5 = mgba.take_screenshot()
print("Screenshot 5:", scr5)

# 8. Try to walk Left to (1, 12)
p_left = step("Left")

# 9. Try to walk Up Column 1
if p_left == (1, 12):
    step("Up") # to (1, 11)
    step("Up") # to (1, 10)
    step("Up") # to (1, 9) - gate!
    step("Up") # to (1, 8)

print("Final position:", get_pos())
mgba.take_screenshot()
