import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# We are at (16, 13)
# 1. Walk Right to (17, 13) (1 step Right)
pos = move(["Right"])

# 2. Walk Down to (17, 20) (7 steps Down)
print("Walking down Column 17...")
for _ in range(7):
    pos = move(["Down"])

# 3. Walk Right to (19, 20) (2 steps Right)
print("Walking right to Column 19...")
for _ in range(2):
    pos = move(["Right"])

# 4. Walk Up to (19, 18) stairs (2 steps Up)
print("Walking up to (19, 18) B4F stairs...")
pos = move(["Up"])
pos = move(["Up"])

# Wait for map transition to B4F
time.sleep(1)
pos = mgba.get_coordinates()
print(f"Position on B4F: {pos}")
mgba.take_screenshot()
