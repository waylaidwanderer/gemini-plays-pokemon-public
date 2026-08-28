import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def step(direction):
    old_pos = get_pos()
    mgba.press_buttons([direction])
    time.sleep(0.55)
    new_pos = get_pos()
    print(f"Stepped {direction}: {old_pos} -> {new_pos}")
    return new_pos

print("Start position:", get_pos())

# We are at (7, 10). Let's test the east bypass route to Row 8!
steps = [
    ("Down", (7, 11)),
    ("Right", (8, 11)),
    ("Right", (9, 11)),
    ("Up", (9, 10)),
    ("Up", (9, 9)),
    ("Up", (9, 8)),
    ("Left", (8, 8)),
    ("Left", (7, 8)),
    ("Left", (6, 8)),
    ("Left", (5, 8)),
    ("Left", (4, 8)),
    ("Left", (3, 8)),
]

for d, expected in steps:
    pos = step(d)
    if pos != expected:
        print(f"BOCKED/DESYNC at {pos} (expected {expected})")
        break

print("Final Position:", get_pos())
mgba.take_screenshot()
