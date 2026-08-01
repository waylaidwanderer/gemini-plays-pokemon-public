import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(1.0)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, current position: {pos}")
    return pos

# Starting at (2, 9)
# Step 1: Walk to (3, 11)
move(["Right", "Down", "Down"])

# Step 2: Step onto (4, 11) RIGHT spinner
pos = move(["Right"])

# Let's see what coordinates we are at now!
print("Final position after spin:", pos)
