import mgba
import time

def wait_for_movement():
    p1 = mgba.get_coordinates()
    time.sleep(0.15)
    p2 = mgba.get_coordinates()
    while p1 != p2:
        p1 = p2
        time.sleep(0.15)
        p2 = mgba.get_coordinates()
    return p1

# We are at (2, 9) on B3F
print("Start Position:", mgba.get_coordinates())

# 1. Walk to (3, 13)
print("Walking to (3, 13)...")
mgba.press_buttons(["Right", "Down", "Down", "Down", "Down"])
wait_for_movement()
print("At:", mgba.get_coordinates())

# 2. Walk to (4, 14)
print("Walking to (4, 14)...")
mgba.press_buttons(["Right", "Down"])
wait_for_movement()
print("At:", mgba.get_coordinates())

# 3. Step Down onto (4, 15) RIGHT spinner -> slides to (8, 15)
print("Stepping onto (4, 15) spinner...")
mgba.press_buttons(["Down"])
time.sleep(3.0) # Let slide finish
pos = wait_for_movement()
print("Landed at:", pos)

# 4. Try walking Down systematically from (8, 15) to see how far Down we can go!
print("Walking Down from Column 8...")
for i in range(1, 10):
    mgba.press_buttons(["Down"])
    pos = wait_for_movement()
    print(f"Step {i} Down: {pos}")

# Let's see where we are
pos = mgba.get_coordinates()
print("Current position after walking Down:", pos)

# Let's test walking Right to find where Column 15 is, or walking Left to see if there is a path!
if pos['y'] > 15:
    print("Testing horizontal walking on Row:", pos['y'])
    # Try walking Left up to 7 steps
    print("Testing walking Left...")
    for i in range(1, 8):
        mgba.press_buttons(["Left"])
        p_test = wait_for_movement()
        print(f"Step {i} Left: {p_test}")
        
    # Walk back to Column 8
    pos_now = mgba.get_coordinates()
    dx = 8 - pos_now['x']
    move_dir = "Right" if dx > 0 else "Left"
    for _ in range(abs(dx)):
        mgba.press_buttons([move_dir])
        wait_for_movement()
        
    # Try walking Right up to 10 steps to see if we can go past Column 15!
    print("Testing walking Right...")
    for i in range(1, 11):
        mgba.press_buttons(["Right"])
        p_test = wait_for_movement()
        print(f"Step {i} Right: {p_test}")

# Take screenshot
screenshot_path = mgba.take_screenshot()
print("Screenshot:", screenshot_path)
