import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# Currently at (24, 15) on B1F
# 1. Walk Up to Row 5 (10 steps Up)
for _ in range(10):
    pos = move(["Up"])

# 2. Walk Left to Column 11 (13 steps Left)
for _ in range(13):
    pos = move(["Left"])

# 3. Walk Down Column 11 to Row 10 (5 steps Down)
for _ in range(5):
    pos = move(["Down"])

# 4. Walk Right to Column 14 (3 steps Right)
for _ in range(3):
    pos = move(["Right"])

# 5. Walk Down Column 14 to Row 14 (4 steps Down)
for _ in range(4):
    pos = move(["Down"])

# 6. Try to walk Down from Row 14 to see if we can reach Row 15 and below!
print("Testing walking Down from Row 14 in the west...")
for _ in range(5):
    pos = move(["Down"])

print("Final position after western exploration:", mgba.get_coordinates())
mgba.take_screenshot()
