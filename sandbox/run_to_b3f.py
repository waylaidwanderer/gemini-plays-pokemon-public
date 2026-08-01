import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    # The emulator runs during press_buttons, including any sleep elements we pass.
    # We retrieve coordinates immediately after.
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

# Starting at (15, 18)
print("Starting sequence to get to B3F...")

# Step 1: Step Left, Left onto (13, 18) LEFT spinner -> slides to (11, 20)
move(["Left", "Left", "sleep 1000"])

# Step 2: From (11, 20) stopper, walk to (14, 22) and step Left onto (13, 22) LEFT spinner -> slides to (9, 24)
move(["Right", "Right", "Right", "Down", "Down"])
move(["Left", "sleep 1000"])

# Step 3: From (9, 24) stopper, walk Left to (8, 24) and step Up onto (8, 23) UP spinner -> slides to (2, 19)
move(["Left"])
move(["Up", "sleep 1000"])

# Step 4: From (2, 19) stopper, walk Left to (1, 19)
move(["Left"])

# Step 5: Walk Up, Up, Up, Up to (1, 15)
move(["Up", "Up", "Up", "Up"])

# Step 6: Walk Right, Right to (3, 15), and Up to (3, 14)
move(["Right", "Right"])
move(["Up"])

# Step 7: Step Right onto (4, 14) DOWN spinner. 
# This slides us Down onto the (4, 15) stairs going Down, warping us to B3F!
print("Stepping onto (4, 14) DOWN spinner...")
move(["Right", "sleep 1500"])

# Final check of coordinates after warp
final_pos = mgba.get_coordinates()
print("Final position after warp sequence:", final_pos)
