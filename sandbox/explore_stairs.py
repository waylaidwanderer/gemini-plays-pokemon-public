import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

# Starting at (27, 11)
print("Starting Row 7 bypass path test on B3F...")

# Step 1: Walk UP 4 steps to (27, 7)
move(["Up", "Up", "Up", "Up"])

# Step 2: Walk Left 7 steps to (20, 7) (passing Column 21 wall!)
move(["Left", "Left", "Left", "Left", "Left", "Left", "Left"])

# Step 3: Walk Down 4 steps to (20, 11)
move(["Down", "Down", "Down", "Down"])

# Step 4: Walk Left 2 steps to (18, 11) (entering the Left Room!)
move(["Left", "Left"])

# Step 5: Walk Down to (18, 15) stairs!
move(["Down", "Down", "Down", "Down"])

print("Final position after exploration:", mgba.get_coordinates())
