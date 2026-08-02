import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# Currently at (25, 15)
# 1. Walk Left to (24, 15)
pos = move(["Left"])

# 2. Try walking Down into (24, 16)
print("Testing walking Down into (24, 16):")
pos = move(["Down"])

# 3. Try pressing A facing Down at (24, 15) (we should be at 24, 15 if blocked)
if pos['y'] == 15:
    print("Blocked. Testing pressing A at (24, 15) facing Down:")
    pos = move(["A"])

print("Final position after test:", mgba.get_coordinates())
mgba.take_screenshot()
