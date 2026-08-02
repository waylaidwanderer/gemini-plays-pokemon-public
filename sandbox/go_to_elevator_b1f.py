import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# Currently at (28, 14) on B1F
# 1. Walk Left to Column 25 (3 steps Left)
for _ in range(3):
    pos = move(["Left"])

# 2. Walk Down to Row 15 (1 step Down)
pos = move(["Down"])

# 3. Walk Down into the trigger coordinate (25, 16)
print("Stepping onto elevator trigger at (25, 16) with Lift Key...")
pos = move(["Down"])

print("Current position after trigger attempt:", mgba.get_coordinates())
mgba.take_screenshot()
