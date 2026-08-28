import mgba
import time
from PIL import Image

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def step(direction):
    old_pos = get_pos()
    print(f"Current: {old_pos}. Stepping {direction}...")
    mgba.press_buttons([direction])
    time.sleep(0.45)
    new_pos = get_pos()
    print(f"New position: {new_pos}")
    return new_pos

print("Start position:", get_pos())

# 1. Walk to (10, 11) from (5, 8)
step("Down")
step("Down")
step("Down")
step("Right")
step("Right")
step("Right")
step("Right")
step("Right")

# 2. Try to walk UP Column 10 to Row 3
print("Testing walking UP Column 10...")
p1 = step("Up") # to (10, 10)
p2 = step("Up") # to (10, 9)
p3 = step("Up") # to (10, 8)
p4 = step("Up") # to (10, 7)
p5 = step("Up") # to (10, 6)
p6 = step("Up") # to (10, 5)
p7 = step("Up") # to (10, 4)
p8 = step("Up") # to (10, 3)

time.sleep(1.0)
print("Final position:", get_pos())
mgba.take_screenshot()
