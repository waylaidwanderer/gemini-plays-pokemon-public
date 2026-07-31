import mgba
import time

def wait_for_movement():
    p1 = mgba.get_coordinates()
    time.sleep(0.1)
    p2 = mgba.get_coordinates()
    while p1 != p2:
        p1 = p2
        time.sleep(0.1)
        p2 = mgba.get_coordinates()
    return p1

# 1. We are at B3F (23, 15). Walk to (2, 9) on B3F
print("Start Position:", mgba.get_coordinates())
print("Navigating to left side...")

buttons = ["Up", "Left", "Left", "Up", "Up", "Up", "Left", "Left", "Left", "Left", "Left"]
mgba.press_buttons(buttons)
pos = wait_for_movement()
print(f"Landed at: {pos}")

# 2. From (2, 9), let's explore column 1, 2, 3 on rows 7, 8, 9, 10
# (1, 7) to (3, 7) are open
print("Exploring top-left room...")
mgba.press_buttons(["Right", "Up", "Up", "Left", "Left"])
pos = wait_for_movement()
print(f"Position: {pos}")

# From (1, 7), walk Down column 1 as far as possible
print("Walking Down column 1...")
for i in range(8):
    mgba.press_buttons(["Down"])
    pos = wait_for_movement()
    print(f"  Step {i+1} Down -> Position: {pos}")
    if pos['x'] != 1:
         break

# From current position, walk to column 3 and go Down as far as possible
print("Walking to column 3 and going Down...")
mgba.press_buttons(["Right", "Right"])
pos = wait_for_movement()
print(f"Position at column 3: {pos}")

for i in range(8):
    mgba.press_buttons(["Down"])
    pos = wait_for_movement()
    print(f"  Step {i+1} Down -> Position: {pos}")
    if pos['y'] == 14: # blocked
         break

# Take a screenshot
screenshot_path = mgba.take_screenshot()
print(f"Screenshot: {screenshot_path}")
