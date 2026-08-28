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

# 1. Walk from (1, 10) to (2, 12)
if get_pos() == (1, 10):
    step("Down")
    step("Down")
    step("Right")

# 2. Turn UP to face switch at (2, 11)
print("Turning UP...")
mgba.press_buttons(["Up"])
time.sleep(0.5)

# 3. Press A exactly 5 times with 1.0s delay to fully toggle and close dialogue!
print("Toggling Mewtwo switch with 5 A-presses...")
for i in range(5):
    print(f"Pressing A {i+1}/5...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
print("Switch toggled!")

# 4. Walk to (1, 12)
step("Left")

# 5. Walk UP Column 1 to Row 6
print("Walking UP Column 1...")
step("Up") # to (1, 11)
step("Up") # to (1, 10)
final_p = step("Up") # to (1, 9)

if final_p == (1, 9):
    print("SUCCESS: Gate is open! State B is active!")
    step("Up") # to (1, 8)
    step("Up") # to (1, 7)
    step("Up") # to (1, 6)
else:
    print("FAILED: Gate is still closed! State A is still active.")

mgba.take_screenshot()
