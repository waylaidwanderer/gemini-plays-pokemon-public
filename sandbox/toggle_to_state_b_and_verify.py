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

# 1. We are already at (2, 12) facing UP. Let's make sure we face UP.
mgba.press_buttons(["Up"])
time.sleep(0.5)

# 2. Toggle the switch to State B (exactly 4 A presses!)
print("Toggling Mewtwo switch...")
for i in range(4):
    print(f"Pressing A {i+1}/4...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
print("Switch toggled!")

# 3. Step Left to (1, 12)
step("Left")

# 4. Walk UP Column 1 to verify gate is open
print("Walking UP Column 1 to verify...")
step("Up") # to (1, 11)
step("Up") # to (1, 10)
final_p = step("Up") # to (1, 9)

if final_p == (1, 9):
    print("SUCCESS: Gate is open! State B is active!")
    # Walk the rest of the way UP to Row 6 to complete the crossing!
    step("Up") # to (1, 8)
    step("Up") # to (1, 7)
    step("Up") # to (1, 6)
else:
    print("FAILED: Gate is still closed! State A is still active.")

mgba.take_screenshot()
