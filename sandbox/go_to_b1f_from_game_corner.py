import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# Currently at (17, 14) in Celadon Game Corner
# 1. Walk Left 1 step to Column 16
pos = move(["Left"])

# 2. Walk Up Column 16 to Row 4 (10 steps Up)
for _ in range(10):
    pos = move(["Up"])

# 3. Walk Right 1 step to Column 17 (this should warp us to B1F at (23, 2)!)
print("Stepping onto secret stairs at (17, 4)...")
pos = move(["Right"])

print("Current position after warp attempt:", mgba.get_coordinates())
mgba.take_screenshot()
