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

# We start at B3F (20, 13)
print("Start Position:", mgba.get_coordinates())

# Let's test stepping on all candidates near the right side!
# First, walk Left to column 19
print("Walking to column 19...")
mgba.press_buttons(["Left"])
pos = wait_for_movement()
print(f"Position: {pos}")

# Test (19, 12) (Up from (19, 13))
print("Testing (19, 12) by walking Up...")
mgba.press_buttons(["Up"])
pos = wait_for_movement()
print(f"Position after Up: {pos}")

# If we didn't warp, walk Down to (19, 14) and (19, 15)
if pos['y'] != 18: # assuming we don't warp
    print("Walking Down column 19...")
    mgba.press_buttons(["Down", "Down"])
    pos = wait_for_movement()
    print(f"Position: {pos}")

# Let's try walking to (21, 14): Right 2
print("Testing column 21 row 14...")
mgba.press_buttons(["Right", "Right"])
pos = wait_for_movement()
print(f"Position: {pos}")

# Let's walk to column 24 row 15 (which is the stairs in some guides!)
print("Walking to (24, 15)...")
current_pos = mgba.get_coordinates()
dx = 24 - current_pos['x']
dy = 15 - current_pos['y']
buttons = []
if dx > 0:
    buttons += ["Right"] * dx
elif dx < 0:
    buttons += ["Left"] * abs(dx)
if dy > 0:
    buttons += ["Down"] * dy
elif dy < 0:
    buttons += ["Up"] * abs(dy)

mgba.press_buttons(buttons)
pos = wait_for_movement()
print(f"Position at (24, 15): {pos}")

# Take a screenshot to inspect
screenshot_path = mgba.take_screenshot()
print(f"Screenshot taken: {screenshot_path}")
