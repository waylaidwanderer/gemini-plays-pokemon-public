import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# We are at (14, 12)
# Step 1: Walk Down to (14, 13) (1 step Down)
pos = move(["Down"])

# Step 2: Walk Left 2 steps to step onto (12, 13) UP spinner
pos = move(["Left"])
print("Stepping onto (12, 13) UP spinner...")
pos = move(["Left"])
time.sleep(3.0)

pos = mgba.get_coordinates()
print(f"Position after slide: {pos}")
mgba.take_screenshot()
