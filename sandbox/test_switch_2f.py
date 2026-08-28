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

# 1. Walk to (2, 12) on 2F West from (5, 8)
step("Down") # to (5, 9)
step("Down") # to (5, 10)
step("Down") # to (5, 11)
step("Left") # to (4, 11)
step("Left") # to (3, 11)
step("Down") # to (3, 12)
step("Left") # to (2, 12)

# 2. Turn UP to face statue at (2, 11)
print("Turning UP...")
mgba.press_buttons(["Up"])
time.sleep(0.5)

# 3. Press A to check for switch dialogue
print("Pressing A...")
mgba.press_buttons(["A"])
time.sleep(1.0)
mgba.take_screenshot()

print("Interaction complete! Current position:", get_pos())
