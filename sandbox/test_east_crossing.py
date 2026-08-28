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

# We are at (9, 10). Let's test walking up Column 12 and then Left on Row 6!
steps = [
    ("Right", (10, 10)),
    ("Right", (11, 10)),
    ("Right", (12, 10)),
    ("Up", (12, 9)),
    ("Up", (12, 8)),
    ("Up", (12, 7)),
    ("Up", (12, 6)),
    ("Left", (11, 6)),
    ("Left", (10, 6)),
    ("Left", (9, 6)),
    ("Left", (8, 6)),
    ("Left", (7, 6)),
]

for d, expected in steps:
    pos = step(d)
    if pos != expected:
        print(f"BLOCKED/DESYNC at {pos} (expected {expected})")
        break

print("Final Position:", get_pos())
mgba.take_screenshot()
