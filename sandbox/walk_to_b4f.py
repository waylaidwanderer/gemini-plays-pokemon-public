import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.15)
    return mgba.get_coordinates()

def wait_for_slide(seconds):
    time.sleep(seconds)
    return mgba.get_coordinates()

# Starting at B3F (2, 19)
print("=== STARTING B3F WESTERN MAZE TO B4F GATE SEQUENCE ===")
pos = mgba.get_coordinates()
print(f"Start Position: {pos}")

# 1. Walk from (2, 19) to (2, 17)
print("\n--- Part 1: Walk to (2, 17) ---")
pos = move(["Left"]) # (1, 19)
print(f"Walk Left: {pos}")

pos = move(["Up"]) # (1, 18)
print(f"Walk Up: {pos}")

pos = move(["Up"]) # (1, 17)
print(f"Walk Up: {pos}")

pos = move(["Right"]) # (2, 17)
print(f"Walk Right: {pos}")

if pos['x'] != 2 or pos['y'] != 17:
    print(f"ERROR: Expected (2, 17), got {pos}")
    exit(1)

# 2. Navigate B3F Western maze from (2, 17)
print("\n--- Part 2: Navigate B3F Western Maze ---")
# walk_to_spinner
for move_dir in ['Left', 'Up', 'Up', 'Right', 'Right', 'Right']:
    pos = move([move_dir])
    print(f"Walk: {pos}")

# Step onto (4, 16) spinner by pressing Up (wait, from 4, 15, pressing Up? Let's see)
print("Pressing Up to step onto spinner...")
pos = move(["Up"])
print(f"Position: {pos}")
pos = wait_for_slide(3.0)
print(f"Position after first slide: {pos}")

# Now walk to (10, 11)
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
mgba.press_buttons(["A"])
time.sleep(1.0)
mgba.press_buttons(["A"])
time.sleep(1.0)

pos = mgba.get_coordinates()
print(f"Final Position: {pos}")
scr = mgba.take_screenshot()
print(f"Screenshot taken: {scr}")
print("=== SEQUENCE COMPLETED ===")
