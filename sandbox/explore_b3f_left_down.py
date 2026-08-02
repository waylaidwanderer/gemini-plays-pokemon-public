import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

print("Executing correct B3F descent sequence...")
# We are at (16, 11)

# Step 1: Walk Down to (16, 12)
move(["Down"])

# Step 2: Step Right onto (17, 12) DOWN spinner -> slides to (17, 16) stopper
print("Stepping onto (17, 12) DOWN spinner...")
move(["Right", "sleep 2500"])

# Step 3: Walk Left all the way to Column 9 on Row 16 (9, 16)
move(["Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left"])

# Step 4: Walk Down to (9, 18)
move(["Down", "Down"])

# Step 5: Walk Right to (10, 18)
move(["Right"])

# Step 6: Step Right onto (11, 18) RIGHT spinner -> slides to (14, 18)
print("Stepping onto (11, 18) RIGHT spinner...")
move(["Right", "sleep 2500"])

# Step 7: Step Right onto (15, 18) DOWN spinner -> slides Down
print("Stepping onto (15, 18) DOWN spinner...")
move(["Right", "sleep 2500"])

final_pos = mgba.get_coordinates()
print("Final position after sliding down:", final_pos)
screenshot_file = mgba.take_screenshot()
print("Saved screenshot to:", screenshot_file)
