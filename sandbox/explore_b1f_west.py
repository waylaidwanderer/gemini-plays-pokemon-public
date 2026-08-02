import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# Current position is (27, 15) on B1F
# 1. Walk Right to Column 28 (1 step Right)
pos = move(["Right"])

# 2. Walk Up Column 28 to Row 5 (10 steps Up)
for _ in range(10):
    pos = move(["Up"])

# 3. Walk Left to Column 11 (17 steps Left)
for _ in range(17):
    pos = move(["Left"])

# 4. Walk Down Column 11 to Row 10 (5 steps Down)
for _ in range(5):
    pos = move(["Down"])

# 5. Walk Right to Column 14 (3 steps Right)
for _ in range(3):
    pos = move(["Right"])

# 6. Walk Down Column 14 to Row 14 (4 steps Down)
for _ in range(4):
    pos = move(["Down"])

# 7. Walk Down Column 14 as far as possible (to Row 25 or until blocked)
print("Testing walking Down from (14, 14)...")
for i in range(14, 26):
    pos = move(["Down"])
    if pos['y'] != i + 1:
        print(f"Blocked at {pos} during Down movement in the west")
        break

print("Final position after western corridor test:", mgba.get_coordinates())
mgba.take_screenshot()
