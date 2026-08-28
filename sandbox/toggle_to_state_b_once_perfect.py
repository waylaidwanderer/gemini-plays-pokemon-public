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

# 1. Walk from current position to (2, 12)
pos = get_pos()
if pos == (1, 10):
    step("Down")
    step("Down")
    step("Right")
elif pos == (2, 12):
    print("Already at switch position!")

print("Facing UP...")
mgba.press_buttons(["Up"])
time.sleep(1.0)

# 2. Toggle Mewtwo Switch with exactly 5 slow A-presses in a single synchronized call (verified working in Turn 64715!)
print("Toggling switch to State B with exactly 5 slow A-presses...")
mgba.press_buttons([
    "A", "sleep 1500",
    "A", "sleep 1500",
    "A", "sleep 1500",
    "A", "sleep 1500",
    "A", "sleep 1500"
])
time.sleep(8.5)
print("Switch toggle complete!")

# 3. Walk to Column 1
step("Left")

# 4. Walk UP Column 1 past the Row 9 gate to Row 6!
print("Testing walking UP Column 1...")
step("Up") # to (1, 11)
step("Up") # to (1, 10)
step("Up") # to (1, 9) - gate!
step("Up") # to (1, 8)
step("Up") # to (1, 7)
step("Up") # to (1, 6)

print("Final Position:", get_pos())
mgba.take_screenshot()
