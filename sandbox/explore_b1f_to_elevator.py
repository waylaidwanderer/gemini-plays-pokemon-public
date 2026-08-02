import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# We are at (21, 2) on B1F.
# 1. Walk Down to Row 5 (3 steps Down)
for _ in range(3):
    pos = move(["Down"])

# 2. Walk Right to Column 28 (7 steps Right)
for _ in range(7):
    pos = move(["Right"])

# 3. Walk Down Column 28 up to Row 25
# If we get blocked, we print where and break so we can walk around
for i in range(5, 25):
    pos = move(["Down"])
    if pos['y'] != i + 1:
        print(f"Blocked at {pos} during Down movement")
        break

print("Finished movement. Current position:", mgba.get_coordinates())
mgba.take_screenshot()
