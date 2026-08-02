import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting B3F bypass from: {pos}")

# Currently at (22, 14) on B3F
# 1. Walk Right 1 step to Column 23
pos = move(["Right"])  # turn Right
pos = move(["Right"])  # step to (23, 14)

# 2. Walk Up Column 23 to Row 12 (2 steps Up)
pos = move(["Up"])     # turn Up
for _ in range(2):
    pos = move(["Up"]) # step to (23, 13) then (23, 12)

# 3. Walk Right to Column 25 (2 steps Right)
pos = move(["Right"])  # turn Right
for _ in range(2):
    pos = move(["Right"]) # step to (24, 12) then (25, 12)

# 4. Walk Up Column 25 to Row 7 (5 steps Up)
pos = move(["Up"])     # turn Up
for _ in range(5):
    pos = move(["Up"]) # step to (25, 11), (25, 10), (25, 9), (25, 8), (25, 7)

# 5. Walk Left along Row 7 to Column 18 (7 steps Left)
pos = move(["Left"])   # turn Left
for _ in range(7):
    pos = move(["Left"]) # step to 24, 23, 22, 21, 20, 19, 18 on Row 7

# 6. Walk Down Column 18 to Row 11 (4 steps Down)
pos = move(["Down"])   # turn Down
for _ in range(4):
    pos = move(["Down"]) # step to 18, 17, 16 on Column 18

print("Finished movement. Current position:", mgba.get_coordinates())
mgba.take_screenshot()
