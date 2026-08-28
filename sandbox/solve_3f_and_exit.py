import mgba
import time
from PIL import Image

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

print("Current position:", get_pos())

# 1. Walk from (1, 10) to switch standing position (2, 12)
print("Walking to switch standing position...")
step("Down") # to (1, 11)
step("Down") # to (1, 12)
step("Right") # to (2, 12)

print("Facing UP...")
mgba.press_buttons(["Up"])
time.sleep(1.0)

# 2. Toggle Mewtwo Switch to State B with exactly 4 slow A-presses
print("Toggling switch to State B with exactly 4 slow A-presses...")
mgba.press_buttons([
    "A", "sleep 1500",
    "A", "sleep 1500",
    "A", "sleep 1500",
    "A", "sleep 1500"
])
time.sleep(7.0)
print("Switch toggle complete!")

# 3. Walk to Column 3 Row 10
# Path: Down to (2, 13) -> Right to (3, 13) -> Right to (4, 13) -> Up to (4, 12) -> Up to (4, 11) -> Left to (3, 11) -> Up to (3, 10)
print("Walking to Column 3 Row 10...")
steps_to_col_3 = [
    ("Down", (2, 13)),
    ("Right", (3, 13)),
    ("Right", (4, 13)),
    ("Up", (4, 12)),
    ("Up", (4, 11)),
    ("Left", (3, 11)),
    ("Up", (3, 10)),
]
for d, expected in steps_to_col_3:
    pos = step(d)
    if pos != expected:
        print(f"BLOCKED/DESYNC at {pos} (expected {expected})")
        exit(1)

# 4. Walk UP Column 3 through open gate to Row 6 (gate at (3, 9) is OPEN in State B!)
print("Walking UP through Column 3 gate to Row 6...")
steps_up_gate = [
    ("Up", (3, 9)),
    ("Up", (3, 8)),
    ("Up", (3, 7)),
    ("Up", (3, 6)),
]
for d, expected in steps_up_gate:
    pos = step(d)
    if pos != expected:
        print(f"BLOCKED/DESYNC at {pos} (expected {expected})")
        exit(1)

# 5. Walk RIGHT along Row 6 to Column 20
print("Walking RIGHT along Row 6 to Column 20...")
pos = get_pos()
while pos[0] < 20:
    pos = step("Right")

# 6. Walk UP Column 20 to Row 3
print("Walking UP Column 20 to Row 3...")
while get_pos()[1] > 3:
    step("Up")

# 7. Walk RIGHT along Row 3 to Column 26
print("Walking RIGHT along Row 3 to Column 26...")
while get_pos()[0] < 26:
    step("Right")

# 8. Step DOWN to drop through the pitfall to 1F East inside the fenced room
print("Dropping through the pitfall to 1F East...")
step("Down")
time.sleep(2.5)

print("Part 1 complete! Landed on 1F East inside the fenced room. Position:", get_pos())
mgba.take_screenshot()
