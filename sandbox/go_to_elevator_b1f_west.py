import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# Currently at (25, 15) on B1F
# 1. Walk Up to Row 9 (6 steps Up)
for _ in range(6):
    pos = move(["Up"])

# 2. Walk Left to Column 20 (5 steps Left)
for _ in range(5):
    pos = move(["Left"])

# 3. Walk Down Column 20 to Row 17 (8 steps Down)
for _ in range(8):
    pos = move(["Down"])

# 4. Walk Right to Column 21 (1 step Right)
pos = move(["Right"])

# 5. Face UP
print("Facing UP at (21, 17)...")
pos = move(["Up"])

# 6. Interact by pressing A (with Lift Key in bag)
print("Pressing A to open the elevator doors...")
pos = move(["A"])

# Let's see if the doors open or if we warp!
mgba.take_screenshot()
