import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# We are at (2, 9) on B3F
# Step 1: Walk to (4, 14)
print("Walking to (4, 14)...")
pos = move(["Right"]) # to (3, 9)
for _ in range(4):
    pos = move(["Down"]) # to (3, 13)
pos = move(["Right"]) # to (4, 13)
pos = move(["Down"]) # to (4, 14)

# Step 2: Step Right onto (5, 14) RIGHT spinner -> slides to (9, 16)
print("Stepping onto (5, 14) RIGHT spinner...")
pos = move(["Right"])
time.sleep(3.0)

pos = mgba.get_coordinates()
print(f"Position at (9, 16) stopper: {pos}")

# Step 3: Walk Right 2 steps onto (11, 16) RIGHT spinner -> slides to (15, 18)
print("Walking to (11, 16) RIGHT spinner...")
pos = move(["Right"])
pos = move(["Right"])
time.sleep(3.0)

pos = mgba.get_coordinates()
print(f"Position at (15, 18) stopper: {pos}")

# Step 4: Walk Down 2 to (15, 20), Right 4 to (19, 20), and Up 2 onto B4F stairs at (19, 18)
print("Walking to B4F stairs via Row 20...")
for _ in range(2):
    pos = move(["Down"])
for _ in range(4):
    pos = move(["Right"])
pos = move(["Up"])
pos = move(["Up"])
time.sleep(1.0)

pos = mgba.get_coordinates()
print(f"Final position: {pos}")
mgba.take_screenshot()
