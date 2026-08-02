import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# We are at (4, 13)
# Step 1: Walk Down to (4, 14)
pos = move(["Down"])

# Step 2: Walk Right to (5, 14) (RIGHT spinner) -> slides us to (9, 16)
pos = move(["Right"])
time.sleep(2.0)
pos = mgba.get_coordinates()
print(f"After first slide: {pos}")

# Step 3: Walk Right 2 steps to step onto (11, 16) RIGHT spinner -> slides us to (15, 17/18)
pos = move(["Right"])
pos = move(["Right"])
time.sleep(3.0)
pos = mgba.get_coordinates()
print(f"After second slide: {pos}")
mgba.take_screenshot()
