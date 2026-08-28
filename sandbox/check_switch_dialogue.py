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

# 1. Walk to (2, 12)
pos = get_pos()
if pos == (1, 10):
    step("Down")
    step("Down")
    step("Right")
elif pos == (2, 12):
    print("Already at switch position!")
else:
    print("Not at starting area, walking to (2, 12) first...")
    if pos[0] > 2:
        for x in range(pos[0]-1, 1, -1):
            step("Left")
    if pos[1] < 12:
        for y in range(pos[1]+1, 13):
            step("Down")

# 2. Face UP towards the statue
print("Facing UP...")
mgba.press_buttons(["Up"])
time.sleep(0.8)

# 3. Press A exactly once to open dialogue
print("Pressing A once to check dialogue...")
mgba.press_buttons(["A"])
time.sleep(1.5)

# Take screenshot to verify the dialogue
print("Taking screenshot to check dialogue text...")
scr = mgba.take_screenshot()
print(f"Screenshot saved: {scr}")

print("Verification check completed! Standing at:", get_pos())
