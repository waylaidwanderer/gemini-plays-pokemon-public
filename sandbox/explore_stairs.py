import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# Currently at (25, 8) on B2F
# Walk Down Column 25 up to Row 15
print("Walking Down Column 25...")
for i in range(8, 15):
    pos = move(["Down"])
    if pos['y'] != i + 1:
        print(f"Blocked at {pos} during Down movement along Column 25")
        break

# If we reached Y=14 or Y=15, try walking Left!
pos = mgba.get_coordinates()
if pos['y'] >= 13:
    print(f"Testing Left movement from Y={pos['y']}...")
    for _ in range(4):
        pos = move(["Left"])

print("Final position:", mgba.get_coordinates())
mgba.take_screenshot()
