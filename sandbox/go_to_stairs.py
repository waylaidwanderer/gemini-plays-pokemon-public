import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at left area: {pos}")

# We are at (2, 9)
# Step 1: Walk Right to (3, 9) (1 step Right)
pos = move(["Right"])

# Step 2: Walk Down to (3, 14) (5 steps Down)
print("Walking down Column 3...")
for _ in range(5):
    pos = move(["Down"])

# Step 3: Walk Right 6 steps to step onto (9, 14) DOWN spinner
print("Walking right to Column 9 to step onto DOWN spinner...")
for _ in range(6):
    pos = move(["Right"])

# Wait for slide to (9, 16) stopper
time.sleep(2.0)
pos = mgba.get_coordinates()
print(f"Position after first slide: {pos}")

# Step 4: Walk Right 2 steps to step onto (11, 16) RIGHT spinner
print("Walking right 2 steps to step onto (11, 16) RIGHT spinner...")
pos = move(["Right"])
pos = move(["Right"])

# Wait for slide to land
time.sleep(3.0)
pos = mgba.get_coordinates()
print(f"Final position after slide maze: {pos}")
mgba.take_screenshot()
