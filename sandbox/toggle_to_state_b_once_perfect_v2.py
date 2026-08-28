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
else:
    # If we are somewhere else, walk to (2, 12)
    print("Warning: unexpected starting position")

print("Facing UP...")
mgba.press_buttons(["Up"])
time.sleep(1.0)

# 2. Toggle Mewtwo Switch with exactly 4 slow A-presses (verified perfect!)
print("Toggling switch to State B with exactly 4 slow A-presses...")
mgba.press_buttons([
    "A", "sleep 1500",
    "A", "sleep 1500",
    "A", "sleep 1500",
    "A", "sleep 1500"
])
time.sleep(7.0)
print("Switch toggle complete!")

# 3. Walk to Column 1 and UP past gate
step("Left") # to (1, 12)
step("Up") # to (1, 11)
step("Up") # to (1, 10)
step("Up") # to (1, 9) - gate!
step("Up") # to (1, 8)

print("Final Position:", get_pos())
mgba.take_screenshot()
