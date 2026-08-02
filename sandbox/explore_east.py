import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# Currently at (23, 9) on B1F
# 1. Walk Right to Column 28 (5 steps Right)
for _ in range(5):
    pos = move(["Right"])

# 2. Walk Down Column 28 as far as possible
print("Walking Down Column 28...")
for i in range(9, 25):
    pos = move(["Down"])
    if pos['y'] != i + 1:
        print(f"Blocked at {pos} during Down movement along Column 28")
        break

print("Final position after exploration:", mgba.get_coordinates())
mgba.take_screenshot()
