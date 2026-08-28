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
    print("Warning: unexpected starting position", pos)

print("Facing UP...")
mgba.press_buttons(["Up"])
time.sleep(1.0)

# 2. Toggle Mewtwo Switch with exactly 4 slow A-presses (verified perfect!)
# 1st A: Opens "A secret switch!"
# 2nd A: Advances to "Who would press it? YES/NO"
# 3rd A: Selects YES (toggles to State B). Advances to "Who wouldn't?"
# 4th A: Closes dialogue completely.
print("Toggling switch to State B with exactly 4 slow A-presses...")
mgba.press_buttons([
    "A", "sleep 1500",
    "A", "sleep 1500",
    "A", "sleep 1500",
    "A", "sleep 1500"
])
time.sleep(7.0)
print("Switch toggle complete!")

# 3. Walk to Column 1 and UP past gate to verify it's open!
step("Left") # to (1, 12)
step("Up") # to (1, 11)
step("Up") # to (1, 10)
step("Up") # to (1, 9) - gate should be open now!
step("Up") # to (1, 8)

print("Final Position:", get_pos())
mgba.take_screenshot()
