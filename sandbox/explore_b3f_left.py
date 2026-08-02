import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting B3F Left Room bypass from: {pos}")

# Currently at (23, 18) on B3F
# 1. Walk UP Column 23 to Row 12 (6 steps Up)
for _ in range(6):
    pos = move(["Up"])

# 2. Walk Right to Column 25 (2 steps Right)
for _ in range(2):
    pos = move(["Right"])

# 3. Walk UP Column 25 to Row 7 (5 steps Up)
for _ in range(5):
    pos = move(["Up"])

# 4. Walk Left along Row 7 to Column 18 (7 steps Left)
for _ in range(7):
    pos = move(["Left"])

# 5. Walk Down Column 18 to Row 18 (11 steps Down)
for _ in range(11):
    pos = move(["Down"])

# 6. Walk Right 1 step to (19, 18) stairs to B4F
print("Stepping onto B4F stairs...")
pos = move(["Right"])

print("Final position after warp attempt:", mgba.get_coordinates())
mgba.take_screenshot()
