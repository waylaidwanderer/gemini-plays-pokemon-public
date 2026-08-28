import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def step(direction):
    mgba.press_buttons([direction])
    time.sleep(0.55)
    return get_pos()

print("Start position:", get_pos())

# 1. Walk to (2, 12)
pos = get_pos()
if pos == (1, 10):
    step("Down")
    step("Down")
    step("Right")
elif pos == (2, 12):
    print("Already at switch position!")
else:
    print("Error: Unknown starting position:", pos)
    exit(1)

# 2. Turn UP towards statue
print("Facing UP...")
mgba.press_buttons(["Up"])
time.sleep(0.6)

# 3. Press A 10 times, taking a screenshot after each press, and sleep 1.2s in between
print("Starting switch dialogue test...")
for i in range(1, 11):
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    scr = mgba.take_screenshot()
    print(f"A-press {i}/10 complete. Screenshot saved: {scr}")

print("Test complete!")
