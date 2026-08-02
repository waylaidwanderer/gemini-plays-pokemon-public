import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting B3F Left Room bypass from: {pos}")

# Currently at (22, 18) on B3F
# 1. Walk UP Column 22 to Row 11 (7 steps Up)
# (22, 11) is a Left spinner, which will slide us Left into wall, stopping at (22, 11)
for _ in range(7):
    pos = move(["Up"])

# 2. Walk Right to Column 23 (1 step Right)
pos = move(["Right"])

# 3. Walk Right onto (24, 11) Right spinner (1 step Right)
# This will slide us to (25, 11) stopper
print("Stepping onto (24, 11) Right spinner...")
pos = move(["Right"])
time.sleep(2.0)

# 4. Walk UP Column 25 to Row 7 (4 steps Up)
for _ in range(4):
    pos = move(["Up"])

# 5. Walk Left along Row 7 to Column 18 (7 steps Left)
for _ in range(7):
    pos = move(["Left"])

# 6. Walk Down Column 18 to Row 18 (11 steps Down)
for _ in range(11):
    pos = move(["Down"])

# 7. Walk Right 1 step to (19, 18) stairs (this will warp us to B4F!)
print("Stepping onto B4F stairs at (19, 18)...")
pos = move(["Right"])

print("Final position after B3F to B4F warp attempt:", mgba.get_coordinates())
mgba.take_screenshot()
