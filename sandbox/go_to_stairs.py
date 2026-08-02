import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at B3F: {pos}")

# Currently at B3F (21, 5)
# 1. Walk Down to Row 7 (2 steps Down)
print("Walking down to Row 7...")
for _ in range(2):
    pos = move(["Down"])

# 2. Walk Left along Row 7 to Column 4 (17 steps Left)
print("Walking left to Column 4...")
for _ in range(17):
    pos = move(["Left"])

# 3. Walk Down Column 4 to Row 14 (7 steps Down)
print("Walking down Column 4...")
for _ in range(7):
    pos = move(["Down"])

# 4. Step Right onto (5, 14) RIGHT spinner -> slides us to (9, 16)
print("Stepping onto (5, 14) RIGHT spinner...")
pos = move(["Right"])
time.sleep(3.0)

pos = mgba.get_coordinates()
print(f"Position at (9, 16) stopper: {pos}")

# 5. Step Right onto (11, 16) RIGHT spinner -> slides us to (15, 18)
if pos['x'] == 9 and pos['y'] == 16:
    print("Walking to (11, 16) RIGHT spinner...")
    pos = move(["Right"])
    pos = move(["Right"])
    time.sleep(3.0)

pos = mgba.get_coordinates()
print(f"Position at (15, 18) stopper: {pos}")

# 6. Walk Up 1 step to (15, 17) and Right 1 step onto (16, 17) UP spinner -> slides us to (16, 13)
if pos['x'] == 15 and pos['y'] == 18:
    print("Navigating to UP spinner...")
    pos = move(["Up"])
    pos = move(["Right"])
    time.sleep(3.0)

pos = mgba.get_coordinates()
print(f"Position at (16, 13) stopper: {pos}")

# 7. Walk Right 1, Down 7, Right 2, Up 2 onto the stairs to B4F at (19, 18)
if pos['x'] == 16 and pos['y'] == 13:
    print("Navigating to B4F stairs...")
    pos = move(["Right"])
    for _ in range(7):
        pos = move(["Down"])
    for _ in range(2):
        pos = move(["Right"])
    pos = move(["Up"])
    pos = move(["Up"])
    time.sleep(1.0)

pos = mgba.get_coordinates()
print(f"Final position on B4F: {pos}")
mgba.take_screenshot()
