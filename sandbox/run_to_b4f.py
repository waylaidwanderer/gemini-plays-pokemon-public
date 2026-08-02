import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# We are at B3F (17, 13)
# 1. Walk to (17, 11) LEFT spinner via Column 19
print("Walking to (17, 11) LEFT spinner...")
pos = move(["Right"])
pos = move(["Right"]) # to (19, 13)
pos = move(["Up"])
pos = move(["Up"]) # to (19, 11)
pos = move(["Left"])
pos = move(["Left"]) # onto (17, 11) LEFT spinner -> slides us to (2, 9)
time.sleep(3.0)

pos = mgba.get_coordinates()
print(f"Position at (2, 9) stopper: {pos}")

# 2. Walk to Column 4, Down to Row 14, and Right onto (5, 14) RIGHT spinner -> slides to (9, 16)
if pos['x'] == 2 and pos['y'] == 9:
    print("Walking to (5, 14) RIGHT spinner...")
    for _ in range(2):
        pos = move(["Right"])
    for _ in range(5):
        pos = move(["Down"])
    pos = move(["Right"])
    time.sleep(3.0)

pos = mgba.get_coordinates()
print(f"Position at (9, 16) stopper: {pos}")

# 3. Walk Right 2 steps onto (11, 16) RIGHT spinner -> slides us to (15, 18)
if pos['x'] == 9 and pos['y'] == 16:
    print("Walking to (11, 16) RIGHT spinner...")
    pos = move(["Right"])
    pos = move(["Right"])
    time.sleep(3.0)

pos = mgba.get_coordinates()
print(f"Position at (15, 18) stopper: {pos}")

# 4. Walk Down 2 to (15, 20), Right 4 to (19, 20), and Up 2 onto B4F stairs at (19, 18)
if pos['x'] == 15 and pos['y'] == 18:
    print("Walking to B4F stairs via Row 20...")
    for _ in range(2):
        pos = move(["Down"])
    for _ in range(4):
        pos = move(["Right"])
    pos = move(["Up"])
    pos = move(["Up"])
    time.sleep(1.0)

pos = mgba.get_coordinates()
print(f"Final position on B4F: {pos}")
mgba.take_screenshot()
