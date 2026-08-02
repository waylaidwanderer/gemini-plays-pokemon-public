import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# Walk up to Row 5
# Current position is (20, 14)
# Let's walk up step by step
for i in range(14, 5, -1):
    pos = move(["Up"])
    if pos['y'] != i - 1:
        print(f"Blocked at {pos}")
        break

# If we are at Row 5, walk right to Column 24
if pos['y'] == 5:
    for i in range(pos['x'], 24):
        pos = move(["Right"])
        if pos['x'] != i + 1:
            print(f"Blocked at {pos}")
            break

# If we are at (24, 5), walk down to Row 17
if pos['x'] == 24 and pos['y'] == 5:
    for i in range(5, 17):
        pos = move(["Down"])
        if pos['y'] != i + 1:
            print(f"Blocked at {pos}")
            break

print("Finished moving. Current position:", mgba.get_coordinates())
mgba.take_screenshot()
