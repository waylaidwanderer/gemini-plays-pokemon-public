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
# 1. Walk Right to Column 23
pos = move(["Right"])

# 2. Walk Up Column 23 to Row 12 (2 steps Up)
for _ in range(2):
    pos = move(["Up"])

# 3. Walk Right to (24, 12) (Right spinner, will slide us to (25, 12))
print("Stepping onto (24, 12) Right spinner...")
pos = move(["Right"])
time.sleep(2.0)

# 4. Walk Up Column 25 to Row 7 (5 steps Up)
for _ in range(5):
    pos = move(["Up"])

# 5. Walk Left along Row 7 to Column 18 (7 steps Left)
for _ in range(7):
    pos = move(["Left"])

# 6. Walk Down Column 18 to Row 11 (4 steps Down)
for _ in range(4):
    pos = move(["Down"])

print("Successfully reached B3F Left Room at:", mgba.get_coordinates())
mgba.take_screenshot()
