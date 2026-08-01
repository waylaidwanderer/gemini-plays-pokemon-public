import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

# Starting at (14, 15)
print("Starting sequence to B3F from (14, 15)...")

# Step 1: Walk to (15, 15), then Down onto (15, 16) DOWN spinner -> slides to (15, 18)
move(["Right", "Down", "sleep 2000"])

# Step 2: Step Left, Left onto (13, 18) LEFT spinner -> slides to (11, 20)
move(["Left", "Left", "sleep 2000"])

# Step 3: From (11, 20) stopper, walk to (14, 22)
move(["Right", "Right", "Right", "Down", "Down"])

# Step 4: Step Left onto (13, 22) LEFT spinner -> slides to (9, 24)
move(["Left", "sleep 2000"])

# Step 5: Walk Left to (8, 24) and step Up onto (8, 23) UP spinner -> slides to (2, 19)
move(["Left", "Up", "sleep 2000"])

# Step 6: From (2, 19) stopper, walk Left to (1, 19) and Up, Up, Up, Up to (1, 15)
move(["Left", "Up", "Up", "Up", "Up"])

# Step 7: Walk Right, Right to (3, 15), and Up to (3, 14)
move(["Right", "Right", "Up"])

# Step 8: Step Right onto (4, 14) DOWN spinner. 
# This slides us Down onto the (4, 15) stairs, warping us to B3F!
print("Stepping onto (4, 14) DOWN spinner to warp...")
move(["Right", "sleep 2500"])

# Final check of coordinates after warp
final_pos = mgba.get_coordinates()
print("Final position after warp sequence:", final_pos)
