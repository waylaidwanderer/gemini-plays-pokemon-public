import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.15)
    return mgba.get_coordinates()

def wait_for_slide(seconds):
    time.sleep(seconds)
    return mgba.get_coordinates()

# Starting at B3F (16, 11)
print("=== STARTING RUN TO B4F GATE ===")
pos = mgba.get_coordinates()
print(f"Start Position: {pos}")

# 1. Walk from B3F (16, 11) to B3F Western maze start (2, 9)
print("\n--- Part 1: Walk to Western Maze Start (2, 9) ---")
# Walk Right 3 to (19, 11)
for i in range(3):
    pos = move(["Right"])
    print(f"Walk Right: {pos}")

# Walk Up 4 to (19, 7)
for i in range(4):
    pos = move(["Up"])
    print(f"Walk Up: {pos}")

# Walk Left 17 to (2, 7)
for i in range(17):
    pos = move(["Left"])
    print(f"Walk Left: {pos}")

# Walk Down 2 to (2, 9)
for i in range(2):
    pos = move(["Down"])
    print(f"Walk Down: {pos}")

# Verify position at start of maze
if pos['x'] != 2 or pos['y'] != 9:
    print(f"WARNING: Unexpected position at start of maze: {pos}")

# 2. Navigate B3F Western maze
print("\n--- Part 2: Navigate B3F Western Maze ---")
# walk_to_spinner
for move_dir in ['Left', 'Up', 'Up', 'Right', 'Right', 'Right']:
    pos = move([move_dir])
    print(f"Walk: {pos}")

# Step onto (4, 16) spinner by pressing Up
print("Stepping onto (4, 16) spinner...")
pos = move(["Up"])
print(f"Step onto spinner: {pos}")
pos = wait_for_slide(3.0)
print(f"Position after first slide: {pos}")

# Walk to (10, 11)
print("Walking to (10, 11)...")
pos = move(["Right"])
print(f"Walk Right: {pos}")
pos = move(["Right"])
print(f"Walk Right: {pos}")

# Walk to (10, 14)
print("Walking to (10, 14)...")
for i in range(3):
    pos = move(["Down"])
    print(f"Walk Down: {pos}")

# Step onto (11, 14) spinner by pressing Right
print("Stepping onto (11, 14) spinner...")
pos = move(["Right"])
print(f"Step onto spinner: {pos}")
pos = wait_for_slide(2.5)
print(f"Position after second slide: {pos}")

# Walk to (14, 18)
print("Walking to (14, 18)...")
pos = move(["Left"])
print(f"Walk Left: {pos}")

# Step onto (13, 18) spinner by pressing Left
print("Stepping onto (13, 18) spinner...")
pos = move(["Left"])
print(f"Step onto spinner: {pos}")
pos = wait_for_slide(2.5)
print(f"Position after third slide: {pos}")

# Walk to (18, 20)
print("Walking to (18, 20)...")
for i in range(7):
    pos = move(["Right"])
    print(f"Walk Right: {pos}")

# Step onto B4F stairs at (18, 19) by pressing Up
print("Stepping onto B4F stairs...")
pos = move(["Up"])
print(f"Position: {pos}")
pos = wait_for_slide(3.0)
print(f"Position after warp to B4F: {pos}")

# 3. Navigate B4F to the gate
print("\n--- Part 3: Navigate B4F to the Gate ---")
pos = move(["Left"])
print(f"Walk Left: {pos}")

for i in range(6):
    pos = move(["Down"])
    print(f"Walk Down: {pos}")

for i in range(6):
    pos = move(["Right"])
    print(f"Walk Right: {pos}")

for i in range(8):
    pos = move(["Up"])
    print(f"Walk Up: {pos}")

# 4. Use Lift Key to open the gate
print("\n--- Part 4: Open B4F Gate ---")
print("Pressing A to use Lift Key...")
# Wait for dialog and text box to appear
mgba.press_buttons(["A"])
time.sleep(1.0)
mgba.press_buttons(["A"])
time.sleep(1.0)

pos = mgba.get_coordinates()
print(f"Final Position: {pos}")
scr = mgba.take_screenshot()
print(f"Screenshot taken: {scr}")
print("=== RUN COMPLETED SUCCESSFULLY ===")
