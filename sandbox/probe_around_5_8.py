import mgba
import time

def check_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

start = check_pos()
print(f"Start pos: {start}")

# Test Down
mgba.press_buttons(["Down"])
time.sleep(0.3)
p = check_pos()
print(f"Tried Down: ended up at {p}")
if p != start:
    mgba.press_buttons(["Up"])
    time.sleep(0.3)
    print(f"Returned to {check_pos()}")

# Test Right
mgba.press_buttons(["Right"])
time.sleep(0.3)
p = check_pos()
print(f"Tried Right: ended up at {p}")
if p != start:
    mgba.press_buttons(["Left"])
    time.sleep(0.3)
    print(f"Returned to {check_pos()}")

# Test Left
mgba.press_buttons(["Left"])
time.sleep(0.3)
p = check_pos()
print(f"Tried Left: ended up at {p}")
if p != start:
    mgba.press_buttons(["Right"])
    time.sleep(0.3)
    print(f"Returned to {check_pos()}")

# Test Up
mgba.press_buttons(["Up"])
time.sleep(0.3)
p = check_pos()
print(f"Tried Up: ended up at {p}")
if p != start:
    mgba.press_buttons(["Down"])
    time.sleep(0.3)
    print(f"Returned to {check_pos()}")
