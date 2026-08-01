import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

# Starting at (22, 17)
print("Testing path Down and Left on B3F...")

# Step 1: Walk Down 4 steps to (22, 21)
move(["Down", "Down", "Down", "Down"])

# Step 2: Try to walk Left through Column 21
pos = move(["Left"])

print("Current coordinates:", pos)
