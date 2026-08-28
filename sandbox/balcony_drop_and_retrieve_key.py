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

# We are at (23, 5). Let's walk back to Row 3 via Column 26!
steps = [
    ("Right", (24, 5)),
    ("Right", (25, 5)),
    ("Right", (26, 5)),
    ("Up", (26, 4)),
    ("Up", (26, 3)), # Testing if we can walk Up through the landing tile!
    ("Left", (25, 3)),
    ("Left", (24, 3)),
    ("Left", (23, 3)),
    ("Left", (22, 3)),
]

for d, expected in steps:
    pos = step(d)
    if pos != expected:
        print(f"BLOCKED/DESYNC at {pos} (expected {expected})")
        break

print("Final Position:", get_pos())
mgba.take_screenshot()
