import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

start = get_pos()
print(f"Start pos: {start}")

# Probe Up
mgba.press_buttons(["Up"])
time.sleep(0.3)
p = get_pos()
print(f"Tried Up: ended up at {p}")
if p != start:
    mgba.press_buttons(["Down"])
    time.sleep(0.3)
    print(f"Returned to {get_pos()}")

# Probe Down
mgba.press_buttons(["Down"])
time.sleep(0.3)
p = get_pos()
print(f"Tried Down: ended up at {p}")
if p != start:
    mgba.press_buttons(["Up"])
    time.sleep(0.3)
    print(f"Returned to {get_pos()}")

# Probe Left
mgba.press_buttons(["Left"])
time.sleep(0.3)
p = get_pos()
print(f"Tried Left: ended up at {p}")
if p != start:
    mgba.press_buttons(["Right"])
    time.sleep(0.3)
    print(f"Returned to {get_pos()}")

# Probe Right
mgba.press_buttons(["Right"])
time.sleep(0.3)
p = get_pos()
print(f"Tried Right: ended up at {p}")
if p != start:
    mgba.press_buttons(["Left"])
    time.sleep(0.3)
    print(f"Returned to {get_pos()}")
