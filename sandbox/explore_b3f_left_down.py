import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

print("Starting Left Room descent test on B3F...")
# We are at (10, 9)

# Step 1: Walk to (13, 11)
move(["Right", "Right", "Right"])
move(["Down", "Down"])

# Step 2: Step Left onto (12, 11) LEFT spinner -> slides to (10, 11)
print("Stepping onto (12, 11) LEFT spinner...")
move(["Left", "sleep 2000"])

# Step 3: Walk to (10, 12)
move(["Down"])

# Step 4: Step Down onto (10, 13) RIGHT spinner -> slides to (14, 13)
print("Stepping onto (10, 13) RIGHT spinner...")
move(["Down", "sleep 2000"])

final_pos = mgba.get_coordinates()
print("Final position after first phase:", final_pos)
screenshot_file = mgba.take_screenshot()
print("Saved screenshot to:", screenshot_file)
