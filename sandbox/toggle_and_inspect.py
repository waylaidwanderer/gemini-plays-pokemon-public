import mgba
import time
from PIL import Image

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def step(direction):
    old_pos = get_pos()
    mgba.press_buttons([direction])
    time.sleep(0.45)
    new_pos = get_pos()
    return new_pos

print("Start position:", get_pos())

# 1. Walk to (2, 12) from (1, 10)
if get_pos() == (1, 10):
    step("Down")
    step("Down")
    step("Right")

# 2. Turn UP
mgba.press_buttons(["Up"])
time.sleep(0.5)

# Take 6 screenshots to capture the entire switch interaction flow!
for i in range(6):
    print(f"Pressing A (step {i+1})...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    sf = mgba.take_screenshot()
    print(f"Captured: {sf}")

# Let's check where we end up
print("End position:", get_pos())
