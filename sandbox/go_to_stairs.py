import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting from: {pos}")

# We are at (17, 7) on B3F
# 1. Walk Right to (25, 7) (8 steps Right)
print("Walking right to Column 25...")
for _ in range(8):
    pos = move(["Right"])

# 2. Walk Up to (25, 6) (1 step Up)
pos = move(["Up"])

# Now we are at (25, 6). Let's run the exact explore_b3f_down.py steps:
print("Starting explore_b3f_down.py sequence...")

# Step 1: Walk Right to Column 26 (1 step Right)
pos = move(["Right"])

# Step 2: Walk Down to Row 10 (4 steps Down)
for _ in range(4):
    pos = move(["Down"])

# Step 3: Walk Left onto (24, 10) Left spinner (2 steps Left)
pos = move(["Left"])
print("Stepping onto (24, 10) Left spinner...")
pos = move(["Left"])
# Add a small sleep to let the slide animation finish completely
time.sleep(2.0)

# Step 4: Walk Down to Row 11 (1 step Down)
pos = move(["Down"])

# Step 5: Walk Left onto (22, 11) Left spinner (1 step Left)
print("Stepping onto (22, 11) Left spinner...")
pos = move(["Left"])
time.sleep(2.0)

# Step 6: Walk Down to Row 15 (4 steps Down)
for _ in range(4):
    pos = move(["Down"])

# Step 7: Walk Left to Column 19 (2 steps Left)
for _ in range(2):
    pos = move(["Left"])

# Step 8: Walk Down to reach the stairs to B4F (3 steps Down)
print("Stepping onto B4F stairs...")
for _ in range(3):
    pos = move(["Down"])

print("Final position after warp sequence:", mgba.get_coordinates())
mgba.take_screenshot()
