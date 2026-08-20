import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

print("Starting Part 1 at:", get_pos())

# 1. Walk Left to (12, 12)
mgba.press_buttons(["Left"])
time.sleep(0.4)
print("Pos:", get_pos())

# 2. Walk Up to (12, 11)
mgba.press_buttons(["Up"])
time.sleep(0.4)
print("Pos:", get_pos())

# 3. Walk Left to (7, 11)
for _ in range(5):
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
print("Pos:", get_pos())

# 4. Walk Up to (7, 10) to warp to 3F
mgba.press_buttons(["Up"])
time.sleep(1.5)
print("Landed on 3F, pos:", get_pos())

# 5. Walk Right to (16, 11) on 3F
print("Walking to (16, 11) on 3F...")
for _ in range(9):
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
print("Pos:", get_pos())

# 6. Walk Left onto (15, 11) to warp to 2F
print("Warping down to 2F...")
mgba.press_buttons(["Left"])
time.sleep(1.5)
print("Landed on 2F east wing, pos:", get_pos())
