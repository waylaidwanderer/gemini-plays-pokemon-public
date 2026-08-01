import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

print("Starting systematic descent on B3F...")
# We are at (12, 16)

# Step 1: Walk to Column 9
move(["Left", "Left", "Left"])

# Step 2: Walk Down to Row 19
move(["Down", "Down", "Down"])

# Step 3: Step Right onto (10, 19) RIGHT spinner -> spins Right, then Up to (14, 18)
print("Stepping onto (10, 19) RIGHT spinner...")
move(["Right", "sleep 3000"])

# Step 4: Step Right onto (15, 18) DOWN spinner -> spins Down
print("Stepping onto (15, 18) DOWN spinner...")
move(["Right", "sleep 3000"])

final_pos = mgba.get_coordinates()
print("Final position after descent sequence:", final_pos)
screenshot_file = mgba.take_screenshot()
print("Saved screenshot to:", screenshot_file)
