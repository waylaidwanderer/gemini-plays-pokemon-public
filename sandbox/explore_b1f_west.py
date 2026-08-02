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
# 1. Walk Up to Row 9
for _ in range(6):
    pos = move(["Up"])

# 2. Walk Left to Column 20
for _ in range(5):
    pos = move(["Left"])

# 3. Walk Down Column 20 as far as possible (checking up to Row 25)
for i in range(9, 25):
    pos = move(["Down"])
    if pos['y'] != i + 1:
        print(f"Blocked at {pos} during Down movement along Column 20")
        break

print("Finished movement. Current position:", mgba.get_coordinates())
mgba.take_screenshot()
