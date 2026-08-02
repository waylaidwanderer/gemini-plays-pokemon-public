import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at B3F: {pos}")

# Currently at (22, 15)
# 1. Walk Right to Column 27 (5 steps Right)
for _ in range(5):
    pos = move(["Right"])

# 2. Walk Down Column 27 as far as possible (up to Row 26)
print("Walking Down Column 27...")
for i in range(15, 26):
    pos = move(["Down"])
    if pos['y'] != i + 1:
        print(f"Blocked at {pos} during Down movement along Column 27")
        break

print("Final position after exploration:", mgba.get_coordinates())
mgba.take_screenshot()
