import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

print("Starting Row 18 spinner sequence down to bottom B3F...")
# We are at (9, 9)

# Step 1: Walk Down to (9, 18)
move(["Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down"])

# Step 2: Walk Right to (10, 18)
move(["Right"])

# Step 3: Step Right onto (11, 18) RIGHT spinner -> slides to (14, 18)
print("Stepping onto (11, 18) RIGHT spinner...")
move(["Right", "sleep 3000"])

# Step 4: Step Right onto (15, 18) DOWN spinner -> slides Down
print("Stepping onto (15, 18) DOWN spinner...")
move(["Right", "sleep 3000"])

final_pos = mgba.get_coordinates()
print("Final position after descent sequence:", final_pos)
screenshot_file = mgba.take_screenshot()
print("Saved screenshot to:", screenshot_file)
